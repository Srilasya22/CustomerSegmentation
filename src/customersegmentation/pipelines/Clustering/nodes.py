"""
This is a boilerplate pipeline 'Clustering'
generated using Kedro 0.19.1
"""
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
def cluster(df,scaled_data):
    try:
        X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

        # Calculate inertia for different values of k
        inertia = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)
            inertia.append(kmeans.inertia_)

        # Plot the Elbow Method curve
        plt.plot(range(1, 11), inertia, marker='o')
        plt.title('Elbow Method For Optimal k')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Inertia')
        plt.show()
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(scaled_data)
        cluster_1_df = df[df["Cluster"]==0]
        print(cluster_1_df)
        cluster_2_df = df[df["Cluster"]==1]
        print(cluster_2_df)
        cluster_3_df = df[df["Cluster"]==2]
        print(cluster_3_df)
        joblib.dump(kmeans, "model.pkl")       
        return df
    except Exception as e:
        logging.ERROR(f"Error occured in clustering {e}")
        raise e
