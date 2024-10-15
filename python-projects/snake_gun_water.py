import random
'''
1 for snake
-1 for water
0 for gun 
'''

computer=random.choice([-1,0,1])
younum = input("enter your choice: ")
youdict ={"snake":1,"water":-1,"gun":0}
reversedict ={1:"snake",-1:"water",0:"gun"}
you=youdict[younum]
print("You chose "+reversedict[you] )
print("Computer chose " +reversedict[computer])
if(computer==you):
    print("It's Draw!")
else:
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose !")
    elif(computer==1 and you==-1):
        print("You Lose !")
    elif(computer==1 and you==0):
        print("You Win !")    
    elif(computer==0 and you==-1):
        print("You Win !")
    elif(computer==0 and you==1):
        print("You Lose !")
    else:
        print("Something went wrong! ")