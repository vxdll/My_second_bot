# Функции связанные с поиском информации в wikipedia
import wikipedia
import re
# Устанавливаем русский язык википедии
wikipedia.set_lang("ru")

# Функция на поиск из википедии

def wiki_search(mess):
    lst = wikipedia.search(mess)
    page = wikipedia.page(lst[0])
    title = page.title
    content = page.content[:500]
    content_2 = content.split('.')
    content_2 = content_2[:-1]
    new_text = ''
    for t in content_2:
        if not("==" in t):
            if(len((t.strip())) > 3):
                new_text = new_text + t + "."
        else:
            break
    new_text = re.sub('\([^()]*\)', '', new_text)
    new_text = re.sub('\([^()]*\)', '', new_text)
    new_text = re.sub('\{[^\{\}]*\}', '', new_text)
    link = page.url
    result = f"{title}\n {new_text}\n {link}"
    return result


