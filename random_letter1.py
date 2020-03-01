import random
word=["самовар", "весна", "лето"]
random.choice(word)
if random.choice(word) =="весна":
    K=["в?сна", "?есна", "в?сна", "ве?на", "вес?а"]
    K=random.choice(word)
    print ('Введите букву: ')
    print(K)
Otv=input()
if K=='в?сна':
    if Otv=='е':
        N=1
    else:
        N=0
elif K=='?есна':
    if Otv=='в':
        N=1
    else:
        N = 0
elif K=='ве?на':
    if Otv =='с':
        N=1
    else:
        N=0
if N==1:
    print ('Победа!')
    print ('слово: самовар')
else:
    print ('Увы, попробуйте в другой раз')
    print ('слово: самовар')

