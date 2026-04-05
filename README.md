# 🔐 Secure Data Transmission using Image Steganography

> 🚀 A full-stack web application that combines **AES Encryption** and **Image Steganography (LSB)** to securely hide and transmit data.

---

## 🌟 Project Overview

This project implements a **dual-layer security system** where sensitive data is:

1. 🔐 **Encrypted using AES (Advanced Encryption Standard)**
2. 🖼 **Hidden inside an image using LSB Steganography**

Additionally, the system provides a **web-based interface** built with Flask, HTML, CSS, and JavaScript for easy interaction.

---

## 🎯 Key Features

✨ AES Encryption for strong data security
✨ LSB Image Steganography for invisible data hiding
✨ File hiding support (not just text)
✨ Random encrypted output generation
✨ Web-based UI (Flask + JS)
✨ Automatic download of stego image
✨ Password-protected encoding & decoding

---

## 🧠 How It Works

### 🔒 Encoding Process

* Upload an image and a secret file
* File is converted to Base64
* Encrypted using AES
* Embedded into image pixels (LSB technique)

📦 Output:

* `stego.png` → Image with hidden data
* `encrypted_output.txt` → Random encrypted text

---

### 🔓 Decoding Process

* Upload stego image
* Extract hidden binary data
* Decrypt using password
* Recover original file

---

## 🛠 Tech Stack

| Technology   | Usage                |
| ------------ | -------------------- |
| 🐍 Python    | Backend logic        |
| ⚡ Flask      | Web framework        |
| 🖼 OpenCV    | Image processing     |
| 🔢 NumPy     | Data handling        |
| 🌐 HTML/CSS  | UI                   |
| ⚙ JavaScript | Frontend interaction |

---

## 📂 Project Structure

```
steganography/
│
├── app.py
├── encode.py
├── decode.py
├── crypto.py
├── utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
├── outputs/
```

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/your-username/steganography-secure-data-transfer.git
cd steganography-secure-data-transfer
pip install -r requirements.txt
```

---

### ▶ Run the App

```bash
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5000
```

---

## 📸 Demo Flow

1. Upload image
2. Upload secret file
3. Enter password
4. Click Encode
5. Download stego image

---

## 🔥 Use Cases

* 🪖 Military & secure communication
* 🔐 Confidential data transfer
* 🖼 Digital watermarking
* 🏢 Corporate data protection
* 🌐 Cybersecurity applications

---

## 🧠 What I Learned

* Cryptography (AES Encryption)
* Steganography (LSB technique)
* Full-stack web development
* Flask API integration
* Debugging real-world issues
* Secure data handling

---

## 💡 Future Enhancements

* 📱 Mobile-friendly UI
* ☁ Cloud deployment
* 🔍 Steganalysis detection resistance
* 📊 Visual analytics
* 🎨 Modern UI/UX

---

## 👨‍💻 Author

**Anuj Mishra**
📍 India
🚀 Passionate about Web Development & Cybersecurity

---

## ⭐ Support

If you like this project, please ⭐ star the repository!

---

## 🔥 Final Note

> This project is not just a simple implementation — it's a **real-world secure communication system** combining encryption, data hiding, and full-stack development.

---
