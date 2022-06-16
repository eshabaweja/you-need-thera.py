import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# the function definitions
def encrypt(plaintext, offset):
    encoded = ''
    for i in plaintext:
        if i in alphabet:
            encoded += alphabet[alphabet.index(i) + offset]
        else:
            encoded += i
    return encoded

def decrypt(plaintext, offset):
    decoded = ''
    for i in plaintext:
        if i in alphabet:
            decoded += alphabet[alphabet.index(i) - offset]
        else:
            decoded += i
    return decoded

def taking_inputs():
    direction = input("\nType 'encode' to encrypt, 'decode'  to decrypt.\n").lower()
    text = input("\nType your message: ").lower()
    shift_num = int(input("\nEnter the offset number: "))
    if (shift_num > 26):
        shift_num %= 26

    ciphering(direction,text,shift_num)

def ciphering(direction,text,shift_num):
    if direction == 'encode':
        print(f"\nThe encoded result is: {encrypt(text,shift_num)}")
    elif direction == 'decode':
        print(f"\nThe decoded result is: {decrypt(text,shift_num)}")
    else:
        print("Invalid Input. Try again. :)")
        taking_inputs()
    reset_cipher = input("\nType 'yes' to go again, 'no' to exit.\n").lower()
    if reset_cipher == 'yes':
        taking_inputs()
    else:
        print("Exiting...")
        return

# main body
print(caesar_art.logo)
taking_inputs()

