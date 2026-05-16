import matplotlib.pyplot as plt

def plot_publications_vs_citations(df):
    fig, ax = plt.subplots()
    ax.plot(df['year'], df['publications'],
            color='blue', marker='o', label='Publications')
    ax.plot(df['year'], df['citations'],
            color='green', marker='s', label='Citations')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    ax.set_title('Publications and Citations Over Time')
    ax.legend()
    return fig, ax

# Sample DataFrame for demonstration
import pandas as pd
data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'publications': [10, 15, 20, 25, 30],
    'citations': [50, 80, 120, 200, 300]
}
df = pd.DataFrame(data)

fig, ax = plot_publications_vs_citations(df)
plt.show()