import json

with open('good-bounce-pids') as f:
    title_list = f.read().splitlines()

with open('solr-out.json', 'r', encoding='utf-8') as s:
    solr_out =  s.read()
    data_dict = json.loads(solr_out)