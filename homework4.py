immutable_var = 1, 2, 3, 4, 'Str', True
print(immutable_var)
immutable_var[2] = 8  # Кортеж не изменяем
print(immutable_var)  # при попытке изменить кортеж мы получим оштбку 'tuple' object does not support item assignment

mutable_list = [1, 2, 'Hello', True, 'World']
mutable_list.append('apple')
print(mutable_list)
mutable_list.extend(['banana', 67])
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
print('Hello' in mutable_list)
print('Hello' not in mutable_list)
