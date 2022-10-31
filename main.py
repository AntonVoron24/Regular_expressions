import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def refactor_data(some_list: list):
    """
    Функция обрабатывает список и приводит к нужному формату.
    :param some_list:
    :return:
    """
    phone_book = []
    for param in some_list:
        phone_search = r'(\+7|8)?\s*\(?(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s*\(?(доб.*\d+)*\)?'
        phone = re.sub(phone_search, r'+7(\2)\3-\4-\5 \6', param[5])
        full_name = ' '.join(param[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], param[3], param[4], phone, param[6]]
        phone_book.append(result)
    return phone_book


def union(contacts: list):
    """
    Функция обработки списка от дублей и пустых записей.
    :param contacts:
    :return:
    """
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts:
            if first_name == new_contact[0] and last_name == new_contact[1]:
                if not contact[2]:
                    contact[2] = new_contact[2]
                if not contact[3]:
                    contact[3] = new_contact[3]
                if not contact[4]:
                    contact[4] = new_contact[4]
                if not contact[5]:
                    contact[5] = new_contact[5]
                if not contact[6]:
                    contact[6] = new_contact[6]

    result_list = []
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list

if __name__ == '__main__':
    try:
        update_data = refactor_data(contacts_list)  # Приводим в порядок данные
        new_phonebook = union(update_data)  # Убираем дубли по lastname и firstname, дополняем данные

        with open("phonebook.csv", "w", encoding='utf-8') as f:  # код для записи файла в формате CSV
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(new_phonebook)
            print("\033[32m {}" .format('Congratulations! This is a success!'))
    except Exception as error:
        print("\033[31m {}" .format(f'ERROR: {error}'))
