from conllu import parse_incr
from io import open

list_def_det = ['a', 'as', 'o', 'os', 'A', 'As', 'O', 'Os']

data_file = open("pt_pud-ud-test.conllu", "r", encoding="utf-8")

with open("test.conllu", "w") as f:
    for token_list in parse_incr(data_file):
        for token in token_list:
            if (token['form'] in list_def_det and token['upos'] == 'DET'):
                token['feats']['PronType'] = 'Art'                
        serialized = token_list.serialize()
        f.write(serialized)
        f.write('\n\n')