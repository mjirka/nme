#!/usr/bin/env python
# coding: utf-8

# # Numerické metody - cvičení (12NME1)
# ## KLFF FJFI ČVUT v Praze
# <!--
# ## Rozvrh pro letní semestr 2022/2023
# * Středa 12:00 - 13:40
# * Trojanova 13, učebna T-105
# * Martin Jirka, jirkama1@fjfi.cvut.cz
# 
# ## Podmínky pro udělění zápočtu
# * maximálně 3 absence
# * zisk alespoň 60 % bodů za úkoly zadávané na cvičeních. Tyto úkoly vypracované v pythonu odevzdávejte na výše uvedený e-mail do začátku následujícího cvičení.
# 
# ## Úkoly
# * [Úkol z cvičení č. 1](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol01.html) (zadání ve fromátu [Jupyter Notebook](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol01.ipynb))
# * [Úkol z cvičení č. 2](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol02.html) (zadání ve fromátu [Jupyter Notebook](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol02.ipynb))
# 
# ## Zápočtová tabulka
# | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | M. Benedová | X+1 |  |  |  |  |  |  |  |  |  |  |
# | R. Beňo | ?+1 |  |  |  |  |  |  |  |  |  |  |
# | M. Bělohlávek | X+1 |  |  |  |  |  |  |  |  |  |  |
# | M. Buloichyk | X+0 |  |  |  |  |  |  |  |  |  |  |
# | M. Divišová | X+1 |  |  |  |  |  |  |  |  |  |  |
# | A. Godál | X+1 |  |  |  |  |  |  |  |  |  |  |
# | F. Janeček | X+1 |  |  |  |  |  |  |  |  |  |  |
# | V. Janota | X+1 |  |  |  |  |  |  |  |  |  |  |
# | L. Karczubová | X+0 |  |  |  |  |  |  |  |  |  |  |
# | Z. Legerský | X+0 |  |  |  |  |  |  |  |  |  |  |
# | J. Macura | X+0 |  |  |  |  |  |  |  |  |  |  |
# | V. Růžičková | X+1 |  |  |  |  |  |  |  |  |  |  |
# | Š. Skalka | X+1 |  |  |  |  |  |  |  |  |  |  |
# | M. Šmíd | X+1 |  |  |  |  |  |  |  |  |  |  |
# | M. Tvrdík | X+1 |  |  |  |  |  |  |  |  |  |  |
# | S. Velichová | X+1 |  |  |  |  |  |  |  |  |  |  |
# 
# Vysvětlivky: X - přítomen, N - nepřítomen, O - omluven, číslo udává počet získaných bodů za domáci úkoly
# 
# //-->
# ## Používané nástroje
# Na cvičeních budeme používat Python v on-line prostředí [Jupyter notebook](https://jupyter.org/). Jupyter notebook lze vytvářet a editovat on-line např. v [Google Colab](https://colab.research.google.com/). Pro vypracování úkolů a off-line práci s Jupyter notebooky na počítači je nejjednodušší nainstalovat si programový balík [Anaconda](https://www.anaconda.com/) (dostupné pro Windows/Mac/Linux), který obsahuje všechny potřebné knihovny (a navíc Python editor [spyder](https://www.spyder-ide.org/) a mnoho dalšího):
# 1. [Návod na instalaci](https://docs.anaconda.com/anaconda/install/)
# 2. [Návod na spuštení Jupyter notebook](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
# 
# **S případnými dotazy na instalaci a spuštění Jupyter Notebooku mě kontaktujte na mailu.**
# 
# Materiály ke cvičením vycházejí z těchto [podkladů](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/index.html).
# 
# 
# ***
# <div style="text-align: right">Akutalizace 20.2.2025</div>
