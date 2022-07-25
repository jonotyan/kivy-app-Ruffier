def ct(*message, **kwargs): #Форматирование текста в консоли (color(c), background(b), effect(e))
    """
    Каждый парамерт может быть равен от 0 до 7

    color;
    background;
    effect;
    """

    text = ''
    for key in kwargs:
        if key == 'color' or key == 'c':
            kwargs[key] = min(7, kwargs[key])
            text += f'\033[{kwargs[key]+30}m'
        elif key == 'background' or key == 'b':
            kwargs[key] = min(7, kwargs[key])
            text += f'\033[{kwargs[key]+40}m'
        elif key == 'effect' or key == 'e':
            kwargs[key] = min(7, kwargs[key])
            text += f'\033[{kwargs[key]}m'

    if len(message) > 1: #Пробелы
        for i in message:
            if message[len(message)-1] == i:
                text += i
            else:
                text += i + " "
    else:
        text += message[0]

    text += '\033[0m'
    return text