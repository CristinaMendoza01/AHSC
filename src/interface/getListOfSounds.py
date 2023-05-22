import os

#################################### TESTING CATEGORIES DIRECTORIES ##################################
screamingDir = "../program/testingSet/screaming"
owlDir = "../program/testingSet/owl"
carDir = "../program/testingSet/car engine"
knockingDir = "../program/testingSet/knocking"
rainDir = "../program/testingSet/rain"
ravenDir = "../program/testingSet/raven bird"
violinDir = "../program/testingSet/violin"
######################################################################################################

def getSounds(categoryDir):
    # Check if CategoryDir exists
    if not os.path.isdir(categoryDir):
        print(f"Directory '{categoryDir}' does NOT exist.")
        return []

    # Get the list of files and directories in categoryDir
    list_elements = os.listdir(categoryDir)

    # Filter only the folders and add them to the list
    folders = [element for element in list_elements if os.path.isdir(os.path.join(categoryDir, element))]

    return folders