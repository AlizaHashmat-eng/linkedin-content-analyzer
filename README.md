# LinkedIn Content Performance Analyzer — Aliza Hashmat

**Short summary**  
A small analytics project analyzing my last 50 LinkedIn posts to identify which formats and tactics drive engagement. Demo to show data workflow, key findings, and a replayable pipeline.

---

## 🚀 Project snapshot
- **Goal:** Turn guesswork into decisions — identify post types that increase engagement.
- **Data:** 50 posts (date, post_type, text, impressions, reactions, comments, shares).
- **Stack:** Python (pandas, scikit-learn), SQL (optional), Streamlit / Power BI (dashboard), Matplotlib/Seaborn.
- **Deliverables:** analysis notebook, sample data CSV, dashboard screenshots.

---

## 📂 Files in this repo
- `data/linkedin_posts_sample.csv` — sample dataset (50 rows).  
- `notebooks/eda.ipynb` — exploratory data analysis & charts.  
- `notebooks/model.ipynb` — lightweight engagement bucket model (optional).  
- `app/streamlit_app.py` — simple Streamlit dashboard (demo).  
- `assets/` — screenshots used in README and post.  
- `README.md` — this file.

---

## 🔎 Key findings (example / demo results)
- **Carousels** show higher median engagement than single images.  
- **Short personal stories** generate more comments.  
- **Clear CTAs** increase shares and saves.

> Note: This repo contains a sample dataset and scripts to reproduce the demo results quickly.

---

## How to run (quick)
1. Clone the repo:
```bash
git clone https://github.com/<alizahashmat-eng>/linkedin-content-analyzer.git
cd linkedin-content-analyzer
git clone https://github.com/<your-username>/linkedin-content-analyzer.git
cd linkedin-content-analyzer
