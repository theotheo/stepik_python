# Про идиоматичность
# 5.2 Словарь. Шаг 6. Частотный словарь
# https://stepik.org/lesson/251914/step/6?unit=245232

# %%
TEXT = 'a aa abC aa ac abc bcd a'
# %% прямолинейное решение

# text = input()
text = TEXT

words = text.lower().split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for word, count in counts.items():
    print(word, count)

# %% через get

# text = input()
text = TEXT

words = text.lower().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(word, count)

# %% defaultdict 
from collections import defaultdict

# text = input()
text = TEXT

words = text.lower().split()
counts = defaultdict(lambda: 0)
for word in words:
    counts[word] += 1

for word, count in counts.items():
    print(word, count)

# %%
adict = defaultdict(lambda: 10)
adict 

# %%
nested_dict = defaultdict(dict)
nested_dict

# %% Counter
from collections import Counter

# text = input()
text = TEXT

words = text.lower().split()
counts = Counter()

for word in words:
    counts[word] += 1

for word, count in counts.items():
    print(word, count)

# %%
print(counts)

# %%
acounter = Counter(['a', 'b', 'c', 'a', 'b', 'b', 'b'])
acounter

# %%
counts = Counter(text.lower().split())
for word, count in counts.items():
    print(word, count)

# %% [markdown]
#  модуль collections
# https://pythonworld.ru/moduli/modul-collections.html
# http://book.pythontips.com/en/latest/collections.html
# defaultdict
# OrderedDict
# counter
# deque
# namedtuple
# enum.Enum (outside of the module; Python 3.4+)

# Варианты подсчета 
# https://treyhunner.com/2015/11/counting-things-in-python/