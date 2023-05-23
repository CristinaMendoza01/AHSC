import classification as cl

print("\nPart 4.2: Classify a test sound into a category from the trainingSet \n")
cl.classify_sound_kNN("testingSet/screaming/9429/9429_13258-lq.json", "trainingSet", 5, descInput=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
cl.classify_sound_kNN("testingSet/car engine/338954/338954_5121236-lq.json", "trainingSet", 5, descInput=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
cl.classify_sound_kNN("testingSet/horror sounds/205630/205630_3579566-lq.json", "trainingSet", 5, descInput=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])