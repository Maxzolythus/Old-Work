#Combat and Shop test
#9/15/2014 - 9/16/2014

import random

Rebellion = {'name': 'Rebellion','atack':(7,20),'cost':100}
Gekkou = {'name': 'Gekkou','atack':(8,19),'cost':90}
Dragonslayer = {'name': 'Dragonslayer','atack':(12,22),'cost':150}
#^Defines what weapons the shop is selling

player = {'weapon':None, 'attack': (0,7), 'health':100, 'coins':1000, 'mana':20,
          'bomb': 3} #Defines the player

print("We have",Rebellion['name'],"for",Rebellion['cost']," coins ", Gekkou['name'],
      "for",Gekkou['cost'],"coins","and",Dragonslayer['name'],"for",
      Dragonslayer['cost'])

shopkeep = input("Whatdaja buyin'? ")

weapons = {'Rebellion':(7,20),'Gekkou':(8,19),'Dragonslayer':(12,22)}
#^Makes it easier for storing the weapons' attack power
#Actually I don't need this one, I could use the other arrays...
#It's too far gone.

if shopkeep.upper() in['REBELLION']:
    player['weapon'] = 'Rebellion'
    player['attack'] = weapons['Rebellion']
    player['coins'] -= Rebellion['cost'] #Calulates your new total of coins

elif shopkeep.upper() in['GEKKOU']:
    player['weapon'] = 'Gekkou'
    player['attack'] = weapons['Gekkou']
    player['coins'] -= Gekkou['cost']

elif shopkeep.upper() in['DRAGONSLAYER']:
    player['weapon'] = 'Dragonslayer'
    player['attack'] = weapons['Dragonslayer']
    player['coins'] -= Dragonslayer['cost']

print("Your health is at",player['health'],"your mana is",player['mana'],
      "your weapon is",player['weapon'],"you have",player['coins'],
      "coins left and",player['bomb'],"bombs left.")#Prints your inventory and health

Handsome_Jack = {'name':'Handsome Jack', 'attack': (0,22),'health':150,
                 'mana':(50)}

Maxwell = {'name':'Maxwell','attack':(0,25),'health':90,'mana':100}

Vey_Hek = {'name':'Vey Hek','attack':(5,20),'health':110,'mana':80}

Skelebun = {'name':'Skeleton','attack':(1,15),'health':80, 'mana': 20}
#Defining teh enemies.

def combat(player,enemy): #Defining the low and high attacks as well as what the enemy is and its health and your health plus a roll for intiative system.
    #low_a,high_a,enemy[num], health, e_health, die, e_die, mana
    print("A wild", enemy['name'],"is attacking you!")
    die = random.randint(1,20)
    e_die = random.randint(1,20)
   
    while enemy['health'] > 0:
        if die > e_die: #If you go first
            WDYD = input("You have the intiative, what do you do? ")
        
            if WDYD.upper() in ["ATTACK"]:
                your_attack = random.randint(*player['attack'])
                enemy['health'] -= your_attack
                if enemy['health'] > 0:
                    print("The enemy's health is:",enemy['health'])
                die = 19
                e_die = 20 #Setting up turns
                
            if WDYD.upper() in ["MAGIC"]:
                your_attack = random.randint(*player['attack'])
                enemy['health'] -= your_attack
                if enemy['health'] > 0:
                    print("The enemy's health is:",enemy['health'])
                player['mana'] -= 2
                print("You have",player['mana'],"mana remaining.")
                if player['mana'] < 0:
                    print("Out of mana.")
                die = 19
                e_die = 20
                
            if WDYD.upper() in ["BOMB"]:
                if player['bomb'] > 0:
                    your_attack = random.randint(0,100)
                    enemy['health'] -= your_attack
                    if enemy['health'] > 0:
                        print("The enemy's health is:",enemy['health'])
                    player['bomb'] -= 1
                if player['bomb'] < 0:
                    print("You are out of bombs.")
                die = 19
                e_die = 20
            
                
        elif e_die > die: #If the enemy goes first
            print("The enemy is attacking!")
            e_attack = random.randint(*enemy['attack'])
            player['health'] -= e_attack
            if player['health'] > 0:
                print("Your health is: ",player['health'])
            die = 20
            e_die = 19 #Setting up turns
            
    if enemy['health'] <= 0:
        print("You Defeated.")
    if player['health'] <= 0:
        print("You have been vanquished.")
        
            
#num = random.randint(0,3)
#enemy = ["spider","soldier","skeleton","Handsome Jack"] #Enemy names
        
sub = random.randint(0,3)

enemy = [Handsome_Jack,Skelebun,Maxwell,Vey_Hek]

opp = enemy[sub]

combat(player,opp)
  
