from time import sleep
cheats = False
sticker = '😊'
cites = 'x, Абзаково, Адлер, Азов, Александров, Алупка, Анапа, Архангельск, Астрахань, Барнаул, Белогорск, Белокуриха, Береговое, Благовещенск, Великий Новгород, Владивосток, Владикавказ, Волгоград, Вологда, Воронеж, Выборг, Вышний Волочек, Вязьма, Гаврилов Посад, Гаспра, Гатчина, Геленджик, Голубицкая, Горно-Алтайск, Городец, Горячий Ключ, Грозный, Гурзуф, Дагомыс, Дарасун, Дербент, Джанхот, Джемете, Джубга, Дивеево, Дивноморское, Дмитров, Должанская, Домбай, Евпатория, Ейск, Екатеринбург, Елабуга, Елец, Ессентуки, Железноводск, Зарайск, Звенигород, Зеленоградск, Золотое, Ивангород, Иваново, Ижевск, Избербаш, Иркутск, Истра, Йошкар-Ола, Казань, Калининград, Калуга, Калязин, Касимов, Каспийск, Кемерово, Керчь, Кинешма, Киров, Кировск, Кисловодск, Коктебель, Коломна, Кореиз, Кострома, Красная Поляна, Краснодар, Красноярск, Криница, Кронштадт, Кудепста, Курган, Курск, Кучугуры, Лазаревское, Лахденпохья, Лермонтово, Лоо, Магас, Майкоп, Манжерок, Марциальные Воды, Махачкала, Мацеста, Межводное, Мезмай, Мисхор, Мончегорск, Морское, Москва, Мурманск, Муром, Мысовое, Мышкин, Находка, Небуг, Нижний Новгород, Николаевка, Новая Анапа, Новая Евпатория, Новомихайловский, Новороссийск, Новосибирск, Новый Свет, Оленевка, Ольгинка, Омск, Орджоникидзе, Оренбург, Павловск, Палех, Паратунка, Партенит, Переделкино, Переславль-Залесский, Пересыпь, Пермь, Петергоф, Петрозаводск, Петропавловск-Камчатский, Плес, Поповка, Поселок За Родину, Поселок Ильич, Прасковеевка, Приморский, Приморско-Ахтарск, Приозерск, Псков, Пятигорск, Ржев, Ростов Великий, Ростов-на-Дону, Рыбачье, Рыбинск, Рязань, Саки, Самара, Санкт-Петербург, Саратов, Светлогорск, Свияжск, Севастополь, Семибалки, Сергиев Посад, Серпухов, Симеиз, Симферополь, Смоленск, Солнечногорское, Сортавала, Сочи, Ставрополь, Старая Ладога, Старая Русса, Старый Оскол, Судак, Суздаль, Сукко, Таганрог, Тамань, Таруса, Тверь, Темрюк, Териберка, Тобольск, Томск, Торжок, Туапсе, Тула, Тутаев, Тюмень, Углич, Улан-Удэ, Ульяновск, Уфа, Феодосия, Форос, Хабаровск, Ханты-Мансийск, Хоста, Царское Село, Чебоксары, Челябинск, Черноморское, Шепси, Шерегеш, Широкая Балка, Шлиссельбург, Штормовое, Шуя, Щелкино, Элиста, Эсто-Садок, Южная Озереевка, Южно-Сахалинск, Юрьев-Польский, Юрьевец, Ялта, Ярославль, Абакан, Александров, Алупка, Алушта, Анадырь, Анапа, Ангарск, Армавир, Архангельск, Астрахань, Ахтубинск, Балаклава, Балаково, Балашиха, Балтийск, Барнаул, Бахчисарай, Белгород, Белокуриха, Белорецк, Бийск, Благовещенск, Бологое, Братск, Брянск, Буйнакск, Валдай, Великие Луки, Великий Новгород, Великий Устюг, Верхотурье, Владивосток, Владикавказ, Владимир, Волгоград, Волгодонск, Вологда, Воркута, Воронеж, Выборг, Гатчина, Геленджик, Горно-Алтайск, Гороховец, Грозный, Гусев, Гусь-Хрустальный, Далматово, Дербент, Дзержинск, Дмитров, Долгопрудный, Дубна, Евпатория, Ейск, Екатеринбург, Елабуга, Ессентуки, Железноводск, Задонск, Звенигород, Зеленогорск, Зеленоградск, Златоуст, Иваново, Игарка, Ижевск, Иннополис, Иркутск, Истра, Йошкар-Ола, Казань, Калининград, Калуга, Калязин, Каспийск, Кемерово, Керчь, Кидекша, Киржач, Киров, Кисловодск, Клин, Ковров, Козельск, Коломна, Комсомольск-на-Амуре, Кострома, Красногорск, Краснодар, Красноярск, Кронштадт, Курган, Курск, Липецк, Магадан, Магас, Магнитогорск, Майкоп, Махачкала, Миасс, Минеральные Воды, Мирный, Мичуринск, Можайск, Москва,'
names = ['Аарон', 'Абрам', 'Аваз', 'Аввакум', 'Август', 'Августа', 'Августин', 'Августина', 'Авдей', 'Авдий', 'Авдотья', 'Авигея', 'Авксентий', 'Авраам', 'Аврор', 'Аврора', 'Автандил', 'Автоноя', 'Агап', 'Агапия', 'Агата', 'Агафон', 'Агафья', 'Аггей', 'Аглая', 'Агнес', 'Агнесса', 'Агнета', 'Агния', 'Агриппина', 'Агунда', 'Ада', 'Адам', 'Аделаида', 'Аделина', 'Аделия', 'Адель', 'Адельфина', 'Адиля', 'Адис', 'Адольф', 'Адриан', 'Адриана', 'Адриенна', 'Аза', 'Азалия', 'Азамат', 'Азарий', 'Азат', 'Азиза', 'Аида', 'Айганым', 'Айгерим', 'Айгуль', 'Айдар', 'Айжан', 'Айлин', 'Айнагуль', 'Айнур', 'Айрат', 'Акакий', 'Аким', 'Аксён', 'Аксинья', 'Акулина', 'Алан', 'Алана', 'Алдона', 'Алевтин', 'Алевтина', 'Александр', 'Александра', 'Александрина', 'Алексей', 'Алексий', 'Ален', 'Алёна', 'Алеся', 'Али', 'Алика', 'Алико', 'Алима', 'Алина', 'Алира', 'Алиса', 'Алихан', 'Алия', 'Алла', 'Алмаз', 'Алоис', 'Алсу', 'Алтжин', 'Альба', 'Альберт', 'Альберта', 'Альбина', 'Альвиан', 'Альвина', 'Альжбета', 'Альфия', 'Альфред', 'Альфреда', 'Аля', 'Амадей', 'Амадеус', 'Амалия', 'Амаль', 'Аманда', 'Амаяк', 'Амвросий', 'Амелия', 'Амин', 'Амина', 'Амира', 'Анаис', 'Анаит', 'Анастасий', 'Анастасия', 'Анатолий', 'Анвар', 'Ангел', 'Ангелина', 'Андоим', 'Андрей', 'Андриана', 'Андрон', 'Андрэ', 'Анеля', 'Анжей', 'Анжела', 'Анжелика', 'Анжиолетта', 'Аникита', 'Анисим', 'Анисия', 'Анисья', 'Анита', 'Анна', 'Антип', 'Антон', 'Антонин', 'Антонина', 'Ануфрий', 'Анфим', 'Анфиса', 'Анэля', 'Аполлинарий', 'Аполлинария', 'Аполлония', 'Апполинарий', 'Арабелла', 'Арам', 'Ариадна', 'Ариана', 'Арий', 'Арина', 'Аристарх', 'Аркадий', 'Арман', 'Армен', 'Арно', 'Арнольд', 'Арон', 'Арсен', 'Арсений', 'Арслан', 'Артамон', 'Артем', 'Артемида', 'Артемий', 'Артур', 'Архелия', 'Архип', 'Архипп', 'Арье', 'Арьяна', 'Асель', 'Асида', 'Асия', 'Аскольд', 'Ассоль', 'Астра', 'Астрид', 'Ася', 'Аурелия', 'Афанасий', 'Афанасия', 'Афиноген', 'Ахмет', 'Ашот', 'Аэлита', 'Аюна', 'Бажена', 'Бахрам', 'Беата', 'Беатриса', 'Бежен', 'Белинда', 'Белла', 'Бенедикт', 'Бенедикта', 'Берек', 'Береслава', 'Бернар', 'Берта', 'Биргит', 'Бирута', 'Богдан', 'Богдана', 'Боголюб', 'Божена', 'Болеслав', 'Бонифаций', 'Бореслав', 'Борис', 'Борислав', 'Борислава', 'Боян', 'Бриллиант', 'Бронислав', 'Бронислава', 'Бруно', 'Булат', 'Вадим', 'Валентин', 'Валентина', 'Валерий', 'Валерия', 'Валерьян', 'Вальдемар', 'Вальтер', 'Ванда', 'Ванесса', 'Варвара', 'Вардан', 'Варлаам', 'Варлам', 'Варфоломей', 'Василий', 'Василина', 'Василиса', 'Васса', 'Ватслав', 'Вацлав', 'Велизар', 'Велимир', 'Велор', 'Венди', 'Венедикт', 'Венера', 'Вениамин', 'Вера', 'Верона', 'Вероника', 'Версавия', 'Веселина', 'Весна', 'Весняна', 'Веста', 'Вета', 'Ветта', 'Вида', 'Видана', 'Викентий', 'Виктор', 'Викторина', 'Виктория', 'Вилен', 'Вилена', 'Вилли', 'Вилора', 'Вильгельм', 'Винетта', 'Виоланта', 'Виолетта', 'Виргиния', 'Виринея', 'Виссарион', 'Вита', 'Виталий', 'Виталина', 'Витаутас', 'Витольд', 'Влад', 'Влада', 'Владимир', 'Владислав', 'Владислава', 'Владлен', 'Владлена', 'Влас', 'Власий', 'Властилина', 'Володар', 'Вольдемар', 'Всеволод', 'Вячеслав', 'Габи', 'Габриеле', 'Габриэлла', 'Гавриил', 'Гаврила', 'Гай', 'Гайдар', 'Галактион', 'Галина', 'Галия', 'Гамлет', 'Гарри', 'Гаспар', 'Гастон', 'Гаянэ', 'Гаяс', 'Гевор', 'Геворг', 'Гелана', 'Геласий', 'Гелена', 'Гелианна', 'Гелла', 'Гений', 'Геннадий', 'Генри', 'Генриетта', 'Генрих', 'Георгий', 'Георгина', 'Гера', 'Геральд', 'Герасим', 'Герда', 'Герман', 'Гермоген', 'Гертруда', 'Глафира', 'Глеб', 'Гликерия', 'Глория', 'Гоар', 'Говхар', 'Гордей', 'Гордон', 'Горислав', 'Горица', 'Гортензия', 'Градимир', 'Гражина', 'Граф', 'Грета', 'Григорий', 'Гузель', 'Гулия', 'Гульмира', 'Гульназ', 'Гульнара', 'Гульшат', 'Гуннхильда', 'Гурий', 'Густав', 'Гюзель', 'Гюльджан', 'Давид', 'Давлат', 'Давыд', 'Дайна', 'Далия', 'Дамиан', 'Дамир', 'Дамира', 'Дан', 'Дана', 'Даниил', 'Данила', 'Данислав', 'Даниэла', 'Дания', 'Данна', 'Данута', 'Даньяр', 'Дар', 'Дара', 'Дарерка', 'Дарина', 'Дария', 'Дарья', 'Дарьяна', 'Даша', 'Даяна', 'Дебора', 'Дементий', 'Демид', 'Демократ', 'Демьян', 'Денис', 'Джамал', 'Джамиля', 'Джанет', 'Джеймс', 'Джема', 'Джемма', 'Дженифер', 'Дженна', 'Дженнифер', 'Джереми', 'Джессика', 'Джоан', 'Джозеф', 'Джордан', 'Джорж', 'Джулия', 'Джульетта', 'Диана', 'Дидим', 'Дик', 'Дилара', 'Дильназ', 'Дильнара', 'Диля', 'Димитрий', 'Дин', 'Дина', 'Динар', 'Динара', 'Динасий', 'Динора', 'Диодора', 'Диомид', 'Дионисия', 'Дита', 'Диша', 'Дмитрий', 'Добрыня', 'Долорес', 'Доля', 'Доминика', 'Домна', 'Дональд', 'Донат', 'Донатос', 'Дора', 'Дорофей', 'Дэнна', 'Ева', 'Евангелина', 'Евгений', 'Евгения', 'Евграф', 'Евдоким', 'Евдокия', 'Евлампий', 'Евлогий', 'Евпраксия', 'Евсей', 'Евстафий', 'Евфимия', 'Егор', 'Екатерина', 'Елеазар', 'Елена', 'Елизавета', 'Елизар', 'Елисей', 'Емельян', 'Епифан', 'Еремей', 'Ермак', 'Ермил', 'Ермиония', 'Ермолай', 'Ерофей', 'Есения', 'Ефим', 'Ефимий', 'Ефимия', 'Ефрем', 'Жаклин', 'Жан', 'Жанетт', 'Жанна', 'Жасмин', 'Ждан', 'Женевьева', 'Жерар', 'Жозефина', 'Жорж', 'Жюли', 'Забава', 'Заира', 'Закир', 'Залина', 'Замир', 'Замира', 'Зара', 'Зарема', 'Зарина', 'Заур', 'Захар', 'Захария', 'Земфира', 'Зенон', 'Зигмунд', 'Зинаида', 'Зиновий', 'Зита', 'Злата', 'Златослава', 'Зорий', 'Зоряна', 'Зосима', 'Зот', 'Зоя', 'Зульфия', 'Зураб', 'Зухра', 'Иакинф', 'Ибрагим', 'Иван', 'Иванна', 'Ивета', 'Иветта', 'Ивона', 'Игнат', 'Игнатий', 'Игорь', 'Ида', 'Иероним', 'Изабелла', 'Измаил', 'Изольда', 'Израиль', 'Изяслав', 'Иларион', 'Илария', 'Илена', 'Илзе', 'Илиан', 'Илиана', 'Илларион', 'Илона', 'Ильзе', 'Ильхам', 'Ильшат', 'Илья', 'Ильяс', 'Инара', 'Инга', 'Инге', 'Ингеборга', 'Индира', 'Инесса', 'Инна', 'Иннокентий', 'Инокентий', 'Иоаким', 'Иоанн', 'Иоанна', 'Иоланта', 'Ион', 'Ионас', 'Ионос', 'Иосиф', 'Ипполит', 'Ираида', 'Ираклий', 'Ирена', 'Иржи', 'Ирина', 'Ириней', 'Ириний', 'Ирма', 'Ирэн', 'Ирэна', 'Иса', 'Исаак', 'Исаакий', 'Исай', 'Исайя', 'Исидор', 'Искандер', 'Искра', 'Ислам', 'Исмаил', 'Иулиан', 'Иулия', 'Июлий', 'Июлия', 'Ия', 'Йенни', 'Казбек', 'Казимир', 'Кай', 'Кайли', 'Калерия', 'Камилла', 'Камиль', 'Камиля', 'Капитолина', 'Капитон', 'Кара', 'Карен', 'Карим', 'Карима', 'Карина', 'Карл', 'Карла', 'Кармелитта', 'Каролина', 'Каспар', 'Касьян', 'Катарина', 'Каторина', 'Келен', 'Ким', 'Кир', 'Кира', 'Кирилл', 'Кирилла', 'Клавдий', 'Клавдия', 'Клара', 'Клариса', 'Кларисса', 'Клаус', 'Клемент', 'Клементий', 'Клементина', 'Клим', 'Климент', 'Климентина', 'Клод', 'Кондрат', 'Кондратий', 'Конкордий', 'Конрад', 'Константин', 'Констанция', 'Консуэло', 'Кора', 'Корней', 'Корнелия', 'Корнилий', 'Краснослав', 'Крис', 'Кристина', 'Ксаннф', 'Ксения', 'Кузьма', 'Куприян', 'Лавр', 'Лаврентий', 'Лада', 'Лазарь', 'Лайма', 'Лали', 'Ламия', 'Лана', 'Ландыш', 'Лаодика', 'Лара', 'Ларион', 'Лариса', 'Лаура', 'Лев', 'Леван', 'Левон', 'Лейла', 'Лейсан', 'Леля', 'Ленар', 'Леокадия', 'Леон', 'Леонард', 'Леонид', 'Леонида', 'Леонтий', 'Леопольд', 'Лера', 'Лермонт', 'Леся', 'Лея', 'Лиана', 'Лигия', 'Лидия', 'Лиза', 'Лика', 'Лили', 'Лилиана', 'Лилия', 'Лилу', 'Лина', 'Линда', 'Линнея', 'Лиора', 'Лира', 'Лис', 'Лия', 'Лола', 'Лолита', 'Лора', 'Луиза', 'Лука', 'Лукерья', 'Лукий', 'Лукия', 'Лукьян', 'Лунара', 'Любава', 'Любим', 'Любовь', 'Любомила', 'Любомир', 'Людвиг', 'Людмила', 'Людовика', 'Люсьен', 'Люций', 'Люция', 'Ляля', 'Мавлюда', 'Магали', 'Магда', 'Магдалина', 'Магистриан', 'Мадина', 'Мадлен', 'Май', 'Майкл', 'Майя', 'Макар', 'Макарий', 'Макс', 'Максим', 'Максимилиан', 'Максимильян', 'Максуд', 'Малика', 'Мальвина', 'Мальта', 'Мансур', 'Мануил', 'Мар', 'Мара', 'Марат', 'Маргарет', 'Маргарита', 'Мариан', 'Марианна', 'Марика', 'Марин', 'Марина', 'Мариса', 'Марисоль', 'Мариша', 'Мария', 'Марк', 'Маркел', 'Марлен', 'Марс', 'Марселина', 'Марсель', 'Марта', 'Мартин', 'Мартина', 'Мартын', 'Маруся', 'Марфа', 'Марьям', 'Марьяна', 'Мастридия', 'Матвей', 'Матильда', 'Матрёна', 'Мафтуха', 'Махмуд', 'Мелания', 'Мелентий', 'Мелиана', 'Мелисса', 'Мелитта', 'Мераб', 'Мериса', 'Мефодий', 'Мечеслав', 'Мечислав', 'Мика', 'Микула', 'Мила', 'Милад', 'Милада', 'Милан', 'Милана', 'Милда', 'Милен', 'Милена', 'Милиса', 'Милица', 'Милолика', 'Милослав', 'Милослава', 'Мир', 'Мира', 'Мирдза', 'Мирей', 'Мирон', 'Миропия', 'Мирослав', 'Мирослава', 'Мирра', 'Мисаил', 'Митрофан', 'Митя', 'Михаил', 'Михайлина', 'Михримах', 'Мичлов', 'Мишель', 'Мишлов', 'Мия', 'Мод', 'Модест', 'Моисей', 'Моник', 'Моника', 'Мстислав', 'Муза', 'Мурат', 'Муслим', 'Мухаммед', 'Мэдисон', 'Мэлор', 'Мэри', 'Мю', 'Надежда', 'Наджия', 'Надия', 'Надя', 'Назар', 'Назарий', 'Назгуль', 'Назира', 'Наиль', 'Наиля', 'Наима', 'Нана', 'Нания', 'Наоми', 'Наталия', 'Наталья', 'Наташа', 'Натан', 'Нателла', 'Наум', 'Нева', 'Нега', 'Нелли', 'Неолина', 'Неонил', 'Неонила', 'Неонилла', 'Нестор', 'Ника', 'Никанор', 'Никита', 'Никифор', 'Никки', 'Никодим', 'Никола', 'Николай', 'Николетта', 'Николь', 'Никон', 'Нил', 'Нила', 'Нилуфар', 'Нильс', 'Нина', 'Нинель', 'Нинна', 'Нисон', 'Нифонт', 'Ноа', 'Новомир', 'Номи', 'Нонна', 'Нора', 'Норман', 'Норманн', 'Нурия', 'Нэнси', 'Овидий', 'Одетта', 'Оксана', 'Октавия', 'Октябрина', 'Октябрь', 'Олан', 'Олег', 'Олесь', 'Олеся', 'Оливия', 'Олимпиада', 'Ольга', 'Ольгерд', 'Онисим', 'Онуфрий', 'Орест', 'Орландо', 'Осип', 'Оскар', 'Остап', 'Остромир', 'Офелия', 'Павел', 'Павла', 'Павлина', 'Памела', 'Памфил', 'Панкрат', 'Пантелеймон', 'Панфил', 'Парамон', 'Парфений', 'Патрисия', 'Патриция', 'Пахом', 'Пелагея', 'Пересвет', 'Перизат', 'Петр', 'Пимен', 'Платон', 'Полианна', 'Полина', 'Порфирий', 'Потап', 'Прасковья', 'Прозор', 'Прокопий', 'Прокофий', 'Протасий', 'Прохор', 'Равиль', 'Рада', 'Радий', 'Радик', 'Радислав', 'Радмила', 'Радомир', 'Радосвета', 'Радослав', 'Радослава', 'Разиль', 'Разумник', 'Раис', 'Раиса', 'Райан', 'Раймонд', 'Ралина', 'Рамазан', 'Рамиз', 'Рамиль', 'Рамина', 'Рамон', 'Ранель', 'Расим', 'Расул', 'Ратибор', 'Ратмир', 'Рафаил', 'Рафаэль', 'Рафик', 'Рашид', 'Рая', 'Ревекка', 'Регина', 'Рем', 'Рема', 'Рената', 'Ренольд', 'Риана', 'Римма', 'Рина', 'Ринат', 'Рита', 'Рифат', 'Рихард', 'Ричард', 'Роберт', 'Роберта', 'Рогнеда', 'Родион', 'Роза', 'Розалина', 'Розалия', 'Роксалана', 'Роксана', 'Ролан', 'Роман', 'Романа', 'Ростислав', 'Ростислава', 'Рубен', 'Рудольф', 'Рузалия', 'Рузанна', 'Рузиля', 'Румия', 'Русалина', 'Руслан', 'Руслана', 'Рустам', 'Руфин', 'Руфина', 'Рушан', 'Рэй', 'Сабина', 'Сабир', 'Сабрина', 'Савва', 'Савел', 'Савелий', 'Сажида', 'Саида', 'Саломея', 'Самвел', 'Самира', 'Самсон', 'Самуил', 'Санда', 'Сандра', 'Сания', 'Санта', 'Сара', 'Сарра', 'Сати', 'Сафина', 'Свет', 'Светлан', 'Светлана', 'Светозар', 'Светослав', 'Святогор', 'Святополк', 'Святослав', 'Святослава', 'Севара', 'Севастьян', 'Север', 'Северин', 'Северина', 'Северьян', 'Селена', 'Семен', 'Серафим', 'Серафима', 'Сергей', 'Сидор', 'Силика', 'Сильва', 'Сильвестр', 'Сильвия', 'Сима', 'Симона', 'Слава', 'Снежана', 'Созия', 'Созон', 'Сократ', 'Соломон', 'Соня', 'София', 'Софья', 'Спартак', 'Спиридон', 'Стакрат', 'Сталий', 'Станимир', 'Станислав', 'Станислава', 'Стелла', 'Степан', 'Стефан', 'Стефания', 'Стивен', 'Стоян', 'Султан', 'Сусанна', 'Тагир', 'Таира', 'Таис', 'Таисия', 'Тайлер', 'Тала', 'Талик', 'Тамаз', 'Тамара', 'Тамерлан', 'Тамила', 'Тара', 'Тарас', 'Татьяна', 'Тельман', 'Тельнан', 'Теодор', 'Теодора', 'Тереза', 'Терентий', 'Тибор', 'Тиграм', 'Тигран', 'Тигрий', 'Тимон', 'Тимофей', 'Тимур', 'Тина', 'Тит', 'Тихомир', 'Тихон', 'Томас', 'Томила', 'Тора', 'Триана', 'Трифон', 'Трофим', 'Тунгуз', 'Ульманас', 'Ульяна', 'Умар', 'Урсула', 'Устин', 'Устина', 'Устинья', 'Фаддей', 'Фадей', 'Фазиль', 'Фаиза', 'Фаина', 'Фанис', 'Фания', 'Фаня', 'Фарид', 'Фарида', 'Фархад', 'Фатима', 'Фая', 'Федор', 'Федосей', 'Федот', 'Фекла', 'Феликс', 'Фелиция', 'Феодосии', 'Феодосий', 'Фердинанд', 'Феруза', 'Фидель', 'Физура', 'Филат', 'Филимон', 'Филипп', 'Флора', 'Флорентий', 'Фома', 'Франсуаза', 'Франц', 'Француаза', 'Фред', 'Фредерика', 'Фрида', 'Фридрих', 'Фрол', 'Фуад', 'Хабиб', 'Хаким', 'Харита', 'Харитон', 'Хилари', 'Хильда', 'Хлоя', 'Христиан', 'Христина', 'Христос', 'Христофор', 'Христя', 'Цветана', 'Цезарь', 'Цецилия', 'Чарльз', 'Челси', 'Чеслав', 'Чеслава', 'Чингиз', 'Чингисхан', 'Чулпан', 'Шакира', 'Шамиль', 'Шарлотта', 'Шарль', 'Шейла', 'Шелли', 'Шерил', 'Шерлок', 'Шота', 'Щеголь', 'Эвелина', 'Эвита', 'Эдвард', 'Эдгар', 'Эдда', 'Эдита', 'Эдмунд', 'Эдуард', 'Элеонора', 'Элиана', 'Элиза', 'Элина', 'Элла', 'Эллада', 'Элоиза', 'Эльвина', 'Эльвира', 'Эльга', 'Эльдар', 'Эльза', 'Эльмира', 'Эльнара', 'Эля', 'Эмили', 'Эмилия', 'Эмиль', 'Эмин', 'Эмма', 'Эммануил', 'Эраст', 'Эрик', 'Эрика', 'Эрнест', 'Эрнестина', 'Эсмеральда', 'Этель', 'Этери', 'Юзефа', 'Юлиан', 'Юлий', 'Юлия', 'Юна', 'Юния', 'Юнона', 'Юнус', 'Юрий', 'Юстин', 'Юханна', 'Юхим', 'Ядвига', 'Яким', 'Яков', 'Якун', 'Ян', 'Яна', 'Янина', 'Янита', 'Янка', 'Януарий', 'Ярина', 'Яромир', 'Ярослав', 'Ярослава', 'Ясмина', 'Ясон']
cites = cites.lower()
cites = cites.split(', ')
cites = set(cites)
cites = list(cites)
def name_pro_ver_ka():
    global name
    if name not in names:
        print('Ошибка!')
        name = input('Напишите своё имя 📝: ')
        name = name.capitalize()
        name_pro_ver_ka()
