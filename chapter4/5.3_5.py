# Про стиль
# %% https://stepik.org/lesson/266210/step/5?unit=247164
# DON'T DO THIS
phones = {"Алена": "8 (975) 257-82-42", "Станислава":"8 (900) 337-28-21", "Федосий":"8 (952) 951-14-54", "Ксения":"8 (943) 484-47-57", "Изабелла":"8 (958) 540-94-17"}

# https://stackoverflow.com/questions/3985563/python-best-formatting-practice-for-lists-dictionary-etc
# DO THIS
phones = {
    "Алена": "8 (975) 257-82-42", 
    "Станислава": "8 (900) 337-28-21", 
    "Федосий": "8 (952) 951-14-54", 
    "Ксения": "8 (943) 484-57-57", 
    "Изабелла": " 8 (958) 540-94-17"
}

# %% # иногда добавляют запятую
# https://www.python.org/dev/peps/pep-0008/#when-to-use-trailing-commas

phones = {
    "Алена": "8 (975) 257-82-42", 
    "Станислава": "8 (900) 337-28-21", 
    "Федосий": "8 (952) 951-14-54", 
    "Ксения": "8 (943) 484-47-57", 
    "Изабелла":" 8 (958) 540-94-17", # запятая!
    "fdfdsfds": "fdsfdsf",
}

# %% Styleguide
## PEP 8 https://www.python.org/dev/peps/pep-0008/
## Google http://google.github.io/styleguide/pyguide.html
## Django https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
## The Hitchhiker's Guide to Python https://docs.python-guide.org/writing/style/

# Linters
# https://ru.wikipedia.org/wiki/Lint

## pylint https://pypi.org/project/pylint/
## flake8 http://flake8.pycqa.org/en/latest/
## black https://github.com/psf/black

# "Холиварный рассказ про линтеры " https://habr.com/ru/company/oleg-bunin/blog/433480/
# https://code.visualstudio.com/docs/python/linting
# https://realpython.com/python-code-quality/


# Docstring
## PEP 257 https://www.python.org/dev/peps/pep-0257/

## https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring


def foo():
    """
    Функция делают фу

    Аргументы функции
    Возвращаемое значение
    """

    print('фу')