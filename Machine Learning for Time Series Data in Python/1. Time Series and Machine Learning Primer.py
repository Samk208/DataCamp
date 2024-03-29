## Plotting a time series (I)
# In this exercise, you'll practice plotting the values of two time series without the time component.

# Two DataFrames, data and data2 are available in your workspace.

# Unless otherwise noted, assume that all required packages are loaded with their common aliases throughout this course.

# Note: This course assumes some familiarity with time series data, as well as how to use them in data analytics pipelines. For an introduction to time series, we recommend the Introduction to Time Series Analysis in Python and Visualizing Time Series Data with Python courses.

Instructions 1/3
15 XP
Print the first five rows of data.

# Plot the values column of both the data sets on top of one another, one per axis object.
# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(y='data_values', ax=axs[0])
data2.iloc[:1000].plot(y='data_values', ax=axs[1])
plt.show()

## Plotting a time series (II)
# You'll now plot both the datasets again, but with the included time stamps for each (stored in the column called "time"). Let's see if this gives you some more context for understanding each time series data.

# Instructions
# 100 XP
# Plot data and data2 on top of one another, one per axis object.
# The x-axis should represent the time stamps and the y-axis should represent the dataset values.

# Plot the time series in each dataset
# fig, axs = plt.subplots(2, 1, figsize=(5, 10))
# data.iloc[:1000].plot(x='time', y='data_values', ax=axs[0])
# data2.iloc[:1000].plot(x='time', y='data_values', ax=axs[1])
# plt.show()

# ## Fitting a simple model: classification
# In this exercise, you'll use the iris dataset (representing petal characteristics of a number of flowers) to practice using the scikit-learn API to fit a classification model. You can see a sample plot of the data to the right.

# Note: This course assumes some familiarity with Machine Learning and scikit-learn. For an introduction to scikit-learn, we recommend the Supervised Learning with Scikit-Learn and Preprocessing for Machine Learning in Python courses.

from sklearn.svm import LinearSVC

# Construct data for the model
X = data[["petal length (cm)","petal width (cm)"]]
y = data[['target']]

# Fit the model
model = LinearSVC()
model.fit(X, y)


## Predicting using a classification model
# Now that you have fit your classifier, let's use it to predict the type of flower (or class) for some newly-collected flowers.

# Information about petal width and length for several new flowers is stored in the variable targets. Using the classifier you fit, you'll predict the type of each flower.

# Instructions
# 100 XP
# Predict the flower type using the array X_predict.
# Run the given code to visualize the predictions.
# Create input array
X_predict = targets[['petal length (cm)', 'petal width (cm)']]

# Predict with the model
predictions = model.predict(X_predict)
print(predictions)

# Visualize predictions and actual values
plt.scatter(X_predict['petal length (cm)'], X_predict['petal width (cm)'],
            c=predictions, cmap=plt.cm.coolwarm)
plt.title("Predicted class values")
plt.show()



## Fitting a simple model: regression
# In this exercise, you'll practice fitting a regression model using data from the Boston housing market. A DataFrame called boston is available in your workspace. It contains many variables of data (stored as columns). Can you find a relationship between the following two variables?

# "AGE": proportion of owner-occupied units built prior to 1940
# "RM" : average number of rooms per dwelling
# Instructions
# 0 XP
# Prepare X and y DataFrames using the data in boston.
# X should be the proportion of houses built prior to 1940, y average number of rooms per dwelling.
# Fit a regression model that uses these variables (remember to shape the variables correctly!).
# Don't forget that each variable must be the correct shape for scikit-learn to use it!

from sklearn import linear_model

# Prepare input and output DataFrames
X = boston[['AGE']]
y = boston[['RM']]

# Fit the model
model = linear_model.LinearRegression()
model.fit(X, y)


## Predicting using a regression model
# Now that you've fit a model with the Boston housing data, lets see what predictions it generates on some new data. You can investigate the underlying relationship that the model has found between inputs and outputs by feeding in a range of numbers as inputs and seeing what the model predicts for each input.

# A 1-D array new_inputs consisting of 100 "new" values for "AGE" (proportion of owner-occupied units built prior to 1940) is available in your workspace along with the model you fit in the previous exercise.

# Instructions
# 100 XP
# Review new_inputs in the shell.
# Reshape new_inputs appropriately to generate predictions.
# Run the given code to visualize the predictions.

# Generate predictions with the model using those inputs
predictions = model.predict(new_inputs.reshape([-1,1]))

# Visualize the inputs and predicted values
plt.scatter(new_inputs, predictions, color='r', s=3)
plt.xlabel('inputs')
plt.ylabel('predictions')
plt.show()


## Inspecting the classification data
# In these final exercises of this chapter, you'll explore the two datasets you'll use in this course.

# The first is a collection of heartbeat sounds. Hearts normally have a predictable sound pattern as they beat, but some disorders can cause the heart to beat abnormally. This dataset contains a training set with labels for each type of heartbeat, and a testing set with no labels. You'll use the testing set to validate your models.

# As you have labeled data, this dataset is ideal for classification. In fact, it was originally offered as a part of a public Kaggle competition.

# Instructions
# 100 XP
# Use glob to return a list of the .wav files in data_dir directory.
# Import the first audio file in the list using librosa.
# Generate a time array for the data.
# Plot the waveform for this file, along with the time array.

import librosa as lr
from glob import glob

# List all the wav files in the folder
audio_files = glob(data_dir + '/*.wav')

# Read in the first audio file, create the time array
audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq

# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()


## Inspecting the regression data
# The next dataset contains information about company market value over several years of time. This is one of the most popular kind of time series data used for regression. If you can model the value of a company as it changes over time, you can make predictions about where that company will be in the future. This dataset was also originally provided as part of a public Kaggle competition.

# In this exercise, you'll plot the time series for a number of companies to get an understanding of how they are (or aren't) related to one another.

# Instructions
# 100 XP
# Import the data with Pandas (stored in the file 'prices.csv').
# Convert the index of data to datetime.
# Loop through each column of data and plot the the column's values over time.

# Read in the data
data = pd.read_csv('prices.csv', index_col=0)

# Convert the index of the DataFrame to datetime
data.index = pd.to_datetime(data.index)
print(data.head())

# Loop through each column, plot its values over time
fig, ax = plt.subplots()
for column in data:
    data[column].plot(ax=ax, label=column)
ax.legend()
plt.show()