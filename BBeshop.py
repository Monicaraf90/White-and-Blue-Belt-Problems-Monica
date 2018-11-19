#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:33:42 2018

@author: monicaalvarenga
"""
#%%
eshop={"Guitar":1000,"Pickbox":5,"Guitar Strings":10,"Insurance":5,"Priority mail":10}


def cart2(lst):
    prices=[]
  
    if eshop=={} or eshop=={"Priority Mail","Insurance"}:
        return "Incorrect"
    
    else:
        for i in eshop:
            prices.append(eshop[i])
        return "Your bill is "+str((prices))
#%%    
        
            
    