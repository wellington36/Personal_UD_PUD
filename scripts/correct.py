from conllu import parse_incr
from io import open

list_def_det = ['a', 'as', 'o', 'os', 'A', 'As', 'O', 'Os']

data_file = open("pt_pud-ud-test.conllu", "r", encoding="utf-8")

with open("pt_pud-ud-test.conllu", "r+") as f: 
    for token_list in parse_incr(data_file): 
        for token in token_list:
            if ((token['form'] in list_def_det) and 
                token['upos'] == 'DET' and 
                token['deprel'] == 'det' and
                any([i['upos'] in ['NOUN', 'PROPN'] for i in token_list if i['id'] == token['head']])):
                
                token['feats']['PronType'] = 'Art'             
        serialized = token_list.serialize()
        f.write(serialized)
