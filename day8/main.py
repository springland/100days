def greet( name = 'Jack Bauer'):
    print(f"Hello {name}")
    print("Hello Hello")
    print("Hello Hello Hello")



from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

def encrypt(text , shift):
    encrypted = ""
    for ch in text:

        encrypted_char_index = alphabet.index(ch)
        encrypted_char_index = (encrypted_char_index + shift)% len(alphabet)
        encrypted+= alphabet[encrypted_char_index]
    return encrypted


def decrpty(text , shift):
    decrypted = ""
    for ch in text :
        index = alphabet.index(ch)
        index = (len(alphabet) + index - shift)%len(alphabet)
        decrypted += alphabet[index]

    return decrypted

def caesar(text , shift , direction):
    target = ""
    factor = 1
    if direction == "decode":
        factor = -1

    for ch in text:

        encrypted_char_index = alphabet.index(ch)
        encrypted_char_index = (len(alphabet) + encrypted_char_index + factor * shift)% len(alphabet)
        target+= alphabet[encrypted_char_index]
    return target

print(caesar(text , shift ,direction))