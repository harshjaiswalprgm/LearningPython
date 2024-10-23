import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_csv('Student_Marks.csv')


overall_mean = df['Marks'].mean()


median_by_class = df.groupby('number_courses')['Marks'].median().to_dict()


mode_by_class = df.groupby('number_courses')['Marks'].apply(lambda x: stats.mode(x)[0].tolist()).to_dict()


print(f"Overall Mean Marks: {overall_mean}")
print(f"Median Marks by Class: {median_by_class}")
print(f"Mode Marks by Class: {mode_by_class}")