
Agglomerative-Hierarchical-Clustering (Bottom Up)
===============================================
In Agglomerative we start with all points as individual clusters and then keep on combining clusters until required number of clusters are not formed using linkages like single, complete, average, ward or centroid.


Idea
------
A phylogenetic tree or evolutionary tree is a branching diagram or "tree" showing the inferred evolutionary relationships among various biological species based upon similarities and differences in their physical or genetic characteristics. The goal of this assignment is to construct the phylogenetic tree based on DNA/Protein sequences of species given in the dataset using Agglomerative(bottom-up) and Divisive(top-down) Hierarchical Clustering.

Dataset
-----------------
The original dataset consists of Amino Acid Sequence of Human Genes.
- Link to the dataset: http://genome.crg.es/datasets/ggalhsapgenes2005/hg16.311.putative.aa.fa

Sample Strings:
>chr10_1000
MAQTRYTQNRWRNEACREKALSTCGCSANVSQPTITTLLTPLTSETTPLREILVVSLKRK
GSDDVRHAIKDNNTLCPFVILKEPINAPSLVCHLHKSCCRHRQLQRSLRLKNYLECYTS*

>chr10_125
MELRALEADLNFLSVILFATFIFSLPLRLLIVIFQRYWAPASTLPPCISQKQPQDTSRLT
NTTSISDEESTANGNLCLSILKILAGLFQAASSSLRIMVMCHF*

Working
---------------
We used the levenshtein distance to find the edit distance between the strings which is used to make a n*n dissimilarity matrix where n is the number of strings. The distance matrix is then used to find the clusters in both top-down (divisive) using DIANA algorithm and then in a bottom-up (agglomerative) fashion.

Dendrogram in truncate mode with p=25:

![alt text](https://github.com/ronak-07/Agglomerative-Hierarchical-Clustering/blob/master/Agglomerative.JPG)

