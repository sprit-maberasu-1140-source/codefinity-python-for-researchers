import pandas as pd

def clean_survey_data(df):
    median_age=df['age'].median()  
    mean_score=df['score'].mean()
    df['age']=df['age'].fillna(median_age)
    df['score']=df['score'].fillna(mean_score)
    return df

data = {
    'participant': ['A', 'B', 'C', 'D', 'E'],
    'age': [25, None, 30, 22, None],
    'score': [85, 90, None, 88, None]
}
survey_df = pd.DataFrame(data)

cleaned_survey_df = clean_survey_data(survey_df)

print(cleaned_survey_df)
