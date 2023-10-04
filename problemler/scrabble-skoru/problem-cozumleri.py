# Problem 0
# verilen bir metindeki harflerin uzerinden gidip,
#  "e" harfi ise "EVET",
#            degil ise "HAYIR" yazmak
# Ornegin "devseu" metni icin su cikti olacak:
# HAYIR
# EVET
# HAYIR
# HAYIR
# EVET
# HAYIR

print("**** 0 ****")

degisken = "devseu"

for i in degisken:
    if i == "e":
        print("EVET")
    else:
        print("HAYIR")



# Problem 1
# verilen bir metinde "e" harfinin kac kere gectigini bulmak
# Ornegin "devseu" metninde "e" harfi 2 kere geciyor
print("**** 1 ****")

def e_sayisi(metin):
    e_sayisi = 0
    for harf in metin:
        if harf == "e":
            e_sayisi += 1
    return e_sayisi

print(e_sayisi(degisken))



# Problem 2
# verilen bir metindeki tum harflerin kacar kere gectigini bulmak
# Ornegin "devseu" metninde:
#         1 tane d,
#         2 tane e,
#         1 tane v,
#         1 tane s,
#         1 tane u harfi var
print("**** 2 ****")

def harf_sayilari(metin):
    harf_sayilari = {}
    for harf in metin:
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1
    return harf_sayilari


print(harf_sayilari(degisken))



# Problem 3
# bir kelimenin scrabble skorunu bulmak
# Ornegin "devseu"nun scrabble skoru 10 puan
print("**** 3 ****")

def scrabble_skoru(metin):
    skor = 0
    for harf in metin:
        if harf in ScrabbleHarfPuanlari:
            skor += ScrabbleHarfPuanlari[harf]
    return skor


ScrabbleHarfPuanlari = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}

print(scrabble_skoru(degisken))

print("**** 4 ****")
# Problem 4 - bonus
# elimizdeki bir liste scrabble tasi ile yazilabilecek scrabble puani en yuksek kelimeyi (veya kelimeleri) yazdirmak
# Ornegin "devseu"nun harfleri ile yazilabilecek en uzun (ingilizce) kelime "suede" 6 puan. Ama en cok puani "devs" kelimesi (8 puan) getiriyor.
# Herhangi bir yerden ingilizce kelime listesi elde edebilirsin.
# Scrabble skorunu turkce harfler icin yazdi isen, burada da turkce kelimeler uretebilirsin.



