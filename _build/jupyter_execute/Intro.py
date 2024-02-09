#!/usr/bin/env python
# coding: utf-8

# # Numerické metody - cvičení (12NME1)
# ## KFE FJFI ČVUT v Praze
# 
# ## Rozvrh pro letní semestr 2023/2024
# * Čtvrtek 10:00 - 11:40, 14:00 - 15:40
# * Trojanova 13, učebna T-124
# * Martin Jirka, martin.jirka@fjfi.cvut.cz
# * obecné informace o výuce a materiály k přednášce jsou [zde](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/)
# 
# ## Podmínky pro udělění zápočtu
# * maximálně 3 absence
# * zisk alespoň 60 % bodů za úkoly zadávané na cvičeních. Tyto úkoly vypracované v pythonu odevzdávejte na výše uvedený e-mail do začátku následujícího cvičení.
# 
# <!-- ## Úkoly
# * [Úkol z cvičení č. 11](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol11.html) (zadání ve formátu [Jupyter Notebook](http://kfe.fjfi.cvut.cz/~jirkama1/Ukol11.ipynb))
# 
# 
# ## Zápočtová tabulka
# | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | Zápočet  | 
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | M. Benedová   | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 0 | / 1   | / 0  | / 0 | |
# | R. Beňo       | - 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 0 | / 0   | - 0  | / 0 | |
# | M. Bělohlávek | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 1 | - 1   | / 1  | / 1 | |
# | M. Buloichyk  | / 1 | - 0.5  | - 1 | - 1 | / 1 | / 0 | / 0.75| / 1 | - 1   | / 0  | / 0 | |
# | M. Divišová   | / 1 | / 0.75 | / 1 | / 1 | / 1 | / 1 | / 0.75| / 1 | / 1   | / 1  | / 0 | |
# | Z. Doležal    | - 0 | / 0.75 | / 1 | / 1 | / 1 | / 1 | / 1   | / 1 | / 1   | / 1  | / 0 | |
# | A. Godál      | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 1 | - 0   | - 0  | - 0 | |
# | F. Janeček    | / 1 | - 1    | / 1 | / 1 | / 1 | / 1 | / 1   | - 1 | / 1   | / 1  | - 1 | |
# | V. Janota     | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 0 | - 1   | / 0  | / 0 | |
# | L. Karczubová | / 1 | / 1    | / 0 | / 0 | / 1 | / 1 | / 1   | / 1 | / 0.5 | / 1  | / 0 | |
# | Z. Legerský   | / 1 | / 0    | - 0 | / 0 | / 1 | / 1 | / 0   | / 0 | / 1   | / 1  | / 1 | |
# | J. Macura     | / 1 | / 1    | / 0 | / 1 | - 1 | / 0 | / 1   | / 1 | / 0.5 | - 0.5| / 0 | |
# | N. Majerová   | - 0 | - 0    | - 0 | - 0 | - 0 | - 0 | - 0   | - 0 | - 0   | - 0  | - 0 | |
# | V. Růžičková  | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 1 | - 0   | / 0  | / 0 | |
# | Š. Skalka     | / 1 | / 1    | / 0 | / 1 | / 0 | / 1 | / 1   | - 0 | / 1   | - 0  | / 1 | |
# | L. Smejkal    | - 0 | - 0    | - 0 | - 0 | - 0 | - 0 | - 0   | - 0 | - 0   | - 0  | - 0 | |
# | M. Šmíd       | / 1 | / 0    | / 1 | / 1 | / 0 | / 1 | / 1   | / 1 | - 1   | / 1  | / 0 | |
# | O. Staněk     | - 0 | - 0    | - 0 | - 0 | - 0 | - 0 | - 0   | - 0 | - 0   | - 0  | - 0 | |
# | M. Tvrdík     | / 1 | / 0.5  | / 1 | / 1 | - 1 | / 1 | / 1   | / 1 | - 0   | / 0  | / 0 | |
# | S. Velichová  | / 1 | / 1    | / 1 | / 1 | / 1 | / 1 | / 1   | / 1 | - 0   | - 0  | / 0 | |
# 
# Vysvětlivky: "/" přítomen, "-" nepřítomen, číslo udává počet získaných bodů za domáci úkoly
# -->
# 
# ## Používané nástroje
# Na cvičeních budeme používat Python v on-line prostředí [Jupyter notebook](https://jupyter.org/). Jupyter notebook lze vytvářet a editovat on-line např. v [Google Colab](https://colab.research.google.com/). Pro vypracování úkolů a off-line práci s Jupyter notebooky na počítači je nejjednodušší nainstalovat si programový balík [Anaconda](https://www.anaconda.com/) (dostupné pro Windows/Mac/Linux), který obsahuje všechny potřebné knihovny (a navíc Python editor [spyder](https://www.spyder-ide.org/) a mnoho dalšího):
# 1. [Návod na instalaci](https://docs.anaconda.com/anaconda/install/)
# 2. [Návod na spuštení Jupyter notebook](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
# 
# **S případnými dotazy na instalaci a spuštění Jupyter Notebooku mě kontaktujte na mailu.**
# 
# Materiály ke cvičením vycházejí z těchto [podkladů](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/index.html).
# 
# ***
# <div style="text-align: right">Akutalizace 09.02.2024</div>
