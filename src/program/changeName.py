import os

folder = "C:/Users/laiad\Desktop/new classes/nightmare_mp3"
files = os.listdir(folder)

for files in files:
    if files.endswith(".mp3"):
        # Obtain the first group of numbers before "_"
        new_name = files.split("_")[0] + ".mp3"

        # Complete dir of the original file and new file
        original_dir = os.path.join(folder, files)
        new_dir = os.path.join(folder, new_name)

        # Rename file
        os.rename(original_dir, new_dir)

        print(f"Rename file: {files} -> {new_name}")
