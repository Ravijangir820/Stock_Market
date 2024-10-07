import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from search import search_file
# Load the stock price data

file_name = input("Enter the file name to search for (e.g., 'myfile.txt'): ")
search_path = None
search_path = search_path if search_path else None

file_path = search_file(file_name,search_path)
print(file_path)
data = pd.read_csv(file_path[0])

# Extract features and target variable
X = data[['Date','High','Low','Close','Open','Adj Close','Volume']]  # Replace with your desired features 
y = data['Close']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,shuffle=False)

print(X_test.columns)

date = X_test['Date']
X_train = X_train.drop(columns=['Date'])
X_test = X_test.drop(columns=['Date'])

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


# Plot the actual vs. predicted values
plt.figure(figsize=(12, 6))
plt.scatter(date, y_test, color='blue', label='Actual')
plt.plot(date, y_pred, color='red', label='Forecast')
plt.title('Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()