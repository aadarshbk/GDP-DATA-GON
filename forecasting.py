import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Assuming 'data' is your GDP growth rate time series data
# Split the data into training and testing sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Fit the ARIMA model
model = ARIMA(train_data, order=(1, 1, 1))
model_fit = model.fit()

# Forecast future GDP growth rates
forecast = model_fit.forecast(steps=len(test_data))

# Print the forecast
print(forecast)
