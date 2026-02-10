from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Game State Constants
MODULE_DATA = {
    1: {
        "title": "Caesar Cipher",
        "type": "caesar",
        "theory": "The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.",
        "tool_name": "Cryptii (Caesar Cipher)",
        "external_tool_url": "https://cryptii.com/pipes/caesar-cipher",
        "mission_cipher": "WKH SDVVZRUG LV VHFXUHBQRGH",
        "correct_answer": "THE PASSWORD IS SECURE_NODE",
        "hint": "Try a shift of -3 (or +23)."
    },
    2: {
        "title": "Steganography",
        "type": "steganography",
        "theory": "Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. Unlike encryption, which hides the content of the message, steganography hides the existence of the message itself.",
        "tool_name": "AperiSolve",
        "external_tool_url": "https://www.aperisolve.com/",
        "mission_cipher": "static/images/level2_1.png",
        "correct_answer": "GHOST_PROTOCOL",
        "hint": "Upload the image to the tool and check the 'Strings' or 'Steghide' output."
    },
    3: {
        "title": "RSA Encryption",
        "type": "rsa",
        "theory": "RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem. It uses a pair of keys: a public key for encryption and a private key for decryption. Its security relies on the practical difficulty of factoring the product of two large prime numbers.",
        "tool_name": "dCode RSA Cipher",
        "external_tool_url": "https://www.dcode.fr/rsa-cipher",
        "mission_cipher": {"p": 61, "q": 53, "e": 17},
        "correct_answer": "2753",
        "hint": "Calculate the Private Key (d). You have p, q, and e. d is the modular multiplicative inverse of e modulo phi(n)."
    },
    4: {
        "title": "Hashing",
        "type": "hash",
        "theory": "A cryptographic hash function is a mathematical algorithm that maps data of arbitrary size to a bit array of a fixed size (the hash value). It is a one-way function, meaning it is practically impossible to invert.",
        "tool_name": "CrackStation",
        "external_tool_url": "https://crackstation.net/",
        "mission_cipher": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "correct_answer": "password",
        "hint": "This is a SHA-256 hash of a very common password."
    },
    5: {
        "title": "Encoded Signature",
        "type": "signature",
        "theory": "Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format. It is commonly used to encode digital signatures and other binary data for transmission over text-based protocols.",
        "tool_name": "Base64Decode",
        "external_tool_url": "https://www.base64decode.org/",
        "mission_cipher": "VFJVU1RfVkVSSUZJRURfMjAyNA==",
        "correct_answer": "TRUST_VERIFIED_2024",
        "hint": "Decode the Base64 string to reveal the verified status code."
    }
}


@app.route('/')
def index():
    return render_template('index.html', modules=MODULE_DATA)


@app.route('/module/<int:module_id>', methods=['GET', 'POST'])
def module(module_id):
    module_data = MODULE_DATA.get(module_id)
    if not module_data:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_input = request.form.get('answer', '').strip()

        # Check answer
        is_correct = False

        # Normalize comparison (case-insensitive for text)
        if str(user_input).upper() == str(module_data['correct_answer']).upper():
            is_correct = True

        if is_correct:
            flash("Access Granted. Integrity Verified.", "success")
            return jsonify({"status": "success", "message": "Access Granted"})
        else:
            return jsonify({"status": "fail", "message": "Integrity Check Failed."})

    return render_template('module.html', module=module_data, module_id=module_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
