def unique_list(my_list):
    kiemtra = []
    return [x for x in my_list if x not in kiemtra and not kiemtra.append(x)]

some_punctuation = ['[',']','?','!',',',':',';','-','_','{','}','(',')','"',"'",'.']

def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)

def remove_parentheses_ja(txt):
    return re.sub(r'（[^>]*）', '', txt)

def lowercase(text):
    if text.isupper():
        return text
    for item in some_punctuation:   
        text = str(item+' ').join(map(lambda piece: piece.strip()[0].lower() + piece.strip()[1:] if len(piece.strip())!=0 else piece, text.split(item)))
    return text

def remove_dup_space(text):
    return re.sub(r'\s\s+', ' ', text.strip())

def give_spaces_punctuation(text):
    for item in some_punctuation:  
        text = str(' '+item+' ').join(text.split(item))
    return remove_dup_space(text)

def preprocessing(text):
    text = remove_dup_space(text)
    text = remove_parentheses_ja(text)
    text = remove_html(text)
    return text.replace('\u200e','').replace('\u3000','').replace("{\\an8}",'').replace('- ','').replace('...','.').replace('…','')

def vietnam_preprocessing(text):
    text = lowercase(text)
    text = give_spaces_punctuation(text)
    text = remove_dup_space(text)
    return text