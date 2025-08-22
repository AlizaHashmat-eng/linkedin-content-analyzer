# notebooks/quick_eda.py
import pandas as pd
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv('data/linkedin_posts_sample.csv')
# Feature
df['engagement'] = df['reactions'] + df['comments'] + df['shares']
# Median engagement by post type
median_by_type = df.groupby('post_type')['engagement'].median().sort_values(ascending=False)


# Plot
plt.figure(figsize=(6,4))
median_by_type.plot(kind='bar')
plt.title('Median engagement by post type')
plt.ylabel('Median engagement')
plt.tight_layout()
plt.savefig('assets/median_engagement_by_type.png', dpi=150)
print('Saved assets/median_engagement_by_type.png')
