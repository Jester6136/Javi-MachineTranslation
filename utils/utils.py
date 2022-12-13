def unique_list(my_list):
    kiemtra = []
    return [x for x in my_list if x not in kiemtra and not kiemtra.append(x)]

def preprocessing(text):
    return text.replace('\u200e','').replace('\u3000','').replace("{\\an8}",'').replace('<font color="japanese">','').replace('<\/i>','').replace('<i>','').replace('- ','').replace('...','.')