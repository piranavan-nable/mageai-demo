from mage_ai.io.file import FileIO
from pandas import DataFrame
import joblib

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df: DataFrame, **kwargs) -> None:

     # Define K-means model
    kmeans_model = KMeans(init='k-means++',  max_iter=400, random_state=42)

    # Train the model
    kmeans_model.fit(data[['products_purchased','complains','money_spent']])

    # Find output for k values between 1 to 12 
    outputs = try_different_clusters(12, data[['products_purchased','complains','money_spent']])
    distances = pd.DataFrame({"clusters": list(range(1, 13)),"sum of squared distances": outputs})

    # Re-Train K means model with k=5
    kmeans_model_new = KMeans(n_clusters = 5,init='k-means++',max_iter=400,random_state=42)

    new_predictions = kmeans_model_loaded.predict(dara[['products_purchased','complains','money_spent']])
 
    # Count the number of data points in each cluster
    cluster_counts = pd.Series(new_predictions).value_counts()

    # Print the counts of data points in each cluster
    print("Cluster Counts:")
    print(cluster_counts)

    # Calculate the average spending behavior for each cluster
    cluster_spending = new_data.groupby(new_predictions)['money_spent'].mean()

    # Print the average spending behavior for each cluster
    print("\nAverage Spending Behavior for Each Cluster:")
    print(cluster_spending)