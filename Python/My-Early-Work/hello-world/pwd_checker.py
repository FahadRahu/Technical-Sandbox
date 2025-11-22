import string
import getpass


# The only aspect changed from the "check_pwd()" function is the use of getpass
# I removed it since it has some compatability with PyCharm, but there's likely a workaround to accomplish pwd privacy
def check_pwd():
    # password = getpass.getpass("Enter Password:  ")  # <-- I disabled the getpass function for now
    # The purpose of using getpass is so that the password shows up as asterisks for privacy, which is a good idea
    # Some IDE's like Pycharm which I use, aren't friendly with getpass without changing some IDE settings
    # I think it might run if running directly from terminal, but in my IDE it doesn't work by default

    # Potential upgrades to this project later could be:
    # 1. Figuring out how to add password privacy features like getpass does - whether using getpass or not
    # 2. Implement a more complex scoring system for how the program judges password strength
    # 3. Add some level of functionality to stop the user from entering common passwords even if the strength is high
    # 4. Give user feedback on aspects they should add/remove/amend from the password they entered.

    password  = input('Enter your password: ')
    print('')
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 2
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Password too weak"
    elif strength == 2:
        remarks = "Password too weak"
    elif strength == 3:
        remarks = "Password Slightly weak"
    elif strength == 4:
        remarks = "Password Slightly strong"
    elif strength == 5:
        remarks = "Strong Password"

    print('Your password has: ', end='\n\n')
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password strength:{strength}")
    print(f"Hint: {remarks}")


def ask_pwd():  # Overhauled the ask_pwd() function

    global pwd_reentry  # <-- "global" lets us access this variable through the entire program
    # The purpose of doing this is so we can "return" what this variable is (True/False) when we define is below.

    print('')  # <-- Added this for formatting purposes so there's a line break between "Hint" and the print below.
    choice = input('Do you want to check another password? (y/n): ')

    choice_check = False  # Variable Checker to see if the user's entry is acceptable
    while not choice_check:  # <-- All this means is "While choice_check is False"

        if choice.upper() == 'Y':
            print('')
            check_pwd()
            # pwd_reentry = True
            # ^^^ We don't need to input this statement since the line above sends us back to start of our code
        elif choice.upper() == 'N':
            pwd_reentry = False  # <-- Variable if the user wants to reenter a pwd: False = "No I don't want to Reenter"
            choice_check = True  # <-- Again, all this does let us exit the while loop we're currently collapsed under
        else:
            print('Invalid choice. Please try again.')
            choice = input('Do you want to check another password? (y/n): ')
            # By default, choice_check remains False
    print('')
    return pwd_reentry


# Overhauled how the file gets executed:
if __name__ == '__main__':  # <-- This alone was causing the program not to run at all
    # There was accidentally a space insertion after the apostrophe.
    # Originally, the code was: "if __name__ == ' __main__'" //  NOW it's: "if __name__ == '__main__'"
    # That singular space at the start of '__main__' was causing the entire program not to run

    print('+++ welcome to PWD checker +++')
    check_pwd()
    pwd_reentry = ask_pwd()  # <-- All this does is set the variable "pwd_reentry" to the value returned by ask_pwd()
    # Since the final statement in "ask_pwd" is "return pwd_reentry" which is either going to be True or False,
    # We can just set the pwd_reentry variable directly above on Line ** to what the "return" of ask_pwd is.

    while pwd_reentry:
        check_pwd()
        ask_pwd()
