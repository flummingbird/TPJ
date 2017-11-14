import json, urllib, config
from urllib.request import urlopen

# add in user io to request using config.NAMESPACE or using user input namespace.? or don't..

ldl_response = urlopen(config.SOLR_DATA);
print(ldl_response)
data = ldl_response.read()
decoded = data.decode('utf-8')
data_dict = json.loads(decoded)

print(data_dict)

with open('files/solr_out_tmp.json', 'w') as out:
    json.dump(data_dict, out, ensure_ascii=False)