name = input('Напишите своё имя 📝: ')
name = name.capitalize()
name_pro_ver_ka()
mistake = 0
word_hard = ''
ext = True
number = 1
last_messages = []
end_letter = ''
num = 0
alphabet_cite_start = {}
alphabet_cite_end = {}
def cite_update():
    global alphabet_cite_start
    global alphabet_cite_end
    alphabet_cite_start = {}
    alphabet_cite_end = {}
    for i in cites:
        if i[0] in alphabet_cite_start:
            alphabet_cite_start[i[0]].extend([i])
        else:
            alphabet_cite_start[i[0]] = [i]
        if i[-1] in alphabet_cite_end:
            alphabet_cite_end[i[-1]].extend([i])
        else:
            alphabet_cite_end[i[-1]] = [i]
def pro_bel():print('\n'*40)
if input('Если хотите пропустить описание нажмите Enter\nЕсли хотите прочитать описание нажмите что-нибудь: ') == '':
    pro_bel()
else:
    pro_bel()
    print(f'{name.capitalize()} {sticker} эта программа была создана для тренировки игры в города')
    sleep(3.2)
    print('Всего есть четыре вида ботов 💻: Авто 🤖, Легкий 🙂, Средний 🤨, Сложный 😠')
    sleep(3.2)
    print('Авто 🤖 - играют боты 💻')
    sleep(3.2)
    print('Легко 🙂 - бот 💻 отвечает так чтобы ты выиграл(а)')
    sleep(3.2)
    print('Средний 🤨 - бот 💻 рандомно отвечает')
    sleep(3.2)
    print('Сложный 😠 - бот 💻 отвечает так чтобы ты не выиграл(а)')
    sleep(3.2)
    print(f'{name.capitalize()} {sticker} в игре есть 265 городов и 1269 имен')
    sleep(3.2)
    if cheats:
        cheats_ = 'Включены'
    else:
        cheats_ = 'Выключены'
    print(f'А также читы сейчас они сейчас {cheats_}')
    sleep(3.2)
    if not cheats:
        print(f'{name.capitalize()} {sticker} чтобы включить читы надо поменять переменную cheats на значение True')
        sleep(4)
