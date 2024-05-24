from art import logo
print(logo)

def caesar(direction, text, shift):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            final_text += alphabet[new_index]
        else:
            final_text += letter
    print(final_text)

user_restart = True

while user_restart == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    choice = input("Do you want to restart the cipher program?\nType 'yes' if you want to go again. Otherwise type 'no'.\n") 
    if choice == "no":
        print("Goodbye!")
        user_restart = False