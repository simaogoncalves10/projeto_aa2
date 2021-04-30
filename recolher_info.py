import urllib.parse, requests, json


#Rescolher a informação da API pub
for n_page in range(146):
    main_api = 'https://gcplatform.bio.di.uminho.pt/api/pub/page/find/pubmedindexed/gastric%20cancer?page={}&size=1000&sort=string'.format(n_page)
    address = 'lhr'
    url = main_api + urllib.parse.urlencode({'address': address})
    json_data = requests.get(url).json()
    print(json_data["content"])

    #Mudar o nome do ficheiro
    filename = "C:\\Users\\Simon\\OneDrive\\Documentos\\GitHub\\projeto_aa2\\pages\\page_{}_gastric_cancer.json".format(n_page)
  

    #Escrever a informação num ficheiro json
    with open(filename, 'a') as json_file:
        json.dump(json_data["content"], json_file, indent=4, sort_keys=True) #Formata o json file, o indent e sort_keys
        
    

