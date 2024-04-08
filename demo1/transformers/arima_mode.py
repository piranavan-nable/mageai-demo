
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    from statsmodels.tsa.statespace.sarimax import SARIMAX



new_df['DateTime'] = pd.to_datetime(new_df['DateTime'])
new_df.set_index('DateTime', inplace=True)

# Plot your data to visualize the time series
new_df['TotalSales'].plot(figsize=(12, 6))
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Split the data into training and testing sets
train_size = int(len(new_df) * 0.8)
train, test = new_df[0:train_size], new_df[train_size:]

# Fit SARIMA model
order = (1, 1, 1)  
seasonal_order = (1, 1, 1, 12)  

model = SARIMAX(train['TotalSales'], order=order, seasonal_order=seasonal_order)
fit_model = model.fit(disp=False)

# Forecast
forecast_steps = len(test)
forecast = fit_model.get_forecast(steps=forecast_steps)

# Get confidence intervals
ci = forecast.conf_int()

# Plot the actual vs predicted values
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['TotalSales'], label='Train')
plt.plot(test.index, test['TotalSales'], label='Test')
plt.plot(forecast.index, forecast.predicted_mean, label='Forecast', color='red')
plt.fill_between(ci.index, ci.iloc[:, 0], ci.iloc[:, 1], color='red', alpha=0.2)
plt.title('Total Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.show()

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
