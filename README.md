## Задание

Для проверки пример запроса в Postman:
{
    "cmd1": "filter",
    "value1": "POST",
    "cmd2": "map",
    "value2": "0"
}


Сделать веб-сервер на flask, который 1) “повторяет” функционал командной строки линукса для обработки файлов. 2) состоит из одного POST метода. Метод должен удовлетворять следующим требованиям:

<aside>
💡 1. Доступен по пути /perform_query
2. Принимает 5 параметров: где 1, 2, 3, 4 - запрос, 5-ый - имя файла. 
Ссылка на [примеры запросов](https://gist.github.com/alexopryshko/4f5264eac09a46a368ac16add1a9e0dc)
3. Метод должен искать файлы внутри директории data. Папка data должна находиться в одной папке с веб-сервером.
4. Обрабатывать файл, следуя написанному запросу, и возвращать ответ клиенту

</aside>

## Рассмотрим язык запросов query

Query поддерживает несколько команд: **filter, map, unique, sort, limit.** Для упрощения задачи всегда выполняются только 2 команды, то есть, например, **cmd1=filter, value1=POST, cmd2=limit, value2=5.** Данный запрос означает, что выполнится команда filter c аргументом POST, далее результат выполнения будет передан на вход команде limit c аргументом 5. 

Давайте рассмотрим каждую команду на примерах. Допустим у вас есть лог-файл работы веб-сервера :

```python
1.181.2.178 [17/May/2015:20:05:36] "GET / HTTP/1.1" 200
1.125.2.148 [17/May/2015:20:05:19] "GET /?flav=rss20 HTTP/1.1" 200
1.170.2.204 [17/May/2015:20:05:03] "POST /?flav=atom HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:36] "GET /images/gle.png HTTP/1.1" 200
1.163.30.77 [17/May/2015:20:05:37] "GET /blog/dot.html HTTP/1.1" 200
```

### Команда **filter**

Команда **filter** принимает в качестве аргумента строку, по которой нужно будет фильтровать строки входных данных. Команда filter является “поиском” по файлу, ее можно применять, например, когда нужно найти запрос с определенными параметрами или IP адресом. В результате выполнения запроса должно быть выведено:

### Команда **map**

Рассмотрим команду **cmd1=map value1=<col>** - этой командой мы изменяем формат исходных данных (проекция). В качестве аргумента **<col>** команда **map** принимает номер колонки. Исходные данные разделяются на колонки на основе пробела. В результате выполнения запроса должно быть выведено:

То есть из всех данных мы оставили только IP адреса запросов.

### Команда unique

Рассмотрим запрос **cmd1=unique value1=””**. У команды unique нет аргументов (в value1 нужно передать пустую строку), из названия следует, что она оставляет только уникальные значения, то есть если ей на вход подать:

```python
1.181.2.178
1.125.2.148
1.170.2.204
1.163.30.77
1.163.30.77
```

В результате выполнения получим на одну запись меньше:

```python
1.181.2.178
1.125.2.148
1.170.2.204
1.163.30.77
```

### Команда sort

Рассмотрим команду **cmd1=sort value1=<asc:desc>.** Команда sort сортирует данные в алфавитном порядке или в обратном алфавитном порядке, в зависимости от переданного аргумента. asc - прямой порядок, desc - обратный.

Рассмотрим команду **cmd1=limit value1=<n>**. Команда limit выводит только необходимое количество строки из запроса. Например, запрос, query=limit:3 выведет только 3 записи:

### Использование двух команд

Язык запросов всегда предполагает использование двух команд. Давайте рассмотрим пример:

**cmd1=filter value1=POST cmd2=map value=0**

В результате выполнения команды **cmd1=filter value1=POST** будет выведено:

Полученные результаты передаются на вход команде map. В результате выполнения команды **cmd2=map value=0** будет выведено:

Давайте рассмотрим еще пример: **cmd1=map value1=0 cmd2=unique value2=””**

В результате выполнения команды **cmd1=map value1=0** будет выведено:

Полученные результаты передаются на вход команде unique. В результате выполнения команды **cmd2=unique value2=””** будет выведено:

## Как выполнять задание

[https://github.com/skypro-008/lesson23_project_source](https://github.com/skypro-008/lesson23_project_source)

## Проверьте себя

- [ ]  Использован файловый дескриптор как генератор.
- [ ]  Применены функции map, filter, sorted, list, set (или dict, или counter).
- [ ]  Решение позволяет конструировать запрос, например, **cmd1=filter&value1=POST, cmd2=limit&value2=5.**
- [ ]  Использованы lambda-функции.

