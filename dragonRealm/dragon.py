import random
import time

won = 0
totLoot = 0

def displayIntro():
	print()
	print()
	print()
	print('You are in a land full of dragons. In front of you,')
	print('you see two caves. In one cave, the dragon is friendly')
	print('and will share his treasure with you. The other dragon')
	print('is greedy and hungry, and will eat you on sight.')
	print()
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
		
	return cave

def chooseCaveDescript():
	caveD = random.randint(1,5)
	theCave = {
		1:'dark and spooky...', 
		2:'dank and smelly', 
		3:'clean and tidy...', 
		4:'eerily familiar...',
		5:'shockingly modern styled...'
	}
	return str(theCave[caveD])

def chooseDragonDescript():
	dragonD = random.randint(1,5)
	dragonD1 = random.randint(1,5)
	dragonSize = {
		1:' large',
		2:' small',
		3:'n average',
		4:' baby',
		5:' tiny'
	}
	dragonAdj = {
		1:'angry',
		2:'nervous',
		3:'skeletal',
		4:'horned',
		5:'racist'	
	}
	return str(dragonSize[dragonD] + ' ' + dragonAdj[dragonD1])	

def chooseLootDescript():
	lootD = random.randint(1,5)
	lootD1 = random.randint(1,3)
	lootAdj = {
		1:'shiny',
		2:'scuffed',
		3:'broken',
		4:'confusing',
		5:'useful'	
	}	
	lootName = {
		1:'collectable card',
		2:'golden cup',
		3:'sword',
		4:'stuff',
		5:'golden plates'	
	}
	lootType = {
		1:'collection',
		2:'stash',
		3:'pile'	
	}
	return str(lootAdj[lootD1] + ' ' + lootName[lootD] + ' ' + lootType[lootD1])
	
def getLoot():
	lootMult = 1
	lootLuck = random.randint(1, 500)
	
	if lootLuck > 350:
		lootMult = 3
		print('This dragon is more generous than average and')
	if lootLuck == 500:
		lootMult = 6
		print('Wow this is a very generous dragon!')
	
	theLoot = random.randint(1, 20)
	
	return lootMult * theLoot

def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	chosenDescript = chooseCaveDescript()
	print('It is ' + chosenDescript)
	time.sleep(2)
	dragonKind = chooseDragonDescript()
	print('A' + dragonKind + ' dragon jumps out in front of you! He opens his jaws and...')
	print()
	time.sleep(4)
	
	friendlyCave = random.randint(1,2)
	
	if chosenCave == str(friendlyCave):
		global totLoot
		global won
		loot = getLoot()
		totLoot += loot
		lootDescript = chooseLootDescript()
		print('He gives you his ' + lootDescript + '...')
		loot = str(loot)
		print('It was worth ' + loot + ' gold.')
		won = 1
	else:
		print('He gobbles you down in one bite!')
		won = 0

playAgain = 'yes'
displayIntro()
time.sleep(5)
while playAgain == 'yes' or playAgain == 'y':	
	
	caveNumber = chooseCave()
	
	checkCave(caveNumber)
	
	if won == 1:
		wealth = str(totLoot)
		print()
		print('Your current adventure has amassed you ' + wealth + ' Gold pieces.')
		time.sleep(3)
		print()
		print('You continue to the next cave in hope of finding more treasure.')
		print()
	else:
		print('Do you want to play again? (yes or no)')
		playAgain = input()
		if playAgain == 'yes' or playAgain == 'y':
			print('You approach two caves after what feels like a strange amount of time.')
			time.sleep(2)
			print('You could have sworn you have done this before, but you haven\'t.')
			print()