import dataset_msigdb 
import pytest 

# @pytest.mark.skip()
# def test_1():    
#     print(dataset.keys())

def test_find_APQ_terms():

    res = {}

    for k in dataset.keys():
        for n,s in [('proliferation','PROLIF'),('apoptosis','APOPT'),('quiescence','QUIESCENT'),('arrest','ARREST')]:
            if k.find(s)>=0:
                # print(k)
                # res[s]
                if n not in res: 
                    res[n] = []

                res[n].append(k)

    import json 

    with open('chk-A-P-Q.json', 'w') as f: 
        json.dump(res, f, indent=4)


dataset = dataset_msigdb.load_msigdb()

