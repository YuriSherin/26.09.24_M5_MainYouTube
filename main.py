import time
class UrTube:
    def __init__(self):
        self.users = []                 # список объектов User
        self.videos = []                # список объектов Video
        self.current_user = None        # текущий пользователь

    def __eq__(self, other):
        if not isinstance(other, (str, Video)):
            raise TypeError("Операнд должен иметь тип 'str' или 'Video'")
        res = other if isinstance(other, str) else other.title
        return self.title == res

    def __str__(self):
        return f"{self.videos}"


    def  log_in(self, login, password):
        """Метод log_in, который принимает на вход аргументы: nickname, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу."""
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        """Метод register, который принимает три аргумента: nickname, password, age,
        и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически."""
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User (nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему')

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None"""
        self.current_user = None

    def add(self, *args):
        """Метод add, который принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos, если с таким же названием видео ещё не существует.
        В противном случае ничего не происходит."""
        for movie in args:
            self.videos.append(movie)


    # def find_video_title(self, vd):
    #     """Метод ищет в списке объектов Videos видео, название которого совпадает
    #     с именем аргумента. Если такой объект находится, возвращается True,
    #     в противном случае возвращается False"""
    #     res = False
    #     for v in self.videos:
    #         if v.title != vd.title:
    #             continue
    #         else:
    #             res = True
    #             break
    #     return res

    # def find_user_nickname(self, nickname):
    #     """Метод ищет в списке пользователей ползователя с nickname.
    #     Если находит, возвращает True, иначе Falsse"""
    #     res = False
    #     for nn in self.users:
    #         if nn.nickname.lower() == nickname.lower():
    #             res = True
    #             break
    #     return res

    def get_videos(self, text):
        """Метод get_videos, который принимает поисковое слово и возвращает список названий
        всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN'
        присутствует в строке 'Urban the best' (не учитывать регистр)."""
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie):
        """Метод watch_video, который принимает название фильма, если не находит
        точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается."""
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')




class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title              # заголовок, строка
        self.duration = duration        # продолжительность, секунды
        self.time_now  = 0              # секунда остановки, изначально = 0
        self.adult_mode = False         # ограничение по возрасту, изначально = False


    def __str__(self):
        return f"{self.title}"


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # имя пользователя, строка
        self.password = password        # пароль в хешированном виде, число
        self.age = age                  # возраст, число

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)






if __name__ == '__main__':
    pass
    # Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    #
    # # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    #
    # # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    #
    # # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    a = ur.current_user
    print(ur.current_user)
    # # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
