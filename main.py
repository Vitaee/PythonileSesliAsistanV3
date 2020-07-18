import sys,time

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QSize, QThread, QTimer, QTime
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QColor
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QWidget, QPlainTextEdit, QVBoxLayout, QApplication, \
    QMainWindow
from commands import commandss
from functioons.functions import (listen, talkUS, open_music, close_music, open_google, open_dc, open_pychr,
open_slck, open_tlg, open_site, sy_hello, sy_hwareu, sy_thnks, cls_system,who_areu, th_dy, wiki, gl_mps, yt_song, gl_srch, tk_nte, rd_nte, dl_nte,
pc_kpt,pc_yndn, pc_otrm,cpu_inf, hdd_inf, ram_inf, wb_cm, havadurumu, yoltarifi, desk_wallpaper,create_folder, wifi_passes, calendar_set,
write_code, google_news, facebook_login,open_games,twit_login)



#takes console log data.
class Logger():
    stdout = sys.stdout
    messages = []

    def flush(self):
        pass

    def start(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self.stdout

    def write(self, text):
        self.messages.append(text)

log = Logger()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Save User Data"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 220
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        buttonWindow1 = QPushButton('Exit Window', self)
        buttonWindow1.move(570, 60)
        buttonWindow1.clicked.connect(self.exit_window)


        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.saveName)
        pybutton.resize(200, 32)
        pybutton.move(300, 20)

        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Music Folder:')
        self.line1 = QLineEdit(self)

        self.line1.move(80, 60)
        self.line1.resize(200, 32)
        self.nameLabel1.move(2, 60)

        pybutton1 = QPushButton('OK', self)
        pybutton1.clicked.connect(self.saveMusics)
        pybutton1.resize(200, 32)
        pybutton1.move(300, 60)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText("Web Sites:")
        self.line2 = QLineEdit(self)

        self.line2.move(80,110)
        self.line2.resize(200,32)
        self.nameLabel2.move(10,110)

        pybutton2 = QPushButton("OK",self)
        pybutton2.clicked.connect(self.saveWeb)
        pybutton2.resize(200,32)
        pybutton2.move(300,110)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText("Wallpapers:")
        self.nameLabel3.move(4,165)

        self.line3 = QLineEdit(self)
        self.line3.move(80,165)
        self.line3.resize(200,32)

        pybutton2 = QPushButton("OK", self)
        pybutton2.clicked.connect(self.saveWallpapers)
        pybutton2.resize(200, 32)
        pybutton2.move(300, 165)

        self.show()

    def saveName(self):
        print("Your data is saved.")
        with open('userDatas/userData.txt', 'a', encoding='utf-8') as file:
            file.write(self.line.text() + "\n")

    def saveMusics(self):
        print("Your data is saved.")
        with open('userDatas/userData.txt', 'a', encoding='utf-8') as file:
            file.write(self.line1.text() + "\n")

    def saveWeb(self):
        print("Your data is saved.")
        with open('userDatas/userData.txt', 'a', encoding='utf-8') as file:
            file.write(self.line2.text() + "\n")

    def saveWallpapers(self):
        print("Your data is saved.")
        with open('userDatas/userData.txt', 'a', encoding='utf-8') as file:
            file.write(self.line3.text() + "\n")


    @pyqtSlot()
    def exit_window(self):
        #self.statusBar().showMessage("Closing Window")
        #self.cams = Gui()
        #self.cams.show()
        self.close()



