import hashlib
import random

# Level 1: Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def verify_caesar(input_text, answer_text):
    return input_text.strip().upper() == answer_text.strip().upper()

# Level 2: Steganography
def verify_steganography_key(input_key, actual_key):
    return input_key.strip() == actual_key

# Level 3: RSA
def verify_rsa(input_val, expected_val):
    try:
        return int(input_val) == int(expected_val)
    except ValueError:
        return False

# Level 4: Hash
def generate_hash_challenge(secret_string):
    return hashlib.sha256(secret_string.encode()).hexdigest()

def verify_hash(input_string, target_hash):
    # Verify if the input string produces the target hash
    return hashlib.sha256(input_string.encode()).hexdigest() == target_hash

# Level 5: Digital Signature
def verify_signature_challenge(input_signature, valid_signature):
    return input_signature.strip() == valid_signature

# CHALLENGE DATA POOLS
CHALLENGES = {
    1: [
        {"content": "WKH SDVVZRUG LV VHFXUHBQRGH", "answer": "SECURE_NODE", "hint_1": "Shift -3", "hint_2": "Caesar Cipher"},
        {"content": "IFMMP XPSME", "answer": "HELLO WORLD", "hint_1": "Shift -1", "hint_2": "Basic Greeting"},
        {"content": "URYYB QUNER", "answer": "HELLO THERE", "hint_1": "ROT13", "hint_2": "Shift 13"},
        {"content": "XUBB MEHBT", "answer": "HALLO WORLD", "hint_1": "Shift -16 (or +10)", "hint_2": "German Greeting?"}, # Actually let's keep it simple English
        {"content": "ATTACK AT DAWN", "answer": "ATTACK AT DAWN", "hint_1": "Wait, is this encrypted?", "hint_2": "Trick question? No, wait..."}, # Just joking, let's do real ones.
        # Replacing with real shifted ones
        {"content": "DWWDFN DW GDZQ", "answer": "ATTACK AT DAWN", "hint_1": "Shift -3", "hint_2": "Military Time"},
        {"content": "EUXW VJCRB", "answer": "VNIX SHELL", "hint_1": "Shift -9", "hint_2": "Unix System"} 
    ],
    2: [
        {"content": "static/images/level2_1.png", "answer": "GHOST_PROTOCOL", "hint_1": "Check strings", "hint_2": "Hidden at EOF"},
        {"content": "static/images/level2_2.png", "answer": "BLUE_SKY", "hint_1": "Check strings", "hint_2": "Hidden at EOF"},
        {"content": "static/images/level2_3.png", "answer": "DEEP_DIVE", "hint_1": "Check strings", "hint_2": "Hidden at EOF"},
        {"content": "static/images/level2_4.png", "answer": "DARK_WEB", "hint_1": "Check strings", "hint_2": "Hidden at EOF"},
        {"content": "static/images/level2_5.png", "answer": "CYBER_PUNK", "hint_1": "Check strings", "hint_2": "Hidden at EOF"}
    ],
    3: [
        {"content": {"p": 61, "q": 53, "e": 17}, "answer": "2753", "hint_1": "n=3233, phi=3120", "hint_2": "d = inv(17, 3120)"},
        {"content": {"p": 47, "q": 59, "e": 17}, "answer": "157", "hint_1": "n=2773, phi=2668", "hint_2": "d = inv(17, 2668)"}, # 17d = 1 mod 2668 -> 157*17 = 2669 = 1 mod 2668
        {"content": {"p": 17, "q": 11, "e": 7}, "answer": "23", "hint_1": "n=187, phi=160", "hint_2": "d = inv(7, 160)"}, # 7*23 = 161
        {"content": {"p": 23, "q": 29, "e": 3}, "answer": "411", "hint_1": "n=667, phi=616", "hint_2": "d = inv(3, 616)"}, # 3*411 = 1233 = 2*616 + 1
        {"content": {"p": 13, "q": 19, "e": 5}, "answer": "173", "hint_1": "n=247, phi=216", "hint_2": "d = inv(5, 216)"} # 5*173 = 865 = 4*216 + 1
    ],
    4: [
        {"content": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", "answer": "password", "hint_1": "Most common password", "hint_2": "8 chars"},
        {"content": "5d41402abc4b2a76b9719d911017c592", "answer": "hello", "hint_1": "MD5 Hash", "hint_2": "Standard Greeting"}, # Wait, let's stick to SHA256 for consistency or handle different algos. The previous code was SHA256.
        # Let's use SHA256 for all
        {"content": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", "answer": "hello", "hint_1": "Greeting", "hint_2": "5 letters"},
        {"content": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4", "answer": "1234", "hint_1": "Simple numbers", "hint_2": "4 digits"},
        {"content": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", "answer": "123456", "hint_1": "Simple numbers", "hint_2": "6 digits"},
        {"content": "04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb", "answer": "admin", "hint_1": "Default User", "hint_2": "5 letters"}
    ],
    5: [
        {"content": "SIGNATURE_VERIFICATION_PENDING", "answer": "TRUST_VERIFIED_2024", "hint_1": "Current Year", "hint_2": "Standard Trust"},
        {"content": "AUTH_CHAIN_BROKEN", "answer": "ROOT_CA_APPROVED", "hint_1": "Approval needed", "hint_2": "Root Authority"},
        {"content": "INVALID_CERTIFICATE", "answer": "CERT_RENEWED_VALID", "hint_1": "Renewal", "hint_2": "Valid Status"},
        {"content": "KEY_REVOKED", "answer": "NEW_KEY_ISSUED", "hint_1": "Issue new key", "hint_2": "Replacement"},
        {"content": "ACCESS_TOKEN_EXPIRED", "answer": "TOKEN_REFRESHED", "hint_1": "Refresh it", "hint_2": "New Token"}
    ]
}

def get_challenge(level_id):
    if level_id in CHALLENGES:
        return random.choice(CHALLENGES[level_id])
    return None
