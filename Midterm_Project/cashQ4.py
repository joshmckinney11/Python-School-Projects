#!/usr/bin/env python
# coding: utf-8

# In[1]:


class CashRegister:
    def __init__(self):
        self._total= 0
        self._items= []
    def addItem(self, item, price):
        self._total = self._total + price
        self._items.append(item)
        
    def CheckRegister (self):
        print("Total cash: $", self._total, sep='')
        print("No. of items: ", len(self._items))
        


# In[ ]:




