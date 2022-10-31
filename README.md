Иногда при знакомстве мы записываем контакты в адресную книгу кое-как с мыслью, что "когда-нибудь потом все обязательно поправим". Копируем данные из интернета или из смски. Добавляем людей в разных мессенджерах. В результате получается адресная книга, в которой совершенно невозможно кого-то нормально найти: мешает множество дублей и разная запись одних и тех же имен.

Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/
Задача: починить адресную книгу, используя регулярные выражения.  
Структура данных будет всегда:   
`lastname,firstname,surname,organization,position,phone,email`  
Предполагается, что телефон и e-mail у человека может быть только один.  
Необходимо:
1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;  
2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;  
3. объединить все дублирующиеся записи о человеке в одну. Предполагается, что тёзок по имени и фамилии быть не может;
4. Сохранить обработанные данные в новый `.csv` файл.