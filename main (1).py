encoded_password = ""

def encode(password):
    global encoded_password
    encoded_password = ''.join(str((int(num) + 3) % 10) for num in password)
    return encoded_password


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            if password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")

        elif choice == '2':
            if encoded_password:
                decoded_password = decode()
                print(f"The encoded password is {encoded_password} and the original password is {decoded_password}:")

            else:
                print("No password has been encoded yet. Please encode a password first.")

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose from the menu.")


if __name__ == "__main__":
    main()
