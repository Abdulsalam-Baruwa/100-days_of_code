alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''def encrypt(plain_text, shift_amount):
    encrypted_text = []

    for letter in plain_text:
        position = alphabet.index(letter) + shift_amount

        encrypted_text.append(alphabet[position])
    print(f"The encoded text is: {''.join(encrypted_text)}")

def decrypt(cipher_text, shift_amount):
    decrypted_text = []

    for letter in cipher_text:
        position = alphabet.index(letter) - shift_amount
        
        decrypted_text.append(alphabet[position])
    print(f"The decoded text is: {''.join(decrypted_text)}")

if direction == 'encode':

    #keyword argument
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)

'''

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            shift_amount = shift * (-1)
        new_position = position + (shift_amount)
        end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    
            
