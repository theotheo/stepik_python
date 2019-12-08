# 5.2 Словарь. Шаг 5. Экстремумы
# https://stepik.org/lesson/251914/step/5?unit=245232
# %% через get 
# https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary

test_dict = {"a": 43, "b": 1233, "c": 8}

min_value = min(test_dict, key=test_dict.get)
max_value = max(test_dict, key=test_dict.get)

print('min: {}'.format(min_value))
print('max: {}'.format(max_value))

# 
test_dict['a'] == test_dict.get('a')

# dict.get
# https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
# %%
test_dict.get('a')

# %%
test_dict.get('not_a_key', 0)

# %% через lambda 
min_value = min(test_dict.items(), key=lambda x: x[1])[0]
max_value = max(test_dict.items(), key=lambda x: x[1])[0]

print('min: {}'.format(min_value))
print('max: {}'.format(max_value))

# %% lambda
func = lambda x: x[1]
print(func)
print(func(['a', 1]))
# print(func(test_dict.items()))

# 
def foo(x):
    pass 

# %%
s = lambda x, y, z: x + y + z 
s(1, 2 ,3)

def s(x, y, z):
    return 1 + 2 + 3