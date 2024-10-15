import sys
import random
def main():
    print("--------------------------------------------------------------------------------------------")
    print("Welcome to rock paper scissor")
    print("Type rock, paper or scissor")
    base = ["rock","paper","scissor"]
    youstr = input("Enter your choice: ")
    if (youstr.lower() not in base):
        user2=input("invalid input please try again(avoid spaces)")
        print("Press enter to restart")
        if(user2==""):
            main()
            return
        else:
            sys.exit()
    computer=random.randint(1,3)
    youdict={"rock":1,"paper":2,"scissor":3}
    reverse_youdict={1:"rock",2:"paper",3:"scissor"}
    you=youdict.get(youstr.lower())
    print(f"You chose {youstr}\nComputer chose {reverse_youdict[computer]}")
    if(you==computer):
        print("Its a draw!")
    else:
        if(you==1 and computer==3):
            print("You win!")
        elif(you==1 and computer==2):
            print("You loose!")
        elif(you==2 and computer==1):
            print("You win!")
        elif(you==2 and computer==3):
            print("You loose!")
        elif(you==3 and computer==1):
            print("You loose!")
        elif(you==3 and computer==2):
            print("You win!")
    user=input("would you like to try again?\nType 'Yes' to restart or don't to exit: ")
    if(user.lower()=="yes"):
                  print("Restarting the program...")
                  main()
    else:
        input("Thankyou for playing,\nPress enter to exit")
        
        sys.exit()
main()
