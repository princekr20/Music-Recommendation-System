import pandas as pd
import pickle

# Load your dataset (change path & file name if needed)
df = pd.read_csv("data/spotify_millsongdata.csv")  # if the file is inside a folder named 'data'



# You can do any preprocessing here if needed

# Save the DataFrame as a pickle file
with open("df.pkl", "wb") as f:
    pickle.dump(df, f)

print("✅ Pickle file created: df.pkl")


import pickle

with open('similarity.pkl', 'rb') as f:
    data = f.read()
    print(data[:100])  # just to see if it looks like binary pickle data

