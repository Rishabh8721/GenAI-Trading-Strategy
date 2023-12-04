def get_openai_api_key():
    encryption_key = 5474
    encrypted_key1 = "ÕÍ­Ä¹Ð²É¨¸ÐÏÅ³ÌÐ¦ÍÄ¯¶¤ÎÄÍ¨¬Ó»ÙÓÏ¶»ÓÛÚÐÑ³Õ·ÛÜ×"
    encrypted_key2 = "ÕÍÛª³ªÚ£ªÐÕº¨Ç®ÖÄÐ¶¤ÎÄÍ¨¬ËÈ¼É»¯¶»ÇºÙÆÑ"
    return _decrypt_key(encrypted_key2, encryption_key)


def _decrypt_key(encrypted_key, encryption_key):
    decrypted_chars = []
    for char in encrypted_key:
        decrypted_char = chr((ord(char) - encryption_key) % 256)
        decrypted_chars.append(decrypted_char)
    decrypted_api_key = ''.join(decrypted_chars)
    return decrypted_api_key


def _encrypt_key(api_key, encryption_key):
    encrypted_chars = []
    for char in api_key:
        encrypted_char = chr((ord(char) + encryption_key) % 256)
        encrypted_chars.append(encrypted_char)
    encrypted_api_key = ''.join(encrypted_chars)
    return encrypted_api_key
