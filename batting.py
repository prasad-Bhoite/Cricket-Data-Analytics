import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a CSV file named 'ODI data.csv' containing your cricket data
# You can read the data into a DataFrame using pandas

file_path = 'ODI data.csv'
cricket_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(cricket_data.head())

# Basic statistics of numerical columns
print("\nBasic statistics of numerical columns:")
print(cricket_data.describe())

# Top 10 players with the highest runs
top_run_scorers = cricket_data.sort_values(by='Runs', ascending=False).head(10)
print("\nTop 10 players with the highest runs:")
print(top_run_scorers[['Player', 'Runs']])

# Convert 'Ave' column to numeric, handling errors with 'coerce' to replace non-numeric values with NaN
cricket_data['Ave'] = pd.to_numeric(cricket_data['Ave'], errors='coerce')

# Convert 'SR' column to numeric, handling errors with 'coerce' to replace non-numeric values with NaN
cricket_data['SR'] = pd.to_numeric(cricket_data['SR'], errors='coerce')

# Convert '100' column to numeric, handling errors with 'coerce' to replace non-numeric values with NaN
cricket_data['100'] = pd.to_numeric(cricket_data['100'], errors='coerce')

# Convert '50' column to numeric, handling errors with 'coerce' to replace non-numeric values with NaN
cricket_data['50'] = pd.to_numeric(cricket_data['50'], errors='coerce')

# Players with the highest average
highest_average_player = cricket_data.loc[cricket_data['Ave'].idxmax()]
print("\nPlayer with the highest average:")
print(highest_average_player[['Player', 'Ave']])

# Strike rate analysis
print("\nStrike rate analysis:")
strike_rate_analysis = pd.cut(cricket_data['SR'], bins=[0, 50, 75, 100, 125, 150], labels=['0-50', '51-75', '76-100', '101-125', '126-150'])
strike_rate_counts = strike_rate_analysis.value_counts()
print(strike_rate_counts)

# Number of players with 100s and 50s
players_with_100s = cricket_data[cricket_data['100'] > 0]
players_with_50s = cricket_data[cricket_data['50'] > 0]
print(f"\nNumber of players with 100s: {len(players_with_100s)}")
print(f"Number of players with 50s: {len(players_with_50s)}")

# Pie chart for the distribution of players based on 100s
plt.figure(figsize=(8, 8))
plt.pie(players_with_100s['100'].value_counts(), labels=players_with_100s['100'].value_counts().index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Players based on 100s')
plt.show()

# Bar chart for the top 10 players with the highest runs
plt.figure(figsize=(10, 6))
plt.bar(top_run_scorers['Player'], top_run_scorers['Runs'], color='skyblue')
plt.xlabel('Player')
plt.ylabel('Runs')
plt.title('Top 10 Players with the Highest Runs')
plt.xticks(rotation=45)
plt.show()

# Heatmap for correlation matrix
correlation_matrix = cricket_data.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()