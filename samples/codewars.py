import re

def decipher_this(s):
    def func(string: str) -> int:
        for i, n in enumerate(string):
            if n.isalpha():
                return i
        return -1  # Если букв нет

    s = s.split()
    new_s = []
    for l in s:
        i = func(l)
        if i <= 0:
            # нет числового кода, пропускаем или обрабатываем иначе
            continue
        first = chr(int(l[:i]))
        last = re.sub(r'[^A-Za-z]', '', l[i:])

        if len(last) < 3:
            new_s.append(first + last)
        else:
            last = list(last)
            last[0], last[-1] = last[-1], last[0]
            last = "".join(last)
            new_s.append(first + last)
    return " ".join(new_s)

print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
