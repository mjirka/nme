#!/usr/bin/env python
# coding: utf-8

# # Úkol 6

# 1. Naměřili jste hodnoty $x=\{-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 \}$ a $ y=\{60.2, 45.3, 30.5, 11.6, 5.2, 3.1, 6.8, 13.2, 32.8, 44.7, 61.5\} $. Naprogramujte metodu nejmenších čtverců, která hodnoty proloží polynomem 3. řádu $f(x)=a+bx+cx^{2}+dx^{3}$ a vypište koeficienty $a, b, c, d$.
# **(1.0 b)**
# 
# (V kódu můžete využít funkce `np.linalg.solve()` a `np.poly1d()`. Řešení: $a \approx 5.15$, $b \approx 0.38$, $c \approx 2.35$, $d \approx -0.01$)

# In[1]:


# kod

