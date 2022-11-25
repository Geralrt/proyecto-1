def main_numerorandom():
    import random
    x= random.randint(0,1000)
    if (x%2==0):
      print(x)
      print("es par")
    else:
      print(x)
      print("es impar")
      
    rnd_lista = [random.randint(0,100) for i in range(random.randint(30,100))]
    print(rnd_lista)
    
    d=[5,2,3,8,7,5,3,1,0]
    for  i in d:
      if (i%2==0):
        print(i)
        print("es par")
      else:
        print(i)
        print("es impar")
        
    for i in range(1,100):
        if i%3==0 and i%5==0:
          print("fizzbuzz")
        elif i%3==0:
          print("fizz")
        elif i%5==0:
          print("buzz")
        else:
          print(i)