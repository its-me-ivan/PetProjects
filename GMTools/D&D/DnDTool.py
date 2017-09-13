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
def rollStats():
    print()
    print('Stat pool: ', end = '')
    for i in range(6):                  #6 stats to roll for
        dice = [roll(6), roll(6), roll(6), roll(6)]     #set dice values
        dice.sort()                     #numerical order
        total = sum(dice[1:4])          #total all but lowest
        #print out the stat
        if i < 5:
            print(str(total) + ', ', end = '')
        else:
            print(str(total))

#generate a rondom NPC
def NPCGen():
    gender = getGender()
    name = nameChoice(gender)
    race = getRace()
    appearance = getAppearance()
    mannerism = getMannerism()
    NPC = 'Name: ' + name + '\n\n' + 'Sex: ' + gender + '\n\n' + 'Race: ' + race + '\n\n' + 'Appearance: ' + appearance + '\n\n' + 'Mannerism: ' + mannerism

    print('-------------------------------------------')
    print(NPC)
    print('-------------------------------------------')

    return NPC

#make a name for NPC (UNDER CONSTRUCTION)
def nameChoice(gender):
    if roll(2) == 2:
        name = pickName(gender)
    else:
        name = makeName()
    return name

#choose for NPC from existing list (UNDER CONSTRUCTION)
def pickName(gender):
    mNames = ['Adair', 'Adriel', 'Altair', 'Aurelian', 'Aurelius', 'Bastian', 'Cassial', 'Cassius', 'Chaniel',
        'Cyprian', 'Diare', 'Darius', 'Destin', 'Drake', 'Drystan', 'Eoin', 'Fineas', 'Finian', 'Fyodor', 'Gareth',
        'Gavriel', 'Griffin', 'Hadriel', 'Hesperos', 'Iagan', 'Ignatius', 'Korbin', 'Kyler', 'Lucien', 'Marius',
        'Mathieu', 'Nuriel', 'Oisin', 'Orion', 'Orpheus', 'Peregrine', 'Perseus', 'Phelan', 'Remus', 'Rhyan', 
        'Rhydderch', 'Sebastian', 'Seraphim', 'Sirius', 'Tavish', 'Tearlach', 'Thaniel', 'Torian', 'Torin', 'Urien',
        'Xanthus', 'Zephyr', 'Zorion']
    fNames = ['Abrielle', 'Adara', 'Aiyana', 'Alissa', 'Alexandra', 'Amara', 'Anatola', 'Anya', 'Arcadia', 
        'Ariadne', 'Arianwen', 'Aurelia', 'Avalon', 'Breena', 'Brielle', 'Cambria', 'Cara', 'Carys', 'Cassia',
        'Cassiopeia', 'Cora', 'Eira', 'Eirian', 'Elysia', 'Evadne', 'Guinevere', 'Hannelore', 'Ianthe', 'Ignacia',
        'Iseult', 'Isolde', 'Jessalyn', 'Kara', 'Kerensa', 'Kyra', 'Leila', 'Lilith', 'Liora', 'Lyra', 'Maia',
        'Mireille', 'Mireya', 'Natania', 'Nerys', 'Nyssa', 'Oralie', 'Ozara', 'Petronela', 'Qadira', 'Quintessa',
        'Raisa', 'Saoirse', 'Sarai', 'Seraphina', 'Sorcha', 'Terra', 'Thalia', 'Theia', 'Tressa', 'Tristana',
        'Uriela', 'Vanora', 'Vespera', 'Yadira', 'Yseilt', 'Zaira', 'Zora']
    nNames = ['Acalia', 'Alaire', 'Auristela', 'Briallan', 'Briseis', 'Dagen', 'Devlin', 'Devlyn', 'Eliron', 'Evanth',
        'Gaerwn', 'Ginerva', 'Katriel', 'Kyrielle', 'Leira', 'Liriene', 'Liron', 'Maylea', 'Meira', 'Neirin',
        'Nyfain', 'Oleisa', 'Orinthea', 'Pryderi', 'Pyralia', 'Pyralis', 'Quinevere', 'Renfrew', 'Saira', 'Sarielle',
        'Serian', 'Severin', 'Ulyssia', 'Vasilis', 'Xara', 'Xylia', 'Yakira', 'Yeira', 'Yeriel', 'Yestin', 'Zaniel',
        'Zarek']
    if gender == 'Male':
        names = mNames
        names.extend(nNames)
        name = names[roll(len(names))-1]
    else:
        names = fNames
        names.extend(nNames)
        name = names[roll(len(names))-1]
    return name

