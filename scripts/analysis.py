import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Load data
df = pd.read_csv("../data/metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df = df.dropna(subset=['title'])

# Add abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# ---- Example Analysis ----
# Publications by Year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.show()

# Top Journals
top_journals = df['journal'].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top Journals")
plt.show()

# Wordcloud
words = " ".join(df['title'].dropna()).lower()
wc = WordCloud(width=800, height=400, background_color="white").generate(words)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
