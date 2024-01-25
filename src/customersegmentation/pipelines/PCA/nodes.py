"""
This is a boilerplate pipeline 'PCA'
generated using Kedro 0.19.1
"""
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# import logging
# import numpy as np 
# import seaborn as sns
# def pc(df, scaled_data):
#     try:
#         pca = PCA(n_components=2)
#         pca_result = pca.fit_transform(scaled_data)

#         # Print the type of pca_result for debugging
#         print("Type of pca_result:", type(pca_result))

      
#         df['PCA1'] = pca_result[:, 0]
#         df['PCA2'] = pca_result[:, 1]

#         # Visualize clusters
#         plt.scatter(df['PCA1'], df['PCA2'], c=df['Cluster'], cmap='viridis')
#         plt.title('Customer Segmentation')
#         plt.xlabel('PCA1')
#         plt.ylabel('PCA2')
#         plt.show()
      
#         sns.countplot(x='Cluster', data=df)
#     except Exception as e:
#         logging.error(f"Error in pca {e}")
#         raise e
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import logging
import numpy as np
import seaborn as sns
def pc(df, scaled_data):
    try:
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(scaled_data)

        # Print the type of pca_result for debugging
        print("Type of pca_result:", type(pca_result))

        df['PCA1'] = pca_result[:, 0]
        df['PCA2'] = pca_result[:, 1]

        # Specify colors based on the 'Cluster' column
        colors = df['Cluster']

        # Visualize clusters with specified colors
        plt.scatter(df['PCA1'], df['PCA2'], c=colors,cmap='viridis')
        plt.title('Customer Segmentation')
        plt.xlabel('PCA1')
        plt.ylabel('PCA2')
        plt.show()
        sns.countplot(x='Cluster', data=df)
        plt.show()
       
        for c in df.drop(['Cluster'],axis=1):
            grid= sns.FacetGrid(df, col='Cluster')
            grid= grid.map(plt.hist, c)
            plt.show()
        
    except Exception as e:
        logging.error(f"Error in visualize_clusters {e}")
        raise e
