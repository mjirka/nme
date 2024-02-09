#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebook a základy Pythonu

# <div class="alert alert-block alert-success"><b>On-line interaktivní verze: </b> Pro spuštení interaktivní verze této stránky klikněte ve vrchním menu na <i class="fa fa-rocket" aria-hidden="true"></i> a zvolte <i>Binder</i>, ve kterém lze <i>Jupyter notebook</i> (JP) upravovat a následně uložit na disk.</div>

# <div class="alert alert-block alert-info"><b>Tip: </b> Tento soubor je možné stáhnout kliknutím na <i class="fa fa-download" aria-hidden="true"></i>, a to ve formě <code>*.ipynb</code> pro pozdější off-line editaci v prostředí <a href="https://www.anaconda.com/">Anaconda</a>, nebo pro on-line editaci v <a href="https://colab.research.google.com/">Google Colab</a>.</div>

# ## Interaktivní Jupyter notebook

# Napište `print('Hello, World!')` a stiskněte `Shift` `+` `Enter` (nebo `Ctrl` `+` `Enter`)

# In[1]:


# print


# Pomocí klávesy `b` vložíte další řádek do JP.
# * Stiskněte `b`.

# Odstranění řádku: vyberte řádek v JP a stiskněte `d` `+` `d`

# Klávesou `a` vložíte nový řádek nad právě vybraný.
# 1. Stiskněte `a`. 
# 2. Vyberte tento nový řádek a stiskněte `m`. Nyní lze do řádku místo kódu zapisovat text,
# 3. Zadávání ukončíte stisknutím kombinace `Shift` `+` `Enter`.
# 4. Pokud chcete řádek převést na kód, stiskněte `y`.
# 

# **Pro nápovědu stiskněte `h`.**

# ## Python

# Jednořádkový komentář se zadává za znak `#`, více řádků lze zakomentovat pomocí `"""` a `"""`:

# In[2]:


# toto je komentar


# Inicializace proměnných `a`, `b`, základní aritmetické operace a výpis výsledku pomocí funkce `print()`:

# In[3]:


# zakladni aritmeticke operace


# <div class="alert alert-block alert-warning"><b>Cvičení 01.01: </b> Vypočtěte objem jehlanu o stranách 3 a 4 majiícího výšku 7. </div>

# In[4]:


# Cviceni 01.01


# ## Podmínkové cykly

# ### If ... else

# <div class="alert alert-block alert-danger"><b>Pozor:</b> vnitřní části kódu je <b>nutné odsadit</b>, obvykle se používají <b>čtyři mezery</b>.</div>

# Za klíčovými slovy `if` a `else` musíme psát `:`.

# In[5]:


# if, else


# ### For ...

# Zde využijeme funkci `range(min,max,krok)`, která vytvoří sekvenci celých čísel od `min` po `max` ***(prvek max není v sekvenci obsažen)*** s uvedeným krokem. Výchozí hodnoty jsou `min = 0` a `krok = 1`.

# In[6]:


# for


# ### While...

# In[7]:


# while


# ### Break

# Pomocí příkazu `break` se ukončí probíhající cyklus. Pokud je cyklus vnořený, ukončí se pouze tento vnořený cyklus. V následujícím příkladu využijeme funkci `len()` která nám vrátí délku seznamu vytvořeného pomocí `range()`.

# In[8]:


# Ze seznamu cislic 0,1,2,... chci vypsat pouze prvni dve cislice. 


# ### Continue

# Příkaz `continue` ukončí aktuální iteraci v cyklu a pokračuje další iterací.

# In[9]:


# Ze seznamu cislic 0,1,2,... chci vypsat vsechny cislice, krome dvojky. 


# ## Funkce

# Funkce se definuje příkazem `def`. Následuje jméno funkce, seznam vstupních parametrů a vše je zakončené `:`. Tělo funkce musí být odsazené. Funkce může vrátit hodnotu pomocí příkazu `return`.

# In[10]:


# funkce


# <div class="alert alert-block alert-warning"><b>Cvičení 01.02: </b> Napište funkci, která rozhodne, zda zadané číslo je liché, nebo sudé, a vypište výsledek. </div>

# In[11]:


# Cviceni 01.02


# ## Numerická knihovna numpy

# Pro import numerické knihovny `numpy` použijeme příkaz:

# In[12]:


import numpy as np


# ### Maticové operace

# Pole (vektor, matice) lze vytvářet pomocí funkce `array()`:

# In[13]:


# vektor

# matice (pole)


# <div class="alert alert-block alert-danger"><b>Pozor:</b> v poli <code>array</code> má <b>první prvek index 0</b>!</div>

# Rozměry pole zjistíme pomocí funkce `shape`:

# In[14]:


# shape


# Funkce `size` vrátí počet prvků v poli:

# In[15]:


# size


# Matici lze transponovat funkcí `transpose()`:

# In[16]:


# transpose


# Pro vytváření polí lze používat následující generátory:

# * Pomocí funkce `arange()` vytvoříme pole s prvky od 0 do 10 **(poslední prvek není obsažen)** a krokem 1:

# In[17]:


# arange


# * Pomocí funkce `linspace()` vygenerujeme pole s prvky od 0 do 10 **(včetně)**, přičemž počet prvků je 20:

# In[18]:


# linspace


# * Příkazem `logspace()` vytvoříme pole od 0 do 10 s počtem prvků 20 v logaritmickém měřítku ($\log_{10}$):

# In[19]:


# logspace


# * Pomocí funkce `zeros()` vytvoříme nulovou matici 2x2:

# In[20]:


# zeros


