from conllu import parse_incr
from io import open

data_file = open("pt_pud-ud-test.conllu", "r", encoding="utf-8")

with open("test_update.conllu", "w") as f:
    for token_list in parse_incr(data_file):
        for token in token_list:
            if ((token['form'] == 'a' or 
                 token['form'] == 'o' or 
                 token['form'] == 'os' or 
                 token['form'] == 'as') and token['upos'] == 'DET'):
                token['feats']['PronType'] = 'Art'                
        serialized = token_list.serialize()
        f.write(serialized)
        f.write('\n\n')