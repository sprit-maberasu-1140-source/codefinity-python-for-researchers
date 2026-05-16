import pandas as pd

def extract_control_above_mean(df):
    mean_measurement = df['measurement'].mean()
    filtered = df[(df['group'] == 'control') & (df['measurement'] > mean_measurement)]
    return filtered.sort_values(by='measurement', ascending=False)

# Sample DataFrame
data = {
    'subject_id': [1, 2, 3, 4, 5, 6],
    'group': ['control', 'treatment', 'control', 'control', 'treatment', 'control'],
    'measurement': [10.5, 15.2, 13.1, 9.8, 16.4, 14.0]
}
df = pd.DataFrame(data)

result = extract_control_above_mean(df)
print(result)