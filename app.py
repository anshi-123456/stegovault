from flask import Flask, render_template, request, send_file
import os
from encode import encode_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    print("✅ Index route hit")
    return render_template("index.html")


@app.route("/encode", methods=["POST"])
def encode():
    image = request.files["image"]
    secret = request.files["file"]
    password = request.form["password"]

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    file_path = os.path.join(UPLOAD_FOLDER, secret.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "stego.png")

    image.save(image_path)
    secret.save(file_path)

    encode_file(image_path, file_path, password, output_path)

    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)