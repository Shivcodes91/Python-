import random
n=random.randint(1,100) 
a=-1
guesses=1
while(a!=n):
     
     a= int(input("Guess the Number:: "))
     if(a<n):
          print("You are close! just guess a higher Number ")
          guesses+=1
     elif(a>n):
          print("You are close! just guess a lower Number ")
          guesses+=1
          
print(f"Hurrah! You have guessed the number {n} correctly in {guesses} attempts")