--Combat and Shop test Lua transfer
--10/14/2014 - 10/22/2014
name = 1
weapon = 1
attack = 2
l_attack = -2
h_attack = 2
cost = 3
health = 3
coins = 4
mana = 5
bombs = 6

Rebellion = {[name] = "Rebellion",[l_attack] = 7, [h_attack] = 20 ,[cost] = 100}
Gekkou = {[name]="Gekkou",[l_attack]=8,[h_attack]=19,[cost]=90}
Dragonslayer = {[name]= "Dragonslayer",[l_attack]=12,[h_attack]=22,[cost]=150}


player = {[weapon]=None, [l_attack]=0,[h_attack]=7, [health]=100, [coins]=1000, [mana]=20,
          [bombs]=3}

print(string.format("We have %s for %s coins,%s for %s coins, and %s for %s coins.",
      Rebellion[name],Rebellion[cost],Gekkou[name],Gekkou[cost],
	  Dragonslayer[name],Dragonslayer[cost]))

io.flush()
print("Whatdaja buyin'? ")
shopkeep = io.read():upper()

--weapons = {[1]=(7,20),[2]=(8,19),[3]=(12,22)}

if shopkeep == "REBELLION" then
    player[weapon] = 'Rebellion'
    player[l_attack] = Rebellion[l_attack]
	player[h_attack] = Rebellion[h_attack]
    player[coins] =  player[coins] - Rebellion[cost]


elseif shopkeep == "GEKKOU" then
    player[weapon] = 'Gekkou'
    player[l_attack] = Gekkou[l_attack]
	player[h_attack] = Gekkou[h_attack]
    player[coins] =  player[coins] - Gekkou[cost]


elseif shopkeep == "DRAGONSLAYER" then
    player[weapon] = 'Dragonslayer'
    player[l_attack] = Dragonslayer[l_attack]
	player[h_attack] = Dragonslayer[h_attack]
    player[coins] =  player[coins] - Dragonslayer[cost]
end

print(string.format("Your health is at %s your mana is %s your weapon is %s you have %s coins left and %s bombs left."
,player[health],player[mana],player[weapon],player[coins],player[bombs]))--Prints your inventory and health


Handsome_Jack = {[name]='Handsome Jack', [l_attack]= 0,[h_attack]=22,[health]=150,[mana]=(50)}
Maxwell = {[name]='Maxwell',[l_attack]=0,[h_attack]=25,[health]=90,[mana]=100}
Vey_Hek = {[name]='Vey Hek',[l_attack]=5,[h_attack]=20,[health]=110,[mana]=80}
Skelebun = {[name]='Skeleton',[l_attack]=1,[h_attack]=15,[health]=80, [mana]= 20}
--Defining teh enemies.

function combat(player,enemy) --Defining the low and high attacks as well as what the enemy is and its health and your health plus a roll for intiative system.low_a,high_a,enemy[num], health, e_health, die, e_die, mana

	local name = 1
	local weapon = 1
	local attack = 2
	local l_attack = -2
	local h_attack = 2
	local cost = 3
	local health = 3
	local coins = 4
	local mana = 5
	local bombs = 6

	local enemy = {[name]='Maxwell',[l_attack]=0,[h_attack]=25,[health]=90,[mana]=100}

	print("A wild "..enemy[name].." is attacking you!")
    die = math.random(1,20)
    e_die = math.random(1,20)

    while enemy[health] > 0 do
        if die > e_die then --If you go first
			io.flush()
            print("You have the intiative, what do you do? ")
			WDYD = io.read():upper()

            if WDYD == "ATTACK" then
                your_attack = math.random(player[l_attack],player[h_attack])
                enemy[health] = enemy[health] - your_attack
                if enemy[health] > 0 then
                    print(string.format("The enemy's health is: %s",enemy[health]))
                end
				die = 19
                e_die = 20 --Setting up turns
			end

            if WDYD == "MAGIC" then
                your_attack = math.random(player[attack])
                enemy[health] = enemy[health] - your_attack
                if enemy[health] > 0 then
                    print("The enemy's health is:",enemy['health'])
                end
				player[mana] = player[mana] - 2
                print(string.format("You have %s mana remaining.",player[mana]))
                if player[mana] < 0 then
                    print("Out of mana.")
                end
				die = 19
                e_die = 20
			end
            if WDYD == "BOMB" then
                if player[bombs] > 0 then
                    your_attack = math.random(0,100)
                    enemy[health] = enemy[health] - your_attack
                    if enemy[health] > 0 then
                        print(string.format("The enemy's health is: %s",enemy[health]))
                    end
					player[bombs] = player[bombs] - 1
				end
                if player[bombs] < 0 then
                    print("You are out of bombs.")
				end
                die = 19
                e_die = 20
			end
		end
        if e_die > die then --If the enemy goes first
            print("The enemy is attacking!")
            e_attack = math.random(enemy[l_attack],enemy[h_attack])
            player[health] = player[health] - e_attack
            if player[health] > 0 then
                print(string.format("Your health is: %s",player[health]))
			end
            die = 20
            e_die = 19 --Setting up turns
		end
	end

    if enemy[health] <= 0 then
        print("You Defeated.")
	end
    if player[health] <= 0 then
        print("You have been vanquished.")
	end
end



sub = math.random(0,3)

enemy = {Handsome_Jack,Skelebun,Maxwell,Vey_Hek}

opp = enemy[sub]

combat(player,opp)
