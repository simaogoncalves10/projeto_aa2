import urllib.parse
import requests
import json


#Rescolher a informação da API pub
for n_page in range(146):
    main_api = 'https://gcplatform.bio.di.uminho.pt/api/pub/page/find/pubmedindexed/gastric%20cancer?page={}&size=1000&sort=string'.format(n_page)
    address = 'lhr'
    url = main_api + urllib.parse.urlencode({'address': address})
    json_data = requests.get(url).json()
    print(json_data)
    
    #Escrever a informação num ficheiro json
    with open('info_recolhida_api_pub.json', 'a') as json_file:
        json.dump(json_data, json_file)



'''
#Rescolher a informação da API gcintegration (Tem os identificadores de todas as doenças e subdoenças de cancro de estômago.)
main_api = 'https://gcplatform.bio.di.uminho.pt/api/gcintegration/findid/maindise?page=0&size=100&sort=string'
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address': address})
json_data = requests.get(url).json()
print(json_data)
    
#Escrever a informação num ficheiro json
with open('info_recolhida_api_gcintegration.json', 'w') as json_file:
    json.dump(json_data, json_file)
'''


'''
#Rescolher a informação da API pub (Tem os termos/nomes/sinónimos dos identificadores anteriores) (incompleto)
for n_page in range(146):
    main_api = 'https://gcplatform.bio.di.uminho.pt/api/pub/page/find/pubmedindexed/gastric%20cancer?page={}&size=1000&sort=string'.format(n_page)
    address = 'lhr'
    url = main_api + urllib.parse.urlencode({'address': address})
    json_data = requests.get(url).json()
    print(json_data)
    
    #Escrever a informação num ficheiro json
    with open('info_recolhida_api_pub.json', 'a') as json_file:
        json.dump(json_data, json_file)
'''