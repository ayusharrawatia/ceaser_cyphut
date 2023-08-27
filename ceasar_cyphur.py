alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text,shift,direction):
    
    if direction == "encode":
        encrypted_text=""  
        for i in text:
            if i in alphabet:
                position=alphabet.index(i)    
                new_position=position+shift
                new_text=alphabet[new_position]
                encrypted_text+=new_text
            else:
                encrypted_text+=i
        print(f"The encoded text is {encrypted_text}")

    elif direction == "decode":
        decrypted_text=""
        for i in text:
            if i in alphabet:
                n=1
                position=alphabet.index(i)
                new_position=position-shift
                new_text=alphabet[new_position]
                decrypted_text+=new_text
            else:
                decrypted_text+=i
        print(f"The decoded text is {decrypted_text}")
    
condition = True  
while condition:
    choice=input("Type 'y' to continue 'q' to exit :")
    if choice == "q":
        condition = False
    elif choice == "y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        ceaser(text,shift,direction)
    else:
        print("Invalid Choice")

