import pygame
import pyautogui
import os
import sys
import pygame_menu
import time
import random
from PyQt5 import QtWidgets, QtCore
from pygame_menu import themes
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, \
    QTableWidgetItem, QFileDialog
import sqlite3
from untitled1 import Ui_Dialog
from untitled2 import Ui_AdminWindow
from AdminClasses import Ui_AdminClasses
from AdminTests import Ui_AdminTests
from AdminTests1 import Ui_AdminTests1
from StudentClass import Ui_StudentClass
from SudentTests import Ui_StudentTests
from RunTest import Ui_Run_Test
from Result import Ui_Result
from AdminJournal import Ui_Journal
from Quest import Ui_Form


def load_image(filename, color_key=None):
    fullname = os.path.join('data', filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', fullname)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)
FPS = 50


on_off = True
login = None
role = None  # для определния вошедшего в систему человека - Учитель или Ученик


def sign_up():
    global name1, password1, on_off, role, login
    con = sqlite3.connect('School.sqlite')
    cur = con.cursor()
    result = cur.execute("SELECT Login FROM persons").fetchall()
    log_pass = [result[i][0] for i in range(len(result))]
    if name1.get_value() in log_pass:
        HELP = "Такой ник уже занят, попробуйте другой"
        ErrorWindow2 = pygame_menu.Menu('Registration', 400, 200, theme=themes.THEME_BLUE)
        ErrorWindow2.add.label(HELP, max_char=-1, font_size=20)
        Registration._open(ErrorWindow2)
    elif len(password1.get_value()) < 6:
        HELP = "Такой пароль слишком короткий, попробуйте другой"
        ErrorWindow3 = pygame_menu.Menu('Registration', 400, 200, theme=themes.THEME_BLUE)
        ErrorWindow3.add.label(HELP, max_char=-1, font_size=20)
        Registration._open(ErrorWindow3)
    else:
        cur.execute('''INSERT INTO persons(Login, Password)
                         VALUES(?, ?)''', (name1.get_value(), password1.get_value()))
        con.commit()
        cur.close()
        on_off = False
        pygame.quit()
        login = name1.get_value()
        role = 'Ученик'


Registration = pygame_menu.Menu('Регистрация', 600, 400, theme=themes.THEME_SOLARIZED)
name1 = Registration.add.text_input('Ник: ', default='')
password1 = Registration.add.text_input('Пароль: ', default='')
Registration.add.button('Зарегистрироваться', action=sign_up)
Registration.add.button('Выйти', action=pygame_menu.events.EXIT)


def registration():
    Autorization._open(Registration)
    pygame.time.set_timer(update_loading, 30)


def sign_in():
    global name, password, on_off, role, login
    con = sqlite3.connect('School.sqlite')
    cur = con.cursor()
    result = cur.execute("SELECT Login, Password, Role FROM persons WHERE Login = ? AND Password = ?",
                         (name.get_value(), password.get_value())).fetchone()
    con.close()
    if result is None:
        HELP = "Возможно вы ввели некорректный ник или пароль"
        ErrorWindow1 = pygame_menu.Menu('Авторизация', 400, 200, theme=themes.THEME_BLUE)
        ErrorWindow1.add.label(HELP, max_char=-1, font_size=20)
        Autorization._open(ErrorWindow1)
    else:
        on_off = False
        pygame.quit()
    role = result[2]
    login = name.get_value()


Autorization = pygame_menu.Menu('Авторизация', 600, 400, theme=themes.THEME_SOLARIZED, onclose=sign_in)
name = Autorization.add.text_input('Ник: ', default='')
password = Autorization.add.text_input('Пароль: ', default='')
Autorization.add.button('Регистрация', action=registration)
Autorization.add.button('Войти', action=sign_in)
update_loading = pygame.USEREVENT
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
Autorization.add.button('Выход', action=pygame_menu.events.EXIT)

while on_off:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if Autorization.is_enabled():
        Autorization.update(events)
        if on_off:
            Autorization.draw(screen)
            if (Autorization.get_current().get_selected_widget()):
                arrow.draw(screen, Autorization.get_current().get_selected_widget())
            pygame.display.flip()


class EmptyComboBox(Exception):
    pass


class WrongFileFormat(Exception):
    pass


class WrongLoginOrPassword(Exception):
    pass


class WrongNumberOfClass(Exception):
    pass


class ShortPassword(Exception):
    pass


class RecurringLogin(Exception):
    pass


class Window2(QDialog, Ui_Dialog):  # главное окно для учеников
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.Login = login


class Window21(QWidget, Ui_StudentClass):  # окно для показа класса ученика
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        self.pushButton.clicked.connect(self.show_Class)
        self.Login = str()

    def GetLogin(self, login):
        self.Login = login

    def show_Class(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT Class FROM persons WHERE Login = ?",
                             (self.Login,)).fetchone()
        # Получили результат запроса, который ввели в текстовое поле
        Class = result[0]
        result1 = cur.execute("SELECT Login, Class FROM persons WHERE Class = ?",
                               (Class, )).fetchall()
        # Заполнили размеры таблицы
        if result1:
            self.tableWidget.setRowCount(len(result1))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result1[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result1):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


class Window221(QWidget, Ui_StudentTests):  # окно для показа выполненных тестов и выбора теста
    def __init__(self, Login):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        self.pushButton_2.clicked.connect(self.PassedTests)
        self.Login = Login
        cur = self.con.cursor()
        result = cur.execute("SELECT NameOfTest FROM admintests WHERE INSTR(Passed, ?) = 0",
                             (self.Login,)).fetchall()
        NamesOfTests = [result[i][0] for i in range(len(result))]
        self.comboBox.addItems(NamesOfTests)

    def PassedTests(self):
        cur = self.con.cursor()
        idStudent, Class = cur.execute('SELECT id, Class FROM persons WHERE Login = ?', (self.Login,)).fetchone()
        result = cur.execute("""SELECT id, Name_Test, Date, Class, Percent FROM running_test
         WHERE idStudent = ? AND Class = ?""",
                             (idStudent, Class)).fetchall()
        # Заполнили размеры таблицы
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def GiveNameOfTest(self):
        return self.comboBox.currentText()

    def GiveLogin(self):
        return self.Login

    def NotEmptyCheckCB(self):
        try:
            if self.comboBox.currentText() == '':
                raise EmptyComboBox
            else:
                return True
        except EmptyComboBox:
            pass


class Window3(QWidget, Ui_AdminWindow):  # главное окно для админа-учителя
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Window321(QWidget, Ui_AdminTests):  # окно для показа всех тестов
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        cur = self.con.cursor()
        result = cur.execute('''SELECT Class FROM persons
                            WHERE Role != "Admin"''').fetchall()
        result1 = sorted(list(set([str(result[i][0]) for i in range(len(result))])))
        self.comboBox.addItems(result1)
        self.pushButton_3.clicked.connect(self.show_Tests)

    def show_Tests(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT id, NameOfTest, Test, Class, Date_added, Passed FROM admintests WHERE Class = ?",
                             (int(self.comboBox.currentText()),)).fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


class Window322(QWidget, Ui_AdminTests1):  # окно для добавления теста в систему
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        self.pushButton.clicked.connect(self.add_Test)
        self.pushButton_3.clicked.connect(self.OpenFile)

    def add_Test(self):
        try:
            cur = self.con.cursor()
            if self.lineEdit.text():
                File = self.lineEdit.text().split('.')
                if File[1] == 'txt':
                    Class = int(File[0][File[0].index('[', 0, -1) + 1:File[0].index(']', 0, -1)])
                    if 1 <= Class <= 11:
                        NameOfTest = File[0].split('/')[-1]
                        result = cur.execute("SELECT NameOfTest FROM admintests WHERE Class = ?",
                                             (Class,)).fetchall()
                        NamesOfTests = [result[i][0] for i in range(len(result))]
                        if NameOfTest not in NamesOfTests:
                            test = list()
                            with open(self.lineEdit.text()) as file:
                                for line in file:
                                    test.append(line)
                            Test = ''.join(test)
                            Passed = ""
                            cur.execute('''INSERT INTO admintests(NameOfTest, Test, Class, Date_added,
                             Passed) VALUES(?, ?, ?, ?, ?)''', (NameOfTest, Test, Class,
                                                                time.strftime('%Y-%m-%d %H:%M:%S'), Passed))
                            self.con.commit()
                            cur.close()
                            self.label_2.setText('Тест добавлен')
                        else:
                            raise RecurringLogin
                    else:
                        raise WrongNumberOfClass
                else:
                    raise WrongFileFormat
        except FileNotFoundError:
            self.label_2.setText('Нет такого файла.')
        except WrongFileFormat:
            self.label_2.setText('Неправильное расширение файла. Нужно .txt!!!')
        except WrongNumberOfClass:
            self.label_2.setText('Некорректный класс.')
        except RecurringLogin:
            self.label_2.setText('Это название теста для этого класса используется, укажите другое.')

    def OpenFile(self):
        try:
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать тест', '',
                'Картинка (*.txt)')[0]
            cur = self.con.cursor()
            File = fname.split('.')
            if fname:
                if File[1] == 'txt':
                    Class = int(File[0][File[0].index('[', 0, -1) + 1:File[0].index(']', 0, -1)])
                    Subobject = File[0][File[0].index(']', 0, -1) + 1:]
                    if 1 <= Class <= 11:
                        NameOfTest = File[0].split('/')[-1]
                        result = cur.execute("SELECT NameOfTest FROM admintests WHERE Class = ?",
                                             (Class, )).fetchall()
                        NamesOfTests = [result[i][0] for i in range(len(result))]
                        if NameOfTest not in NamesOfTests:
                            test = list()
                            with open(self.lineEdit.text()) as file:
                                for line in file:
                                    test.append(line)
                            Test = ''.join(test)
                            Passed = ""
                            cur.execute('''INSERT INTO admintests(NameOfTest, Test, Class, Date_added,
                             Passed) VALUES(?, ?, ?, ?, ?)''', (NameOfTest, Test, Class,
                                                                time.strftime('%Y-%m-%d %H:%M:%S'), Passed))
                            self.con.commit()
                            cur.close()
                            self.label_2.setText('Тест добавлен')
                        else:
                            raise RecurringLogin
                    else:
                        raise WrongNumberOfClass
                else:
                    raise WrongFileFormat
        except FileNotFoundError:
            self.label_2.setText('Нет такого файла.')
        except WrongNumberOfClass:
            self.label_2.setText('Некорректный класс.')
        except RecurringLogin:
            self.label_2.setText('Это название теста для этого класса используется, укажите другое.')


