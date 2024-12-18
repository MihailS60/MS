def send_email(recipient, *,message,sender="university.help@gmail.com"):
    if recipient == 'vasyok1337@gmail.com':
        print('\n',message,recipient)               # Это сообщение для проверки связи
        return
    if recipient == 'urban.student@mail.ru':
        print('\n', message, f'отправитель {sender} и получатель {recipient}')
        return
    if  sender== 'urban.info@gmail.com':
        print('\n',message,f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} и получатель {recipient}')               # Нельзя отправить письмо самому себе!
        return
    if recipient == sender:
        print('\n',message,recipient)               # Нельзя отправить письмо самому себе!
        return

    print('\n',message,f'отправитель {sender} и получатель',[recipient[j] for j in range(0, len(recipient)) if sender==recipient[j]])
    return

def check_mail(adress_correct, recipient_int):

    print('\n', 'Проверяем полученные адреса : ', '\n', recipient_int, '\n')
    s = ['@', '.com', '.ru', '.net']                       # ключевые элементы почтового адреса
    flag_ = []                                             # флажки ошибок
    adress_false=[]

    for i in range(1, len(recipient_int) + 1):
        flag_.append([])
        for j in range(1, len(s) + 1):
            if recipient_int[i - 1].find(s[j - 1]) == -1:    # на наличие списка s=['@','.com','.ru','.net']
                flag_[i - 1].insert(j - 1, 'False')
            else:
                flag_[i - 1].insert(j - 1, 'True')
            continue

        if (flag_[i - 1][0] == 'True') and (
                flag_[i - 1][1] == 'True' or flag_[i - 1][2] == 'True' or flag_[i - 1][3] == 'True'):
            # тестовая печать   print(recipient[i - 1], 'Адрес правильный')
            adress_correct.append(recipient_int[i - 1])           # список правильных адресов
            continue
        # разделитель       print('-------------------------------')
        elif (flag_[i - 1][0] == 'True') and (
                flag_[i - 1][1] == 'False' or flag_[i - 1][2] == 'False' or flag_[i - 1][3] == 'False'):
            print(recipient_int[i - 1], 'содержит "@" и не оканчивается на ".com"/".ru"/".net"')
            print('-------------------------------')
        elif (flag_[i - 1][0] == 'False') and (
                flag_[i - 1][1] == 'True' or flag_[i - 1][2] == 'True' or flag_[i - 1][3] == 'True'):
            print(recipient_int[i - 1], 'не содержит "@" и оканчивается на ".com"/".ru"/".net"')
            print('-------------------------------')
        elif (flag_[i - 1][0] == 'False') and (
                flag_[i - 1][1] == 'False' or flag_[i - 1][2] == 'False' or flag_[i - 1][3] == 'False'):
            print(recipient_int[i - 1], 'не содержит "@" и не оканчивается на ".com"/".ru"/".net"')
            print('-------------------------------')
        adress_false.append(recipient_int[i - 1])           # список некорректных адресов

    print('Правильные адреса : ',[adress_correct[j] for j in range(0, len(adress_correct)) if len(adress_correct)>0])
    print('Невозможно отправить/получить письма с адресов : ',[adress_false[j] for j in range(0, len(adress_false)) if len(adress_false) > 0])
    return




sender_list=['university.help@gmail.com','urban.teacher@mail.ru','urban.info@gmail.com']
recipient_list = ['aa@aa', 'urban.info@gmail.com','dd.com','urban.student@mail.ru','urban.fan@mail.ru', 'dfg@y.net', 'ff@dfg.ru', 'hh','university.help@gmail.com', 'pp.net','@','ghj@er.com','vasyok1337@gmail.com', '.com', '.ru', '.net']
adress_correct =[]

check_mail(adress_correct,recipient_list)   # проверяем корректность адреса "Получатель"
recipient_final=adress_correct.copy()   # "Получатель" без некорректных адресов
adress_correct.clear()                   #   очистка списка
check_mail(adress_correct,sender_list)        # проверяем  корректность адреса "Отправитель"

send_email('vasyok1337@gmail.com',message='Это сообщение для проверки связи')
send_email('urban.student@mail.ru',message='Пожалуйста, исправьте задание',sender="urban.teacher@mail.ru")
send_email('urban.fan@mail.ru',message='Вы видите это сообщение как лучший студент курса!',sender="urban.info@gmail.com")
send_email(recipient_final,message='Нельзя отправить письмо самому себе!')





