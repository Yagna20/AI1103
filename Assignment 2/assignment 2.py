from random import randint
required_outcomes = 0
i=0
while i <= 50000:
  dice1 = randint(1,6)
  dice2 = randint(1,6)
  if dice1<dice2:
    required_outcomes+=1
  i+=1
print("Probablity by simulation:", required_outcomes/50000)
print("Probablity accordint to theory:", 5/12)
print("Error in probablity", 5/12-required_outcomes/50000)
