# Напишите программу, которая выводит n первых элементов последовательности 122333444455555…
# (число повторяется столько раз, чему оно равно).

def func(x):
    result = []
    num = 1

    while len(result) < x:

        for _ in range(num):
            if len(result) < x:
                result.append(str(num))

        num+=1

    return "".join(result)

