import library.ahorcado
import library.numerorandom
import library.primeraclase
import library.lista
import library.estrella
import library.triqui
import library.triqui3d

print("""
      =================
        𝐁𝐈𝐄𝐍𝐕𝐄𝐍𝐈𝐃𝐎
      =================""")
opcion = "1"
while opcion != "0":
    print("""
     Selecciona la opcion
     1)triqui3d
     2)triqui
     3)estrella
     4)lista
     5)primeraclase
     6)numerorandom
     7)ahorcado""")
    opcion = input()
    if opcion == "1":
        library.triqui3d.main_triqui3d()
    if opcion == "2":
        library.triqui.main_triqui()
    if opcion == "3":
        library.estrella.main_estrella()
    if opcion == "4":
        library.lista.main_estrella()
    if opcion == "5":
        library.primeraclase.main_primeraclase()
    if opcion == "6":
        library.numerorandom.main_numerorandom()
    if opcion == "7":
        library.ahorcado.main_ahorcado()
        