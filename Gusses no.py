import random
n= random.randint(1,100)
a = -1  
guesses = 1

while(a!=n):
    a = int(input("Gusses the number :"))
    if (a>n):
        print("Lower number plaese ")
        guesses +=1
        
    elif (a<n):
        print("Higher number please ")
        guesses +=1
        
print(f"Congratulations you gussed the number {n} in {guesses} attempts")
        
    