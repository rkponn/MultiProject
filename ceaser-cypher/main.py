alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shift):
    cipher = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position -= 26
        cipher += alphabet[new_position]
    print(f"The encoded text is {cipher}")

def decrypt(message, shift):
    cipher = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_position += 26
        cipher += alphabet[new_position]
    print(f"The decoded text is {cipher}")

if direction == "encode":
    encrypt(message, shift)
else:
    decrypt(message, shift)


