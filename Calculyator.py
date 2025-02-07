#Sodda kankulyator
#Kod muallifi Karimov Mirodil  
def plus():
    while True:
      amallar = input("Qaysi amalni tanlaysiz? (+ - * / yoki 'exit' chiqish uchun): ")

      if amallar.lower() == "exit":
          print("Dastur tugadi.")
          break  
      son1=int(input("Birinchi sonni kiriting: "))
      son2=int(input("Ikkinchi sonni kiriting: "))
      if amallar=='+':
            yigindi1=son1+son2
            print(f"{son1}qo`shganda{son2} yig`indisi {yigindi1}")
      elif amallar=='-':
            yigindi2=son1-son2
            print(f"{son1} ayriganda {son2} javob {yigindi2}")
      elif amallar=='*':
            yigindi3=son1*son2
            print(f"{son1} ko`paytirsa{son2} javob {yigindi3}")
      elif amallar=="/":
         if son2 == 0:
            print("Xatolik! Nolga bo‘lish mumkin emas.")
         else:
            print(son1 / son2)
plus()
