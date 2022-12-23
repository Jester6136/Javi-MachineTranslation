final_path = 'F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\final_data'

print('concat data!')
data_vi  = []
data_ja = []
with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\Tatoeba_2K\\data.ja','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_ja.extend(lines)
with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\Tatoeba_2K\\data.vi','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_vi.extend(lines)

with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\TEDjavi_106K\\ddd\\train\\train.ja','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_ja.extend(lines)
with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\TEDjavi_106K\\ddd\\train\\train.vi','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_vi.extend(lines)

with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\wiki_20K\\train.ja','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_ja.extend(lines)
with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\JaViCorpus\\wiki_20K\\train.vi','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_vi.extend(lines)

with open('F:\\ubuntu\\Javi-MachineTranslation\\datacrawler\\ja.train','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_ja.extend(lines)
with open('F:\\ubuntu\\Javi-MachineTranslation\\datacrawler\\vi.train','r',encoding='utf8') as f:
    lines = f.readlines()
    lines = list(map(lambda line:line.replace('\n',''),lines))
    data_vi.extend(lines)

with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\final_data\\train.vi', 'w',encoding='utf8') as f:
    f.write('\n'.join(data_vi))

with open('F:\\ubuntu\\Javi-MachineTranslation\\javi_data\\final_data\\train.ja', 'w',encoding='utf8') as f:
    f.write('\n'.join(data_ja))
print('successfully!')