class Window33(QWidget, Ui_Journal):  # окно для показа выполненных тестов учениками
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT id, Login, Name_Test, Date, Class, Percent FROM running_test").fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        result = cur.execute('''SELECT Class FROM persons
                                    WHERE Role != "Admin"''').fetchall()
        result1 = sorted(list(set([str(result[i][0]) for i in range(len(result))])))
        self.comboBox.addItems(result1)
        result = cur.execute('''SELECT Login FROM running_test
                 WHERE Class = ?''', (int(self.comboBox.currentText()),)).fetchall()
        result1 = sorted(list(set([str(result[i][0]) for i in range(len(result))]))) + ['Все']
        self.comboBox_2.addItems(result1)
        self.pushButton.clicked.connect(self.show_Results)

    def show_Results(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute('''SELECT count(*) FROM running_test
                 WHERE Class = ?''',
                             (int(self.comboBox.currentText()),)).fetchone()[0]
        if int(result) > 0:
            if self.comboBox_2.currentText() == 'Все':
                result = cur.execute('''SELECT id, Login, Name_Test, Date, Class,  Percent FROM running_test
                         WHERE Class = ?''', (int(self.comboBox.currentText()),)).fetchall()
                self.tableWidget.setRowCount(len(result))
                # Если запись не нашлась, то не будем ничего делать
                self.tableWidget.setColumnCount(len(result[0]))
                self.titles = [description[0] for description in cur.description]
                self.tableWidget.setHorizontalHeaderLabels(self.titles)
                # Заполнили таблицу полученными элементами
                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            else:
                result1 = cur.execute('''SELECT id, Login, Name_Test, Date, Class, Percent FROM running_test
                                 WHERE Class = ? AND Login = ?''',
                                     (int(self.comboBox.currentText()), self.comboBox_2.currentText())).fetchall()
                if result1:
                    self.tableWidget.setRowCount(len(result1))
                    # Если запись не нашлась, то не будем ничего делать
                    self.tableWidget.setColumnCount(len(result1[0]))
                    self.titles = [description[0] for description in cur.description]
                    self.tableWidget.setHorizontalHeaderLabels(self.titles)
                    # Заполнили таблицу полученными элементами
                    for i, elem in enumerate(result1):
                        for j, val in enumerate(elem):
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


END_GAME, count_Quests, count_YourRightAnswers, is_ST = False, 0, 0, False


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(274, 109)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 191, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Начало теста"))
        self.pushButton.setText(_translate("Form", "Начать игру"))


class Form(QtWidgets.QWidget):
    def __init__(self, NameOfTest, Login):
        super(Form, self).__init__()
        ui = Ui_Form()
        ui.setupUi(self)
        self.NameOfTest = NameOfTest
        self.Login = Login
        ui.pushButton.clicked.connect(self.okno)

    def okno(self):
        #Вывод окна
#        sys.exit(app.exec_())
        self.hide()
        pyGame(self.NameOfTest)
        self.RW = ResultWindow(self.NameOfTest, self.Login)
        self.RW.pushButton.clicked.connect(self.Close)
        self.RW.show()

    def Close(self):
        global is_ST
        is_ST = True


def pyGame(NameOfTest):
    global END_GAME, count_Quests, count_YourRightAnswers
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)
    sprite_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    tile_width = tile_height = 50
    tile_image = {'wall': pygame.transform.scale(load_image('box.png'), (tile_width, tile_height)),
                  'empty': pygame.transform.scale(load_image('grass.png'), (tile_width, tile_height))}
    player_image = load_image('mar.png')
    con = sqlite3.connect("School.sqlite")
    cur = con.cursor()
    result = cur.execute("SELECT Test FROM admintests WHERE NameOfTest = ?",
                         (NameOfTest,)).fetchone()[0].split('\n')
    Quests, RightAnswers = [result[i].split(';')[0] for i in range(len(result[:-1]))], \
                           [result[i].split(';')[1] for i in range(len(result[:-1]))]
    count_Quests = len(Quests)
    dict_x = {}
    count = 0
    count_lives = 3
    level_map = list()

    class Tile(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(sprite_group)
            self.image = tile_image[tile_type]
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(hero_group)
            self.image = player_image
            self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.pos = (pos_x, pos_y)

        def move(self, x, y):
            self.pos = (x, y)
            self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 15,
                                                   tile_height * self.pos[1] + 5)

    def load_level(filename):
        filename = 'data/' + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, level_map))
        return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))

    def generate_level(level):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    new_player = Player(x, y)
                    level[y][x] = '.'
                elif level[y][x] == 'x':
                    Tile('empty', x, y)
                    dict_x[(y, x)] = False
        return new_player, x, y

    def move(hero, movement):
        nonlocal count, count_lives
        x, y = hero.pos
        index = int()
        if len(Quests) > 0:
            index = random.choice([i for i in range(len(Quests))])
        if movement == 'up':
            if y > 0:
                if level_map[y - 1][x] == '.':
                    hero.move(x, y - 1)
                elif level_map[y - 1][x] == 'x':
                    if not dict_x[(y - 1, x)]:
                        hero.move(x, y - 1)
                        answer = pyautogui.prompt(Quests[index])
                        if answer == RightAnswers[index]:
                            count += 1
                            del Quests[index]
                            del RightAnswers[index]
                        else:
                            del Quests[index]
                            del RightAnswers[index]
                            count_lives -= 1
                        dict_x[(y - 1, x)] = True
                    hero.move(x, y - 1)
        elif movement == 'down':
            if y < max_y:
                if level_map[y + 1][x] == '.':
                    hero.move(x, y + 1)
                elif level_map[y + 1][x] == 'x':
                    if not dict_x[(y + 1, x)]:
                        hero.move(x, y + 1)
                        answer = pyautogui.prompt(Quests[index])
                        if answer == RightAnswers[index]:
                            count += 1
                            del Quests[index]
                            del RightAnswers[index]
                        else:
                            del Quests[index]
                            del RightAnswers[index]
                            count_lives -= 1
                        dict_x[(y + 1, x)] = True
                    hero.move(x, y + 1)
        elif movement == 'left':
            if x > 0:
                if level_map[y][x - 1] == '.':
                    hero.move(x - 1, y)
                elif level_map[y][x - 1] == 'x':
                    if not dict_x[(y, x - 1)]:
                        hero.move(x - 1, y)
                        answer = pyautogui.prompt(Quests[index])
                        if answer == RightAnswers[index]:
                            count += 1
                            del Quests[index]
                            del RightAnswers[index]
                        else:
                            del Quests[index]
                            del RightAnswers[index]
                            count_lives -= 1
                        dict_x[(y, x - 1)] = True
                    hero.move(x - 1, y)
        elif movement == 'right':
            if x < max_x:
                if level_map[y][x + 1] == '.':
                    hero.move(x + 1, y)
                elif level_map[y][x + 1] == 'x':
                    if not dict_x[(y, x + 1)]:
                        hero.move(x + 1, y)
                        answer = pyautogui.prompt(Quests[index])
                        if answer == RightAnswers[index]:
                            count += 1
                            del Quests[index]
                            del RightAnswers[index]
                        else:
                            del Quests[index]
                            del RightAnswers[index]
                            count_lives -= 1
                        dict_x[(y, x + 1)] = True
                    hero.move(x + 1, y)

    pygame.display.set_caption(NameOfTest)
    running = True
    level_map = load_level('map.txt')
    hero, max_x, max_y = generate_level(level_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move(hero, 'up')
                if event.key == pygame.K_DOWN:
                    move(hero, 'down')
                if event.key == pygame.K_RIGHT:
                    move(hero, 'right')
                if event.key == pygame.K_LEFT:
                    move(hero, 'left')
        if count_lives == 0:
            END_GAME, count_YourRightAnswers = True, count
            running = False
        if len(Quests) == 0:
            END_GAME, count_YourRightAnswers = True, count
            running = False
        screen.fill(pygame.Color('black'))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        pygame.display.flip()
    pygame.quit()


class ResultWindow(QWidget, Ui_Result):
    def __init__(self, NameOfTest, Login):
        global count_Quests, count_YourRightAnswers
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("School.sqlite")
        cur = self.con.cursor()
        idTest = cur.execute("SELECT id FROM admintests WHERE NameOfTest = ?",
                             (NameOfTest,)).fetchone()[0]
        result = cur.execute("SELECT id, F_and_L_names FROM persons WHERE Login = ?",
                             (Login,)).fetchone()
        self.label.setText(f'Спасибо за прохождение теста, {result[1]}!')
        self.label_2.setText(f'Ваш результат: {count_YourRightAnswers}/{count_Quests}')
        cur.execute('''INSERT INTO running_test(idStudent, idTest, Login, Name_Test, Date, Percent)
                                                             VALUES(?, ?, ?, ?, ?, ?)''',
                    (result[0], idTest, Login,
                     NameOfTest, time.strftime('%Y-%m-%d %H:%M:%S'), int(count_YourRightAnswers / count_Quests)))
        self.con.commit()
        result0 = cur.execute("SELECT Passed FROM admintests WHERE NameOfTest = ?",
                             (NameOfTest,)).fetchone()[0]
        Passed = '\n'.join([result0, result[1]])
        cur.execute('''UPDATE admintests 
                SET Passed = ? 
                WHERE NameOfTest = ?''', (Passed, NameOfTest))
        self.con.commit()
        cur.close()


class Application(QMainWindow):  # сборка классов в одно приложение
    def __init__(self, role, login):
        super(Application, self).__init__()
        self.login = login
        self.role = role
        self.setWindowTitle('Меню для учителя')
        self.WOS = Window2(self.login)
        self.AW = Window3()
        if self.role == "Admin":
            self.AW.show()
            self.AW.pushButton_2.clicked.connect(self.show_AdminJournal)
            self.AW.pushButton_3.clicked.connect(self.show_AdminTests)
        elif self.role == "Ученик":
            self.WOS.show()
            self.WOS.pushButton.clicked.connect(self.show_MyClass)
            self.WOS.pushButton_3.clicked.connect(self.show_MyTests)

    def show_AdminTests(self):  # показать окно с тестами в системе
        self.AWTests = Window321()
        self.AWTests.pushButton_2.clicked.connect(self.backToAW1)
        self.AWTests.pushButton.clicked.connect(self.show_AWAdd_Test)
        self.AWTests.show()
        self.AW.close()

    def show_AdminJournal(self):  # показать пройденные учениками тесты
        self.AWJournal = Window33()
        self.AWJournal.pushButton_2.clicked.connect(self.backToAW3)
        self.AWJournal.show()
        self.AW.close()

    def backToAW1(self):
        if self.AWTests.isVisible():
            self.AW.show()
            self.AWTests.close()

    def backToAW3(self):
        if self.AWJournal.isVisible():
            self.AW.show()
            self.AWJournal.close()

    def show_AWAdd_Test(self):  # показать добавляющее тесты окно
        self.AWAdd_Test = Window322()
        self.AWAdd_Test.pushButton_2.clicked.connect(self.backToAWTests)
        self.AWAdd_Test.show()
        self.AWTests.close()

    def backToAWTests(self):
        if self.AWAdd_Test.isVisible():
            self.AWTests.show()
            self.AWAdd_Test.close()

    def show_MyClass(self):  # показать класс ученика
        self.SC = Window21()
        self.SC.GetLogin(self.login)
        self.SC.pushButton_2.clicked.connect(self.backToWOS1)
        self.SC.show()
        self.WOS.close()

    def backToWOS1(self):
        self.WOS.show()
        self.SC.close()

    def show_MyTests(self):  # показать теста для ученика
        self.ST = Window221(self.login)
        self.ST.pushButton.clicked.connect(self.show_RunTest)
        self.ST.pushButton_3.clicked.connect(self.backToWOS2)
        self.ST.show()
        self.WOS.close()

    def backToWOS2(self):
        self.WOS.show()
        self.ST.close()

    def show_RunTest(self):  # показать окно с прохождением теста
        self.ST.close()
        self.Game = Form(self.ST.GiveNameOfTest(), self.ST.GiveLogin())
        self.Game.show()
        print(is_ST)
        if is_ST:
            self.Game.close()
            self.ST.show()
            print(is_ST)

    # def Show(self):
    #     self.RW.pushButton.clicked.connect(self.backToST)
    #     self.RW.show()
    #
    # def backToST(self):
    #     self.RW.close()
    #     self.ST.show()


def except_hook(cls, exception, traceback):  # функция для лёгкого поиска ошибок
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':  # запуск программы
    app = QApplication(sys.argv)
    ts = Application(role, login)
    sys.excepthook = except_hook
    sys.exit(app.exec_())
