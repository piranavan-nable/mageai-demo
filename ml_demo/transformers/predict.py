if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import joblib
from pandas import DataFrame

@transformer
def transform(df: DataFrame, *args, **kwargs) -> DataFrame:
    
    # Load the saved K-means model
    kmeans_model_loaded = joblib.load('kmeans_model.pkl')
    
    # Use the loaded K-means model to predict clusters for the new data
    new_predictions = kmeans_model_loaded.predict(df[['products_purchased','complains','money_spent']])

    # # Count the number of data points in each cluster
    # cluster_counts = pd.Series(new_predictions).value_counts()

    # # Print the counts of data points in each cluster
    # print("Cluster Counts:")
    # print(cluster_counts)

    # # Calculate the average spending behavior for each cluster
    # cluster_spending = new_data.groupby(new_predictions)['money_spent'].mean()

    # # Print the average spending behavior for each cluster
    # print("\nAverage Spending Behavior for Each Cluster:")
    # print(cluster_spending)
    return 1
