import json

pids_input = input("pidlist filename?: ")

solr_file = input("solr_json to strip pids_input out of?: ")

with open('files/'+ pids_input) as f:
    pid_list = f.read().splitlines()

with open('files/' + solr_file, 'r', encoding='utf-8') as s:
    solr_out =  s.read()
    data_dict = json.loads(solr_out)

remaining_pids = []


for i in data_dict["response"]["docs"]:
    if i["PID"] in pid_list:
        continue
    else:  
        remaining_pids.append(i["PID"])


bads = list(set(bad_pids))

for z in bads:
    print(z)