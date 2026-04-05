from flask import Flask, render_template, request, send_file
import os
from encode import encode_file

app = Flask(__name__)

# 📂 Folder setup
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# 🏠 Home Route
@app.route("/")
def index():
    return render_template("index.html")


# 🔐 Encode Route
@app.route("/encode", methods=["POST"])
def encode():
    try:
        image = request.files["image"]
        secret = request.files["file"]
        password = request.form["password"]

        # Save uploaded files
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        file_path = os.path.join(UPLOAD_FOLDER, secret.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "stego.png")

        image.save(image_path)
        secret.save(file_path)

        # Call encoding function
        encode_file(image_path, file_path, password, output_path)

        # Return file for download
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"❌ Error: {str(e)}"


# 🚀 Run app (for local testing)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)