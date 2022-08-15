# parcing
В рамках задачи необходимо собрать информацию о том, в каких фильмах снимались актеры (граф связей актёров со всего мира, для того, чтобы выяснить, кто с кем работает чаще и т.д).

Первый файл описывает топ-50 самых популярных актеров на данный момент, второй — фильмы, в которых они снимались. 

Первый файл содержит информацию для каждого актёра: 
1. Биографию (bio). 
2. Дата рождения (born).
3. Список фильмов (movies) — первые 15 штук на странице актера.
4. Имя актера (name). 
5. Ссылка на персональную страницу (ключ url).

Второй файл содержит информацию для каждого фильма:
1. Ссылка на страницу фильма (url). 
2. Название фильма (title). 
3. Список актёров (cast) с перечислением имён.
