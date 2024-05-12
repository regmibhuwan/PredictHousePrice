#importing necessary libraries
from sklearn.linear_model import LinearRegression
import numpy as np

#Example data
#x represents the features (house sizes in sq feet)
#y represents the target variable (house prices in thousand dollars)
x = np.array([[600], [800], [1000], [1200], [1400]])
y = np.array([150, 180, 210, 240, 270])

#Creating a linear regression model
model = LinearRegression()

#Training the model on the data
model.fit(x, y)

#Making a Prediction of price if size is 1100 sq feet
predicted_price = model.predict(np.array([[1100]]))

print(f"The predicted price of a 1100 sq feet house is ${predicted_price[0]: .2f} thousand.")


