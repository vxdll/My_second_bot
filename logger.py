# Логирование
def log(message):
    file = open('bd.txt', 'a')
    file.write(f"{message.from_user.first_name}, {message.from_user.last_name}, {message.text}, {message.answer}\n")
    file.close()

