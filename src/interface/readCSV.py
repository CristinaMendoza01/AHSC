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
alarmProbs = []

insectSounds = [] # 1
insectProbs = []

respiratorySounds = [] # 2
respiratoryProbs = []

screamingSounds = [] # 3
screamingProbs = []

with open('../program/results.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    # sound_id, category_1, prob_1, category_2, prob_2, category_3, prob_3, category_4, prob_4, category_5, prob_5
    for row in csv_reader:
        sound_id = row['sound_id']
        num_cat_1 = row['category_1']
        prob_1 = row['prob_1']
        num_cat_2 = row['category_2']
        prob_2 = row['prob_2']
        num_cat_3 = row['category_3']
        prob_3 = row['prob_3']
        num_cat_4 = row['category_4']
        prob_4 = row['prob_4']
        num_cat_5 = row['category_5']
        prob_5 = row['prob_5']


        # print(num_cat_1)
        if(num_cat_1 == str(0)):
            alarmSounds.append(sound_id)
            alarmProbs.append(prob_1)

        if (num_cat_1 == str(1)):
            insectSounds.append(sound_id)
            insectProbs.append(((num_cat_1, prob_1), (num_cat_2, prob_2), (num_cat_3, prob_3), (num_cat_4, prob_4), (num_cat_5, prob_5)))

        if (num_cat_1 == str(2)):
            respiratorySounds.append(sound_id)
            respiratoryProbs.append(((num_cat_1, prob_1), (num_cat_2, prob_2), (num_cat_3, prob_3), (num_cat_4, prob_4), (num_cat_5, prob_5)))

        if (num_cat_1 == str(3)):
            screamingSounds.append(sound_id)
            screamingProbs.append(((num_cat_1, prob_1), (num_cat_2, prob_2), (num_cat_3, prob_3), (num_cat_4, prob_4), (num_cat_5, prob_5)))

# print(screamingProbs)

# # PROBS
# for s in screamingProbs:
#     print(s[])
