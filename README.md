# AHSC
GitHub Repository for the MTL 2023 course Project

This project is called AHSC: Automatic Horror Sound Classification and it's about to create a software that classifies different horror sounds. Basically, we get horror sounds from Freesound (https://freesound.org/) and we create a software application that classifies these sounds into different categories.

AHSC is an innovative project developed as part of the Music Technology Workshop elective course for ICT engineering degrees at Pompeu Fabra University. The aim of this project is to develop a software application based on the 'Freesound' website to classify horror sounds by using a new tagging system created by us to classify these horror sounds automatically in subcategories. With almost 12000 available horror-related sounds on the website without specific tags, this project proposes a solution that involves using metadata and implementing classification algorithms to generate subcategories, which will allow for more accurate and specific searches.

To achieve this, the project employs the Python programming language and the Pycharm IDE, along with the powerful 'Essentia' libraries that help with sound analysis and descriptor extraction, and the 'Scikit-learn' library for machine learning techniques.

# Installation for the developer
1. Download or clone the repository locally
2. Open the project with an IDE
3. Open the terminal on the folder freesound-python-master and run the command: python setup.py install
4. Install the libraries required
5. Run the project

# Installation for the user
First option:
1. Download or clone the repository locally
2. Go to the folder executable
3. Double click the .exe

Second option:
1. In GitHub, go to the folder executable
2. Download the file .exe
3. Double click the .exe

# Requirements
See the REQUIREMENTS.txt

# Organization
The code is in the folder AHSC/src and it is divided into different folders:
* interface: Contains all the files related to the code part to develop the visual interface of AHSC.
* program: Currently, contains all the files needed to execute the program, included the trainingSet and testingSet, but it will disappear.
* training: It will contain all the files and dataset related to train the classifier.
* classification: It will contain all the files related to classify the dataset.
* dataset: It will contain all the .json files of the horror sounds that will be classified.
* mir-data notebook: Contains a file mirdata.py which is the notebook from mridangam_stroke called mridangam_stroke_classification_example.ipynb

# Team members
Arnau Adan (arnau.adani01@estudiant.upf.edu)

Víctor Alcaide (victor.alcaide02@estudiant.upf.edu)

Sara Barbé (sara.barbe01@estudiant.upf.edu)

Laia Duch (laia.duch01@estudiant.upf.edu)

Naiara Garmendia (naiara.garmendia01@estudiant.upf.edu)

Cristina Mendoza (cristina.mendoza01@estudiant.upf.edu)
