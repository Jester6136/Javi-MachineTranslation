import pandas as pd
from utils import unique_list

rawdata = pd.read_csv('rawdata.csv')
rawdata = rawdata.values.tolist()
identical_name_data =[]
for i in range(len(rawdata)):
    tmp = []
    for j in range(len(rawdata)):
        if(rawdata[i][0]==rawdata[j][0]):
            tmp.append(rawdata[j])
    if len(tmp)>1:
        identical_name_data.append(tmp)
identical_name_data  = unique_list(identical_name_data)

non_duplicate_lang_flag_data = []
for items in identical_name_data:
    check_vi = False
    check_ja = False
    for item in items:
        if item[1]=='ja':
            check_ja = True
        if item[1]=='vi':
            check_vi = True
    if check_vi and check_ja:
        non_duplicate_lang_flag_data.append(unique_list(items))

data=[]
for items in non_duplicate_lang_flag_data:
    if len(items) ==2:
        data.append(items)
    else:
        for items in have_some_subs:
            mmm = []
            ck_tmp_vi=False
            ck_tmp_ja=False
            for item in items:
                if(item[1]=='ja' and not ck_tmp_ja):
                    ck_tmp_ja=True
                    mmm.append(item)
                if(item[1]=='vi' and not ck_tmp_vi):
                    ck_tmp_vi=True
                    mmm.append(item)
        data.append(mmm)

data_to_csv = []
for items in data:
    vi_data = []
    ja_data = []
    if items[0][1] == 'vi':
        data_to_csv.append([items[1][0],items[1][2],items[1][3],items[1][4],items[0][2],items[0][3],items[0][4]])
    if items[0][1] == 'ja':
        data_to_csv.append([items[0][0],items[0][2],items[0][3],items[0][4],items[1][2],items[1][3],items[1][4]])

df2 = pd.DataFrame(data_to_csv, columns=['movie_name','ja_release','ja_source','ja_author','vi_release','vi_source','vi_author'])

df2.to_csv('cleaned_data.csv',index=False)

print('Done! file saved to cleaned_data.csv')