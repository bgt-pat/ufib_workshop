dataset['Time'] = dataset['Time'] - dataset['Time'].iloc[0] # subtract initial time
dataset['seconds'] = dataset['Time'].dt.total_seconds() # append seconds to dataset
dataset.head()