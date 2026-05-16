import pandas as pd
from scipy.stats import ttest_ind

def compare_groups_ttest(df):
    group_a = df[df['group'] == 'A']['outcome']
    group_b = df[df['group'] == 'B']['outcome']
    t_stat, p_val = ttest_ind(group_a, group_b, nan_policy='omit')
    print("T-statistic:", t_stat)
    print("P-value:", p_val)
    if p_val < 0.05:
        interpretation = "The difference between groups is statistically significant (p < 0.05)."
    else:
        interpretation = "The difference between groups is not statistically significant (p >= 0.05)."
    print(interpretation)
    return t_stat, p_val
