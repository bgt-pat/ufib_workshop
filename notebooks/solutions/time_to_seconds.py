dataset['Time'] = dataset['Time'] - dataset['Time'].iloc[0] # subtract initial time
dataset['hours'] = dataset['Time'].dt.total_seconds() # append seconds to dataset
dataset[[r"$T_1$", r"$T_2$", r"$T_3$"]] += 273.15
dataset.head()