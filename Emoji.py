emoji = input(">").lower()

def emoji_indicator(emoji):
    listed = emoji.split(" ")
    # strr = str(listed)
    happy = False
    sad = False
    for i in listed:
        if 'sad' == i:
            sad = True
        elif 'happy' == i:
            happy = True
    # if 'sad' in strr :
    #     sad = True
    # elif 'happy' in strr:
    #     happy = True
    book = {
        'sad': '😢',
        'happy': '😊'
    }
    if sad:
        return book.get('sad')
    elif happy:
        return book.get('happy')

print(emoji_indicator(emoji))