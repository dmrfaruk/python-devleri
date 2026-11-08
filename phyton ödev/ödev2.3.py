try :
    istenen_sayı=int(input("bir sayı giriniz"))
    print("girdiğiniz sayı=",istenen_sayı)
except ValueError:
    print("Lütfen geçerli bir sayı giriniz")
