from alphabet import alphabet

direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt\n")
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number: "))

# size = len(message)


def encrypt(plain_message, shift_amount):
    cipher_text = ""
    for letter in plain_message:
       temp = alphabet.index(letter)
       new_position = temp + shift_amount
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f"The encrypted text is {cipher_text}")
def decrypt(cipher_text, shift_amount):
    encode_text = ""
    for letter in cipher_text:
        temp = alphabet.index(letter)
        new_position = temp - shift_amount
        new_letter = alphabet[new_position]
        encode_text += new_letter
    print(f"The encoded text is {encode_text}")

if direction == "encode":
    encrypt(plain_message=message, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text = message, shift_amount=shift)
