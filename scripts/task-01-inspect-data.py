import pandas as pd

# 1. Load the dataset
df = pd.read_csv("/home/mariam-musavi/OneDrive/02-Development/WASP-Relational-Learning-Planning/wasp_asp_exercise/train-features/spanner/features_small.csv")
# 2. Separate the complexity row (Row 0) and drop metadata tracking columns
complexities = df.iloc[0].drop(labels=["dead-end", "source"])

# 3. Cast the complexity scores to integers and sort them in ascending order
sorted_features = complexities.astype(int).sort_values()

# 4. Extract and print the top 5 lowest-complexity features along with their column indices
print("--- Top 5 Lowest Complexity Features ---")
for rank, (feature_name, complexity_score) in enumerate(sorted_features.head(5).items(), 1):
    column_index = df.columns.get_loc(feature_name)
    print(f"Rank {rank} | Column Index: {column_index} | Complexity: {complexity_score}")
    print(f"Formula: {feature_name}\n")