# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


# load in dataset
df = pd.read_excel("packer stats.xlsx")

# aggregate stats by season
season_summary = df.groupby("season").agg({
    "total_points": "mean",
    "opp_points": "mean",
    "pass_yds": "mean",
    "rush_yds": "mean",
    "sacks": "mean",
    "int": "mean"
}).reset_index()

# Save summary to CSV
season_summary.to_csv("season_summary.csv", index=False)

# EDA
sns.set_style("whitegrid")

packers_green = "#203731"
packers_gold = "#FFB612"

def plot_trend(x, y, title, ylabel):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=season_summary, x=x, y=y, marker="o", linewidth=2.5, color=packers_green, 
                 markerfacecolor=packers_gold, markeredgecolor=packers_green, markersize=8)
    plt.title(title, fontsize=14, color=packers_green)
    plt.xlabel("Season", fontsize=12, color=packers_green)
    plt.ylabel(ylabel, fontsize=12, color=packers_green)
    plt.xticks(rotation=45, color=packers_green)
    plt.yticks(color=packers_green)
    plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)
    plt.show()

# Plot key trends
plot_trend("season", "total_points", "Packers' Average Points Per Season", "Avg Points")
plot_trend("season", "opp_points", "Packers' Average Points Allowed Per Season", "Avg Opponent Points")
plot_trend("season", "pass_yds", "Packers' Passing Yards Per Season", "Avg Passing Yards")
plot_trend("season", "rush_yds", "Packers' Rushing Yards Per Season", "Avg Rushing Yards")
plot_trend("season", "sacks", "Packers' Average Sacks Allowed Per Season", "Avg Sacks")
plot_trend("season", "int", "Packers' Average Interceptions Thrown Per Season", "Avg Interceptions")


# Season-over-Season Performance Analysis**
# - Identify what led to improvement in scoring and what still needs work

# compute year over year stats
season_summary["points_diff"] = season_summary["total_points"].diff()
season_summary["pass_yds_diff"] = season_summary["pass_yds"].diff()
season_summary["rush_yds_diff"] = season_summary["rush_yds"].diff()
season_summary["sacks_diff"] = season_summary["sacks"].diff()
season_summary["int_diff"] = season_summary["int"].diff()

# Find seasons with the biggest improvements and declines in scoring
best_season = season_summary.loc[season_summary["points_diff"].idxmax()]
worst_season = season_summary.loc[season_summary["points_diff"].idxmin()]

print(f"Best season improvement: {best_season['season']} with a {best_season['points_diff']} point increase")
print(f"Worst season decline: {worst_season['season']} with a {worst_season['points_diff']} point drop")

# Identify correlations between stats and total points to determine key performance drivers
correlations = season_summary[["total_points", "pass_yds", "rush_yds", "sacks", "int"]].corr()["total_points"].sort_values(ascending=False)
print("Correlation with Total Points:\n", correlations)

# Visualize correlation of stats with total points
plt.figure(figsize=(10, 6))
sns.barplot(x=correlations.index, y=correlations.values, palette="Greens_r")
plt.title("Correlation of Stats with Total Points", fontsize=14, color=packers_green)
plt.ylabel("Correlation", fontsize=12, color=packers_green)
plt.xticks(rotation=45, color=packers_green)
plt.axhline(0, color="black", linestyle="--")
plt.show()

# Feature selection (select relevant features)
features = ['pass_yds', 'rush_yds', 'sacks', 'int']
# Creating a binary target: Win if total_points > 24, Loss otherwise
df['win'] = np.where(df['total_points'] > 24, 1, 0)  # You can adjust the threshold as needed

# Handling missing values (if any)
df = df.dropna(subset=features + ['win'])

# Split data into features (X) and target (y)
X = df[features]
y = df['win']

# Standardize the features (important for Logistic Regression)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
log_reg = LogisticRegression()

# Train the model
log_reg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)

# Classification Report (Precision, Recall, F1-Score)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualize Confusion Matrix
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Loss', 'Win'], yticklabels=['Loss', 'Win'])
plt.title("Confusion Matrix")
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()