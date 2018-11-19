#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:25:40 2018

@author: monicaalvarenga
"""
#%%
eshop={"Guitar":1000,"Pickbox":5,"Guitar Strings":10}

prices=[]

def cart1(lst):
  
    if eshop=={}:
       return None
   
    else:
        for i in eshop:
            prices.append(eshop[i])
        return "Your bill is "+str(sum(prices))
#%%


