from random import *

# Список вариантов ответа.
answer_lst = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
              'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
              'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
              'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
              'Перспективы не очень хорошие', 'Весьма сомнительно']

shuffle(answer_lst)  # Перемешаем для более случайного выбора.

# Приветствие.
print('Привет, Мир! Я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как мне называть тебя? \n')
print(f'Приветствую, {name}!')

# Алгоритм программы.
while True:
    input('Задай свой вопрос. \n')
    print(choice(answer_lst))
    question = input('У тебя ещё остались вопросы? (Да / Нет) \n')
    if question.lower() == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
