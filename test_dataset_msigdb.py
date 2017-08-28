import dataset_msigdb 
import pytest 

# @pytest.mark.skip()
# def test_1():    
#     print(dataset.keys())

def test_2():
    # dataset = dataset_msigdb.load_msigdb()
    res = {} 
    for k in dataset.keys():
        for s in ['PROLIF','APOPT','QUIESCENT','ARREST']:
            if k.find(s)>=0:
                # print(k)
                # res[s]
                if s not in res: 
                    res[s] = []

                res[s].append(k)

    import json 

    with open('chk-phenotypes.json', 'w') as f: 
        json.dump(res, f, indent=4)
    
    # xxx

dataset = dataset_msigdb.load_msigdb()    