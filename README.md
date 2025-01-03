# Использование скриптов

Этот проект включает скрипты для работы с базой данных учеников, которые помогают исправлять оценки, удалять замечания и добавлять похвалы.

## Установка и настройка

- Поместите файл со скриптами

Создайте файл `scripts.py` в корневой папке проекта, рядом с файлом `manage.py`.

Скопируйте в него следующие функции:

`find_schoolkid`

`fix_marks`

`delete_chastisements_for`

`create_commendation`

- Убедитесь, что проект настроен

Активируйте виртуальное окружение проекта.

Убедитесь, что база данных заполнена тестовыми данными.

## Как использовать скрипты

Откройте Django Shell Запустите shell с помощью команды:

`python manage.py shell`

Импортируйте функции Внутри shell подключите скрипт:

`from scripts import find_schoolkid, fix_marks, delete_chastisements_for, create_commendation`

Используйте функции:

### Поиск ученика

`schoolkid = find_schoolkid('Фролов Иван')`

Если ученик найден, возвращается объект Schoolkid. Если ученики с таким именем отсутствуют или найдено несколько, выводится соответствующее сообщение.

### Исправление оценок
```
if schoolkid:
    fix_marks(schoolkid)
```
Все двойки и тройки ученика будут заменены на пятёрки. Скрипт выводит количество исправленных оценок.

### Удаление замечаний

`delete_chastisements_for('Фролов Иван')`

Удаляет все замечания для указанного ученика.

### Добавление похвалы

`create_commendation('Фролов Иван', 'Музыка')`

Добавляет похвалу на последнем уроке указанного предмета. Текст похвалы выбирается случайно.

## Примеры использования
```
from scripts import find_schoolkid, fix_marks, delete_chastisements_for, create_commendation

schoolkid = find_schoolkid('Фролов Иван')
if schoolkid:
    fix_marks(schoolkid)
    delete_chastisements_for('Фролов Иван')
    create_commendation('Фролов Иван', 'Музыка')
```

## Примечания

Скрипты предназначены для использования в учебных целях.

