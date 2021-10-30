from conllu import parse_incr
from io import open

data_file = open("pt_bosque-ud-dev.conllu", "r", encoding="utf-8")

with open("dev_without_features.conllu", "w") as f:
    for token_list in parse_incr(data_file):
        for token in token_list:
            if (token['form'] == 'de'):
                print(token['deprel'])
        serialized = token_list.serialize()
        f.write(serialized)
        f.write('\n\n')