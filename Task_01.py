def caesar_cipher_encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet using modulo 26
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_text += encoded_char
        else:
            # Non-alphabet characters are added without encoding
            encoded_text += char
    return encoded_text

# Decoded 
def caesar_cipher_decode(encoded_text, shift):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Reverse the shift using modulo 26
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_text += decoded_char
        else:
            # Non-alphabet characters are added without decoding
            decoded_text += char
    return decoded_text

print("Do you want encrept or decrept? ")
user_input = input("e/d").lower()
print()
if user_input == 'e':
    print('Encryption mode selected')
    print()
    text = input("Enter the encryped text: ")
    shift = int(input("Enter the key valu: "))
    encoded_text = caesar_cipher_encode(text, shift)
    print(f"Encoded Text: {encoded_text}")
elif user_input == 'd':
    print("Decryption mode selected")
    print()
    text = input("Enter the decryped text: ")
    shift = int(input("Enter the key valu: "))
    decoded_text = caesar_cipher_decode(text, shift)
    print(f"Decoded Text: {decoded_text}")
