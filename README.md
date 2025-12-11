CS549 - Final Project
Michael Morgan, Kevin Stratton, Yotam


Game Reccomendation Model: a model that reccomends games based on the user's games that are played using a K-Means Clustering Algorithm

Major Files to look out for:

# EditData
This folder contains the cleanup process for the dataset we used (playstation dataset). Look at CleanUp.ipynb for more details

###### CleanUp.ipynb
This jupyter notebook within the EditData folder holds the process of reading in our .csv, and performing EDA in looking at the graphs
raw information and manipulating the dataset to reduce the use of missing and unnecessary information. This file also outputs the
cleaned up .csv, title 'CleanedUpData.csv', used to make a .csv file suitable for our model to perform.

###### jupyter_requirements.txt
When running this from your own virtual environment run the command 'pip install -r jupyter_requirements.txt' to download all the dependencies necessary to
run the CleanUp notebook.

###### CleanedUpData.csv
The resulting outputted information, a byproduct of CleanUp.ipynb. This contains the files where the Genres columns had the Multi Label Binarizer applied, making
analysis and further work easier on. Also contains 9 less columns, and over 700 less rows than the original, raw .csv. 

###### data
This subfolder contains a copy of the CleanUpData, the original .csv used (playstation_4_games.csv), and an About_data file that contains the source for the original dataset.


Datasplit.py: splitting the cleaned up data into training and test data. 

Train_KMeans.ipynb: the training of the K-means model. It creates the following files:
    user_vectors: the "users" set of games represented as vectors
    cluster_labels: the labeling of clusters
    kmeans_model: saving the kmeans model

TestsandPlot.ipynb: the results of the kmeans model. displays the silhoulette score and graph of the kmeans model



