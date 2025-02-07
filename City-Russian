from time import sleep
cheats = False
cites = 'x, Абзаково, Адлер, Азов, Александров, Алупка, Анапа, Архангельск, Астрахань, Барнаул, Белогорск, Белокуриха, Береговое, Благовещенск, Великий Новгород, Владивосток, Владикавказ, Волгоград, Вологда, Воронеж, Выборг, Вышний Волочек, Вязьма, Гаврилов Посад, Гаспра, Гатчина, Геленджик, Голубицкая, Горно-Алтайск, Городец, Горячий Ключ, Грозный, Гурзуф, Дагомыс, Дарасун, Дербент, Джанхот, Джемете, Джубга, Дивеево, Дивноморское, Дмитров, Должанская, Домбай, Евпатория, Ейск, Екатеринбург, Елабуга, Елец, Ессентуки, Железноводск, Зарайск, Звенигород, Зеленоградск, Золотое, Ивангород, Иваново, Ижевск, Избербаш, Иркутск, Истра, Йошкар-Ола, Казань, Калининград, Калуга, Калязин, Касимов, Каспийск, Кемерово, Керчь, Кинешма, Киров, Кировск, Кисловодск, Коктебель, Коломна, Кореиз, Кострома, Красная Поляна, Краснодар, Красноярск, Криница, Кронштадт, Кудепста, Курган, Курск, Кучугуры, Лазаревское, Лахденпохья, Лермонтово, Лоо, Магас, Майкоп, Манжерок, Марциальные Воды, Махачкала, Мацеста, Межводное, Мезмай, Мисхор, Мончегорск, Морское, Москва, Мурманск, Муром, Мысовое, Мышкин, Находка, Небуг, Нижний Новгород, Николаевка, Новая Анапа, Новая Евпатория, Новомихайловский, Новороссийск, Новосибирск, Новый Свет, Оленевка, Ольгинка, Омск, Орджоникидзе, Оренбург, Павловск, Палех, Паратунка, Партенит, Переделкино, Переславль-Залесский, Пересыпь, Пермь, Петергоф, Петрозаводск, Петропавловск-Камчатский, Плес, Поповка, Поселок За Родину, Поселок Ильич, Прасковеевка, Приморский, Приморско-Ахтарск, Приозерск, Псков, Пятигорск, Ржев, Ростов Великий, Ростов-на-Дону, Рыбачье, Рыбинск, Рязань, Саки, Самара, Санкт-Петербург, Саратов, Светлогорск, Свияжск, Севастополь, Семибалки, Сергиев Посад, Серпухов, Симеиз, Симферополь, Смоленск, Солнечногорское, Сортавала, Сочи, Ставрополь, Старая Ладога, Старая Русса, Старый Оскол, Судак, Суздаль, Сукко, Таганрог, Тамань, Таруса, Тверь, Темрюк, Териберка, Тобольск, Томск, Торжок, Туапсе, Тула, Тутаев, Тюмень, Углич, Улан-Удэ, Ульяновск, Уфа, Феодосия, Форос, Хабаровск, Ханты-Мансийск, Хоста, Царское Село, Чебоксары, Челябинск, Черноморское, Шепси, Шерегеш, Широкая Балка, Шлиссельбург, Штормовое, Шуя, Щелкино, Элиста, Эсто-Садок, Южная Озереевка, Южно-Сахалинск, Юрьев-Польский, Юрьевец, Ялта, Ярославль, Абакан, Александров, Алупка, Алушта, Анадырь, Анапа, Ангарск, Армавир, Архангельск, Астрахань, Ахтубинск, Балаклава, Балаково, Балашиха, Балтийск, Барнаул, Бахчисарай, Белгород, Белокуриха, Белорецк, Бийск, Благовещенск, Бологое, Братск, Брянск, Буйнакск, Валдай, Великие Луки, Великий Новгород, Великий Устюг, Верхотурье, Владивосток, Владикавказ, Владимир, Волгоград, Волгодонск, Вологда, Воркута, Воронеж, Выборг, Гатчина, Геленджик, Горно-Алтайск, Гороховец, Грозный, Гусев, Гусь-Хрустальный, Далматово, Дербент, Дзержинск, Дмитров, Долгопрудный, Дубна, Евпатория, Ейск, Екатеринбург, Елабуга, Ессентуки, Железноводск, Задонск, Звенигород, Зеленогорск, Зеленоградск, Златоуст, Иваново, Игарка, Ижевск, Иннополис, Иркутск, Истра, Йошкар-Ола, Казань, Калининград, Калуга, Калязин, Каспийск, Кемерово, Керчь, Кидекша, Киржач, Киров, Кисловодск, Клин, Ковров, Козельск, Коломна, Комсомольск-на-Амуре, Кострома, Красногорск, Краснодар, Красноярск, Кронштадт, Курган, Курск, Липецк, Магадан, Магас, Магнитогорск, Майкоп, Махачкала, Миасс, Минеральные Воды, Мирный, Мичуринск, Можайск, Москва,'
cites = cites.lower()
cites = cites.split(', ')
cites = set(cites)
cites = list(cites)
mistake = 0
ext = True
number = 1
last_messages = []
end_letter = ''
num = 0
def pro_bel():print('\n'*40)
if input('Если хотите пропустить описание нажмите Enter\nЕсли хотите прочитать описание нажмите что-нибудь: ') == '':
    pro_bel()
