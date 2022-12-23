import sys
sys.path.append('/media/ba/N_Vol/ubuntu/Javi-MachineTranslation')
from config import *
import os
import pandas as pd
from utils import preprocessing
from sklearn.model_selection import train_test_split
import re

DATA_PATH = 'F:\\ubuntu\\Javi-MachineTranslation\\data'
print('getdata raw...')
def convert_to_seconds(inputs:str):
    input_split = inputs.split(':')
    hh,mm,ss=input_split[0],input_split[1],input_split[2]
    return float(hh)*60*60+float(mm)*60+float(ss.replace(',','.'))

approximate_time = 0.8

data = []

for file in os.listdir(DATA_PATH):
    folder_path = os.path.join(DATA_PATH, file)
    if os.path.isdir(folder_path):
        ja_folder = os.path.join(folder_path,'ja')
        vi_folder = os.path.join(folder_path,'vi')
        data_vn = []
        for piece in os.listdir(vi_folder):
            vi_sub = os.path.join(vi_folder, piece)
            if vi_sub.strip().endswith('.srt'):
                with open(vi_sub,'r',encoding='utf8') as f:
                    subs_vn = ''.join(f.readlines()).replace('\n\n\n','\n\n').strip().split('\n\n')
                    for item in subs_vn:
                        blocks = item.split('\n')
                        times = blocks[1].split(' --> ')
                        print(times,file)
                        sub_index,time_start,time_end,content = blocks[0],convert_to_seconds(times[0]),convert_to_seconds(times[1]),' '.join(blocks[2:])
                        data_vn.append([sub_index,time_start,time_end,content])

        data_ja = []
        for piece in os.listdir(ja_folder):
            ja_sub = os.path.join(ja_folder, piece)
            if ja_sub.strip().endswith('.srt'):
                with open(ja_sub,'r',encoding='utf8') as f:
                    subs_ja = ''.join(f.readlines()).strip().split('\n\n')
                    for item in subs_ja:
                        blocks = item.split('\n')
                        times = blocks[1].split(' --> ')
                        sub_index,time_start,time_end,content = blocks[0],convert_to_seconds(times[0]),convert_to_seconds(times[1]),' '.join(blocks[2:])
                        data_ja.append([sub_index,time_start,time_end,content])
        data_tmp = []
        for vn_index in range(len(data_vn)):
            for ja_index in range(vn_index+50):
                if ja_index >= len(data_ja):
                    break
                if(abs(data_vn[vn_index][1]-data_ja[ja_index][1])<=approximate_time):
                    data_tmp.append([data_vn[vn_index],data_ja[ja_index]])
        data.append(data_tmp)

data_format = []
for sub in data:
    for item in sub:
        data_format.append([preprocessing(item[0][3]),preprocessing(item[1][3])])

df = pd.DataFrame(data_format, columns=['vi','ja'])
df.to_csv('F:\\ubuntu\\Javi-MachineTranslation\\datacrawler\\javi.csv',index=False)

df = pd.read_csv('F:\\ubuntu\\Javi-MachineTranslation\\datacrawler\\javi.csv')
print('getdata raw successfully')
print('preprocessing data....')
vi = list(df['vi'])
ja = list(df['ja'])
preprocessed = []
for i in range(len(vi)):
    preprocessed.append([preprocessing(ja[i]),vietnam_preprocessing(preprocessing(vi[i]))])

df2 = pd.DataFrame(preprocessed, columns=['ja','vi'])
df2_clean = df2.drop_duplicates('vi')
df2_clean.to_csv("cleaned_javi.csv",index=False)
print('preprocessing data successfully')
print('saved to cleaned_javi.csv')

print('make train dataset')
df2 = pd.read_csv('F:\\ubuntu\\Javi-MachineTranslation\\datacrawler\\cleaned_javi.csv')
vi = list(df2['vi'])
ja = list(df2['ja'])
f1 = open('ja.train','w',encoding='utf8')
f2 = open('vi.train','w',encoding='utf8')
for i,item in enumerate(ja):
    if (len(vi[i])>15):
        f1.write(str(ja[i])+'\n')
        f2.write(str(vi[i])+'\n')
f1.close()
f2.close()
print('make train dataset successfully')