Nothing Here! Yet!
CS549
Michael Morgan, Kevin Stratton, Yotam Boiani


Game Reccomendation model: a model that reccomends games based on the user's games that are played using a Kmeans clustering algorithm

Major Files to look out for:

Data: this file contains the cleanup process for the dataset we used (playstation dataset). Look at CleanUp.ipynb for more details

Datasplit.py: splitting the cleaned up data into training and test data. 

Train_KMeans.ipynb: the training of the K-means model. It creates the following files:
    user_vectors: the "users" set of games represented as vectors
    cluster_labels: the labeling of clusters
    kmeans_model: saving the kmeans model

TestsandPlot.ipynb: the results of the kmeans model. displays the silhoulette score and graph of the kmeans model



