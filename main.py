# n = int(input('Кол-во элементов списка: '))
# x = []
# for _ in range(n):
#   print('Введите', _ + 1, 'число:', end = ' ')
#   num = int(input())
#   x.append(num)
#
# print('Изначальный список:', x)
n = 5
x = [1, 4, -3, 0, 10]

for i_1 in range(n - 1):
  print(i_1)
  minimal = i_1
  print(minimal)
  print()

  for i_2 in range(i_1, n):
    print(i_2)
    if x[i_2] < x[minimal]:
      minimal = i_2
    print(minimal)
    print()

  x[i_1], x[minimal] = x[minimal], x[i_1]
  print(x)

print('Отсортированный список:', x)