class Worker(QObject):
    finished = pyqtSignal()  # give worker class a finished signal
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class


    def do_work(self):
        class Jarvis():
            def __init__(self, commands):
                self.commands = commands

            def run(self, command):
                answer = self.commands.eylem(command)
                if type(answer) is str:
                    return None
                else:
                    return answer

        class Command:
            def __init__(self):
                self.liste = []
                self.func = None

            def control(self, word):
                return word in self.liste

            def add(self, word):
                if type(word) is list:
                    for m in word:
                        if m not in self.liste:
                            self.liste.append(m)

                elif type(word) is str:
                    if word not in self.liste:
                        self.liste.append(word)

            def process(self, func):
                self.func = func

            def eylem(self, **kwargs):
                if type(self.func) is str:
                    return self.func
                return self.func(**kwargs)

        class Commands:
            def __init__(self):
                self.commandlist = []

            def add_commands(self, command):
                self.commandlist.append(command)

            def eylem(self, word, **kwargs):

                print(f"You said: {word}" + f" | {time.strftime('%X')}")
                for k in self.commandlist:
                    if k.control(word):
                        return k.eylem(**kwargs)

                return talkUS(f"Sorry, I don't have command like this: {word}")

        all_process = Commands()
        mrb = Command()
        mrb.add(commandss.meraba)
        mrb.process(sy_hello)
        all_process.add_commands(mrb)

        nsl = Command()
        nsl.add(commandss.nasilsin)
        nsl.process(sy_hwareu)
        all_process.add_commands(nsl)

        thks = Command()
        thks.add(commandss.iltifat)
        thks.process(sy_thnks)
        all_process.add_commands(thks)

        musc = Command()
        musc.add(commandss.mzik)
        musc.process(open_music)
        all_process.add_commands(musc)

        cls_musc = Command()
        cls_musc.add(commandss.mzik_kes)
        cls_musc.process(close_music)
        all_process.add_commands(cls_musc)

        open_gl = Command()
        open_gl.add(commandss.browser)
        open_gl.process(open_google)
        all_process.add_commands(open_gl)

        site_open = Command()
        site_open.add(commandss.site)
        site_open.process(open_site)
        all_process.add_commands(site_open)

        close_system = Command()
        close_system.add(commandss.kapatma)
        close_system.process(cls_system)
        all_process.add_commands(close_system)

        who_au = Command()
        who_au.add(commandss.whoreu)
        who_au.process(who_areu)
        all_process.add_commands(who_au)

        the_day = Command()
        the_day.add(commandss.gun)
        the_day.process(th_dy)
        all_process.add_commands(the_day)

        dc_open = Command()
        dc_open.add(commandss.discord)
        dc_open.process(open_dc)
        all_process.add_commands(dc_open)

        tlg_open = Command()
        tlg_open.add(commandss.telegram)
        tlg_open.process(open_tlg)
        all_process.add_commands(tlg_open)

        slck_open = Command()
        slck_open.add(commandss.slack)
        slck_open.process(open_slck)
        all_process.add_commands(slck_open)

        pychr_open = Command()
        pychr_open.add(commandss.pycharm)
        pychr_open.process(open_pychr)
        all_process.add_commands(pychr_open)

        wiki_pedia = Command()
        wiki_pedia.add(commandss.wikipedia)
        wiki_pedia.process(wiki)
        all_process.add_commands(wiki_pedia)

        maps = Command()
        maps.add(commandss.goglemaps)
        maps.process(gl_mps)
        all_process.add_commands(maps)

        yt_bue = Command()
        yt_bue.add(commandss.youtube)
        yt_bue.process(yt_song)
        all_process.add_commands(yt_bue)

        research = Command()
        research.add(commandss.arstr)
        research.process(gl_srch)
        all_process.add_commands(research)

        taking_note = Command()
        taking_note.add(commandss.take_note)
        taking_note.process(tk_nte)
        all_process.add_commands(taking_note)

        delete_note = Command()
        delete_note.add(commandss.del_note)
        delete_note.process(dl_nte)
        all_process.add_commands(delete_note)

        read_notes = Command()
        read_notes.add(commandss.read_note)
        read_notes.process(rd_nte)
        all_process.add_commands(read_notes)

        pc_close = Command()
        pc_close.add(commandss.blgs_kapat)
        pc_close.process(pc_kpt)
        all_process.add_commands(pc_close)

        pc_restart = Command()
        pc_restart.add(commandss.blgs_ynden)
        pc_restart.process(pc_yndn)
        all_process.add_commands(pc_restart)

        pc_sleep = Command()
        pc_sleep.add(commandss.blgs_otrm)
        pc_sleep.process(pc_otrm)
        all_process.add_commands(pc_sleep)

        pc_cpu = Command()
        pc_cpu.add(commandss.islemci)
        pc_cpu.process(cpu_inf)
        all_process.add_commands(pc_cpu)

        pc_ram = Command()
        pc_ram.add(commandss.ramm)
        pc_ram.process(ram_inf)
        all_process.add_commands(pc_ram)

        pc_hdd = Command()
        pc_hdd.add(commandss.dsk)
        pc_hdd.process(hdd_inf)
        all_process.add_commands(pc_hdd)

        open_webcam = Command()
        open_webcam.add(commandss.webcm)
        open_webcam.process(wb_cm)
        all_process.add_commands(open_webcam)

        weather_rep = Command()
        weather_rep.add(commandss.weather_report)
        weather_rep.process(havadurumu)
        all_process.add_commands(weather_rep)

        make_directions = Command()
        make_directions.add(commandss.yoltarif)
        make_directions.process(yoltarifi)
        all_process.add_commands(make_directions)

        change_wallpaper = Command()
        change_wallpaper.add(commandss.chnge_wallpaper)
        change_wallpaper.process(desk_wallpaper)
        all_process.add_commands(change_wallpaper)

        folder_create = Command()
        folder_create.add(commandss.folder)
        folder_create.process(create_folder)
        all_process.add_commands(folder_create)

        show_wifipass = Command()
        show_wifipass.add(commandss.wi_fi)
        show_wifipass.process(wifi_passes)
        all_process.add_commands(show_wifipass)

        set_calendar = Command()
        set_calendar.add(commandss.calendar_comand)
        set_calendar.process(calendar_set)
        all_process.add_commands(set_calendar)

        code_write = Command()
        code_write.add(commandss.codes)
        code_write.process(write_code)
        all_process.add_commands(code_write)

        daily_news = Command()
        daily_news.add(commandss.news_google)
        daily_news.process(google_news)
        all_process.add_commands(daily_news)

        face_login = Command()
        face_login.add(commandss.face)
        face_login.process(facebook_login)
        all_process.add_commands(face_login)

        game_open = Command()
        game_open.add(commandss.steam_games)
        game_open.process(open_games)
        all_process.add_commands(game_open)

        twit_logins = Command()
        twit_logins.add(commandss.twittr)
        twit_logins.process(twit_login)
        all_process.add_commands(twit_logins)

        jarvis = Jarvis(all_process)

        while self.continue_run:
            if not self.continue_run:
                break
            else:
                jarvis.run(listen())


        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # set the run condition to false on stop
        talkUS("See you later!")
        sys.exit()



