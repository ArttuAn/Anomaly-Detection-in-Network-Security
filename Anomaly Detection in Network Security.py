# Import required libraries
import numpy as np                  # For numerical operations
import matplotlib.pyplot as plt     # For plotting and visualizations
import pandas as pd                 # For data manipulation and reading CSV files
from sklearn.cluster import KMeans  # For the K-means algorithm
from sklearn.preprocessing import StandardScaler  # For standardizing the dataset

# Read the data
df = pd.read_csv("log2.csv")  # Reading the CSV data into a pandas DataFrame

# TODO: Exploring the data (first few rows, data types, summary statistics, etc.)
# df.head(), df.info(), df.describe()

# Selecting the subset of features

# Converting Action to numerical labels

# Standardizing the data

# Initial visualizations

# Training the K-means model

# Evaluating the model

# Using the trained model for "predictions" / using the model to see to which cluster a given data point belngs to

# Interpreting the results