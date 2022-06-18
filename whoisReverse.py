import requests

api_key = <api key here>
company_name = <company name here>

url = f'http://api.whoxy.com/?key={api_key}&reverse=whois&company={company_name}'

r = requests.get(url)
packages_json = r.json()

domain_names = packages_json['search_result']
domain_name_list = [d['domain_name'] for d in domain_names if 'domain_name' in d]

textfile = open('reverse_whois.txt', 'w')
for e in domain_name_list:
    textfile.write(e + '\n')
textfile.close()
