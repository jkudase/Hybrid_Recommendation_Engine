from User_Based_Module import preprocessing
import numpy as np
from django.template.defaultfilters import length

class kmeans:
	"Implementation of kmeans algorithm"

	def __init__(self, matrix, k):
		"Initializer takes in a user-movie matrix and the number of clusters"
		self.data = matrix
		self.k = k
		self.iteration = 0
		self.num_users = len(self.data)
		self.num_movies = len(self.data[0]) 
		'''
		print("self.k:",self.k)
		print("self.num_users:",self.num_users)
		print("self.num_movies:",self.num_movies)
		'''
		
		
		# List of cluster numbers, initalized randomly 
		self.cluster_num = np.random.randint(0, self.k, size=self.num_users)
		#print("self.cluster_num:",self.cluster_num)
		# Initialize centroids to zero
		self.centroids = np.zeros((self.k, self.data.shape[1]))
		
		#print("self.data shape:",self.data.shape[1])
		'''
		print("self.centroids rows:",len(self.centroids))
		print("self.centroids :",len(self.centroids[0]))
		'''
	def updateCentroids(self):
		"Update the centroid of each cluster"
		for c in range(self.k):
			self.centroids[c] = np.mean([self.data[u] for u in range(self.num_users) if self.cluster_num[u] == c], axis=0)
			
	def assignPointsToCluster(self):
		"Assign each of the points to cluster"
		self.old_cluster_num = self.cluster_num
		self.cluster_num = np.array([np.argmin([np.linalg.norm(u-c) for c in self.centroids]) for u in self.data])

	def kCluster(self):
		"Performs clustering"

		# Flag for whether clustering is done
		done = False

		#print("K-means algorithm running...")
		while not done:
			self.updateCentroids()
			self.assignPointsToCluster()
			self.iteration += 1

			# Check whether clustering is done
			changes = np.sum((self.old_cluster_num - self.cluster_num) != 0)
			if changes == 0:
				done = True
			#print("Changes: %d" % changes)
		#print("self.centroids:",len(self.centroids))
		return (self.cluster_num, self.centroids)


