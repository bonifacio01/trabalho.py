B = int(input("Digite o ano atual:"))

A = int(input("Digite o ano que você nasceu:"))

v = B - A
print("RESULTADO:")

print (v)

if v >= 18:
    print ("você está apto a votar!")
else:
    print("aguarde a maior idade!")