else:
    pro_bel()
    print('Это программа была создана для тренировки игры в города')
    sleep(2)
    print('Всего есть три вида ботов: Авто, Средний, Сложный')
    sleep(2)
    print('Авто 🙂 - играют боты')
    sleep(2)
    print('Средний 🤨 - бот рандомно отвечает')
    sleep(2)
    print('Сложный 😠 - бот отвечает так чтобы ты не выиграл(а)')
    sleep(2)
def if_is_difficult():
    global mistake
    mistake = 0
    if difficult == 'авто':pass
    elif difficult == 'средний': pass
    elif difficult == 'сложный':pass
    else:
        print('Ошибка!')
        mistake += 1
difficult = input('Напишите сложность бота: ')
difficult = difficult.lower()
if_is_difficult()
while mistake != 0:
    difficult = input('Напишите сложность бота: ')
    difficult = difficult.lower()
    if_is_difficult()
else:
    pro_bel()
print(f'Ваш(и) бот(ы): {difficult.capitalize()}')
true = True
last_messages.append(f'Ваш(и) бот(ы): {difficult.capitalize()}')
def answer_cite(cite):
    global ext
    global number
    global mistake
    global cites
    global end_letter
    global true
    if cite == 'x' and true:
        true = False
        if difficult == 'авто':
            end_letter = 'а'
        else:
            end_letter = ''
    cite = cite.lower()
    alphabet_cite_start = {}
    alphabet_cite_end = {}
    if cites.count(cite) == 1 or cite == 'x':
        mistake = 0
        cites.remove(cite)
        if cite[-1] == 'ь' or cite[-1] == 'ъ' or cite[-1] == 'ы':
            cite = list(cite)
            cite.pop(-1)
            cite = ''.join(cite)
        if cite == 'x':
            end_letter = ''
        for i in cites:
            if i[0] in alphabet_cite_start:
                alphabet_cite_start[i[0]].extend([i])
            else:
                alphabet_cite_start[i[0]] = [i]
            if i[-1] in alphabet_cite_end:
                alphabet_cite_end[i[-1]].extend([i])
            else:
                alphabet_cite_end[i[-1]] = [i]
        if cite[0] == end_letter or end_letter == '':
            if end_letter == '' and difficult == 'авто':
                end_letter = 'а'
            else:
                if end_letter == 'ь' or end_letter == 'ъ' and end_letter == 'ы':
                    end_letter = cite[-2]
                else:
                    end_letter = cite[-1]
            if difficult == 'авто':
                sleep(0.8)
                if end_letter in alphabet_cite_start:
                    if len(alphabet_cite_start[end_letter]) != 0:
                        print(f'Бот-авто №{number} придумал: {alphabet_cite_start[end_letter][0].title()}')
                else:
                    print(f'Бот-авто №{number} проиграл 😥')
                    ext = False
                if end_letter in alphabet_cite_start.keys():
                    word = alphabet_cite_start[end_letter][0].lower()
                    if type(alphabet_cite_start[end_letter]) == type(''):
                        word = alphabet_cite_start[end_letter].lower()
                else:
                    word = ''
                if number == 2:
                    number = 1
                else:
                    number += 1
                if ext:
                    answer_cite(word)
            elif difficult == 'средний':
                ot_vet = ''
                mistake = 1
                if end_letter == 'x':
                    end_letter = ''
                pro_ver_ka = True
                if end_letter != '':
                    if end_letter not in alphabet_cite_start:
                        mistake = 3
                while mistake != 0 and mistake != 3:
                    if mistake == 1 and pro_ver_ka:
                        mistake = 0
                        pro_ver_ka = False
                    if end_letter != '':
                        if cheats:
                            alphabet_end_letter = alphabet_cite_start[end_letter]
                            alphabet_end_letter = ' '.join(alphabet_end_letter)
                            print('\nХакер 🥸: Вот ваши варианты\n')
                            print(alphabet_end_letter)
                        ot_vet = input(f'Напишите город на букву - "{end_letter.title()}": ')
                        ot_vet = ot_vet.lower()
                    else:
                        ot_vet = input(f'Напишите город на любую букву: ')
                        ot_vet = ot_vet.lower()
                    mistake += 1
                    if ot_vet in cites:
                        if ot_vet[0] == end_letter or end_letter == '':
                            mistake = 0
                            if ot_vet[-1] == 'ь' or ot_vet[-1] == 'ъ' and ot_vet[-1] == 'ы':
                                end_letter = ot_vet[-2]
                            else:
                                end_letter = ot_vet[-1]
                            last_messages.append(f'Вы: {ot_vet.title()}')
                            for i in last_messages:
                                print(i)
                    if mistake != 0:
                        if mistake != 3:
                            print(f'Осталось попыток ☹️: {3-mistake}')
                else:
                    if not ot_vet in cites:
                        print('Вы проиграли 😥')
                    else:
                        cites.remove(ot_vet)
                        alphabet_cite_start = {}
                        alphabet_cite_end = {}
                        for i in cites:
                            if i[0] in alphabet_cite_start:
                                old_cite_start = alphabet_cite_start[i[0]]
                                if i in alphabet_cite_start.keys():
                                    alphabet_cite_start[i[0]].extend([i, old_cite_start])
                                else:
                                    alphabet_cite_start[i[0]] = [i, old_cite_start]
                            else:
                                alphabet_cite_start[i[0]] = i
                            if i[-1] in alphabet_cite_end:
                                old_cite_end = alphabet_cite_end[i[-1]]
                                if i in alphabet_cite_end.keys():
                                    alphabet_cite_end[i[-1]].extend([i, old_cite_end])
                                else:
                                    alphabet_cite_end[i[-1]] = [i, old_cite_end]
                            else:
                                alphabet_cite_end[i[-1]] = i
                    if mistake == 0:
                        pro_bel()
                    if end_letter in alphabet_cite_start:
                        last_messages.append(f'Бот-средний 🤨: {alphabet_cite_start[end_letter][0].title()}')
                        pro_bel()
                        for i in last_messages:
                            print(i)
                    else:
                        if mistake == 0:
                            print(f'Вы выиграли 🙂')
                        ext = False
                    if end_letter in alphabet_cite_start.keys():
                        word = alphabet_cite_start[end_letter][0].lower()
                        if type(alphabet_cite_start[end_letter]) == type(''):
                            word = alphabet_cite_start[end_letter].lower()
                    else:
                        word = ''
                    if ext:
                        answer_cite(word)
            elif difficult == 'сложный':
                ot_vet = ''
                mistake = 1
                if end_letter == 'x':
                    end_letter = ''
                pro_ver_ka = True
                if end_letter != '':
                    if end_letter not in alphabet_cite_start:
                        mistake = 3
                        ot_vet = 'x'
                while mistake != 0 and mistake != 3:
                    if mistake == 1 and pro_ver_ka:
                        mistake = 0
                        pro_ver_ka = False
                    if end_letter != '':
                        if cheats:
                            alphabet_end_letter = alphabet_cite_start[end_letter]
                            alphabet_end_letter = ' '.join(alphabet_end_letter)
                            print('\nХакер 🥸: Вот ваши варианты\n')
                            print(alphabet_end_letter)
                        ot_vet = input(f'Напишите город на букву - "{end_letter.title()}": ')
                        ot_vet = ot_vet.lower()
                    else:
                        ot_vet = input(f'Напишите город на любую букву: ')
                        ot_vet = ot_vet.lower()
                    mistake += 1
                    if ot_vet in cites:
                        if ot_vet[0] == end_letter or end_letter == '':
                            mistake = 0
                            if ot_vet[-1] == 'ь' or ot_vet[-1] == 'ъ' and ot_vet[-1] == 'ы':
                                end_letter = ot_vet[-2]
                            else:
                                end_letter = ot_vet[-1]
                            last_messages.append(f'Вы: {ot_vet.title()}')
                            for i in last_messages:
                                print(i)
                    if mistake != 0:
                        if mistake != 3:
                            print(f'Осталось попыток ☹️: {3 - mistake}')
                else:
                    if not ot_vet in cites:
                        print('Вы проиграли 😥')
                    else:
                        cites.remove(ot_vet)
                        alphabet = {'а': [], 'б': [], 'в': [], 'г': [], 'д': [], 'е': [], 'ё': [], 'ж': [],
                                    'з': [], 'и': [], 'й': [], 'к': [], 'л': [], 'м': [], 'н': [], 'о': [],
                                    'п': [], 'р': [], 'с': [], 'т': [], 'у': [], 'ф': [], 'х': [], 'ц': [],
                                    'ч': [], 'ш': [], 'щ': [], 'ъ': [], 'ы': [], 'ь': [], 'э': [], 'ю': [],
                                    'я': []}
                        alphabet_for = {'а': [], 'б': [], 'в': [], 'г': [], 'д': [], 'е': [], 'ё': [], 'ж': [],
                                    'з': [], 'и': [], 'й': [], 'к': [], 'л': [], 'м': [], 'н': [], 'о': [],
                                    'п': [], 'р': [], 'с': [], 'т': [], 'у': [], 'ф': [], 'х': [], 'ц': [],
                                    'ч': [], 'ш': [], 'щ': [], 'ъ': [], 'ы': [], 'ь': [], 'э': [], 'ю': [],
                                    'я': []}
                        alphabet_end_letter_end = []
                        if end_letter not in alphabet_cite_start:
                            print('Вы выиграли 🙂')
                        else:
                            alphabet_end_letter = alphabet_cite_start[end_letter]
                            alphabet_cite_end = {}
                            for i in alphabet_end_letter:
                                if i[-1] in alphabet_cite_end:
                                    if i[-1] == 'ь' or i[-1] == 'ы' or i[-1] == 'ъ':
                                        alphabet_cite_end[i[-2]].extend([i])
                                    else:
                                        alphabet_cite_end[i[-1]].extend([i])
                                else:
                                    if i[-1] == 'ь' or i[-1] == 'ы' or i[-1] == 'ъ':
                                        alphabet_cite_end[i[-2]] = [i]
                                    else:
                                        alphabet_cite_end[i[-1]] = [i]
                            for i in alphabet_end_letter:
                                if i[-1] == 'ь' or i[-1] == 'ы' or i[-1] == 'ъ':
                                    alphabet_end_letter_end.append(i[-2])
                                else:
                                    alphabet_end_letter_end.append(i[-1])
                            for i in alphabet_for:
                                if i not in alphabet_end_letter_end:
                                    alphabet.pop(i)
                            for i in alphabet_end_letter:
                                if i[-1] in alphabet_cite_start.keys():
                                    alphabet[i[-1]].extend(alphabet_cite_start[i[-1]])
                            for i in alphabet:
                                alphabet[i] = len(alphabet[i])
                            minimum = min(alphabet.values())
                            word = ''
                            word_hard = ''
                            for i in alphabet:
                                if alphabet[i] == minimum:
                                    word = i
                            if len(alphabet_end_letter) != 0:
                                last_messages.append(f'Бот-сложный 😠: {alphabet_cite_end[word][0].title()}')
                                print(f'Бот-сложный 😠: {alphabet_cite_end[word][0].title()}')
                                word_hard = alphabet_cite_end[word][0]
                            else:
                                if mistake == 0:
                                    print(f'Вы выиграли 🙂')
                                ext = False
                            if ext:
                                answer_cite(word_hard)
        else:
            print('Ошибка!')
    else:
        print('Ошибка!')
answer_cite('x')
