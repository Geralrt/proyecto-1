def main_ahorcado():
    
    import random
    n = random.randint (0,5)
    print(n)
    lista = ["palabra","carro","gato","maleta","murcielago","amor"]
    w = 0 
    palabra = lista[n] 
    guess = ["_"]*len(palabra)
    tries = 7
    while True:
        t = input()
        flag = False
        
        
        for i,p in enumerate(palabra):
            if p == t:
                flag = True
                guess[i] = p
        if not flag:
            w+=1
        if w==tries:
            print("Ahorcado")
            break
        print("".join(guess))
        if "".join(guess) == palabra or t == palabra:
             print("Ganador")
             break
    
    