import random
'''
snake = 1  

gun = 0

water = -1

'''

computer = random.choice([-1, 0, 1])
youstr = input("enter your choice:")
youDict = {"s":1,"g":0,"w":-1}
reverseDict = {1:"snake",0:"gun",-1:"water"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if (computer == you):
    print("tie!")


else:
    
   if (computer ==-1 and you ==1):
      print("you win!")
    
   elif (computer ==-1 and you ==0):
      print("you lose!")
    
   elif  (computer == 1 and you ==-1):
      print("you lose!")    
      
    
   elif  (computer == 1 and you ==0):
      print("you win!")   
  
   elif  (computer == 0 and you ==-1):
      print("you win!")    
    
   elif  (computer == 0 and you ==1):
      print("you lose!")
    
   else:
      print ("something went wrong !")
    