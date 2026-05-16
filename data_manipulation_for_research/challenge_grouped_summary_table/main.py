import pandas as pd

def grouped_summary_table(df):
    
    pass
    summary = df.groupby(['experiment','group'])['score'].agg(['mean','std'])
    return summary

# Sample DataFrame for demonstration
data = {
    'experiment': ['A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'group': ['control', 'treatment', 'control', 'treatment', 'control', 'control', 'treatment'],
    'score': [88, 92, 85, 78, 90, 87, 80]
}
df = pd.DataFrame(data)
result = grouped_summary_table(df)
print(result)
