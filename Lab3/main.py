import time

base_string = input("Введите строку ->")
sub_string = input("Введите подстроку ->")

tabulat = False
tabulation = input("Вы хотите включить чувствительность к пробелам? (да/нет) =>")
if tabulation == "да":
    base_string = base_string.replace(' ','')
    sub_string = sub_string.replace(' ','')
elif tabulation != "нет":
    print("Вы ввели что-то не так, поэтому я всё решил сам, чувствительность - отключена!")

senset = False
sensetivity = input("Вы хотите включить чувствительность к регистру? (да/нет) =>")
if sensetivity == "да":
    senset = True
elif sensetivity != "нет":
    print("Вы ввели что-то не так, поэтому я всё решил сам, чувствительность - отключена!")

def prefix(s):
    p = [0] * len(s)
    i = j = 0

    while j < len(s):
        if s[i] == s[j]:
            p[j] = i + 1
            i += 1
            j += 1
        elif i:
            i = p[i - 1]
        else:
            p[j] = 0
            j += 1
    return p


def KMPalg(s, sub):
    p = prefix(sub)
    i = j = 0

    while i < len(s):
        if sub[j] == s[i]:
            i += 1
            j += 1

            if j == len(sub):
                return "\nРасположение найденной подстроки => " + str(i - len(sub))

        elif j > 0:
            j = p[j - 1]
        else:
            i += 1

    return "\nВведённая подстрока не найдена!"

def preprocess(w):
    # Строит таблицу смещений
    T = [len(w) for _ in range(1105)]
    for i in range(len(w)):
        T[ord(w[i])] = len(w) - i   # сколько символов с правого края до этой буквы
    return T

def BM(s, sub):
    d = preprocess(sub)
    i = j = k = len(sub)

    while j > 0 and i <= len(s):
        if s[k - 1] == sub[j - 1]:
            k -= 1
            j -= 1

        else:
            i += d[ord(s[k - 1])]
            j = len(sub)
            k = i

    if j <= 0:
        return "\nРасположение найденной подстроки => " + str(k)
    else:
        return "\nВведённая подстрока не найдена!"

def standart_search(s, sub):
    k = -1
    for i in range(len(s) - len(sub) + 1):
        success = True
        for j in range(len(sub)):
            if sub[j] != s[i + j]:
                success = False
                break

        if success:
            k = i
            break

    if k != -1:
        return "\nРасположение найденной в строке подстроки: " + str(k)
    else:
        return "\nВведённая подстрока не найдена"

if senset == False:
    KMP_start_time = time.time()
    print(KMPalg(base_string, sub_string))
    print(f"{(time.time() - KMP_start_time)*1000000}секунд")
else:
    KMP_start_time = time.time()
    print(KMPalg(base_string.lower(), sub_string.lower()))
    print(f"{(time.time() - KMP_start_time)}секунд")


if senset == False:
    BM_start_time = time.time()
    print(BM(base_string, sub_string))
    print(f"{(time.time() - BM_start_time)}секунд")
else:
    BM_start_time = time.time()
    print(BM(base_string.lower(), sub_string.lower()))
    print(f"{(time.time() - BM_start_time)}секунд")


if senset == False:
     ST_start_time = time.time()
     print(standart_search(base_string,sub_string))
     print(f"{(time.time() - ST_start_time)} секунд")
else:
     ST_start_time = time.time()
     print(standart_search(base_string.lower(), sub_string.lower()))
     print(f"{(time.time() - ST_start_time)} секунд")