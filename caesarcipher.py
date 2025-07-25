def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

text = "Hello, World! 123"
key = 3

encrypted_text = caesar_cipher(text, key, 'encrypt')
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, -key, 'decrypt')
print(f"Decrypted: {decrypted_text}")
