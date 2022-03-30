def print_message(poruka):
    print(poruka)

def sum(a,b):
    return a+b

def ispisi_pozdrav_na_ekran(ime):
    pozdravna_poruka = "Zdravo \"" + ime + "\"!!"
    print(pozdravna_poruka)
    print(pozdravna_poruka.lower())
    print(len(pozdravna_poruka))
    print(pozdravna_poruka.replace("Z","s"))

def da_li_je_jednako(a,b):
    jednakost = a==b
    print(jednakost)
    
    
print_message("zdravo")
ispisi_pozdrav_na_ekran("Ilija")
da_li_je_jednako(5,6)

da_li_je_jednako("5","6")

def funkcija_2x_plus_1(x):
    print(2*x+1)

funkcija_2x_plus_1(5)

rezultat=sum(5,6)
print(rezultat)

rezultat=sum(1,2)
print(rezultat)
broj=5
print(broj)
print(1+2)
print(5+6)

a=False
b=False

print(a or b)
print(not a)
print(5+5)
print("5"+"5")
print(str(5)+"5")
print(5+int("5"))

