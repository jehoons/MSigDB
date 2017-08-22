import dataset_msigdb 

def test_this():
    dataset = dataset_msigdb.load_msigdb()
    print(dataset.keys())

