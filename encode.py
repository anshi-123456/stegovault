import cv2
import base64
import os
from crypto import encrypt_data
from utils import bytes_to_binary, generate_positions

DELIMITER = '11111111111111111111111111111110'  # 32-bit

def encode_file(image_path, file_path, password, output_path):
    print("🚀 Starting encoding...")

    img = cv2.imread(image_path)

    if img is None:
        print("❌ Image not found")
        return

    # Read file
    with open(file_path, "rb") as f:
        file_data = f.read()

    if len(file_data) == 0:
        print("⚠ Warning: File is empty")

    print(f"📦 File size: {len(file_data)} bytes")

    # Base64 encode
    file_data_b64 = base64.b64encode(file_data).decode()

    # Encrypt
    encrypted = encrypt_data(file_data_b64, password)

    # 🔥 SHOW RANDOM OUTPUT
    print("\n🔐 ENCRYPTED RAW BYTES:")
    print(encrypted)

    print("\n🔤 RANDOM ENCRYPTED TEXT:")
    print(encrypted.decode('utf-8', errors='ignore'))

    encoded_preview = base64.b64encode(encrypted).decode()

    print("\n🔑 BASE64 ENCRYPTED OUTPUT:")
    print(encoded_preview)

    # Save encrypted preview
    with open("encrypted_output.txt", "w") as f:
        f.write(encoded_preview)

    print("📄 Saved → encrypted_output.txt")

    # Convert to binary
    binary_data = bytes_to_binary(encrypted) + DELIMITER

    h, w, _ = img.shape
    total_pixels = h * w * 3

    if len(binary_data) > total_pixels:
        print("❌ File too large for image")
        return

    positions = generate_positions(password, total_pixels)

    data_index = 0

    print("🖼 Embedding data into image...")

    for pos in positions:
        if data_index >= len(binary_data):
            break

        pixel_index = pos // 3
        color_index = pos % 3

        row = pixel_index // w
        col = pixel_index % w

        pixel = img[row, col]
        pixel[color_index] = int(format(pixel[color_index], '08b')[:-1] + binary_data[data_index], 2)

        data_index += 1

    cv2.imwrite(output_path, img)

    print("✅ Encoding complete →", output_path)


# ================= RUN =================
if __name__ == "__main__":
    encode_file("input2.png", "secret.txt", "mypassword", "stego.png")