from alphabet import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
message = input("Type your message: \n")
shift = int(input("Type the shift number: "))

size = len(message)

def encrypt(message, shift):
    for i in range(size):
       temp = alphabet.index(message[i])
       new = temp + shift - 1
       print(alphabet[new], end="")

encrypt(message, shift)