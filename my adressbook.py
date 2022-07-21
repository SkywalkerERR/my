contacts = {

}

i = 0



#Поиск номера по имени
def find(person):
    a = 0
    for i in contacts:
            a = contacts[i].split()

            if a[0] == person:
                print('По имени',a[0],'найден номер! -',a[1])
            else:
                print('Контакт не найден')

#Показать контакт
def get_info():
    for i in range(len(contacts)):
        print(contacts[i+1])

#Добавление контакта
def info(information):
    global i
    i += 1
    contacts[i] = information
    print('Контакт успешно добавлен!')
    print(contacts)

#Удаление контакта
def deleted(why):
    for product,values in list(contacts.items()):
        if why in values:
            del contacts[product]

#Изменить имя контакта
def changer(what,change):
    for product,values in list(contacts.items()):
        if what in values:
            s = values.split()
            contacts[product] = (change + s[1]).split()
#Сохранить контакты
def save():
    g = []
    j = 0
    for number, value in list(contacts.items()):
        g.append(value)
        str_g = ' '.join(g)
    with open('contacts.txt', 'a') as f:
        for index in g:
            f.write(index + '\n')



#Основа
while True:
#Приветствие
    hello = (input('Что вам нужно?: ')).lower()
    if hello == 'добавить контакт':
        name, number = input('Введите имя и телефон: ').split()
        person = name, number
        person_info = ' '.join(person)
        info(person_info)

    elif hello == 'найти номер':
        who = input('Чей номер ищем?: ')
        find(who)
    elif hello == 'показать контакты':
        get_info()

    elif hello == 'изменить контакт':
        what = input('Имя изменяемого контакта: ')
        one = input('На какое имя изменить: ')
        changer(what,one)
        print('Имя контакта ',what,' успешно изменено на ',one)

    elif hello == 'удалить контакт':
        dele = input('Какой контакт удалить?: ')
        deleted(dele)
        print('Контакт ',dele,' успешно удалён!')



    elif hello == 'стоп':
        save()
        break
