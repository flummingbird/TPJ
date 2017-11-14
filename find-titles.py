import json

titles = input("titles to check for filename?: ")
sorl_file = input("solr_json to check for bad pids name?: ")

with open('bounce-titles') as f:
    title_list = f.read().splitlines()

 with open('solr-out.json', 'r', encoding='utf-8') as s:
     solr_out =  s.read()
     data_dict = json.loads(solr_out)



for x in title_list:
    for i in data_dict["response"]["docs"]:
        if x == i['dc.title'][0] or x + ':' == i['dc.title'][0]:
            print(i["PID"])


# if x not in data_dict and x + ':' not in data_dict:
#     print(x + ' not found')
    
# didn't work perfectly see bounce titles many missed \\" ect \( \)

# print(title_list[0])
# print(data_dict["response"]["docs"][0]["dc.title"][0])
