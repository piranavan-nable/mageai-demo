if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Create the K means model for different values of K
def try_different_clusters(K, data_f):

    cluster_values = list(range(1, K+1))
    inertias=[]

    for c in cluster_values:
        model = KMeans(n_clusters = c,init='k-means++',max_iter=400,random_state=42)
        model.fit(data_f)
        inertias.append(model.inertia_)

    return inertias

@custom
def transform_custom(data,*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    # Define K-means model
    kmeans_model = KMeans(init='k-means++',  max_iter=400, random_state=42)

    # Train the model
    kmeans_model.fit(data[['products_purchased','complains','money_spent']])

    # Find output for k values between 1 to 12 
    outputs = try_different_clusters(12, data[['products_purchased','complains','money_spent']])
    distances = pd.DataFrame({"clusters": list(range(1, 13)),"sum of squared distances": outputs})

    # Re-Train K means model with k=5
    kmeans_model_new = KMeans(n_clusters = 5,init='k-means++',max_iter=400,random_state=42)

    kmeans_model_new.fit_predict(data[['products_purchased','complains','money_spent']])

    return kmeans_model_new


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
