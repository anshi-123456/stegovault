import cv2
import base64
from crypto import decrypt_data
from utils import binary_to_bytes, generate_positions

DELIMITER = '11111111111111111111111111111110'

print("🚀 Decode module loaded...")

def decode_file(image_path, password, output_file):
    print("🚀 Starting decoding...")

    img = cv2.imread(image_path)

    if img is None:
        print("❌ Image not found")
        return

    h, w, _ = img.shape
    total_pixels = h * w * 3

    positions = generate_positions(password, total_pixels)

    binary_data = ""

    print("📥 Extracting data...")

    # 🔥 FAST extraction
    for pos in positions:
        pixel_index = pos // 3
        color_index = pos % 3

        row = pixel_index // w
        col = pixel_index % w

        pixel = img[row, col]
        binary_data += format(pixel[color_index], '08b')[-1]

        if len(binary_data) >= 32 and binary_data[-32:] == DELIMITER:
            break

    if DELIMITER not in binary_data:
        print("❌ No hidden data found")
        return

    print("✅ Extraction complete")

    binary_data = binary_data[:-32]

    try:
        cipher_data = binary_to_bytes(binary_data)

        # 🔥 SHOW RANDOM TEXT
        print("\n🔐 ENCRYPTED RAW BYTES:")
        print(cipher_data)

        print("\n🔤 RANDOM TEXT:")
        print(cipher_data.decode('utf-8', errors='ignore'))

        print("\n🔑 BASE64 VIEW:")
        print(base64.b64encode(cipher_data).decode())

        print("\n🔐 Decrypting...")

        decrypted = decrypt_data(cipher_data, password)

        print("\n🔓 ORIGINAL TEXT:")
        print(decrypted)

        file_data = base64.b64decode(decrypted)

        with open(output_file, "wb") as f:
            f.write(file_data)

        print("✅ File recovered →", output_file)

    except Exception as e:
        print("❌ Error:", e)


# ================= RUN =================
if __name__ == "__main__":
    decode_file("stego.png", "mypassword", "output.txt")