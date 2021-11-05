import random
health=50
difficulty=int(random.randint(1,3))
print(difficulty)
portion_health = int(random.randint(25,50)/difficulty)
health = health + portion_health

