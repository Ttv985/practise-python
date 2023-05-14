array = input("Введите последовательность чисел через пробел: ").split()
num = int(input("Введите число: "))

array.append(num)

try:
    array = list(map(int, array))
except ValueError:
    print("Error")
    exit()
else:
    pass

def qsort():
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]
    return (array)
result = qsort()
print("Отсортированный список: ", result)

def find(array, num):
    for i, a in enumerate(array):
        if a == num:
            return i
    return False


print("Индекс введённого числа: ",find(array, num))

r_num = find(array, num) + 1
l_num = find(array, num) - 1
max_num = max(array)
x = array.index(max_num)
if find(array, num) == x:
    print("Ближайший больший элемент отсутствует")
else: print("Ближайший больший элемент имеет индекс: ",r_num)
if l_num < 0:
    print("Ближайший меньший элемент отсутствует")
else: print("Ближайший меньший элемент имеет индекс: ",l_num)

