TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly, impressive 
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
delka1 = "-" * 62
delka2 = "-" * 54
uzivatel = input("jake je vase jmeno? ")
heslo_uzivatelu = input("jake je vas heslo? ")
vyberte_cislo = input("jake je cislo vybraneho textu ? ")
print(f"vase jmeno je : {uzivatel}")
print(f"vas heslo je : {heslo_uzivatelu}")
print(f"Vas cislo vybranehu je : {vyberte_cislo}")
if uzivatel in dict_uzivatelu_heslo and heslo_uzivatelu in dict_uzivatelu_heslo[uzivatel]:
    print(f"heslo : {heslo_uzivatelu}")
    print(delka)
    print(f"Vítejte v aplikaci {uzivatel} .Máme 3 texty k analýze.")
else:
    print(delka)
    print("omlouvame se, nejste v nasi aplikaci")
    print(delka1)
    print("Prosím, vaše heslo je nesprávné, zadejte prosím správné heslo.")
    print(delka1)
    quit()
if vyberte_cislo.isnumeric():
    vyberte_cislo = int(vyberte_cislo)
if vyberte_cislo in range(len(TEXTS) + 1):
    vyberte_cislo_textu = vyberte_cislo - 1
    muj_text_vybranehu = TEXTS[vyberte_cislo_textu]
    print(delka)
    print(f"zadejte cislo mezi 1 a 3 vyberte textu: {vyberte_cislo}")
    print(delka)
else:
    print(delka2)
    print("omlouvame se, vybrabrane cislo neodpovida vyberu textu")
    print(delka2)
    quit()
number_words = muj_text_vybranehu.split()
clean_words = []
for clean_word in number_words:
    clean_words.append(clean_word.strip(".,"))
print(f"Ve vybraném textu je {len(clean_words)} slov.")
counterTitle = 0
for cislo_title in clean_words:
    if cislo_title.istitle():
        counterTitle += 1
print(f"Existuje {counterTitle} slov typu titlecase.")
counterIsupper = 0
for cislo_upper in clean_words:
    if cislo_upper.isupper():
        counterIsupper += 1
print(f"Je zde {counterIsupper} velké slovo.")
counterIslower = 0
for cislo_lower in clean_words:
    if cislo_lower.islower():
        counterIslower += 1
print(f"Obsahuje {counterIslower} malých slov.")
counterIsnumeric = 0
for cislo_numeric in clean_words:
    if cislo_numeric.isnumeric():
        counterIsnumeric += 1
print(f"Existují {counterIsnumeric} číselné řetězce.")
sum_word = 0
for sumText1 in clean_words:
    if sumText1.isdigit():
        sum_word = sum_word + int(sumText1)
print(f"Součet všech čísel {sum_word}")
print(delka)
titulka1 = " OCCURENCES "
titulka1.strip()
print(f"LEN| {titulka1} |NR.")
print(delka)
clean_words1 = clean_words[0].strip("Situate")
clean_words2 = clean_words[27]
clean_words3 = clean_words[12].strip("impr")
clean_words4 = clean_words[13]
clean_words5 = clean_words[1].strip("ab")
clean_words6 = clean_words[11].strip("ruge")
clean_words7 = clean_words[49].strip("Ral")
clean_words8 = clean_words[14].strip("e")
clean_words9 = clean_words[15].strip("th")
clean_words10 = clean_words[48].strip("peacif")
clean_words11 = clean_words[51].strip("raves")
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
print("  6|".rstrip(), len_word6, "         |".rstrip(), len(len_word6))
print("  7|".rstrip(), len_word7, "      |".rstrip(), len(len_word7))
print("  8|".rstrip(), len_word8, "      |".rstrip(), len(len_word8))
print("  9|".rstrip(), len_word9, "           |".rstrip(), len(len_word9))
print(" 10|".rstrip(), len_word10, "           |".rstrip(), len(len_word10))
print(" 11|".rstrip(), len_word11, "           |".rstrip(), len(len_word11))




