def caesar_encrypt(text: str, shift_value: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in text:
        alpha_i = alphabet.find(char)
        index = (alpha_i + shift_value) % (len(alphabet))
        encrypted += alphabet[index]

    return encrypted


def caesar_decrypt(text: str, shift_value: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for char in text:
        alpha_i = alphabet.find(char)
        index = (alpha_i - shift_value) % (len(alphabet))
        decrypted += alphabet[index]

    return decrypted
