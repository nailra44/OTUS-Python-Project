a = [1,2,3]
b = [1,2,3]
c = a
print("a == b ", a == b)
print("a is b ", a is b)
print("a of id ", id(a))
print("b of id ", id(b))
print("c of id ", id(c))
print("a is b ", a is b)
print("a == c ", a == c)
print("a is c ", a is c)

print(a, b, c)
a.append(4)
b.append(9)
c.append(5)
print(a, b, c)


num_a = 10000000 ** 50
num_b = 10000000 ** 50

print("num_a == num_b", num_a == num_b)
print("num_a is num_b", num_a is num_b)


print("a is list type?", isinstance(a, (list, tuple)), type(a))

t = ()
print("t is list-like type?", isinstance(t, (list, tuple)), type(t))

exists = True
print("exist is type of int?", isinstance(exists, int), type(exists))
print("exists to int", int(exists))
print("exists is 1", exists is 1)
print("exists == 1", exists == 1)
print("exists of id ", id(exists))
print("id of int ", id(int))

def get_list(input_list=None):
    if input_list is None:
       input_list = []
    return input_list
empty_list = []
res = get_list()
print("empty list == res?", empty_list == res)
print("empty list is res?", empty_list is res)

print("empty list is res?", empty_list is get_list(empty_list))

cache = {}

def get_user(user_id):
    if user_id not in cache:
       u = ... #элипсис
       cache[user_id] = u
       return u
    return cache[user_id]

u3 = get_user(7)

u1 = get_user(7)
u2 = get_user(7)
"""
u1 == u2 # is True

u1.id == u2.id # is True

u1 is u2 # is False
u1 is not u2 # is True
"""
print("type(a)", type(a))
print("type(a) is type(b) ", type(a) is type(b))
print("type(a) is type(c) ", type(a) is type(c))


'''инициализация репозитория - git init
   добаление файла git add lesson3.py
   просмотр статуса git status
   добавление user git config --global user.Nailra
   добавление email git config --global user.email "nailra44@yandex.ru"
   commit файла git commit -m "install commit me"
   или git commit
   просмотр изменений в файле до commit git diff lesson3.py
   добавление для commita git add lesson3.py
   commit файла git commit -m "install commit me2"
   git diff lesson3.py Команда git diff показывает разницу между:
     Текущим состоянием файла на диске (working directory)
     Последним коммитом
   git log --oneline  просмотр сколько было сохранений
   git show 2934fa1  просмотр сохранения по хэшу
   git rm .idea/.gitignore - удаление файла из репо
   git rm --cached lesson3.py - Удаляем из индекса Git, но оставляем файл на диске
   git rm -f .idea/.gitignore - удаление файла из репо безвозвратно
   git restore .\lesson2.py - восстановление из файла если не было commit
   git reset - возвращение удалённого файла
   git reset --hard HEAD -
       Сбрасывает индекс (staging area) к состоянию HEAD (последнего коммита)
       Сбрасывает рабочую директорию к состоянию HEAD
       Удаляет все незакоммиченные изменения
       Что происходит при выполнении:
       Все изменения в отслеживаемых файлах исчезнут
       Все добавленные в staging файлы (git add) сбросятся
       Рабочая директория станет идентичной последнему коммиту
   git ls-files - просмотр всех отслеживаемых файлов
   git ls-tree -r HEAD --name-only - 
   для создания исключений необходимо в файл gitignore имена файлов которые надо игнорировать
   git checkout -b feature/modifi-lists команда создает новую ветку и переключается на нее - изоляция изменений
     feature/ — для новой функциональности (как у вас)
     bugfix/ — для исправления ошибок
     hotfix/ — для срочных исправлений
     release/ — для подготовки релиза
   git checkout master - вернутся в мастер
   git checkout feature/modifi-lists - переключение между ветками
   git merge feature/modifi-lists - слить изменения
   git branch - проверить в какой ветке сейчас
   git branch -M main переименовать branch 
   git remote add origin https://github.com/nailra44/OTUS-Python-Project.git - добавить удалённый репозиторий
   git remote -v - проверить добавление
   git push -u origin main - запушить проект в репозиторий
   tig - удобное приложение для просмотра commit
   tig - удобное приложение для просмотра commit
   
   nailra44@yandex.ru
'''
