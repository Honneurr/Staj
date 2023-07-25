#!/usr/bin/env python
# coding: utf-8

# In[7]:


def main():
    try:
        sayilar = int(input("Toplam kaç sayı gireceksiniz? "))
        numbers = []
        for x in range(sayilar):
            sayi = float(input(f"{x+1}. sayıyı giriniz: "))
            numbers.append(sayi)

        siralama = sorted(numbers)

        print("Sıralanmış sayılar:")
        for deger in siralama:
            print(deger)

    except ValueError:
        print("Hatalı cevap. Lütfen bir sayı girin")

if __name__ == "__main__":
    main() 


# ## 
