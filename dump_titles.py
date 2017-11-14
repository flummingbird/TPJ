#spit out titles
import json

file_name = input("outfile name?: ")

with open('solr_out_tmp.json', 'r', encoding='utf-8') as s:
     solr_out =  s.read()
     data_dict = json.loads(solr_out)

file_str = ''
with open(file_name, 'w') as out:
    for i in data_dict["response"]["docs"]:
        file_str += i['dc.title'][0] + "\n"
    out.write(file_str)


