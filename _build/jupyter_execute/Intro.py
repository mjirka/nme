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
# <!--
# ## Úkoly
# * [Úkol z cvičení č. 11](https://mjirka.github.io/nme/Ukol11.html) (zadání [ve formátu Jupyter Notebook](https://mjirka.github.io/nme/Ukol11.ipynb))
# //-->
# 
# ## Zápočtová tabulka
# ### Cvičení v 10:00
# | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | Beran |/ 1 |/ 0 | - 0 | - 0.6 |/ 1 | / 1 | / 1 | / 1 | / 1 | / 0.5 | / 0 |
# | Bláha |/ 1 |/ 1 | / 1 | / 1 |-  1| / 0 | / 1 | / 1 | / 0| - 0 | / 0|
# | Černík |/ 1 |/ 1| / 1 | / 1  |/ 1 | / 1 | / 1 | / 1 | / 0| / 0 | - 0|
# | Fojtík |/ 1 |/ 1| / 0.5 | / 1 |/ 1 | / 1 | / 1 | / 1 | / 0| / 0 | / 0|
# | Heinl |/ 1 | / 1| / 1 | /  1|- 1 | / 1 | / 1 | - 0 | / 0| / 0 | / 0|
# | Janderová |/ 1|/ 1| - 1 | / 1 |- 1 | / 1 | - 1 | / 0 | / 0| - 0 | / 0|
# | Kohout |/ 1|/ 1| / 1 | / 1 |/  1| / 1 | / 1 | / 0 | / 0| / 0 | / 0|
# | Kollár |/ 1|- 1| / 0 | - 0 |/  0| - 1 | / 1 | / 1 | / 1 | - 1 | / 0|
# | Kratochvíl |/ 1|/ 1| / 1 | / 1 |/  1| / 1 | / 1 | / 0 | - 1 | / 0 | / 0|
# | Krupka |/ 1|/ 1| / 1 | / 1 |/  1| / 1 | / 0 | - 1 | / 1| / 0 | / 0|
# | Kuchař |/ 1|/ 1| - 1 | / 1 |/  1| / 1 | / 1 | / 1 | / 1| / 0.75 | - 1|
# | Kulda |/ 1|/ 1| - 1 | / 1 |/  1| / 1 | / 1 | / 1 | / 1| /  0 | / 0|
# | Linx |/ 1|/ 1| - 1 | / 1 |/  1| - 1 | / 1 | / 1 | / 0| / 0 | / 0|
# | Mutaková |/ 0.6|- 0| - 0 | - 0 |- 0| - 0 | - 0 | - 0 | - 0| -  0| - 0|
# | Nejedlá |/ 1|- 1| - 1 | / 1 |/  1| / 1 | / 1 | - 0 | / 1| / 0 | / 0|
# | Pacal |/ 1|/ 1| / 1 | / 1 |-  1| / 0 | / 1 | / 0 | - 0| / 1 | - 0|
# | Paleta |/ 1|/ 1| / 1 | / 1 |/  1| / 1 | / 1 | / 0 | / 0| / 0 | / 0|
# | Povolný |/ 1|/ 1| - 1 | / 1 |/  1| - 1 | / 1 | - 1 | / 1| / 1 | / 1|
# | Rajtmajer |/ 1|/ 1| / 1 | / 1 |- 0 | / 1 | / 1 | / 0 | / 1| / 1 | / 0|
# | Rybak |/ 0.7|/ 0| - 1 | - 1 |/  1| / 1 | / 1 | / 0.5 | / 1| / 0 | / 0|
# | Selivonenko |/ 1|/ 0| - 0 | - 0.6 |/  1| / 1 | / 1 | / 1 | / 1| / 0.25 | / 1|
# | Sipetic |/ 1|/ 1| / 1 | / 1 |-  1| / 1 | / 1 | / 1 | - 0| / 0.5 | - 0|
# | Stránský |/ 1|/ 1| / 1 | / 1 |/  1| / 1 | / 1 | / 0 | - 0| / 0 | - 0|
# | Šana |/ 1|- 0.5| / 0 | / 0 |-  0| / 1 | / 1 | / 1 | / 1| / 1 | - 1|
# | Šika |/ 1|/ 1 | / 1 | / 1 |/  0.5| / 1 | / 1 | / 0 | / 0| / 0.75 | / 0|
# | Šimanová |/ 1|- 1 | / 1 | - 1 |/  1| / 1 | / 1 | / 1 | / 1| / 0.5 | / 1|
# | Trlicová |/ 1|/ 1 | - 1 | / 1 |/  1| / 1 | / 1 | / 0 | - 1| / 0.75 | / 0|
# | Velek |/ 1| / 1 | - 1 | / 1 |-  0| / 1 | / 1 | / 0 | / 1| / 0 | - 0|
# | Veselý |/ 1|/ 1 | / 1 | / 1 |/  1| / 1 | - 1 | / 0 | / 0| / 0 | / 0|
# 
# ### Cvičení ve 14:00
# | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | Blažek | - 0 |/ 1| / 1 | / 1 |- 0 | / 1 | / 1 | / 1 | / 1| / 1 | / 0|
# | Borková |- 1 |/ 1| / 1 | / 0.6 |/ 1 | / 1 | / 1 | - 0 | / 1| - 0 | / 0|
# | Březina |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | / 1 | / 1 | / 1| / 0.5 | / 0|
# | Dedek |/ 1 |- 1| / 0.75 | / 1|/ 1 | / 1 | / 1 | / 1 | / 0.5| / 0 | / 1|
# | Denisov |- 0 |/ 0.5| / 1 | / 1|- 1 | / 1 | / 0.5 | / 1 | - 0| / 0.75| / 0|
# | Feldbabelová |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | / 1 | / 1 | / 0| / 0| / 0|
# | Hanušová |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | - 1 | / 0 | / 1| / 0| / 0|
# | Hauptmann |/ 1 |- 1| / 0.5 | / 1|- 1 | / 0 | / 1 | / 1 | / 1| / 1| - 0|
# | Hrdličková |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | / 1 | - 0 | / 1| - 0| / 0|
# | Chudožilov |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | / 1 | / 1 | / 0| - 0| - 0|
# | Karamonová |/ 1 |/ 1| / 1 | / 0.6 |/ 1 | / 1 | / 1 | - 0 | / 1| /0 | / 0|
# | Kohut |/ 1 |/ 1| / 1 | / 1|/ 1 | / 0 | - 1 | / 1 | / 0| / 0| / 0|
# | Kolík |/ 1 |/ 1| / 1 | / 0.6 |/ 1 | / 1 | / 0 | / 1 | / 1| / 0| / 0|
# | Kouřimská |/ 1 |/ 1| - 1 | / 0.6|/ 1 | / 1 | / 1 | - 1 | / 1| - 0| / 0|
# | Králová |- 0 |/ 0.5| / 0.75 | / 0.6|/ 1 | / 1 | / 0.5 | / 0.5 | - 1| / 0.5| - 0.25|
# | Kubíček |/ 1 |/ 1| - 1 | - 1|- 1 | / 1 | / 1 | / 1 | / 1| / 1| / 0|
# | Lerchová |/ 1 |/ 1| /  1 | / 1|/  1| / 1 | / 1 | / 1 | - 1| / 0| - 0|
# | Maronczak |/ 1 |/ 1| / 1 | / 1|- 1 | - 1 | / 1 | / 0 | / 0| / 0| / 0|
# | Maštera |/ 1 |/ 1| - 1 | / 1|/  1| / 1 | / 1 | / 1 | / 1| / 0| - 0|
# | Nezhentsev |/ 1 |/ 1| / 1 | - 1|/ 1 | - 1 | / 0 | / 1 | / 0| / 0 | / 0|
# | Nosek |/ 1 |/ 1| / 0.75 | / 1|/ 1 | / 1 | / 1 | / 1 | / 1| / 0.75 | / 0|
# | Salčáková |/ 1 |/ 1| - 1 | / 1|/ 1 | / 1 | / 1 | - 0 | / 0| - 0| / 0|
# | Stanek |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | / 1 | - 1 | / 0| - 1| / 0|
# | Suleimenov |/ 1 |/ 0.5| / 1 | / 1|/ 1 | / 1 | - 1 | / 1 | / 1| - 0| / 0|
# | Šanovec |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | - 1 | / 0 | / 1| / 0| / 0|
# | Šimek |/ 1 |/ 0.5| / 1 | / 1|/ 1 | / 1 | - 0 | / 1 | / 1| / 0| / 0|
# | Šlosárek |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | - 1 | / 1 | / 0| / 0| / 0|
# | Tuček |/ 1 |/ 1| / 1 | / 1|/ 1 | / 1 | - 1 | / 0 | / 0| / 0 | / 0|
# | Veselá |/ 1 |/ 1| / 0.75 | / 1|/ 1 | / 1 | / 1 | / 0 | / 1| / 0| / 0|
# | Yuskiv |/ 1 |/ 0| - 1 | - 0.6|/  1| / 1 | / 1 | / 0 | - 1| / 0.5| / 0|
# 
# Vysvětlivky: "/" přítomen, "-" nepřítomen, číslo udává počet získaných bodů za domáci úkoly
# 
# 
# ## Používané nástroje
# Na cvičeních budeme používat Python v on-line prostředí [Jupyter notebook](https://jupyter.org/). Jupyter notebook lze vytvářet a editovat on-line např. v [Google Colab](https://colab.research.google.com/). Pro vypracování úkolů a off-line práci s Jupyter notebooky na počítači je nejjednodušší nainstalovat si programový balík [Anaconda](https://www.anaconda.com/) (dostupné pro Windows/Mac/Linux), který obsahuje všechny potřebné knihovny (a navíc Python editor [spyder](https://www.spyder-ide.org/) a mnoho dalšího):
# 1. [Návod na instalaci](https://docs.anaconda.com/anaconda/install/)
# 2. [Návod na spuštení Jupyter Notebook](https://freelearning.anaconda.cloud/get-started-with-anaconda/18571)
# 
# **S případnými dotazy na instalaci a spuštění Jupyter Notebooku mě kontaktujte na mailu.**
# 
# Materiály ke cvičením vycházejí z těchto [podkladů](http://kfe.fjfi.cvut.cz/~vachal/edu/nme/cviceni/index.html).
# 
# ***
# <div style="text-align: right">Akutalizace 2.5. 2024</div>
