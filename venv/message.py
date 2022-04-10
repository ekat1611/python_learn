import imaplib
from imapclient import imap_utf7
from email.parser import BytesParser, Parser
from email.policy import default


EMAIL_SERVER = 'outlook.office365.com'
EMAIL_LOGIN = 'test_tricolor@outlook.com'
EMAIL_PASSWORD = 'Ekat160618'

# Авторизуемся
mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
mail.login(EMAIL_LOGIN, EMAIL_PASSWORD)
# Выводим список папок в почтовом ящике
mailList = mail.list()[1]
for value in mailList:
    print(imap_utf7.decode(value), value)

# Подключаемся к папке "входящие"
mail.select()
result, data = mail.search(None, "ALL")
# Получаем строку номеров писем
ids = data[0]
# Разделяем ID писем
id_list = ids.split()
# Берем последний ID
latest_email_id = id_list[-1]
# Получаем тело письма (RFC822) для данного ID
result1, data = mail.fetch(latest_email_id, "(RFC822)")
# Тело письма в необработанном виде
raw_email = data[0][1]
# Парсим сообщение
message = Parser(policy=default).parsestr(str(raw_email, 'UTF-8'))
# Получем тело сообщения (закодированное в base64)
message_body = message.get_body(preferencelist=('plain', 'html'));
# Получаем HTML содержимое тела сообщения
message_html_content = message_body.get_content()

# Выводим результат в консоль
print(message_html_content)






