immutable_var = 9, 8, 7, False, 'String'
print('Immutable tuple:', immutable_var)

# Если изменить элемент кортежа
# immutable_var[0] = 10
# print(immutable_var)
# На экран будет выведено:
# C:\Users\xlouo\PycharmProjects\Lesson0\.venv\Scripts\python.exe C:\Users\xlouo\PycharmProjects\Lesson0\module_1_5.py
# (9, 8, 7, False, 'String')
# Traceback (most recent call last):
#   File "C:\Users\xlouo\PycharmProjects\Lesson0\module_1_5.py", line 4, in <module>
#     immutable_var[0] = 10
#    ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
#
# Process finished with exit code 1
# После того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять.

mutable_list = [9, 8, 'q', 'w']
mutable_list.append('Modified')
print('Mutable list:', mutable_list)