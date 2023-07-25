#!/usr/bin/env python
# coding: utf-8

# In[10]:


def algoritma(dizi):
    n = len(dizi)
    for i in range(n):
        for c in range(0, n-i-1):
            if dizi[c] > dizi[c+1]:
                dizi[c], dizi[c+1] = dizi[c+1], dizi[c]
    




def main():
    try:
        sayilar = int(input("Toplam kaç sayı gireceksiniz? "))
        numbers = []
        for x in range(sayilar):
            sayi = float(input(f"{x+1}. sayıyı giriniz: "))
            numbers.append(sayi)

        algoritma(numbers)

        print("Sıralanmış sayılar:")
        for deger in numbers:
            print(deger)

    except ValueError:
        print("Hatalı cevap. Lütfen bir sayı girin")

if __name__ == "__main__":
    main() 


# ## 
