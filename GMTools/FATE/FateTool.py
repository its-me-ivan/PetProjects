import random, sys, string

#function to roll dice
def roll(sides):
    diceRoll = random.randint(1, sides)         #chooses random number on dice
    return diceRoll                             #return as an integer

#show dice rolls
def rollDisp(quant, sides):
    print()
    if quant == 1:
        print('Result: ' + str(roll(sides)))
    else:
        print('Results: ', end = '')
        total = 0
        for i in range(quant):                      #run once per dice
            dice = roll(sides)                      #store this roll
            total += dice                           #add to total
            if i % 15 == 0 and i > 1:               #line break after 15 rolls
                print()
                print('         ', end = '')
            if (i + 1) == quant:                    #last number has no comma
                print(str(dice))
            else:
                print(str(dice) + ', ', end = '')   #list rolls
        print()
        print('Total: ' + str(total))

#roll a character stat pool of 6 stats each 4d6 drop low
def fateRoll():
    print()
    print('Results: ', end = '')
    total = 0
    for i in range(4):                          #run once per dice
        dice = roll(3)-2                        #store this roll
        total += dice                           #add to total
        if (i + 1) == 4:                    #last number has no comma
            print(str(dice))
        else:
            print(str(dice) + ', ', end = '')   #list rolls
    print()
    print('Total: ' + str(total))

#main function
choice = 'initial'      #arbitrary initial value

print('-------------------------------------------')        #show commands
print('Ivan\'s GM Helper (Fate Version)')
print('Comands:')
print('Number and kind of dice to roll (ex: 10d20)')
print('\"roll\" to roll a set of Fate Dice')
print('\"quit\" to quit')
print('-------------------------------------------')

lastNPC = 'None Saved\n'

while choice != 'quit':         #until they hit quit
    print()
    print('What do you want?')
    choice = input()            #recieve input
    choice = choice.lower()     #convert to lowercase

    #option to roll a stat pool
    if choice == 'stats':
        rollStats()
    #option to create NPC
    elif choice == 'npc':
        lastNPC = NPCGen()
    #option to save NPC
    elif choice == 'save':
        saveNPC(lastNPC)
    #option to test shit
    elif choice == 'test':
        saveNPC(lastNPC)
    #option to quit
    elif choice == 'quit':
        print()
        print('Later nerds.')
        input()
        sys.exit()
    #option to roll 4 Fate Dice 
    elif choice == 'roll':
        fateRoll()
    #option to roll dice
    elif 'd' in choice:         #look for a d, as in 5d20
        d = choice.find('d')
        try:
            if d == 0:          #if d is the first character roll 1
                quant = 1
            else:               #else roll indicated number
                quant = int(choice[0:d])
            sides = int(choice[d + 1:len(choice)])
        except:                 #if there are characters that cause errors in the int conversion
            print()
            print('Not a valid input')      #mention error
            continue            #resttart loop
        if quant < 1 or sides < 2:              #if bad values
            print()
            print('Not a valid input')
            continue
        rollDisp(quant, sides)
    #invalid choice
    else:
        print()
        print('Not a valid input')
