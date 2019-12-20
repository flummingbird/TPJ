import json

titles = input("titles to check for, filename?: ")

solr_file = input("solr_json to check for bad pids name?: ")

out_pids = input("filename for pids to be output to?: ")

with open('files/'+ titles) as f:
    title_list = f.read().splitlines()

with open('files/' + solr_file, 'r', encoding='utf-8') as s:
    solr_out =  s.read()
    data_dict = json.loads(solr_out)


# with open('files/bounce-titles') as f:
#     title_list = f.read().splitlines()

#  with open('files/solr-out.json', 'r', encoding='utf-8') as s:
#      solr_out =  s.read()
#      data_dict = json.loads(solr_out)

pid_str = ''

with open('files/' + out_pids, 'w') as pid_out:
    for x in title_list:
        for i in data_dict["response"]["docs"]:
            if x == i['dc.title'][0] or x + ':' == i['dc.title'][0]: #special case on the ':' only applied to bounce titles. can be taken out.
                pid_str += i['PID'] + '\n'
                print(i['PID'])
    pid_out.write(pid_str)
    
# if x not in data_dict and x + ':' not in data_dict:
#     print(x + ' not found')
    
# didn't work perfectly see bounce titles many missed \\" ect \( \)

# print(title_list[0])
# print(data_dict["response"]["docs"][0]["dc.title"][0])
