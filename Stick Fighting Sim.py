import random 
import time
import threading
##########
#list 
hit_range = [4, 4, 5, 6, 6, 7, 8, 9, 10]
chance = [1, 2, 3, 4, 5]

#verable
burn = 3
op_health = (50)
health = (50)
block = (5)
fight_stan = ("attack, block")

#functions
def winning():
  if op_health <= 0:
    print("YOU WON")
    exit()
  elif health <= 0:
    print("you lost")
    exit()
#this is the function for the burn feature later down this code line go to 187 for the code
def on_fire():
  for i in range(4):
    global op_health
    while waiting:
      time.sleep(0.00001)
    print("")
    print("Your opponent is on fire there health is {}".format(op_health))
    op_health -= 2
    time.sleep(1) 
#user name input 
print("hello and welcome to Stick Fighting Simulator")
time.sleep(1)
print("")
user_name = input("Can you please input your name ").lower()
if user_name == "jotaro":
  print("")
  print("DIOOO")
else:
  print("")
  time.sleep(0.5)
  print("hello " + user_name)

#this is just a welcome and an explination 
print("")
time.sleep(1)
print("In this simulator you will be fighting a computer")
print("")
print("For you attacking you will be rolling a dice ")
print("")
print("1 to 4 is a hit 5 to 6 is a miss")
time.sleep(2.5)
while True:
  print("")
  p_class = input("Pick your class Normal Fire Earth ").lower()
  if p_class.lower() not in ("fire", "normal", "earth", "broken"):
    print("")
    print("sorry not a class")
    continue
    break
  else:


    #Noraml fighting this is the code for the normal class
    print("")
    time.sleep(0.5)
    if p_class == "normal":
      while True:
        time.sleep(1.3)
        print("")
        fight = input("would you like to attack or block ")
        while fight != "attack" and fight != "block":
          fight = input("would you like to attack or block ")
        if fight == "attack":
          chance = random.randrange(1, 7, 1)
          chance = int(chance)
          print("")
          print("you rolled a {}".format(chance))
#this is for the dice rolling mecanic for where it will read the veriable printed and then decide of it is one of these numbers and if so number what is in said number 
          if chance == 1 and fight == "attack":
            number = random.randint(1, 9) -1
            hit = hit_range[number]
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 2 and fight == "attack":
            number = random.randint(1, 9) -1
            hit = hit_range[number]
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 3 and fight == "attack":
            number = random.randint(1, 9) -1
            hit = hit_range[number]
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 4 and fight == "attack":
            number = random.randint(1, 9) -1
            hit = hit_range[number]
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          elif chance == 5:
            print("you tried to fight but couldn't")
          elif chance == 6:
            print("Your opponent blocked")
        elif fight == "block":
          print("")
          print("your health now is {}".format(health))
        else:
          print("")
          print("sorry that is not a action please do again")

          

        #attacking back
#this is the fighting back it will roll a number between 1 and 2 and if the number is 1 and the user didn't pick block and the roll isn't a 6 then attack back if one of those things are done then don't attack back
        time.sleep(0.5)
        number = random.randint(1, 2)
        if number == 1 and fight != "block" and chance != 6:
          number = random.randint(1, 9) -1
          hit = hit_range[number]
          health -= hit 
          time.sleep(0.2)
          print("")
          print("Your oppent fought back your health is {}".format(health))
        else:
          time.sleep(0.2)
          print("")
          print("Your opponent tried to fight back and couldn't") 
        if op_health <= 0 or health <= 0: 
          break

    fire_hit = [5, 5, 6, 7, 7, 8, 9, 10]

    #Fire attacks this is the code for the fire class
    if p_class == "fire":
      while True:
        time.sleep(0.3)
        print("")
        waiting = True
        fight = input("would you like to attack, block or burn ")
        waiting = False
        while fight != "attack" and fight != "block" and fight != "burn":
          fight = input("would you like to attack or block or burn ")
        if fight == "attack":
          chance = random.randrange(1, 7, 1)
          chance = int(chance)
          print("")
          print("you rolled a {}".format(chance))
