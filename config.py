#config
import secret_var

ENDPOINT = '/solr/select?defType=dismax&q='
NAMESPACE = 'tulane-p16313coll68'
FILTERLIST = '&fl=PID%2C+mods_abstract_mt+dc.title'
WRITER = '&wt=json&indent=true&rows=999999'

SOLR_DATA  = secret_var.URL + ENDPOINT + NAMESPACE + FILTERLIST + WRITER

print('solr_data = ' + SOLR_DATA)
