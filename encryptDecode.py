alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart ="yes"
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #If the user enters a number/symbol/space   
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if  (char.isalpha()):
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  return restart 


from encryptDecodeLogo import logo
print(logo)


while (restart =="yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #If the user enters a shift that is greater than the number of letters in the alphabet
    if(shift>26):
        shift = shift%26

    restart=caesar(start_text=text, shift_amount=shift, cipher_direction=direction).lower()
if(restart=="no"):
    print("Goodbye")
