📊 CORD-19 Research Data Explorer

This project is part of the Frameworks Assignment. It guides you through analyzing the CORD-19 research dataset and building a simple Streamlit web app to visualize insights from COVID-19 research papers.

🎯 Objectives

By completing this project, you will:

Load and explore a real-world dataset (metadata.csv)

Apply basic data cleaning techniques

Create meaningful visualizations (matplotlib & seaborn)

Build an interactive Streamlit app

Present insights effectively

📂 Project Structure
Frameworks_Assignment/
│
├── data/
│   └── metadata.csv           # Dataset (or a smaller sample)
│
├── notebooks/
│   └── exploration.ipynb      # Jupyter Notebook for exploration (optional)
│
├── scripts/
│   └── analysis.py            # Data analysis & static visualizations
│
├── app.py                     # Streamlit web application
├── requirements.txt           # Dependencies list
└── README.md                  # Project documentation

📂 Dataset

This project uses the CORD-19 metadata file from Kaggle:
🔗 CORD-19 Research Challenge

⚠️ Important:

The full dataset is very large. For this assignment, download only the metadata.csv file.

Place metadata.csv inside the data/ directory before running the scripts or app.

⚙️ Installation

Clone this repo

git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment


Create and activate a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

📊 Data Analysis

Run the analysis script for cleaning and static visualizations:

python scripts/analysis.py


This will generate:

Publications by Year (bar chart)

Top Journals Publishing COVID-19 Research (bar chart)

Word Cloud of Paper Titles

🌐 Streamlit App

To launch the interactive app:

streamlit run app.py


Then open your browser at http://localhost:8501/

Features include:

Filter publications by year range

View sample data interactively

Explore publication trends and top journals

📝 Reflections

Handling missing values was necessary (e.g., titles, publish_time).

Publication counts showed a sharp increase in 2020–2021, consistent with the pandemic timeline.

Journals like BMJ and The Lancet appeared frequently.

Word frequency in titles highlighted keywords such as COVID-19, SARS-CoV-2, coronavirus.

📦 Requirements

Python 3.7+

pandas

matplotlib

seaborn

streamlit

wordcloud

🙌 Acknowledgment

Dataset source: CORD-19 Research Challenge