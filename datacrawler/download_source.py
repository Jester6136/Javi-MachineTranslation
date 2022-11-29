import pandas as pd
from utils import unique_list
import requests

cleaned_data = pd.read_csv('cleaned_data.csv')

for item in cleaned_data[['movie_name','ja_source','vi_source']]:
    newpath = r'C:\Program Files\arbitrary' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # The link should be of the file directly
    url = 'https://www.opensubtitles.org/en/subtitleserve/sub/9318487'
    file_extension = '.rar'   # Example .wav
    r = requests.get(url)
    filename = 'Videodrome (1983)'+file_extension
    with open(filename, 'wb') as f:
            # You will get the file in base64 as content
            f.write(r.content)