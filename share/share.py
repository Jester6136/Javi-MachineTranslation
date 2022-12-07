import pandas as pd
import requests
import os
import re
import zipfile
data = pd.read_csv('https://raw.githubusercontent.com/Jester6136/data_opensubs/main/cleaned_data.csv')
data = data[['movie_name','ja_source','vi_source']].values.tolist()
r = requests.get("https://0327-113-160-133-144.ap.ngrok.io")
key = int(r.text)
data = data[key:]

import os
root_path_user = os.getcwd()
path = os.path.join(root_path_user, 'data')
if not os.path.exists(path):
    os.mkdir(path)
for item in data:
    movie_name,ja_source,vi_source=item[0],item[1],item[2]
    movie_name = re.sub('[^A-Za-z0-9]+', '_', movie_name).strip('_')
    directory = movie_name
    parent_dir = root_path_user+"\\data"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    file_extension = '.rar' 

    url = ja_source
    r_ja = requests.get(url)
    file_name_ja = path+'/ja'+file_extension
    
    with open(file_name_ja, 'wb') as f:
            f.write(r_ja.content)

    url_vi = vi_source
    r_vi = requests.get(url_vi)
    file_name_vi = path+'/vi'+file_extension
    with open(file_name_vi, 'wb') as f:
            # You will get the file in base64 as content
            f.write(r_vi.content)

    if not os.path.exists(path+'/vi'):
        os.mkdir(path+'/vi')
    if not os.path.exists(path+'/ja'):
        os.mkdir(path+'/ja')
    r = requests.get("https://0327-113-160-133-144.ap.ngrok.io")
    with zipfile.ZipFile(file_name_ja, 'r') as zip_ref:
        zip_ref.extractall(path+'/ja')

    with zipfile.ZipFile(file_name_vi, 'r') as zip_ref:
        zip_ref.extractall(path+'/vi')
    