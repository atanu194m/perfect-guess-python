import random
'''
stone = 1

paper = 0

scissor = -1

'''

computer = random.choice([-1, 0, 1])
youstr = input("enter your choice:")
youDict = {"s":1,"p":0,"c":-1}
reverseDict = {1:"stone",0:"paper",-1:"scissor"}

you = youDict[youstr]
print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if computer == you:
    print("tie!")
    
else:
    
    if computer == 1 and you == 0:
        print("you win!")
     
    elif computer == 1 and you == -1:
        print("you lose!")
     
    elif computer == 0 and you == -1:
        print("you win!")    
     
    elif computer == 0 and you == 1:
        print("you lose!")
        
    elif computer == -1 and you == 1:
        print("you win!")    
        
    elif computer == -1 and you == 0:
        print("you lose!")   
