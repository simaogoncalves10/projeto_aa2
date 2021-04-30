import json
from os import listdir
from os.path import isfile, join


lista=[]  


files = [f for f in listdir("pages") if isfile(join("pages", f))]

for file in files:
    f = open('pages/'+file)
    data = json.load(f) 
    for i in data: lista.append(i)
    f.close()

print(lista)

with open('info_gastric_cancer.json', 'w') as json_file:
    json.dump(lista, json_file,indent=1)