#this is the same rolling mechanic for fire just with a different attack strength 
          if chance == 1 and fight == "attack":
            wack = fire_hit[random.randint(0, len(fire_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 2 and fight == "attack":
            wack = fire_hit[random.randint(0, len(fire_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 3 and fight == "attack":
            wack = fire_hit[random.randint(0, len(fire_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 4 and fight == "attack":
            wack = fire_hit[random.randint(0, len(fire_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          elif chance == 5:
            print("you tried to fight but couldn't")
          elif chance == 6:
            print("Your opponent blocked")
#this is block it's pretty self explanitory 
        elif fight == "block":
          print("")
          print("your health now is {}".format(health))
#this is where the special attack is kept this is the burn function when typing burn it will run a start a function that is at the top and make a thread with it attacking each time while everything runs in the back ground and it will wait for a input or next attack to display what the burn as done
        elif fight == "burn":
            x = threading.Thread(target=on_fire)
            time.sleep(0.1)
            x.start()

        else:
          print("")
          print("sorry that is not a action please do again")

          
        #fire attacking back
#this is the same for the normal attack just for the fire class
        time.sleep(0.5)
        number = random.randint(1, 2)
        if number == 1 and fight != "block" and chance != 6:
          number = random.randint(1, 9) -1
          hit = fire_hit[number]
          health -= hit 
          time.sleep(0.2)
          print("")
          print("Your oppent fought back your health is {}".format(health))
        else:
          time.sleep(0.2)
          print("")
          print("Your opponent tried to fight back and couldn't") 
        if op_health <= 0 or health <= 0: 
          break

    earth_hit = [4, 4, 5, 5, 6, 7, 8, 9]
    heal = [5]
    #Earth fighting this is the code for the earth class
    print("")
    time.sleep(0.5)
    if p_class == "earth":
      while True:
        time.sleep(1.3)
        print("")
        fight = input("would you like to attack or block or heal ")
        while fight != "attack" and fight != "block" and fight != "heal":
          fight = input("would you like to attack or block or heal ")
        if fight == "attack":
          chance = random.randrange(1, 7, 1)
          chance = int(chance)
          print("")
          print("you rolled a {}".format(chance))
#this is the same rolling mecanic for all the other classes
          if chance == 1 and fight == "attack":
            wack = earth_hit[random.randint(0, len(earth_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 2 and fight == "attack":
            wack = earth_hit[random.randint(0, len(earth_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 3 and fight == "attack":
            wack = earth_hit[random.randint(0, len(earth_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          if chance == 4 and fight == "attack":
            wack = earth_hit[random.randint(0, len(earth_hit)-1)]
            hit = wack
            op_health -= hit 
            print("")
            print("your opponents health is now {}".format(op_health))
          elif chance == 5:
            print("you tried to fight but couldn't")
          elif chance == 6:
            print("Your oppenent blocked")
        elif fight == "block":
          print("")
          print("your health now is {}".format(health))
#This is the specail attack for the earth class the heal command it will pick a unmber between 1 and 2 and if it is 1 it will start the heal and give a random heal number between 4 and 7 and it will apply it to the player it also can't go above 50 and if the number is 2 it will miss the heal to prevent spam
        elif fight == "heal":
          number = random.randint(1, 2)
          if number == 1:
            heal = random.randrange(4, 7, 1)
            heal = int(heal)
            if health + heal >= 50:
              health = 50
            else:  
              health += heal
            print("your healed your health is now {}".format(health))
          elif number == 2:
            print("Your hand miss healing your wound")
        else:
          print("")
          print("sorry that is not a action please do again")

          

        #attacking back
#this is the same attack just for the earth class aswell 
        time.sleep(0.5)
        number = random.randint(1, 2)
        if number == 1 and fight != "block" and chance != 6:
          number = random.randint(1, 7) -1
          hit = earth_hit[number]
          health -= hit 
          time.sleep(0.2)
          print("")
          print("Your oppent fought back your health is {}".format(health))
        else:
          time.sleep(0.2)
          print("")
          print("Your opponent tried to fight back and couldn't") 
        if op_health <= 0 or health <= 0: 
          break

        #Noraml fighting this is the code for the normal class
    print("")
    time.sleep(0.5)
    if p_class == "broken":
      while True:
        time.sleep(1.3)
        print("")
        fight = input("would you like attack or block ")
        while fight != "attack" and fight != "block":
          fight = input("would you like to attack or block ")
        if fight == "attack":
          op_health -= 50
          print("")
          print("your opponents health is now {}".format(op_health))
        elif fight == "block":
          print("")
          print("your health now is {}".format(health))
        else:
          print("")
          print("sorry that is not a action please do again")

          

        #attacking back
    #this is the fighting back it will roll a number between 1 and 2 and if the number is 1 and the user didn't pick block and the roll isn't a 6 then attack back if one of those things are done then don't attack back
        time.sleep(0.5)
        number = random.randint(1, 2)
        if number == 1 and fight != "block" and chance != 6:
          number = random.randint(1, 9) -1
          hit = hit_range[number]
          health -= hit 
          time.sleep(0.2)
          print("")
          print("Your oppent fought back your health is {}".format(health))
        else:
          time.sleep(0.2)
          print("")
          print("Your opponent tried to fight back and couldn't") 
        if op_health <= 0 or health <= 0: 
          break
    
    #after the break command is active which will happen after the opponents health or your health is bellow 0 then do the winning function
    print = winning()