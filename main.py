import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def analyze_data(data_path):
  # Load the data into a Pandas dataframe
  df = pd.read_csv(data_path)

  # Calculate some basic statistics
  mean = df['column_name'].mean()
  std = df['column_name'].std()
  min_val = df['column_name'].min()
  max_val = df['column_name'].max()

  # Print the results
  print(f"Mean: {mean}")
  print(f"Standard Deviation: {std}")
  print(f"Minimum Value: {min_val}")
  print(f"Maximum Value: {max_val}")

  # Create a histogram to visualize the distribution of the data
  df.hist(column='column_name', bins=50)
  plt.show()
  
  # Use K-Means clustering to group the data into clusters
  kmeans = KMeans(n_clusters=5)
  kmeans.fit(df[['column_name_1', 'column_name_2']])
  df['cluster'] = kmeans.predict(df[['column_name_1', 'column_name_2']])

  # Create a scatterplot to visualize the clusters
  plt.scatter(df['column_name_1'], df['column_name_2'], c=df['cluster'], cmap='viridis')
  plt.xlabel('Column Name 1')
  plt.ylabel('Column Name 2')
  plt.show()

# Example usage
analyze_data("data.csv")
