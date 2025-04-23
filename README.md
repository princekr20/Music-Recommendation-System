Music Recommendation System

This project is a **lyrics-based music recommendation system** that uses **Natural Language Processing (NLP)** and the **Spotify API** to recommend similar songs based on lyrics and display their album covers. 
It features a clean and interactive **Streamlit web app**.

---

## 🎯 Objective
To recommend songs based on the lyrical similarity of a given song. The user enters or selects a song, and the system returns the top 5 most similar songs along with their album covers.

---

## 🧰 Technologies Used
- **Python** for backend logic
- **Streamlit** for web interface
- **NLTK** for natural language processing
- **TF-IDF (Term Frequency–Inverse Document Frequency)** for converting text to numbers
- **Cosine Similarity** for comparing songs
- **Spotipy (Spotify API)** to fetch album art
- **Pickle** for saving and loading models and data

---

## 🗂️ Files
- `generate_similarity.py`: Script to preprocess lyrics, create TF-IDF matrix, compute similarity, and save as `.pkl`
- `app.py`: Main Streamlit app that loads pickled data and runs the recommendation interface
- `df.pkl`: Pickled DataFrame containing song titles and artists
- `similarity.pkl`: Pickled similarity matrix between songs

---
