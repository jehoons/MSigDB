import os
import pandas as pd
import dataloader

_baseurl = 'http://143.248.32.25/~jhsong/dataset/GSEA'

def return_loader(): 
    return dataloader._dataloader(_baseurl+'/msigdb.v6.0.symbols.gmt')


def load_msigdb():
    with open(return_loader().find(), 'r') as f: 
        lines = f.readlines()
        
    msigdb = {} 
    for l0 in lines: 
        l0 = l0.split('\t')
        group = l0[0]
        wwwsite = l0[1]
        geneset = l0[2:]
        msigdb[group] = {'wwwsite': wwwsite, 'geneset': geneset}
    
    return msigdb

    