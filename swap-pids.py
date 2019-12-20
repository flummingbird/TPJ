import json

pids_input = input("pidlist filename?: ")

solr_file = input("solr_json to strip pids_input out of?: ")

with open('files/'+ pids_input) as f:
    pid_list = f.read().splitlines()

with open('files/' + solr_file, 'r', encoding='utf-8') as s:
    solr_out =  s.read()
    data_dict = json.loads(solr_out)

remaining_pids = []


#this is supposed to take out bad pids, and keep the remaining? why? don't I want to erase the bad pids
for j in pid_list:
    for k in data_dict['response']['docs']
        if j == k:
            continue
        else: 
            remaining_pids.append(k)


#this has already worked (or has it) 
# takes each pid in solr_file if it is in the list of pids, do nothing. bc we know it to be bad?
# if it doesn't match anyone???? wtf am I thinking
for i in data_dict["response"]["docs"]:
    if i["PID"] in pid_list:
        continue
    else:  
        remaining_pids.append(i["PID"])


bads = list(set(remaining_pids))

for z in bads:
    print(z)
