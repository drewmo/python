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
	caveD = random.randint(1,41)
	theCave = {
		1:'dark and spooky...', 
		2:'dank and smelly', 
		3:'clean and tidy...', 
		4:'eerily familiar...',
		5:'shockingly modern styled...',
		6:'covered in spider webs...',
		7:'dark but glowing in the distance...',
		8:'painted with no sense of coordination...',
		9:'hard to describe...',
		10:'hardly worth entering...',
		11:'home to a rich orphaned vigilante and his butler...',
		12:'only slightly better than the last one...',
		13:'significantly dangerous...',
		14:'obviously going to get you killed...',
		15:'ringing with the sound of tiny clicks...',
		16:'tropical in nature...',
		17:'worth a quick glance...',
		18:'orange? Yep. orange...',
		19:'hiding something within, you can feel it...',
		20:'where your had your heart broken...',
		21:'starting to give you the creeps...',
		22:'staring back at you...',
		23:'fully organic and FDA certified...',
		24:'one of those late night reruns...',
		25:'shrouded in mystery...',
		26:'just a painting on the wall...',
		27:'...this doesn\'t make any sense...',
		28:'starting to get on your nerves...',
		29:'drawing you in...',
		30:'spooky, but only slightly...',
		31:'just like the one you live in...',
		32:'spewing out foul smelling wind...',
		33:'trying to speak...',
		34:'awful to look at...',
		35:'the one you saw in that magazine that one time...',
		36:'hidden a secret...',
		37:'your garden variety cave...',
		38:'not you garden variety cave...',
		39:'boring to describe so I won\'t...',
		40:'starting to give off the impression that it is alive...',
		41:'the cave now formerly known as cave...'
	}
	return str(theCave[caveD])

def chooseDragonDescript():
	dragonD = random.randint(1,15)
	dragonD1 = random.randint(1,15)
	dragonAdj = {
		1:' large',
		2:' small',
		3:'n average',
		4:' baby',
		5:' tiny',
		6:' huge',
		7:' volcanic',
		8:' spectral',
		9:' contagious',
		10:' steaming',
		11:' frozen',
		12:' dripping',
		13:' shiny',
		14:' hiding',
		15:' venomous'
	}
	dragonAdj1 = {
		1:'angry',
		2:'nervous',
		3:'skeletal',
		4:'horned',
		5:'racist',
		6:'goth-like',
		7:'blue',
		8:'red',
		9:'fat',
		10:'rotten',
		11:'velvet',
		12:'calculating',
		13:'horrifying',
		14:'fantastic',
		15:'confused',	
	}
	return str(dragonAdj[dragonD] + ' ' + dragonAdj1[dragonD1])	

def chooseLootDescript():
	lootD = random.randint(1,11)
	lootD1 = random.randint(1,23)
	lootD2 = random.randint(1,18)
	lootAdj = {
		1:'shiny',
		2:'scuffed',
		3:'broken',
		4:'confusing',
		5:'useful',
		6:'broken',
		7:'orange',
		8:'curly',
		9:'shattered',
		10:'vibrating',
		11:'secret'	
	}	
	lootName = {
		1:'collectable card',
		2:'golden cup',
		3:'sword',
		4:'stuff',
		5:'golden plates',
		6:'Orin Berry',
		7:'shield',
		8:'boot',
		9:'silverware',
		10:'chalice',
		11:'frog',
		12:'princess',
		13:'glasses',
		14:'chest',
		15:'axe',
		16:'whip',
		17:'scale',
		18:'bat wing',
		19:'skeleton bone',
		20:'horse hooves',
		21:'battle armor',
		22:'mithril thong',
		23:'silver grinder'
	}
	lootType = {
		1:'collection',
		2:'stash',
		3:'pile',
		4:'',
		5:'box',
		6:'picture',
		7:'account',
		8:'description',
		9:'allowance',
		10:'drawing...it is not good so you take his word for it.',
		11:'cupboard',
		12:'hoard',
		13:'stack',
		14:'throng',
		15:'bundle',
		16:'set',
		17:'store',
		18:'assortment'	
	}
	return str(lootAdj[lootD] + ' ' + lootName[lootD1] + ' ' + lootType[lootD2])
	
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
			global totLoot
			totLoot = 0
			print('You approach two caves after what feels like a strange amount of time.')
			time.sleep(2)
			print('You could have sworn you have done this before, but you haven\'t.')
			print()