def if_is_difficult():
    global mistake
    mistake = 0
    if difficult == 'авто':pass
    elif difficult == 'легко':pass
    elif difficult == 'средний': pass
    elif difficult == 'сложный':pass
    else:
        print('Ошибка!')
        mistake += 1
difficult = input(f'{name.capitalize()} {sticker} напишите сложность бота 💻: Авто 🤖, Легко 🙂, Средний 🤨, Сложный 😠 Без смайликов! : ')
difficult = difficult.lower()
if_is_difficult()
while mistake != 0:
    difficult = input(f'{name.capitalize()} {sticker} напишите сложность бота 💻: Авто 🤖, Легко 🙂, Средний 🤨, Сложный 😠 Без смайликов! : ')
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
    global alphabet_cite_start
    global alphabet_cite_end
    global word_hard
    if cite == 'x' and true:
        true = False
        if difficult == 'авто':
            end_letter = 'а'
        else:
            end_letter = ''
    cite = cite.lower()
    if cites.count(cite) == 1 or cite == 'x':
        mistake = 0
        cites.remove(cite)
        if cite[-1] == 'ь' or cite[-1] == 'ъ' or cite[-1] == 'ы':
            cite = list(cite)
            cite.pop(-1)
            cite = ''.join(cite)
        if cite == 'x':
            end_letter = ''
        cite_update()
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
                        print(f'Бот💻-Авто 🤖 №{number} придумал: {alphabet_cite_start[end_letter][0].title()}')
                else:
                    print(f'Бот💻-Авто 🤖 №{number} проиграл 😥')
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
            elif difficult == 'легко':
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
                            alphabet_end_letter = ', '.join(alphabet_end_letter)
                            print(f'\nХакер 🔎🥸💻: Вот ваши варианты {name.capitalize()} {sticker}\n')
                            print(alphabet_end_letter.title())
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на букву - "{end_letter.title()}": ')
                        ot_vet = ot_vet.lower()
                    else:
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на любую букву: ')
                        ot_vet = ot_vet.lower()
                    mistake += 1
                    if ot_vet in cites:
                        if ot_vet[0] == end_letter or end_letter == '':
                            mistake = 0
                            if ot_vet[-1] == 'ь' or ot_vet[-1] == 'ъ' and ot_vet[-1] == 'ы':
                                end_letter = ot_vet[-2]
                            else:
                                end_letter = ot_vet[-1]
                            last_messages.append(f'{name.capitalize()} {sticker}: {ot_vet.title()}')
                            pro_bel()
                            for i in last_messages:
                                print(i)
                    if mistake != 0:
                        if mistake != 3:
                            print(f'{name.capitalize()} {sticker} осталось попыток ☹️: {3 - mistake}')
                else:
                    if not ot_vet in cites:
                        print(f'Вы проиграли {name.capitalize()} 😥')
                    else:
                        cites.remove(ot_vet)
                        cite_update()
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
                            pro_bel()
                            for i in last_messages:
                                print(i)
                            print(f'Вы выиграли {name.capitalize()} 🙂')
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
                            maximum = max(alphabet.values())
                            word = ''
                            for i in alphabet:
                                if alphabet[i] == maximum:
                                    word = i
                            if len(alphabet_end_letter) != 0:
                                last_messages.append(f'Бот💻-Легкий 🙂: {alphabet_cite_end[word][0].title()}')
                                print(f'Бот💻-Легкий 🙂: {alphabet_cite_end[word][0].title()}')
                                word_hard = alphabet_cite_end[word][0]
                            else:
                                if mistake == 0:
                                    pro_bel()
                                    for i in last_messages:
                                        print(i)
                                    print(f'Вы выиграли {name.capitalize()} 🙂')
                                ext = False
                            if ext:
                                answer_cite(word_hard)
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
                            alphabet_end_letter = ', '.join(alphabet_end_letter)
                            print(f'\nХакер 🔎🥸💻: Вот ваши {name.capitalize()} {sticker} варианты\n')
                            print(alphabet_end_letter.title())
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на букву - "{end_letter.title()}": ')
                        ot_vet = ot_vet.lower()
                    else:
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на любую букву: ')
                        ot_vet = ot_vet.lower()
                    mistake += 1
                    if ot_vet in cites:
                        if ot_vet[0] == end_letter or end_letter == '':
                            mistake = 0
                            if ot_vet[-1] == 'ь' or ot_vet[-1] == 'ъ' and ot_vet[-1] == 'ы':
                                end_letter = ot_vet[-2]
                            else:
                                end_letter = ot_vet[-1]
                            last_messages.append(f'{name.capitalize()} {sticker}: {ot_vet.title()}')
                            pro_bel()
                            for i in last_messages:
                                print(i)
                    if mistake != 0:
                        if mistake != 3:
                            print(f'{name.capitalize()} {sticker} Осталось попыток ☹️: {3-mistake}')
                else:
                    if not ot_vet in cites:
                        print(f'Вы проиграли {name.capitalize()} 😥')
                    else:
                        cites.remove(ot_vet)
                        cite_update()
                    if mistake == 0:
                        pro_bel()
                    if end_letter in alphabet_cite_start:
                        last_messages.append(f'Бот💻-Средний 🤨: {alphabet_cite_start[end_letter][0].title()}')
                        pro_bel()
                        for i in last_messages:
                            print(i)
                    else:
                        if mistake == 0:
                            pro_bel()
                            for i in last_messages:
                                print(i)
                            print(f'Вы выиграли {name.capitalize()} 🙂')
                        ext = False
                    if end_letter in alphabet_cite_start.keys():
                        word = alphabet_cite_start[end_letter][0].lower()
                        if type(alphabet_cite_start[end_letter]) == type(''):
                            word = alphabet_cite_start[end_letter][0].lower()
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
                            alphabet_end_letter = ', '.join(alphabet_end_letter)
                            print(f'\nХакер 🔎🥸💻: Вот ваши варианты {name.capitalize()} {sticker}\n')
                            print(alphabet_end_letter.title())
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на букву - "{end_letter.title()}": ')
                        ot_vet = ot_vet.lower()
                    else:
                        ot_vet = input(f'{name.capitalize()} {sticker} напишите город на любую букву: ')
                        ot_vet = ot_vet.lower()
                    mistake += 1
                    if ot_vet in cites:
                        if ot_vet[0] == end_letter or end_letter == '':
                            mistake = 0
                            if ot_vet[-1] == 'ь' or ot_vet[-1] == 'ъ' and ot_vet[-1] == 'ы':
                                end_letter = ot_vet[-2]
                            else:
                                end_letter = ot_vet[-1]
                            last_messages.append(f'{name.capitalize()} {sticker}: {ot_vet.title()}')
                            pro_bel()
                            for i in last_messages:
                                print(i)
                    if mistake != 0:
                        if mistake != 3:
                            print(f'{name.capitalize()} {sticker} осталось попыток ☹️: {3 - mistake}')
                else:
                    if not ot_vet in cites:
                        print(f'Вы проиграли {name.capitalize()} 😥')
                    else:
                        cites.remove(ot_vet)
                        cite_update()
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
                            pro_bel()
                            for i in last_messages:
                                print(i)
                            print(f'Вы выиграли {name.capitalize()} 🙂')
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
                                last_messages.append(f'Бот💻-Сложный 😠: {alphabet_cite_end[word][0].title()}')
                                print(f'Бот💻-Сложный 😠: {alphabet_cite_end[word][0].title()}')
                                word_hard = alphabet_cite_end[word][0]
                            else:
                                if mistake == 0:
                                    pro_bel()
                                    for i in last_messages:
                                        print(i)
                                    print(f'Вы выиграли {name.capitalize()} 🙂')
                                ext = False
                            if ext:
                                answer_cite(word_hard)
        else:
            print('Ошибка!')
    else:
        print('Ошибка!')
answer_cite('x')
