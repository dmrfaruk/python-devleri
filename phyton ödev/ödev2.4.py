import random
tutulan=random.randint(1,100)
while True:
    tahmin=int(input("bir tahmin yapınız"))
    if tahmin>tutulan:
        print("tahmin tutulandan büyük,tekrar dene")
    elif tahmin<tutulan:
        print("tahmin tutulandan küçük,tekrar dene")
    else:
        print("tahmin doğru,tebrikler")
        break