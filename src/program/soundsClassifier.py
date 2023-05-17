import classification as cl

print("\nPart 4.2: Classify a test sound into a category from the trainingSet \n")
cl.classify_sound_kNN("testingSet/screaming/9429/9429_13258-lq.json", "trainingSet", 5, descInput=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#cl.classify_sound_kNN("testClass/guitar/399479/399479_7575123-lq.json", "testDownload",5, descInput=[2,10])
#cl.classify_sound_kNN("./src/program/testClass/guitar/110455/110455_1075352-lq.json", "./src/program/testDownload/", 3, descInput=[2, 10])
#cl.classify_sound_kNN("./src/program/testClass/piano/673720/673720_8981843-lq.json", "./src/program/testDownload/", 3, descInput = [0, 1, 14, 15])