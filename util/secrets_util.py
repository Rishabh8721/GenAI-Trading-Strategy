def get_openai_api_key():
    encryption_key = 5474
    encrypted_key = "ÕÍ­Ä¹Ð²É¨¸ÐÏÅ³ÌÐ¦ÍÄ¯¶¤ÎÄÍ¨¬Ó»ÙÓÏ¶»ÓÛÚÐÑ³Õ·ÛÜ×"
    return _decrypt_key(encrypted_key, encryption_key)


def _decrypt_key(encrypted_key, encryption_key):
    decrypted_chars = []
    for char in encrypted_key:
        decrypted_char = chr((ord(char) - encryption_key) % 256)
        decrypted_chars.append(decrypted_char)
    decrypted_api_key = ''.join(decrypted_chars)
    return decrypted_api_key
