from alphabet import alphabet

direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt\n")
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number: "))

# size = len(message)

def encrypt(message, shift):
    cipher_text = ""
    for letter in message:
       cipher_text = ""
       temp = alphabet.index(letter)
       new_position = temp + shift
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(message, shift)