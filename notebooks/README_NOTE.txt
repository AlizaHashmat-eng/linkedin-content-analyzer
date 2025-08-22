Run steps (local):
1) python -m venv venv
2) source venv/bin/activate # or venv\Scripts\activate on Windows
3) pip install -r requirements.txt
4) python generate_sample_data.py # creates data/linkedin_posts_sample.csv
5) python notebooks/quick_eda.py # creates assets/median_engagement_by_type.png
6) streamlit run app/streamlit_app.py # run demo app


If you skip streamlit, just commit the CSV and the generated png to assets and push to GitHub.