#  * Funkcí `ones()` vytvoříme jednotkovou matici 3x3:

# In[21]:


# ones


# * Pomocí funkce `eye()` vytvoříme matici 3x3 s jedničkami na diagonále, ostatní hodnoty jsou nulové:

# In[22]:


# eye


# * Pole náhodných čísel v rozmezí 0 az 1 se vygeneruje pomocí funkce `np.random.rand()`:

# In[23]:


# random


# Pro přístup k prvkům pole `A` používáme syntaxi `A[i,j]`, kde `i` je index řádku a `j` je index sloupce:

# In[24]:


# pole


# Pro přístup k prvkům pole používáme syntaxi `[min:max:krok]`. Mějme vektor $\mathbf{v}=(0,1,2,3,4,5,6)$. Nyní z něj vyjmeme první ("0") až šestý prvek ("5"), a to s krokem 2:

# In[25]:


# pole - vyber


# Podobně u matice $A$ vybereme např. poslední dva prvky ve třetím sloupci.

# In[26]:


# pole - vyber


# U matice $A$ vybereme první řádek:

# In[27]:


# pole - vyber


# U matice $A$ vybereme první sloupec:

# In[28]:


# pole - vyber


# Násobení matic a vektorů se provádí pomocí operátoru `dot`:

# In[29]:


# matice 2x3

# matice 3x2

# vysledek


# <div class="alert alert-block alert-danger"><b>Pozor:</b> operace <b>C*C</b> násobí matice po prvcích (není to maticové násobení)</div>

# In[30]:


# maticove nasobeni

# nasobeni po prvcich


# ### Funkce

# `numpy` obsahuje často používané funkce a konstanty (napr. `sqrt()`, `log()`, `log10()`, `sin()`, `abs()`, `e`, `pi`, ...):

# In[31]:


# numpy - funkce


# Součet prvků v poli je dán funkcí `sum()`:

# In[32]:


# soucet prvku v poli


# Minimální a maximální hodnotu v poli určíme funkcí `min()` a `max()`:

# In[33]:


# maximalni hodnota v poli

# minimalni hodnota v poli


# Funkce `average()` vrací průměrnou hodnotu; `std()` je směrodatná odchylka a `var()` je rozptyl:

# In[34]:


# prumerna hodnota

# smerodatna odchylka

# rozptyl


# Index prvku v poli lze najít pomocí funkce `argwhere()`:

# In[35]:


# argwhere


# <div class="alert alert-block alert-info"><b>Tip: </b> Další příklady a návody pro práci s knihovnou <code>numpy</code> lze nalézt na <a href='https://numpy.org/'>https://numpy.org/</a>.</div>

# ## Visualizace dat

# Pro kreslení grafů využijeme knihovnu `matplotlib.pyplot`:

# In[36]:


import matplotlib.pyplot as plt


# ### Graf jedné proměnné

# Vygenerujeme $x$ a $y$ hodnoty pro funkci `sin()`:

# In[37]:


# hodnoty x a y


# Nejdříve je potřeba vytvořit obrázek pomocí `fig`. Vykreslení dat provedeme příkazem `plot()`:

# In[38]:


# vykresleni x,y


# Přidáme popisky os pomocí `set_xlabel()`, `set_ylabel()` a název grafu pomocí `set_title()`:

# In[39]:


# popisky os, nazev grafu


# Přidáme funkci `cos()`, nastavíme barvu (`color`), styl (`linestyle`) a šířku (`linewidth`) linky. Průhlednost se nastavuje parametrem `alpha`. Legendu zobrazíme příkazem `legend()`:

# In[40]:


# funkce cos()

# vykreslime funkci cos()


# Na závěr obrázek uložíme příkazem `savefig()`:

# In[41]:


# ulozeni obrazku


# ### Visualizace závislosti dvou proměnných

# Mějme funkci $z(x,y)$, která závisí na dvou proměnných $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, a vykreslíme její závislost v 2D grafu.

# Vytvoříme mřížku $x\times y$ pomocí funkce `meshgrid()`:

# In[42]:


# meshgrid


# Spočítáme hodnoty funkce $z(x,y)$:

# In[43]:


# hodnoty z


# 2D graf vykreslíme pomocí funkce `pcolor()` s parametrem `shading='auto'`:

# In[44]:


# vykresleni dat


# Kontury získáme použitím funkce `contour()`:

# In[45]:


# contour


# ### 3D visualizace

# Máme stejnou funkci $z(x,y)=\exp(-\sqrt{x^2+y^2})\cos(2x)\sin(2y)$, kterou nyní chceme vykreslit v 3D grafu. Nejdříve vytvoříme trojrozměrnou osu:

# In[46]:


# 3D graf


# Vytvoříme mřížku $x\times y$ pomocí funkce `meshgrid`:

# In[47]:


# meshgrid


# Spočítáme hodnoty funkce $z(x,y)$:

# In[48]:


# hodnoty z


# 3D data vykreslíme pomocí funkce `plot_surface()` a přidáme popisky os:

# In[49]:


# vykresleni dat - plot_surface


# <div class="alert alert-block alert-warning"><b>Cvičení 01.03: </b> Vykreslete průběh funkce log(<i>x</i>) pro <i>x</i> od 0.1 do 10. Osy grafu popište, přidejte legendu a obrázek uložte ve formátu *.jpg.</div>

# In[50]:


# Cviceni 01.03


# <div class="alert alert-block alert-info"><b>Tip: </b> Další příklady a návody pro práci s knihovnou <code>matplotlib</code> lze nalézt na <a href='https://matplotlib.org/'>https://matplotlib.org/</a>.</div>
