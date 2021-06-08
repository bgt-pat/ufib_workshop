import pandas as pd

path = "https://raw.githubusercontent.com/bgt-pat/ufib_workshop/main/data/example1.txt"
dataset = pd.read_csv(path,delimiter="\t",names = ["Time", r"$T_1$", r"$T_2$", r"$T_3$"])

dataset['Time'] = pd.to_datetime(dataset['Time']) # needed in order to convert the strings to datetime64
dataset.head()