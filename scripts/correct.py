from conllu import parse_incr
from io import open
import sys

list_def_det = ['a', 'as', 'o', 'os', 'A', 'As', 'O', 'Os']

def correctDet(file):

    data_file = open(file, "r", encoding="utf-8")

    with open(file, "r+") as f: 
        for token_list in parse_incr(data_file): 
            for token in token_list:
                if ((token['form'] in list_def_det) and 
                    token['upos'] == 'DET' and 
                    token['deprel'] == 'det' and
                    any([i['upos'] in ['NOUN', 'PROPN'] for i in token_list if i['id'] == token['head']])):
                
                    if token['feats'] == None:
                        token['feats'] = {'PronType': 'Art'}
                    else:
                        token['feats']['PronType'] = 'Art'           
            serialized = token_list.serialize()
            f.write(serialized)

for conll in sys.argv[1:]:
    correctDet(conll)