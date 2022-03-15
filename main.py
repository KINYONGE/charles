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
my_clean_text = clean_words
my_dict = {}
symbol = "|"
for word in my_clean_text:
    my_dict[len(word)] = my_dict.get(len(word), 0) + 1
for my_key in sorted(my_dict):
    print("{:>2} {} {}".format(my_key, symbol, my_dict[my_key] * "*"), "{} {}".format(symbol, my_dict[my_key]))




