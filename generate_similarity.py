import pandas as pd
import nltk
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')

# Preprocessing
stemmer = PorterStemmer()

def preprocess(text):
    text = text.lower().replace('\n', ' ')
    tokens = nltk.word_tokenize(text)
    stemmed = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed)

# Load data
df = pd.read_csv("data/spotify_millsongdata.csv")
df = df.sample(5000).drop("link", axis=1).reset_index(drop=True)
df.dropna(subset=['text'], inplace=True)

# Preprocess lyrics
df['processed_text'] = df['text'].apply(preprocess)

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df['processed_text'])

# Compute similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Save similarity matrix and basic song info
pickle.dump(similarity, open("similarity.pkl", "wb"))
pickle.dump(df[['song', 'artist']], open("songs.pkl", "wb"))

print("✅ similarity.pkl and songs.pkl files generated successfully!")
