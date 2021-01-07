import yaml


def get_datas(path):
    with open(path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        data = datas['datas']
        ids = datas['ids']
        return [data, ids]
        #print(datas)
        #print(data)
        #print(ids)

#get_datas("./datas.yml")
