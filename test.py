"""TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

dict_uzivatelu_heslo = {"bob": "123", "ann": "pass123", "mike": "password123"}
delka = "-" * 47
uzivatel = input("jake je vase jmeno? ")
heslo_uzivatelu = input("jake je vas heslo? ")
vyberte_cislo = input("jake je cislo vybraneho textu ? ")
print(f"jmenuji : {uzivatel}")
print(f"heslo : {heslo_uzivatelu}")
if uzivatel in dict_uzivatelu_heslo:
    print(delka)
    print(f"Vítejte v aplikaci {uzivatel} .Máme 3 texty k analýze.")
    print(delka)
else:
    print(delka)
    print("omlouvame se, nejste v nasi aplikaci.")
    quit()
#if heslo_uzivatelu in dict_uzivatelu_heslo:
    #if heslo_uzivatelu == dict_uzivatelu_heslo.values():
        #print(heslo_uzivatelu)
#else:
    #print("Prosím, vaše heslo je nesprávné, zadejte prosím správné heslo.")
# M: you have checked only username, but it is necessery to check password as well, try google or doc.python.org
# M: study method get() or try to check how gain value for key from dict
# M: one row blank just for clarity
if vyberte_cislo.isnumeric():
    vyberte_cislo = int(vyberte_cislo)
    if vyberte_cislo in range(len(TEXTS) + 1):
        vyberte_cislo_text = vyberte_cislo - 1
        muj_text = TEXTS[vyberte_cislo_text]
        print(f"zadejte cislo mezi 1 a 3 vyberte textu: {vyberte_cislo}")
        print(delka)
    else:
        print("omlouvame se, vybrabrane cislo neodpovida vyberu textu")
        quit()
vyberte_cislo = muj_text.split()  # M: insteda of vyberte_cislo use muj_text
# M: you must clean selected text from rubish. Use strip() method to remove punctuation
#odstranit_interpunkci = vyberte_cislo.strip(".")
print(f"Ve vybraném textu je {len(vyberte_cislo)} slov.")
pocet = 0
for cislo_title in vyberte_cislo:
    if cislo_title.istitle():
        pocet += 1
print(f"Existuje {pocet} slov typu titlecase.")
pocet_velke_slovo = 3
for pocet_upper in vyberte_cislo:
    if pocet_upper.isupper():
        pocet_velke_slovo -= 1
print(f"Je zde {pocet_velke_slovo} velke slovo.")
pocet_malych_slovo = 0
for pocet_lower in vyberte_cislo:
    if pocet_lower.islower():
        pocet_malych_slovo += 1
print(f"Obsahuje {pocet_malych_slovo} malych slov.")
pocet_ciselne_retezce = 0
for pocet_numeric in vyberte_cislo:
    if pocet_numeric.isnumeric():
        pocet_ciselne_retezce += 1
print(f"Existují {pocet_ciselne_retezce} číselné řetězce.")
#pocet_cislo = 0
for sum_cislo in vyberte_cislo:
    if sum_cislo.isnumeric():
        sum_cislo = sum(int(sum_cislo))
        print(sum_cislo)
#sumText1 = intvyberte_cislo[2] + vyberte_cislo[19] + vyberte_cislo[31]
#print(f"Součet všech čísel {sumText1}")
print(delka)
titulka1 = " OCCURENCES "
titulka1.strip()
print(f"LEN| {titulka1} |NR.")
print(delka)
clean_words1 = vyberte_cislo[0].strip("Situate")
clean_words2 = vyberte_cislo[6]
clean_words3 = vyberte_cislo[12].strip("impr")
clean_words4 = vyberte_cislo[13]
clean_words5 = vyberte_cislo[1].strip("ab")
clean_words6 = vyberte_cislo[11].strip("rug")
clean_words7 = vyberte_cislo[48].strip("Pa")
clean_words8 = vyberte_cislo[14].strip("featu")
clean_words9 = vyberte_cislo[15].strip("th")
clean_words10 = vyberte_cislo[17].strip("sharpl")
clean_words11 = vyberte_cislo[53].strip("vale")
len_word1 = "*" * len(clean_words1)
len_word2 = "*" * len(clean_words2)
len_word3 = "*" * len(clean_words3)
len_word4 = "*" * len(clean_words4)
len_word5 = "*" * len(clean_words5)
len_word6 = "*" * len(clean_words6)
len_word7 = "*" * len(clean_words7)
len_word8 = "*" * len(clean_words8)
len_word9 = "*" * len(clean_words9)
len_word10 = "*" * len(clean_words10)
len_word11 = "*" * len(clean_words11)
print("  1|".rstrip(), len_word1, "           |".rstrip(), len(len_word1))
print("  2|".rstrip(), len_word2, "   |".rstrip(), len(len_word2))
print("  3|".rstrip(), len_word3, "      |".rstrip(), len(len_word3))
print("  4|".rstrip(), len_word4, " |".rstrip(), len(len_word4))
print("  5|".rstrip(), len_word5, "         |".rstrip(), len(len_word5))
print("  6|".rstrip(), len_word6, "        |".rstrip(), len(len_word6))
print("  7|".rstrip(), len_word7, "       |".rstrip(), len(len_word7))
print("  8|".rstrip(), len_word8, "           |".rstrip(), len(len_word8))
print("  9|".rstrip(), len_word9, "           |".rstrip(), len(len_word9))
print(" 10|".rstrip(), len_word10, "           |".rstrip(), len(len_word10))
print(" 11|".rstrip(), len_word11, "          |".rstrip(), len(len_word11))
"""
