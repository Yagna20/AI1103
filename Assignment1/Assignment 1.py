from random import randint
required_outcomes = 0
required=0
i=0
while i <= 50000:
  male1 = randint(0,1)
  male2 = randint(0,1)
  if male1 == 1 and male2 == 1:
    required_outcomes+=1
  if male1 == 1 or male2 == 1:
    required+=1
    
  i+=1
print("(i)")
print("Probablity by simulation:", required_outcomes/50000)
print("Probablity accordint to theory:", 1/3)
print("Error in probablity", 1/3-required_outcomes/50000)
required_outcomes = 0
i=0
while i <= 50000:
  female1 = 1
  female2 = randint(0,1)
  if female1==female2:
    required_outcomes+=1    
  i+=1
print("(ii)")
print("Probablity by simulation:", required_outcomes/50000)
print("Probablity accordint to theory:", 1/2)
print("Error in probablity", 1/2-required_outcomes/50000)
