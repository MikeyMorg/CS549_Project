# CS549 - Final Project
Michael Morgan, Kevin Stratton, Yotam Boiani

# Abstract
Game Reccomendation Model: a model that reccomends games based on the user's games that are played using a K-Means Clustering Algorithm

# EditData
This folder contains the cleanup process for the dataset we used (playstation dataset). Look at CleanUp.ipynb for more details

### CleanUp.ipynb
This jupyter notebook within the EditData folder holds the process of reading in our .csv, and performing EDA in looking at the graphs
raw information and manipulating the dataset to reduce the use of missing and unnecessary information. This file also outputs the
cleaned up .csv, title 'CleanedUpData.csv', used to make a .csv file suitable for our model to perform.

### jupyter_requirements.txt
When running this from your own virtual environment run the command 'pip install -r jupyter_requirements.txt' to download all the dependencies necessary to
run the CleanUp notebook.

### CleanedUpData.csv
The resulting outputted information, a byproduct of CleanUp.ipynb. This contains the files where the Genres columns had the Multi Label Binarizer applied, making
analysis and further work easier on. Also contains 9 less columns, and over 700 less rows than the original, raw .csv. 

### data
This subfolder contains a copy of the CleanUpData, the original .csv used (playstation_4_games.csv), and an About_data file that contains the source for the original dataset.

# CSVCLEAN
This folder contains the information for the virtual environment used when cleaning up the data -- feel free to ignore, or use it on your own system if you'd like to play around
with the environment.

# KMeans_Model

### Datasplit.py
This file contains the process of splitting the cleaned up data into training and test data. 

### TestsandPlot.ipynb
the results of the kmeans model. displays the silhoulette score and graph of the kmeans model.

### Train_KMeans.ipynb
This notebook is where we start training the K-means model. It creates the following files, located in the subfolder 'Important_Data':

## Important_Data
 Subfolder with the the files created from Train_KMeans.ipynb
###### user_vectors.npy
The "users" set of games represented as vectors.

###### cluster_labels.npy
Our K-mean cluster labels.

###### kmeans_model.pkl
The k-means model is saved here.




