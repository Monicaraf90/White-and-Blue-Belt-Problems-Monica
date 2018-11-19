#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:03:16 2018

@author: monicaalvarenga
"""
#%%
from WBeshop import cart1
    
def test_cart1():
    values=[["Guitar"]]
    
    for i in values:
        assert cart1(i) == 1000

def test_shopping_cart_pickbox():
    assert cart1(["Pickbox"]) == "Your bill is 5"
#%%
from BBeshop import cart2
    
def test_cart2():
    values=[["Guitar"]]
    
    for i in values:
        assert cart2(i) == 1000

def test_shopping_cart2_pickbox():
    assert cart2(["Pickbox"]) == "Your bill is 5"
    
    
    
    
    
