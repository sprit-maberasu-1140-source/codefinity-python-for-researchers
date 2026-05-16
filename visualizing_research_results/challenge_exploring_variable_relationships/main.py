import pandas as pd
import matplotlib.pyplot as plt

def plot_study_vs_score(df):
    # Create scatter plot
    plt.scatter(df['study_hours'], df['exam_score'])
    # Calculate correlation coefficient
    correlation = df['study_hours'].corr(df['exam_score'])
    # Annotate correlation on plot
    annotation_text = f"Correlation: {correlation:.2f}"
    plt.annotate(
        annotation_text,
        xy=(0.05, 0.95),
        xycoords='axes fraction',
        fontsize=12,
        verticalalignment='top'
    )
    # Label the axes
    plt.xlabel('Study Hours')
    plt.ylabel('Exam Score')
    # Set the plot title
    plt.title('Study Hours vs Exam Score')
    # Show the plot
    plt.show()

# Sample DataFrame for demonstration
data = {
    'study_hours': [2, 4, 6, 8, 10],
    'exam_score': [55, 60, 65, 80, 90]
}
df = pd.DataFrame(data)
plot_study_vs_score(df)