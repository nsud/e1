import random

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']


def one(words):
    word = random.choice(words)
    return word


def mask(word):
    word_ = []
    str_ = f'{"-" * len(word)}' #    {word}'
    print(str_)
    for i in enumerate(word):
        word_.append(f'{i[0]}{i[1]}')
    d_ = dict(zip(word_, str_))
    return d_


def game_s(word, d_, a):
    for sym in enumerate(word):
        tmp = d_.get(f'{sym[0]}{sym[1]}')
        if tmp is not None and sym[1] == a:
            d_[f'{sym[0]}{sym[1]}'] = sym[1]
    str_ = jo(d_)
    print(str_)
    return str_


def jo(d_):
    str_ = ''
    for k, v in d_.items():
        str_ += v
    return str_


def common():
    fail = 0

    word = one(words)
    d_ = mask(word)
    while fail < 4:
        a = input('Угадай букву: ').lower()
        if a in word:
            str_ = game_s(word, d_, a)
            if '-' not in str_:
                print('WIN!!!')
                break
        else:
            fail += 1
            print(f'Начислено {fail} штрафных баллов')
    else:
        print('GAME OVER')

#main()
