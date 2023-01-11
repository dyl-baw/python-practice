alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def caesar(text, shift, cipher_direction):
#     final_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if cipher_direction == "encode":
#             new_position = position + shift
#             if new_position > 25:
#                 new_position = new_position - 25
#             new_letter = alphabet[new_position]
#             final_text += new_letter
#             print(f"The endcoded text is {final_text}")
#         if cipher_direction == "decode":
#             old_position = position - shift
#             if old_position < 0:
#                 old_position = old_position + 25
#             old_letter = alphabet[old_position]
#             final_text += old_letter
#             print(f"The decrypted text is {decrypted_text}")

def encrypt(text, shift):
    encrypted_text = ""
    for letters in text:
        current_position = alphabet.index(letters)
        new_position = current_position + shift
        if new_position > 25:
            new_position = new_position - 25
        new_letter = alphabet[new_position]
        encrypted_text += new_letter
    print(f"The endcoded text is {encrypted_text}")


def decrypt(text, shift):
    decrypted_text = ""
    for letters in text:
        current_position = alphabet.index(letters)
        old_position = current_position - shift
        if old_position < 0:
            old_position = old_position + 25
        old_letter = alphabet[old_position]
        decrypted_text += old_letter
    print(f"The decrypted text is {decrypted_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You have chosen an invalid option.")