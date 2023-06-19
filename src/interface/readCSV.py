import csv

classesAndLabels = { 0: 'Alarm',
                     1: 'Insect',
                     2: 'RespiratorySounds',
                     3: 'Screaming',
                     4: 'Bell',
                     5: 'Bird',
                     6: 'BowedStringInstruments',
                     7: 'Creature',
                     8: 'Door_window',
                     9: 'Explosion',
                     10: 'Fire',
                     11: 'Guitar',
                     12: 'Gunshot',
                     13: 'Hits_footsteps',
                     14: 'Household_appliances',
                     15: 'Howl',
                     16: 'Interferences',
                     17: 'KeyboardInstruments',
                     18: 'Laughter',
                     19: 'Motor vehicle',
                     20: 'Nightmare',
                     21: 'Rain',
                     22: 'Telephone',
                     23: 'Tools',
                     24: 'Whispering',
                     25: 'Wind'
                     }

alarmSounds = [] # 0
insectSounds = [] # 1
respiratorySounds = [] # 2
screamingSounds = [] # 3
bellSounds = [] # 4
birdSounds = [] # 5
bowedSounds = [] # 6
creatureSounds = [] # 7
doorSounds = [] # 8
explosionSounds = [] # 9
fireSounds = [] # 10
guitarSounds = [] # 11
gunshotSounds = [] # 12
footSounds = [] # 13
houseSounds = [] # 14
howlSounds = [] # 15
interferencesSounds = [] # 16
keyboardSounds = [] # 17
laughSounds = [] # 18
motorSounds = [] # 19
nightmareSounds = [] # 20
rainSounds = [] # 21
telephoneSounds = [] # 22
toolSounds = [] # 23
whisperSounds = [] # 24
windSounds = [] # 25

with open('../program/results.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    # sound_id, category_1, prob_1, category_2, prob_2, category_3, prob_3, category_4, prob_4, category_5, prob_5
    for row in csv_reader:
        num_cat_1 = row['category_1']

        # print(num_cat_1)
        if(num_cat_1 == str(0)):
            alarmSounds.append(row)
        if (num_cat_1 == str(1)):
            insectSounds.append(row)
        if (num_cat_1 == str(2)):
            respiratorySounds.append(row)
        if (num_cat_1 == str(3)):
            screamingSounds.append(row)
        if(num_cat_1 == str(4)):
            bellSounds.append(row)
        if(num_cat_1 == str(5)):
            birdSounds.append(row)
        if (num_cat_1 == str(6)):
            bowedSounds.append(row)
        if (num_cat_1 == str(7)):
            creatureSounds.append(row)
        if (num_cat_1 == str(8)):
            doorSounds.append(row)
        if (num_cat_1 == str(9)):
            explosionSounds.append(row)
        if (num_cat_1 == str(10)):
            fireSounds.append(row)
        if (num_cat_1 == str(11)):
            guitarSounds.append(row)
        if (num_cat_1 == str(12)):
            gunshotSounds.append(row)
        if (num_cat_1 == str(13)):
            footSounds.append(row)
        if (num_cat_1 == str(14)):
            houseSounds.append(row)
        if (num_cat_1 == str(15)):
            howlSounds.append(row)
        if (num_cat_1 == str(16)):
            interferencesSounds.append(row)
        if (num_cat_1 == str(17)):
            keyboardSounds.append(row)
        if (num_cat_1 == str(18)):
            laughSounds.append(row)
        if (num_cat_1 == str(19)):
            motorSounds.append(row)
        if (num_cat_1 == str(20)):
            nightmareSounds.append(row)
        if (num_cat_1 == str(21)):
            rainSounds.append(row)
        if (num_cat_1 == str(22)):
            telephoneSounds.append(row)
        if (num_cat_1 == str(23)):
            toolSounds.append(row)
        if (num_cat_1 == str(24)):
            whisperSounds.append(row)
        if (num_cat_1 == str(25)):
            windSounds.append(row)

def orderList(list):
    orderedList = sorted(list, key=lambda x: x['prob_1'], reverse=True)
    return orderedList
