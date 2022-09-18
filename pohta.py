#скрипт присилае нам лист
import smtplib as smtp
from getpass import getpass
#Пишем базовую информацию о себе:

# Почта, с которой будет отправлено письмо
email = 'xakepmail@yandex.ru'
# Пароль от нее (вместо ***)
password = '***'
# Почта, на которую отправляем письмо
dest_email = 'demo@xakep.ru'
# Тема письма
subject = 'IP'
# Текст письма
email_text = 'TEXT'
#Дальше сформируем письмо:

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)
#Последний штрих — настроить подключение к почтовому сервису. Я пользуюсь Яндекс.Почтой, поэтому настройки выставлял для нее.

server = smtp.SMTP_SSL('smtp.yandex.com') # SMTP-сервер Яндекса
server.set_debuglevel(1) # Минимизируем вывод ошибок (выводим только фатальные ошибки)
server.ehlo(email) # Отправляем hello-пакет на сервер
server.login(email, password) # Заходим на почту, с которой будем отправлять письмо
server.auth_plain() # Авторизуемся
server.sendmail(email, dest_email, message) # Вводим данные для отправки (адреса свой и получателя и само сообщение)
server.quit() # Отключаемся от сервера
#В строке server.ehlo(email) мы используем команду EHLO. Большинство серверов SMTP поддерживают ESMTP и EHLO,або HELLO Ес EHLO,- использовать HELO.

