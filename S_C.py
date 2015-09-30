import random
# instead of using an if/then tree, first we store the damage range 
# of all the weapons in the game
WEAPONS = {'stick': (3, 10), None:(1,8), 'knife':(4,16)}

#and instead of tracking inventory with one variable, have a 'player' who
# has stuff in a dictionary:

player = {'weapon':None, 'health': None}

#to give the player stuff, you add it to his dictionary:

player['weapon'] = 'stick'

# while we're at it, we can treat the monsters the same way:

SPIDER = {name:'spider', 'health':5, 'attack':(1, 5) } 

# so for any given fight there's a player and an enemy:
# and two possible outcomes for each combatant. You'll want to report 
# the damage (which varies) and the result:

def combat (player, enemy):
    player_damage = random.range(*WEAPONS[player['weapon']])
    enemy_damage = random.range(*enemy['attack'])

    player_win = player_damage > enemy['health']
    enemy_win= enemy_damage  > player['health']

    return player_damage, player_win , enemy_damage, enemy_win

# of course, you also want flavor text. So you can set that up as another dictionary.
# you might want to make different dictionaries for different parts of the game
# to give a different flavor to the fights as you did above:

SIMPLE_FIGHT = {
player_damage: 'You hit the %s for %i damage',
enemy_damage: '%s hits you for %i damage',
player_win: 'The %s dies!',
enemy_win: 'You die!'
}

def describe_combat(player, enemy, fight_description):
   player_damage, player_win , enemy_damage, enemy_win = combat(player, enemy)

   print(fight_description['player_damage'] % (enemy['name'], player_damage))
   print(fight_description['enemy_damage'] % (enemy['name'], enemy_damage))

   if player_win:
      print (fight_description['player_win'] % enemy['name'])
      return True

   if enemy_win:
      print (fight_description['player_win'] % enemy['name'])
      return False
   return None # this means a draw :)


 # with that in place, you can play out a fight like so:


fight_result = describe_combat(player, SPIDER, SIMPLE_FIGHT)
if fight_result is None:
    print()
# what do you do for draws?
elif fight_result:
    print()
# you've won.
else:
    print()
