# split data into training, and test sets
import pandas as pd
from sklearn.model_selection import train_test_split

# obtain cleaned data
data = pd.read_csv("EditData/data/CleanedUpData.csv")

#split data into training and test sets
train_data, test_data = train_test_split(data, 
                test_size=0.2, # 20% for test set, 80% for training + validation
                random_state=42, #ensure reproducibility
                shuffle=True) #shuffle the data before splitting

# sava datasets to csv files
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

