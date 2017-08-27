import os
import pandas as pd 
from os.path import dirname, exists, join

#module_dir = dirname(__file__)
#repo = 'git@github.com:jehoons/downloader.git'
#if not exists(join(module_dir, 'downloader')): 
#    os.system('git clone %s %s/downloader' % (repo, module_dir))

from downloader import _downloader


def return_loader(): 
    _baseurl = 'http://143.248.32.25/~jhsong/dataset/GSEA'
    return _downloader(_baseurl+'/msigdb.v6.0.symbols.gmt')


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




    
