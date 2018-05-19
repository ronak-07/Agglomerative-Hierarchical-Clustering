from scipy.cluster import hierarchy
import numpy as np
import scipy
import matplotlib.pyplot as plt
import distance
import time
		
"""
input: Two numbers
output: Minimum of the two numbers
"""
def minimum(double1,double2):
	if (double1< double2):
		return double1
	else:
		return double2
		
"""
input: Two numbers
output:Maximum of the two numbers
"""
def maximum(double1,double2):
	if (double1>double2):
		return double1
	else:
		return double2

"""
Performs agglomerative clustering
input:	distance matrix,its size and iteration value k
output:	returns the modified distance matrix
"""
def clust(a,size,k):
	min =999.0
	m=555
	n=555
	for i in range(0,size-1):
		for j in range (1,size):
			if (i<j):
				if (a[i][j]<min):
					min = a[i][j]
					m=i
					n=j	
	big_list=[]				
	if(m<n):																#To keep track of the order							
		big_list.append(dict[m])
		big_list.append(dict[n])
		dict[m]=big_list
		del dict[n]		
	#This section of the function is used to fill values in Z			   
	if(new_clusters[m]==-1 and new_clusters[n]==-1):						#both are -1
		Z[k][0]=m
		Z[k][1]=n
		x=minimum(m,n)
		new_clusters[x]=size+k
		Z[k][3]=2
	elif(new_clusters[m]!=-1 and new_clusters[n]!=-1):						#both not -1
		Z[k][0]=new_clusters[m]
		Z[k][1]=new_clusters[n]
		if(m<n):
			new_clusters[m]=size+k
		else:
			new_clusters[n]=size+k
		Z[k][3]=Z[int(maximum(Z[k][0],Z[k][1])-size)][3] + 1
	elif(new_clusters[m]!=-1 and new_clusters[n]==-1):						#m is not -1 and n is -1			
		if(m<n):
			Z[k][0]=new_clusters[m]
			Z[k][1]=n
			Z[k][3]=Z[int(maximum(Z[k][0],Z[k][1])-size)][3] + 1
			new_clusters[m]=size+k
		else:
			Z[k][0]=m
			Z[k][1]=new_clusters[n]
			Z[k][3]=Z[int(maximum(Z[k][0],Z[k][1])-size)][3] + 1
			new_clusters[n]=size+k
	elif(new_clusters[m]==-1 and new_clusters[n]!=-1):						#m is -1 and n is not -1
		if(m<n):
			Z[k][0]=m
			Z[k][1]=new_clusters[n]
			Z[k][3]=Z[int(maximum(Z[k][0],Z[k][1])-size)][3] + 1
			new_clusters[m]=size+k
		else:
			Z[k][0]=new_clusters[m]
			Z[k][1]=n
			Z[k][3]=Z[int(maximum(Z[k][0],Z[k][1])-size)][3] + 1
			new_clusters[n]=size+k
	else:
		print("Error")	
	Z[k][2]=min
	for j in range(0,size):
		if (j!=n):
			a[j][m] = minimum(a[j][m],a[j][n])
		a[m][j] = a[j][m]
		a[j][n] = 9999.0
		a[n][j] = 9999.0	
	return a

"""
This is used to form the dendrogram
"""
def augmented_dendrogram(*args, **kwargs):
	data = scipy.cluster.hierarchy.dendrogram(*args, **kwargs)
	if not kwargs.get('no_plot', False):
		for i, d in zip(data['icoord'], data['dcoord']):
			x = 0.5 * sum(i[1:3])
			y = d[1]
			plt.plot(x, y, 'ro')
			plt.annotate("%.3g" % y, (x, y), xytext=(0,12),textcoords='offset points',va='top', ha='center')
	return data
	

#MAIN
a=np.load('distance_matrix.npy')
size=len(a)
dict={}
Z=np.zeros(shape=(size-1,4))
new_clusters={}
for i in range(0,size):
	list=[]
	list.append(i)
	dict[i]=list
for i in range(0,size):
	new_clusters[i]=-1
start=time.time()
for k in range(0,size-1):
	a = clust(a,size,k)
print("Clustering done\t" + str(time.time()-start))
#Plot dendrogram
names=[i for i in range(0,size)]
plt.figure(figsize=(25, 25))
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
plt.xlabel('Sequence No.')
plt.ylabel('Distance')
augmented_dendrogram(Z,labels=names,show_leaf_counts=True,p=25,truncate_mode='lastp')
plt.show()