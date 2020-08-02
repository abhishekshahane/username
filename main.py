import func
"""
Code below this line is to be modified
with the appropriate function calls.
Below is merely an example of how this can
be used.
"""
func.putin("a", "main.com")
func.putin("b", "a.com")
def main():
    a = input("Would you like to display something(Y/N):  ")
    if a == "Y":
        web = input("Enter the exact website you want the username of:  ")
        func.displayout(web)
        again = input("Would you like to get another username(Y/N):  ")
        if again == "Y":
            main()
        elif again == "N":
            print("Save your work.")
            exit()
    elif a == "N":
        print("Save your work.")
        exit()
if __name__ == "__main__":
    main()