class Gui(QWidget):
    stop_signal = pyqtSignal()  # make a stop signal to communicate with the worker in another thread

    def __init__(self):
        #super(Gui,self).__init__(parent=parent)
        super().__init__()
        self.initUI()

    def initUI(self):
        # Buttons:
        self.btn_start = QPushButton('Run!',self)
        self.btn_start.resize(self.btn_start.sizeHint())
        self.btn_start.setStyleSheet("""
                                background-color:#BFFF33;color:#040403;
                                border-width: 2px;
                                border-radius: 10px;
                                border-color: beige;
                                min-width: 4em;
                                padding: 5.5px;
                                """)
        self.btn_start.move(0, 430)

        self.btn_stop = QPushButton('Exit!',self)
        self.btn_stop.resize(self.btn_stop.sizeHint())
        self.btn_stop.setStyleSheet("""
                        background-color: red;
                        border-width: 2px;
                        border-radius: 10px;
                        border-color: beige;
                        min-width: 4em;
                        padding: 5.5px;""")
        self.btn_stop.move(650, 430)

        #Sreen Size Etc.
        self.setFixedSize(750,463)
        self.setWindowTitle('Voice Assistant')
        self.setWindowIcon(QIcon('icons/AIico.ico'))
        oImage = QImage("images/ImageBck.jpg")
        sImage = oImage.scaled(QSize(750, 463))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        #Text edit
        self.b = QPlainTextEdit(self)
        self.b.setStyleSheet("""
                        background: transparent;
                        color: #B9FC02 ;
                        """)

        self.b.zoomIn(range=2)
        self.b.setReadOnly(True)


        self.b.move(105,360)
        self.b.resize(535,100)

        # Thread:
        self.thread = QThread()
        self.worker = Worker()
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)

        # Start Button action:
        self.btn_start.clicked.connect(self.thread.start)


        # Stop Button action:
        self.btn_stop.clicked.connect(self.stop_thread)

        # Update Data
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        self.setLayout(windowLayout)

        self.show()


    def createGridLayout(self):
        time = self.getTime()
        self.time_label = QLabel(self)

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        self.stop_signal.emit()  # emit the finished signal on stop

    def getTime(self):
        return time

    def updateTime(self):
        log.start()
        time = QTime.currentTime().toString()
        while log.messages:
            self.b.insertPlainText(log.messages[0])
            log.messages.pop(0)

        return time


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window()

    gui1 = Gui()
    timer = QTimer()
    timer.timeout.connect(gui1.updateTime)

    timer.start(1000)


    sys.exit(app.exec_())
