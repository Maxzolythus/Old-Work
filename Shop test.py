#Shop test
#9/15/2014

#weapons = { None:(0,7), 'Rebellion':(7,20),'Gekkou':(8,19),
#           'Dragonslayer':(12,22)}

Rebellion = {'name': 'Rebellion','atack':(7,20),'cost':100}
Gekkou = {'name': 'Gekkou','atack':(8,19),'cost':90}
Dragonslayer = {'name': 'Dragonslayer','atack':(12,22),'cost':150}

#Defines what weapons the shop is selling
player = {'weapon':None, 'health':100, 'coins':1000} #Defines the player

print("We have",Rebellion['name'],"for",Rebellion['cost']," coins ", Gekkou['name'],
      "for",Gekkou['cost'],"coins","and",Dragonslayer['name'],"for",
      Dragonslayer['cost'])

shopkeep = input("Whatdaja buyin'? ")

if shopkeep.upper() in['REBELLION']:
    player['weapon'] = 'Rebellion'
    player['coins'] -= Rebellion['cost'] #Calulates your new total of coins

elif shopkeep.upper() in['GEKKOU']:
    player['weapon'] = 'Gekkou'
    player['coins'] -= Gekkou['cost']

elif shopkeep.upper() in['DRAGONSLAYER']:
    player['weapon'] = 'Dragonslayer'
    player['coins'] -= Dragonslayer['cost']

print(player)#Prints your inventory and health


