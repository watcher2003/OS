from string import punctuation

print("MENU:\n"
      "1. A\n"
      "2. B")





def dodavannya_sliv():
    slova= text.split()
    for slovo in slova:
        if len(slovo) <=2:
            slova.remove(slovo)
    slova.sort(reverse=0)
    print('\n'.join(set(slova)))

def rahuvannya_bukv():
    bukvy = {}
    for bukva in text :
        if bukva  in punctuation and bukva == " ":
            continue
        else:
            if bukva in bukvy:
                bukvy[bukva]+=1
            else:
                bukvy[bukva]=1
    for char in bukvy:
        print("Буква ", char, " вжито ", bukvy[char], " раз")







while True:
    i = str(input("Виберить опцію меню: "))
    if i=="a" or i=="а" or i=='А' or i=="A" or i=="1":
        text=(input('Напишіть слово: '))
        dodavannya_sliv()


    elif i=="B" or i=="b" or i=="Б" or i=="б" or i== "2":
        text=str(input('Напишіть слово : '))
        rahuvannya_bukv()

    else:
        print("опції незнайдено!")