#make a name for NPC (UNDER CONSTRUCTION)
def makeName():
    nameParts = [['', '', '', '', '', 'a', 'be', 'de', 'el', 'fa', 'jo', 'ki', 'la', 'ma', 'na', 'o', 'pa', 're', 'si', 'ta', 'va'],
        ['bar', 'ched', 'dell', 'far', 'gran', 'hal', 'jen', 'kel', 'lim', 'mor', 'net', 'penn', 'quil', 'rond', 'sark', 'shen', 'tur', 'vash', 'yor', 'zen'],
        ['', 'a', 'ac', 'ai', 'al', 'am', 'an', 'ar', 'ea', 'el', 'er', 'ess', 'ett', 'ic', 'id', 'il', 'in', 'is', 'or', 'us']]
    name = nameParts[0][roll(len(nameParts[0]))-1] + nameParts[1][roll(len(nameParts[1]))-1] + nameParts[2][roll(len(nameParts[2]))-1]
    name = name.title()
    return name

#choose gender for NPC
def getGender():
    choose = roll(10)
    if choose < 7:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender

#choose race for NPC
def getRace():
    race = ''
    choose = roll(22)
    if choose < 10:
        race = 'Human'
    elif choose < 13:
        race = 'Dwarf'
    elif choose < 16:
        race = 'Elf'
    elif choose < 18:
        race = 'Halfling'
    elif choose < 19:
        race = 'Dragonborn'
    elif choose < 20:
        race = 'Gnome'
    elif choose < 21:
        race = 'Half-Elf'
    elif choose < 22:
        race = 'Half-Orc'
    else:
        race = 'Tiefling'
    return race

#choose appearance for NPC
def getAppearance():
    appList = ['Wears distinctive jewlery', 'Piercings', 'Flamboyant, outlandish clothes', 'Formal, clean clothes',
        'Ragged, dirty clothes', 'Obvious scar', 'Missing teeth', 'Missing Finger(s)', 'Different colored eyes',
        'Tatoos', 'Birthmark', 'Androgynous', 'Bald', 'Braided hair or beard', 'Strange hair color', 'Distinctive nose',
        'Distinctive posture', 'Exceptionally beutiful', 'Exceptionally ugly', 'Exceptionally tall', 'Exceptionally short',
        'Fatty build', 'Elderly', 'Two gnomes disguized as one big person', 'Child', 'Muscular build']
    appearance = appList[roll(len(appList))-1]
    return appearance

#choose mannerism for NPC
def getMannerism():
    manList = ['Prone to singing and humming', 'Particularly low or high voice', 'Overenunciates', 'Uses big words',
        'Frewquently uses wrong word', 'Cusses like a sailor', 'Makes jokes or puns', 'Prone to predictions of doom',
        'Fidgets', 'Squints', 'Stares into the distance', 'Chews something', 'Paces', 'Taps fingers', 'Twirls hair or beard',
        'Stares intently', 'Closes eyes when talking', 'Slurs words', 'Russian accent', 'Irish accent', 'Absentminded',
        'Iritated by everything', 'Hidey-ho friends!', 'Doesn\'t percieve gender', 'Alergies', 'Clumsy']
    mannerism = manList[roll(len(manList))-1]
    return mannerism


#main function
choice = 'initial'      #arbitrary initial value

print('-------------------------------------------')        #show commands
print('Ivan\'s DM Helper (Python Version)')
print('Comands:')
print('Number and kind of dice to roll (ex: 10d20)')
print('\"stats\" to roll a character stat pool')
print('\"npc\" to generate a random NPC')
print('\"quit\" to quit')
print('-------------------------------------------')

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
    #option to test shit
    elif choice == 'test':
        print(lastNPC)
    #option to quit
    elif choice == 'quit':
        print()
        print('Later nerds.')
        input()
        sys.exit()
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
