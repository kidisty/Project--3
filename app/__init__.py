from flask import Flask
from config import Config
import pandas as pd
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)
app.config.from_object(Config)

df = pd.read_csv('lego_clean_data_GK_KGv2.csv')
df['Year'] = df['Year'] - df['Year'].min()

df_x = df[['piece_count', 'difficulty', 'star_rating', 'Year', 'Price']]
nbrs = NearestNeighbors(n_neighbors=6).fit(df_x)
print ("got through model")

from app import routes