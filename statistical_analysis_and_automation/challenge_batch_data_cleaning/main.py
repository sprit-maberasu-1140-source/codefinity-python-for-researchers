import pandas as pd

def clean_scores_batch(site_dataframes):
    cleaned_dfs = []
    for df in site_dataframes:
        mean_score = df['score'].mean()
        cleaned_df = df.copy()
        cleaned_df['score'] = cleaned_df['score'].fillna(mean_score)
        cleaned_dfs.append(cleaned_df)
    return cleaned_dfs

df1 = pd.DataFrame({'id': [1, 2, 3], 'score': [90, None, 85]})
df2 = pd.DataFrame({'id': [4, 5, 6], 'score': [None, 78, 80]})
site_data = [df1, df2]

cleaned_data = clean_scores_batch(site_data)
print(cleaned_data[0])
print(cleaned_data[1])