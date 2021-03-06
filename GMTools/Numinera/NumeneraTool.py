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

#generate a rondom NPC
def NPCGen():
    gender = getGender()
    name = nameChoice(gender)
    appearance = getAppearance()
    mannerism = getMannerism()
    NPC = 'Name: ' + name + '\n\n' + 'Sex: ' + gender + '\n\n' + 'Appearance: ' + appearance + '\n\n' + 'Mannerism: ' + mannerism

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
    mNames = ['Adair', 'Adriak', 'Altair', 'Aurelian', 'Aureliak', 'Bastian', 'Casskis', 'Cassid', 'Chan',
        'Cyprian', 'Diare', 'Darius', 'Destin', 'Darmuk', 'Drystan', 'Eoin', 'Fineak', 'Folan', 'Dydor', 'Gareth',
        'Gavrien', 'Grikin', 'Nadriel', 'Hesperog', 'Iagan', 'Ignatak', 'Korgin', 'Kyger', 'Lucig', 'Marius',
        'Matheg', 'Nuriel', 'Oisin', 'Orgon', 'Orpheus', 'Perin', 'Perseg', 'Phelan', 'Remus', 'Rhyan', 
        'Rhydderch', 'Sebast', 'Seraphim', 'Sirius', 'Tavish', 'Tearlach', 'Thaniel', 'Torian', 'Torin', 'Urien',
        'Xanthus', 'Zephyr', 'Zorion']
    fNames = ['Abrielle', 'Adara', 'Aiyana', 'Alissa', 'Alegandra', 'Amara', 'Anatola', 'Anya', 'Arcadia', 
        'Ariadne', 'Ariaga', 'Aurelia', 'Avalon', 'Breena', 'Brianuk', 'Cambria', 'Cara', 'Carys', 'Cassia',
        'Caniopa', 'Cora', 'Eira', 'Eirian', 'Elysia', 'Evadne', 'Guinekar', 'Hannelore', 'Ianthe', 'Ignacia',
        'Iseult', 'Isolde', 'Jessalyd', 'Kara', 'Kerensa', 'Kyra', 'Leilak', 'Lilith', 'Liora', 'Lyra', 'Moy',
        'Mireioy', 'Mireya', 'Natania', 'Nerys', 'Nyssa', 'Oralie', 'Ozara', 'Petronela', 'Qadira', 'Quintessa',
        'Raisa', 'Saoirse', 'Sarai', 'Seraphin', 'Sorcha', 'Terra', 'Thaliad', 'Theiak', 'Tressa', 'Tristaga',
        'Vuriel', 'Vanora', 'Vespera', 'Yadira', 'Yseilt', 'Zaira', 'Zora']
    nNames = ['Akaliak', 'Alaire', 'Auristev', 'Briallan', 'Briseis', 'Dagen', 'Devlin', 'Devlam', 'Eliron', 'Evanth',
        'Gaegwin', 'Ginerva', 'Katriel', 'Kyrielle', 'Leirum', 'Liriene', 'Liron', 'Maylea', 'Meira', 'Neirin',
        'Nyfain', 'Oleisa', 'Orinthea', 'Pryderi', 'Pyralia', 'Pyralis', 'Quinevek', 'Renfrew', 'Saira', 'Sarielle',
        'Serian', 'Severin', 'Ulyssa', 'Vasilis', 'Xara', 'Xylia', 'Yakira', 'Yeira', 'Yeriel', 'Yestin', 'Zaniel',
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
    nameParts = [['', '', '', '', '', 'a', 'be', 'ba', 'de', 'da', 'el', 'fa', 'fo', 'jo', 'ki', 'ko', 'la', 'ma', 'mu', 'na', 'o', 'pa', 'po', 'pe', 're', 'si', 'so', 'ta', 'va', 'wi'],
        ['bar', 'ched', 'dell', 'far', 'gran', 'hal', 'jen', 'kel', 'lim', 'mor', 'net', 'penn', 'quil', 'rin', 'rond', 'sark', 'shen', 'tur', 'vash', 'yor', 'zen'],
        ['', '', '', '', 'a', 'ac', 'ai', 'al', 'am', 'an', 'ar', 'ek', 'el', 'er', 'ess', 'et', 'ik', 'id', 'il', 'in', 'is', 'or', 'us']]
    name = nameParts[0][roll(len(nameParts[0]))-1] + nameParts[1][roll(len(nameParts[1]))-1] + nameParts[2][roll(len(nameParts[2]))-1]
    name = name.title()
    return name

#choose gender for NPC
def getGender():
    choose = roll(2)
    if choose < 2:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender

#choose appearance for NPC
def getAppearance():
    appList = ['Wears distinctive jewlery', 'Piercings', 'Flamboyant, outlandish clothes', 'Formal, clean clothes', 'Pet seski follows',
        'Ragged, dirty clothes', 'Obvious scar', 'Missing teeth', 'Missing Finger(s)', 'Different colored eyes', 'Cat eyes', 'Scrap metal clothing'
        'Tatoos', 'Birthmark', 'Androgynous', 'Bald', 'Braided hair or beard', 'Strange hair color', 'Distinctive nose', 'Cybernetic implants',
        'Distinctive posture', 'Exceptionally beutiful', 'Exceptionally ugly', 'Exceptionally tall', 'Exceptionally short', 'Long canines',
        'Fatty build', 'Elderly', 'Tentacle', 'Child', 'Muscular build', 'Extremely large eyes', 'Missing limb', 'alien', 'extra fingers', 'Forked tongue']
    appearance = appList[roll(len(appList))-1]
    return appearance

#choose mannerism for NPC
def getMannerism():
    manList = ['Prone to singing and humming', 'Particularly low or high voice', 'Overenunciates', 'Uses big words',
        'Frequently uses wrong word', 'Cusses like a sailor', 'Makes jokes or puns', 'Prone to predictions of doom',
        'Fidgets', 'Squints', 'Stares into the distance', 'Chews something', 'Paces', 'Taps fingers', 'Twirls hair or beard',
        'Stares intently', 'Closes eyes when talking', 'Slurs words', 'Russian accent', 'Irish accent', 'Absentminded',
        'Iritated by everything', 'Hidey-ho friends!', 'Doesn\'t percieve gender', 'Alergies', 'Clumsy', 'Sweedish Chef voice',
        'Laughs nervously between sentances', 'Head jolts arround like a bird', 'Talks slowly', 'Talks rapidly', 'Keeps trying to talk about fishing']
    mannerism = manList[roll(len(manList))-1]
    return mannerism

#Save the last NPC generated to a text file
def saveNPC(NPC):
    #allow user to add notes
    print('\nWhat notes would you like?')
    notes = input()
    #save info
    SavedNPCs = open('SavedNPCs.txt', 'a')
    SavedNPCs.write(NPC + '\n\nNotes: ' + notes + '\n-------------------------------------------\n')
    SavedNPCs.close()

#main function
choice = 'initial'      #arbitrary initial value

print('-------------------------------------------')        #show commands
print('Ivan\'s GM Helper (Numenera Version)')
print('Comands:')
print('Number and kind of dice to roll (ex: 10d20)')
print('\"npc\" to generate a random NPC')
print('\"save\" to save your last NPC')
print('\"quit\" to quit')
print('-------------------------------------------')

lastNPC = 'None Saved\n'

while choice != 'quit':         #until they hit quit
    print()
    print('What do you want?')
    choice = input()            #recieve input
    choice = choice.lower()     #convert to lowercase

    #option to roll a stat pool
    if choice == 'npc':
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
