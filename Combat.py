#Quick Combat Test
#9/9/2014

import random

def combat(enemy): #Defining the low and high attacks as well as what the enemy is and its health and your health plus a roll for intiative system.
    #low_a,high_a,enemy[num], health, e_health, die, e_die, mana
    print("A wild", enemy,"is attacking you!")
    health = 100
    e_health = 10
    die = random.randint(1,20)
    e_die = random.randint(1,20)
    low_a= 0
    high_a= 20
    mana = 20
    while e_health > 0:
        if die > e_die: #If you go first
            WDYD = input("You have the intiative, what do you do? ")
        
            if WDYD.upper() in ["ATTACK"]:
                your_attack = random.randint(low_a,high_a)
                e_health -= your_attack
                if e_health > 0:
                    print("The enemy's health is:",e_health)
                die = 19
                e_die = 20 #Setting up turns
                
            if WDYD.upper() in ["MAGIC"]:
                your_attack = random.randint(low_a + 1,high_a + 5)
                e_health -= your_attack
                if e_health > 0:
                    print("The enemy's health is:",e_health)
                mana -= 2
                print("You have ", mana," mana remaining.")
                if mana < 0:
                    print("Out of mana.")
                die = 19
                e_die = 20

            if WDYD.upper() in ["BOMB"]:
                your_attack = random.randint(0,high_a + 10)
                e_health -= your_attack
                if e_health > 0:
                    print("The enemy's health is:",e_health)
                die = 19
                e_die = 20
                
        elif e_die > die: #If the enemy goes first
            print("The enemy is attacking!")
            e_attack = random.randint(low_a,high_a)
            health -= e_attack
            if health > 0:
                print("Your health is: ",health)
            die = 20
            e_die = 19 #Setting up turns
            
    if e_health <= 0:
        print("You Defeated.")
    if health <= 0:
        print("You have been vanquished.")
            
num = random.randint(0,3)
enemy = ["spider","soldier","skeleton","Handsome Jack"] #Enemy names
combat(enemy[num])    

            
            
            
    
    
    
