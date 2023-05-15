import soundata

dataset = soundata.initialize('fsd50k')
dataset.download()  # download the dataset
dataset.validate()  # validate that all the expected files are there

example_clip = dataset.choice_clip()  # choose a random example clip
print(example_clip)  # see the available data

# python 3.8
# numpy 1.20.0
# pip install typing-extensions