if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from pandas import DataFrame
import pandas as pd
import joblib

@custom
def segment_customerts(df:DataFrame,*args, **kwargs) -> None:


    # Load the saved K-means model
    kmeans_model_loaded = joblib.load('kmeans_model.pkl')
    print(kmeans_model_loaded)

    #print(df)
    print("Columns in the DataFrame:")
    print(df.columns)

    # Strip leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Check if all required columns exist in the DataFrame
    required_columns = ['products_purchased', 'complains', 'money_spent']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print(f"Error: Missing columns in DataFrame: {missing_columns}")
    else:
        # Access the desired columns
        print(df[['products_purchased', 'complains', 'money_spent']])


    # Use the loaded K-means model to predict clusters for the new data
    new_predictions = kmeans_model_loaded.predict(df[['products_purchased','complains','money_spent']])
    
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