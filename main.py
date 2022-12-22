import pandas as pd
import matplotlib.pyplot as plt

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

# Example usage
analyze_data("data.csv")
