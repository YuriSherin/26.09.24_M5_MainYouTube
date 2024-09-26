import time
class UrTube:
    def __init__(self):
        self.users = []                 # список объектов User
        self.videos = []                # список объектов Video
        self.current_user = None        # текущий пользователь

    def __str__(self):
        """Метод для функций print, format возвращает строку,
        содержащую названия всех video из списка videos"""
        name_video = ""
        for video in self.videos:
            name_video += video.title + '\n'
        name_video = name_video[ : len(name_video) - 1]
        return name_video


    def  log_in(self, login, password):
        """Метод log_in, который принимает на вход аргументы: nickname, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        for user in self.users:
            # if login == user.nickname and password == user.password:
            if login == user and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        """Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически."""
        for user in self.users:
            if user == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User (nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        # print(f'Пользователь {nickname} зарегистрирован и вошел в систему')

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None"""
        self.current_user = None

    def add(self, *args):
        """Метод add, который принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos, если с таким же названием видео ещё не существует.
        В противном случае ничего не происходит."""
        for movie in args:
            if movie in self.videos:
                continue
            else:
                self.videos.append(movie)


    def get_videos(self, text):
        """Метод get_videos, который принимает поисковое слово и возвращает список названий
        всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN'
        присутствует в строке 'Urban the best' (не учитывать регистр)."""
        list_movie = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie):
        """Метод watch_video, который принимает название фильма, если не находит
        точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается."""
        if self.current_user and self.current_user < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(11):
                        print(video.time_now, end=' ')
                        video.time_now += 1
                        time.sleep(1)
                    print('Конец видео')
                    video.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title              # заголовок, строка
        self.duration = duration        # продолжительность, секунды
        self.time_now  = 0              # секунда остановки, изначально = 0
        self.adult_mode = False         # ограничение по возрасту, изначально = False


    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # имя пользователя, строка
        self.password = hash(password)  # пароль в хешированном виде, число
        self.age = age                  # возраст, число

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if not isinstance(other, (str, User)):
            raise TypeError("Операнд должен иметь тип 'str' или 'User'")
        res = other if isinstance(other, str) else other.nickname
        return self.age == res


    def __lt__(self, other):
        if not isinstance(other, (int, User)):
            raise TypeError("Операнд должен иметь тип 'int' или 'User'")
        res = other if isinstance(other, int) else other.age
        return self.age < res

if __name__ == '__main__':

    # Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
