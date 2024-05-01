import random
import string
import shutil
import pyperclip as pc
import os

os.system('title PyPass V2 @ Rotenda Sino')

restart_script = True

while restart_script:
    SL = ("----------------------------------------------------------------------------")
    print(SL)
    print("Password Generator V1 @ Rotenda Sino")

    def generate_password(length, include_letters, include_numbers, include_symbols):
        characters = ''

        if include_letters == 'Y':
            characters += string.ascii_letters
        if include_numbers == 'Y':
            characters += string.digits
        if include_symbols == 'Y':
            ascii_punctuation = ''.join(char for char in string.punctuation if char.isascii() and char not in '')
            characters += ascii_punctuation

        if not characters:
            print(SL)
            print("Error: Select At Least One Parameter (Letters, Numbers, Symbols)")
            return None

        return ''.join(random.choice(characters) for _ in range(length))

    while True:
        names = {'Y': 'Yes', 'N': 'No'}
        messages = {'Y': ' ', 'N': ''}

        print(SL)
        chosen_length = input("Length: ")  
    
        if chosen_length.isdigit() and int(chosen_length) > 0:
            formatted_length = "{:,}".format(int(chosen_length)).replace(",", ".")
            print(SL)
            print(f"{formatted_length} Digits Have Been Selected")
            print(SL)
        
        else:
            print(SL)
            print("Error: Length Has To Be A Positive Number")
            continue  # go back to the beginning of the loop

        want_letters = input("Letters? 'Y'es 'N'o: ").upper()

        while want_letters not in ['Y', 'N']:
            print(SL)
            print("Error: Select Either 'Y'es or 'N'o ")
            print(SL)
            want_letters = input("Letters? 'Y'es 'N'o: ").upper()

        if want_letters == 'Y':
            print(SL)
            print("Letters Will Be Included")
            print(SL)

        elif want_letters == 'N':
            print(SL)
            print("Letters Won't Be Included")
            print(SL)

        else:
            continue  # go back to the beginning of the loop

        want_numbers = input("Numbers? 'Y'es 'N'o: ").upper()

        while want_numbers not in ['Y', 'N']:
            print(SL)
            print("Error: Select Either 'Y'es or 'N'o ")
            print(SL)
            want_numbers = input("Numbers? 'Y'es 'N'o: ").upper()

        if want_numbers == 'Y':
            print(SL)
            print("Numbers Will Be Included")
            print(SL)

        elif want_numbers == 'N':
            print(SL)
            print("Numbers Won't Be Included")
            print(SL)

        else:
            continue  # go back to the beginning of the loop

        want_symbols = input("Symbols? 'Y'es 'N'o: ").upper()

        while want_symbols not in ['Y', 'N']:
            print(SL)
            print("Error: Select Either 'Y'es or 'N'o ")
            print(SL)
            want_symbols = input("Symbols? 'Y'es 'N'o: ").upper()

        if want_symbols == 'Y':
            print(SL)
            print("Symbols Will Be Included")
            print(SL)

        elif want_symbols == 'N':
            print(SL)
            print("Symbols Won't Be Included")
            print(SL)

        else:
            continue  # go back to the beginning of the loop

        print("Your Configuration:")
        terminal_width, _ = shutil.get_terminal_size()
        total_width = len(" Password Length : 55")  
        spaces = (terminal_width - total_width) // 2
        generated_password = generate_password(int(chosen_length), want_letters, want_numbers, want_symbols)

        if generated_password is None:
            continue  # go back to the beginning of the loop

        print(f"Password Length: {formatted_length}")
        print(f"Letters: {names[want_letters]}{messages[want_letters]}")
        print(f"Numbers: {names[want_numbers]}{messages[want_numbers]}")
        print(f"Symbols: {names[want_symbols]}{messages[want_symbols]}")
        print(SL)
        
        password_generated = False  # Flag to check if the password was generated successfully
        generate_again = True  # Flag to check if the user wants to generate another password

        while True:
            
            want_generate = input("Generate Password? 'Y'es or 'N'o: ").upper()

            if want_generate == 'Y':
                print(SL)
                print("Generated Password:")
                print(SL)
                print("")
                print(generated_password)
                print("")
                password_generated = True  # Set the flag to True
            
            elif want_generate == 'N':
                print(SL)
                print("Password Won't Be Generated")
                print(SL)
                break  # exit loop
            
            else:
                print(SL)
                print("Error: Select Either 'Y'es or 'N'o ")
                print(SL)
                continue  # go back to the beginning of the loop

            while True:
                want_copy_clipboard = input("Copy To Clipboard? 'Y'es 'N'o: ").upper()
                
                if want_copy_clipboard == 'Y':
                    print(SL)
                    print("Password Has Been Copied To Clipboard")
                    print(SL)
                    clipboard = generated_password
                    pc.copy(generated_password)
                    generate_again = False  # Set the flag to False to prevent generating another password
                    break  # exit loop and ask for length again
                    
                elif want_copy_clipboard == 'N':
                    print(SL)
                    print("Password Has Not Been Copied To Clipboard")
                    print(SL)
                    generate_again = False
                    break  # exit loop and ask for length again

                else:
                    print(SL)
                    print("Error: Select Either 'Y'es or 'N'o ")
                    print(SL)

            if not generate_again:
                break  # exit the password generation loop

        while True:
            want_generate_again = input("Generate Again? 'Y'es 'N'o: ").upper()

            if want_generate_again == 'Y':
                password_generated = False  # Reset the flag for the new password generation
                break  # exit loop and generate another password

            elif want_generate_again == 'N':
                restart_script = False  # Set the flag to False to exit the entire script
                exit()  # close the entire program

            else:
                print(SL)
                print("Error: Select Either 'Y'es or 'N'o ")
                print(SL)

        if password_generated:  # Prompt to generate another password only if a password was successfully generated
            print(SL)
            print("Generate Password Again")
            print(SL)
