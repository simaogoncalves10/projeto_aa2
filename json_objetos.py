import json
import pandas as pd


class Info:
    def __init__(self, id=None, idGenerator=None, source=None, createdDate=None, lastModifiedDate=None, title=None, summary=None, content=None, xdbRefs=None, meshTerms=None, keywords=None):
        self.id = id
        self.idGenerator = idGenerator
        self.source = source
        self.createdDate = createdDate
        self.lastModifiedDate = lastModifiedDate
        self.title = title
        self.summary = summary
        self.content = content
        self.xdbRefs = xdbRefs
        self.meshTerms = meshTerms
        self.keywords = keywords


    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


    def __repr__(self):
        #return str(self)
        return f'{self.id}'
        
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary':self.summary,
        }
 

info_list = []
with open('info_gastric_cancer.json', 'r') as json_file:
    info_data = json.loads(json_file.read())
    for i in info_data: 
        info_list.append(Info(**i))



df = pd.DataFrame.from_records([a.to_dict() for a in info_list])
df.index = df["id"]
del df["id"]
print(df)

df.to_csv('dataset_gastric_cancer.csv', sep=",")
