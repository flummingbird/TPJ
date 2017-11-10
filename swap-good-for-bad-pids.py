import json

with open('good-bounce-pids.txt') as f:
    g_pid_list = f.read().splitlines()

with open('solr-out.json', 'r', encoding='utf-8') as s:
    solr_out =  s.read()
    data_dict = json.loads(solr_out)

bad_pids = []


for i in data_dict["response"]["docs"]:
    if i["PID"] in g_pid_list:
        continue
    else:  
        bad_pids.append(i["PID"])


bads = list(set(bad_pids))

for z in bads:
    print(z)