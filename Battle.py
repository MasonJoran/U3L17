import time
import random

print('-'*65)
print()

print('Welcome to the mock Pokemon battle! You will be battling another trainer and their 6 Pokemon with your own! ')
time.sleep(0.5)
print('Good luck!')
time.sleep(0.5)
print()
print('                    ...Commencing Pokemon battle...                    ')
time.sleep(0.5)
time.sleep(0.5)
print('-'*65)


print()
print('You have been challenged by your rival! Prepare to battle! ')
time.sleep(0.2)
print()
print('Go! Gengar! ')
time.sleep(0.2)
print()
print('Your opponent sent out Charizard! ')
time.sleep(0.5)
print('-'*65)

#Health values of the players pokemon
Gengar_hp = 150
#Health values of the players pokemon

#

#Health values of the enemys pokemon
Charizard_hp = 250
#Health values of the enemys pokemon

current_pokemon = 'Gengar'
rival_pokemon = 'Charizard'

if current_pokemon == 'Gengar':
	current_pokemonhp = Gengar_hp
if rival_pokemon == 'Charizard':
	enemy_pokemonhp = Charizard_hp
print()
print()
print(current_pokemon + ' HP: ' + str(current_pokemonhp))
print(rival_pokemon + ' HP: ' + str(enemy_pokemonhp))	
print()	
print()	

while current_pokemonhp >= 0 and enemy_pokemonhp >= 0:
		
	rival_attack = random.randint(1,4)
	rival_attack = str(rival_attack)

		
	if current_pokemon == 'Gengar':

		print('-'*15)
		print('1' + ': Shadow Ball')
		print('2' + ': Lick ')
		print('3' + ': Mega Drain ')
		print('4' + ': Fire Punch ')
		print('-'*15)
		print()
		attack = input('Please choose your attack from above with the corresponding number!: ')
		print()
		print('-' *65)

		
		if attack ==  '1':
			enemy_pokemonhp = enemy_pokemonhp - 45
			print()
			print('Your Gengar uses Shadow Ball! It deals 45 damage!')
			print()

		if attack ==  '2':
			enemy_pokemonhp = enemy_pokemonhp - 30
			print()
			print('Your Gengar uses Lick! It deals 30 damage!')
			print()

		if attack ==  '3':
			current_pokemonhp = current_pokemonhp + 35
			if current_pokemonhp > 150:
				current_pokemonhp = 150
			enemy_pokemonhp = enemy_pokemonhp - 25
			print()
			print('Your Gengar uses Mega Drain! It deals 25 damage and Gengar recovers 35 health!')
			print()

		if attack ==  '4':
			enemy_pokemonhp = enemy_pokemonhp - 50			
			print()
			print('Your Gengar uses Fire Punch! It deals 50 damage! ')
			print()

		while attack not in ['1', '2', '3', '4']:
			print('That is not a valid attack! Choose an attack!')
			print()
			attack = input('Please choose your attack from above with the corresponding number!: ')
			print()



	if rival_pokemon == 'Charizard':

		if rival_attack ==  '1':
			current_pokemonhp = current_pokemonhp - 50
			print()
			print('Enemy Charizard uses Flamethrower! It deals 45 damage!')
			print()
			print()	
			
		if rival_attack ==  '2':
				current_pokemonhp = current_pokemonhp - 35
				print()
				print('Enemy Charizard uses Bite! It deals 35 damage!')


		if rival_attack ==  '3':
			current_pokemonhp = current_pokemonhp - 30
			print()
			print('Enemy Charizard uses Fly! It deals 30 damage!')
			
		if rival_attack ==  '4':
			current_pokemonhp = current_pokemonhp - 65	
			print()
			print('Enemy Charizard uses Dragon Rage! It deals 65 damage! ')

	print()
	print()
	print(current_pokemon + ' HP: ' + str(current_pokemonhp))
	print()
	print(rival_pokemon + ' HP: ' + str(enemy_pokemonhp))	
	print()	
	print()	

		
		

		



