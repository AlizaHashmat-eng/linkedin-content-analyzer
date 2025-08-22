# generate_sample_data.py
import pandas as pd
import random
from datetime import datetime, timedelta


types = ['carousel','image','text','video']
topics = ['personal','tech','ai','growth','branding']


rows = []
start = datetime.today() - timedelta(days=200)
for i in range(50):
d = start + timedelta(days=i*3)
t = random.choice(types)
topic = random.choice(topics)
impressions = random.randint(200,5000)
reactions = random.randint(5,400)
comments = random.randint(0,80)
shares = random.randint(0,50)
text = f"Sample post {i+1} about {topic}"
rows.append({
'date': d.strftime('%Y-%m-%d'),
'post_type': t,
'topic': topic,
'text': text,
'impressions': impressions,
'reactions': reactions,
'comments': comments,
'shares': shares
})


df = pd.DataFrame(rows)
df.to_csv('data/linkedin_posts_sample.csv', index=False)
print("Saved data/linkedin_posts_sample.csv")
