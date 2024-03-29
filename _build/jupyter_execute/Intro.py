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
# ## Úkoly
# * [Úkol z cvičení č. 6](https://mjirka.github.io/nme/Ukol06.html) (zadání [ve formátu Jupyter Notebook](https://mjirka.github.io/nme/Ukol06.ipynb))
# * [Úkol z cvičení č. 7](https://mjirka.github.io/nme/Ukol07.html) (zadání [ve formátu Jupyter Notebook](https://mjirka.github.io/nme/Ukol07.ipynb))
# 
# ## Zápočtová tabulka
# ### Cvičení v 10:00
# | | 1 | 2 | 3 | 4 | 5 | 6 |
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | Beran |/ 1 |/ 0 | - 0 | - 0.6 |/ 1 | /  |
# | Bláha |/ 1 |/ 1 | / 1 | / 1 |-  1| /  |
# | Černík |/ 1 |/ 1| / 1 | / 1  |/ 1 | /  |
# | Fojtík |/ 1 |/ 1| / 0.5 | / 1 |/ 1 | /  |
# | Heinl |/ 1 | / 1| / 1 | /  1|- 1 | /  |
# | Janderová |/ 1|/ 1| - 1 | / 1 |- 1 | /  |
# | Kohout |/ 1|/ 1| / 1 | / 1 |/  1| /  |
# | Kollár |/ 1|- 1| / 0 | - 0 |/  0| -  |
# | Kratochvíl |/ 1|/ 1| / 1 | / 1 |/  1| /  |
# | Krupka |/ 1|/ 1| / 1 | / 1 |/  1| /  |
# | Kuchař |/ 1|/ 1| - 1 | / 1 |/  1| /  |
# | Kulda |/ 1|/ 1| - 1 | / 1 |/  1| /  |
# | Linx |/ 1|/ 1| - 1 | / 1 |/  1| -  |
# | Mutaková |/ 0.6|- 0| - 0 | - 0 |- 0| -  |
# | Nejedlá |/ 1|- 1| - 1 | / 1 |/  1| /  |
# | Pacal |/ 1|/ 1| / 1 | / 1 |-  1| /  |
# | Paleta |/ 1|/ 1| / 1 | / 1 |/  1| /  |
# | Povolný |/ 1|/ 1| - 1 | / 1 |/  1| -  |
# | Rajtmajer |/ 1|/ 1| / 1 | / 1 |- 0 | /  |
# | Rybak |/ 0.7|/ 0| - 1 | - 1 |/  1| /  |
# | Selivonenko |/ 1|/ 0| - 0 | - 0.6 |/  1| /  |
# | Sipetic |/ 1|/ 1| / 1 | / 1 |-  1| /  |
# | Stránský |/ 1|/ 1| / 1 | / 1 |/  1| /  |
# | Šana |/ 1|- 0.5| / 0 | / 0 |-  0| /  |
# | Šika |/ 1|/ 1 | / 1 | / 1 |/  0.5| /  |
# | Šimanová |/ 1|- 1 | / 1 | - 1 |/  1| /  |
# | Trlicová |/ 1|/ 1 | - 1 | / 1 |/  1| /  |
# | Velek |/ 1| / 1 | - 1 | / 1 |-  0| /  |
# | Veselý |/ 1|/ 1 | / 1 | / 1 |/  1| /  |
# 
# ### Cvičení ve 14:00
# | | 1 | 2 | 3 | 4 | 5 | 6 |
# | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
# | Blažek | - 0 |/ 1| / 1 | / 1 |- 0 | /  |
# | Borková |- 1 |/ 1| / 1 | / 0.6 |/ 1 | /  |
# | Březina |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Dedek |/ 1 |- 1| / 0.75 | / 1|/ 1 | /  |
# | Denisov |- 0 |/ 0.5| / 1 | / 1|- 1 | /  |
# | Feldbabelová |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Hanušová |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Hauptmann |/ 1 |- 1| / 0.5 | / 1|- 1 | /  |
# | Hrdličková |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Chudožilov |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Karamonová |/ 1 |/ 1| / 1 | / 0.6 |/ 1 | /  |
# | Kohut |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Kolík |/ 1 |/ 1| / 1 | / 0.6 |/ 1 | /  |
# | Kouřimská |/ 1 |/ 1| - 1 | / 0.6|/ 1 | /  |
# | Králová |- 0 |/ 0.5| / 0.75 | / 0.6|/ 1 | /  |
# | Kubíček |/ 1 |/ 1| - 1 | - 1|- 1 | /  |
# | Lerchová |/ 1 |/ 1| /  1 | / 1|/  1| /  |
# | Maronczak |/ 1 |/ 1| / 1 | / 1|- 1 | -  |
# | Maštera |/ 1 |/ 1| - 1 | / 1|/  1| /  |
# | Nezhentsev |/ 1 |/ 1| / 1 | - 1|/ 1 | -  |
# | Nosek |/ 1 |/ 1| / 0.75 | / 1|/ 1 | /  |
# | Salčáková |/ 1 |/ 1| - 1 | / 1|/ 1 | /  |
# | Stanek |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Suleimenov |/ 1 |/ 0.5| / 1 | / 1|/ 1 | /  |
# | Šanovec |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Šimek |/ 1 |/ 0.5| / 1 | / 1|/ 1 | /  |
# | Šlosárek |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Tuček |/ 1 |/ 1| / 1 | / 1|/ 1 | /  |
# | Veselá |/ 1 |/ 1| / 0.75 | / 1|/ 1 | /  |
# | Yuskiv |/ 1 |/ 0| - 1 | - 0.6|/  1| /  |
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
# <div style="text-align: right">Akutalizace 21.3. 2024</div>
