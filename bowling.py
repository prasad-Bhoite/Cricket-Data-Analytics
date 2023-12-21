import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Bowling_ODI.csv'
cricket_data = pd.read_csv(file_path)

# Display basic information about the dataset
print(cricket_data.info())

# Display basic statistics of numerical columns
print(cricket_data.describe())

# Plotting histograms for numerical columns
cricket_data.hist(figsize=(10, 10))
plt.show()

# Convert 'Runs' column to numeric, handling errors
cricket_data['Runs'] = pd.to_numeric(cricket_data['Runs'], errors='coerce')

# Box plot for selected columns
selected_columns = ['Runs', 'Wkts', 'Ave', 'Econ', 'SR']

# Correlation matrix and heatmap
correlation_matrix = cricket_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Top 10 Wkts takers
top_10_wkts_takers = cricket_data.sort_values(by='Wkts', ascending=False).head(10)

# Plot bar chart for top 5 Wkts takers (categorical)
plt.figure(figsize=(10, 6))
sns.countplot(y='Player', data=top_10_wkts_takers.head(5), palette='viridis')
plt.title('Top 5 Wkts Takers')
plt.xlabel('Count')
plt.ylabel('Player')
plt.show()