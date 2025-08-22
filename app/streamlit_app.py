# app/streamlit_app.py
import streamlit as st
import pandas as pd


st.set_page_config(page_title='LinkedIn Content Analyzer (Demo)', layout='centered')
st.title('LinkedIn Content Analyzer — Demo')


# Load sample data
@st.cache_data
def load_data():
df = pd.read_csv('../data/linkedin_posts_sample.csv')
df['engagement'] = df['reactions'] + df['comments'] + df['shares']
return df


df = load_data()


st.subheader('Sample data')
st.dataframe(df[['date','post_type','topic','impressions','reactions','comments','shares','engagement']].head())


st.subheader('Median engagement by post type')
median_by_type = df.groupby('post_type')['engagement'].median().sort_values(ascending=False)
st.bar_chart(median_by_type)


st.write('Top findings (demo): carousels and videos tend to show higher median engagement in this sample.')
