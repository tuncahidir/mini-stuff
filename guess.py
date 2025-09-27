#import edilecek
import random
from itertools import count

#sayı tutulacak
num = random.randint(1, 100)
tries = 0

while True:
    while not (s := input("Tahmin: ")).isdigit():
        print("Lütfen sayı girin.")
    guess = int(s)
    tries += 1

    if num == guess:
        print(f"{tries} denemede bildin")
        break

    else:
        d = abs(guess - num)
        if d <= 5:
            print("Sıcak") 
        elif d<= 10:
            print("Ilık")
        else:
            print("Soğuk")
 
    if guess < num:
        print("Daha büyük bir sayı dene")
    else:
        print("Daha küçük bir sayı dene")

    if tries == 10:
        print("Bilemedin")
        break
    