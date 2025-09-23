from alphabet import alphabet
from art import logo
answer = ""
print(logo)

continue_game = True

while continue_game:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt\n")
    message = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: "))



    def caesar(plain_message, shift_amount, direction):
        cipher_text = ""
        if direction == "decode":
            shift_amount *= -1
        for letter in plain_message:
            if letter in alphabet:    #letter.isalpha():
                temp = alphabet.index(letter) 
                new_position = temp + (shift_amount % 27)
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter

        print(f"The {direction} text is {cipher_text}")


    caesar(plain_message=message, shift_amount=shift, direction=direction)
    answer =  input("Do you want to continue? ").lower()
    if answer == "no":
        continue_game = False
        print("good bye!")



# size = len(message)

# def caesar(plain_message, shift_amount, direction):
#     cipher_text = ""
#     for letter in plain_message:
#        temp = alphabet.index(letter)
#        if direction == "encode":
#           new_position = temp + shift_amount
#        elif direction == "decode":
#           new_position = temp - shift_amount
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#     print(f"The {direction} text is {cipher_text}")
# def encrypt(plain_message, shift_amount):
#     cipher_text = ""
#     for letter in plain_message:
#        temp = alphabet.index(letter)
#        new_position = temp + shift_amount
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#     print(f"The encrypted text is {cipher_text}")
# def decrypt(cipher_text, shift_amount):
#     encode_text = ""
#     for letter in cipher_text:
#         temp = alphabet.index(letter)
#         new_position = temp - shift_amount
#         new_letter = alphabet[new_position]
#         encode_text += new_letter
#     print(f"The encoded text is {encode_text}")

# if direction == "encode":
#     encrypt(plain_message=message, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text = message, shift_amount=shift)
