#!/usr/bin/env python
# coding: utf-8

# # Úkol 3

# 1. Gauss-Jordanovou metodou vypočítejte inverzní matici $\mathbb{A}^{-1}$ pro 
# 
# $\mathbb{A}=
# \begin{pmatrix}
# 1 & -1 & 3\\
# 2 & 1 & 2\\
# -2& -2 & 1
# \end{pmatrix}
# $. **(1.0 b)**
# 
# (Pro ověření svého řešení můžete použít funkci `np.linalg.inv()`.)

# In[1]:


import numpy as np

A = np.array([
[1,-1,3],
[2,1,2],
[-2,-2,1]
])

