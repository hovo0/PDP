alphabet = "abcdefghijklmnopqrstuvwxyz"  
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

custom_text = "hello world"
shift_value = 3

encrypted = caesar_encrypt(custom_text, shift_value)
decrypted = caesar_decrypt(encrypted, shift_value)

print("Original: ", custom_text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)