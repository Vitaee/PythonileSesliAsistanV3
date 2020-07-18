import subprocess, pyautogui, pyttsx3
import time, datetime, random, requests, cv2, os , sys ,ctypes
import webbrowser, wikipedia, psutil
import speech_recognition as sr

from win10toast import ToastNotifier
from commands import commandss
from random import choice
from googletrans import Translator
from googlesearch import search
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from youtube_search import YoutubeSearch
from subprocess import Popen

# more futures (functions) will be added

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talkUS(audio):
    print("Assistant: " + audio + f"  {time.strftime('%X')} " + chr(9995) )
    engine.say(audio)
    engine.runAndWait()


def listen():
    global command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening " + chr(9786) + "\n")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=6)
    print("Stop! " + chr(9888) + "\n")

    try:
        command = r.recognize_google(audio, language="en-en")

    except sr.UnknownValueError:
        print("Your last command is not understood:" + chr(9785) + "\n")
        command = listen()

    except sr.HTTPError:
        print("Please check your network connection.")
        command = listen()
    except sr.RequestError:
        print("Request error. Please try again.")
        command = listen()

    return command.lower()


def open_music():
    talkUS(random.choice(commandss.music) + chr(9835))
    comp_name = os.path.expanduser('~')

    try:
        with open(r'C:\Users\{}\Desktop\VoiceAssistant\userDatas\userData.txt'.format(comp_name[9:]), 'r+', encoding='utf-8') as f:
            music_path = [line.strip() for line in f]
    except Exception as err:
        print(err)
        talkUS("error when looking for music path")
    try:
        DIR = r"{}".format(music_path[1])
        music = filter(lambda x: x.lower().endswith("mp3"), os.listdir(DIR))
        music = list(music)
        song = random.choice(music)
        webbrowser.open(os.path.join(DIR, song))
    except:
        talkUS("Your music path is wrong")

def close_music():
    talkUS("Closing your music")
    os.system("taskkill /im Music.UI.exe /f")

def open_google():
    talkUS(random.choice(commandss.brwserdns))
    webbrowser.open("https://www.google.com.tr")

def sy_hello():
    comp_name = os.path.expanduser('~')
    try:
        with open(r'C:\Users\{}\Desktop\VoiceAssistant\userDatas\userData.txt'.format(comp_name[9:]), 'r', encoding='utf-8') as file:
            data = [line.strip() for line in file]
    except: talkUS("Please check user data.txt something went wrong please try again.")
    try:
        talkUS(random.choice(commandss.merbdonus) + " " + data[0])
        toaster = ToastNotifier()
        toaster.show_toast("Assistant Says:",
                       "Hello To You!",
                       icon_path=r"C:\Users\{}\Desktop\VoiceAssistant\icons\notif.ico".format(comp_name[9:]),
                       duration=8)

        while toaster.notification_active(): time.sleep(0.1)
    except: talkUS("Sorry ı don't know your name please add your name in user data.txt as a first data.")
def sy_hwareu():
    talkUS(random.choice(commandss.nslsndonus))

def sy_thnks():
    talkUS(random.choice(commandss.iltifatdns))

def open_site():
    talkUS(random.choice(commandss.sitedns))
    comp_name = os.path.expanduser('~')
    with open(r'C:\Users\{}\Desktop\VoiceAssistant\userDatas\userData.txt'.format(comp_name[9:]), 'r+', encoding='utf-8') as f:
        website_data = [line.strip() for line in f]
    websites = []
    prefixes = ("https://","www","http://")
    for word in website_data[:]:
        if word.startswith(prefixes):
            websites.append(word)

    webbrowser.open(random.choice(websites))

def cls_system():
    talkUS(random.choice(commandss.kptmadonus))
    sys.exit()


def who_areu():
    talkUS(random.choice(commandss.whoreudns))

def th_dy():
    strDay = datetime.datetime.now().strftime("%B %d %A")
    talkUS(random.choice(commandss.gundns) + f" {strDay}")

def open_dc():
    comp_name = os.path.expanduser('~')
    # discord application location
    talkUS("Opening discord")
    try: Popen(f"C://Users//{comp_name[9:]}//AppData//Local//Discord//app-0.0.306/discord.exe")
    except: talkUS("Got an error while opening discord check your discord path please.")
def open_tlg():
    # telegram application location
    talkUS("Opening telegram")
    try: Popen(f"D://Telegram//Telegram.exe")
    except: talkUS("Got an error while opening discord check your telegram path please.")
def open_slck():
    # set slack application location
    talkUS("Opening slack")
    comp_name = os.path.expanduser('~')
    try: Popen(f"C://Users//{comp_name[9:]}//AppData//Local//slack//slack.exe")
    except: talkUS("Got an error while opening discord check your slack path please.")
def open_pychr():
    # pycharm application location
    talkUS("Opening pycharm")
    try: Popen(f"C://Program Files//JetBrains//PyCharm 2020//bin//pycharm64.exe")
    except: talkUS("Got an error while opening discord check your pycharm path please.")
def wiki():
    talkUS("Please tell me a word for searching on wikipedia.")
    a = listen()

    wikipedia.set_lang("en")
    try:
        results = wikipedia.summary(a, sentences=2)
        talkUS(results)
    except: talkUS("Sorry ı can't read data from wikipedia. Please try again")
def gl_mps():
    talkUS("Where would you like to see?")
    try:
        location = listen()
        webbrowser.open("https://www.google.nl/maps/place/" + location)
    except:
        talkUS("Some error accured please try again.")
        location = listen()
        webbrowser.open("https://www.google.nl/maps/place/" + location)


def yt_song():
    talkUS("Which song or video would you like me to open? just tell me please.")
    try:
        youtube = listen()
        result = YoutubeSearch(youtube, max_results = 1).to_dict()
        talkUS("I am opening which ı find for you on youtube")
        for i in result:
            print("https://www.youtube.com.tr" + i['link'])

        webbrowser.open("https://www.youtube.com.tr" + i['link'])
    except:
        talkUS("Unknown error accrued. Please try again.")
        youtube = listen()
        result = YoutubeSearch(youtube, max_results=1).to_dict()
        talkUS("I am opening which ı find for you on youtube")
        for i in result:
            print("https://www.youtube.com.tr" + i['link'])

        webbrowser.open("https://www.youtube.com.tr" + i['link'])


def searchOnGoogle(gl_ans,outputList):
    for output in search(gl_ans,tld = "co.in",lang = "tr", num = 10, stop = 5 , pause = 2):
        print(output)
        outputList.append(output)
    return outputList

def openLink(outputList):
    webbrowser.open(outputList[0])

def gl_srch():
    outputList = []
    talkUS("What ı should research on google?")
    gl_ans = listen()
    talkUS("I am opening the web site which ı found it on google")
    searchOnGoogle(gl_ans,outputList)
    openLink(outputList)

def tk_nte():
    talkUS("Please tell me something to let me record as a note")
    file1 = open("NoteFile.txt","a+")
    note = listen()
    file1.write(note + "\n")
    file1.close()
    talkUS("I did write your notes.")

def rd_nte():
    with open("NoteFile.txt", 'r', encoding='utf-8') as file:
        talkUS(file.read())
        talkUS("I did read your notes.")

def dl_nte():
    talkUS("Are you sure want to delete your notes?")
    del_ans = listen()
    if "Yes" in del_ans or "yes" in del_ans:
        file1 = open("NoteFile.txt","r+")
        file1.truncate(0)
        talkUS("Successfully deleted your notes.")

    if "No" in del_ans or "no" in del_ans:
        talkUS("Your notes will not be deleted")

def pc_kpt():
    talkUS("Your computer is closing in a five seconds.")
    time.sleep(5)
    os.system("shutdown /s")

def pc_yndn():
    talkUS("I will restart your computer now.")
    os.system("shutdown /r")

def pc_otrm():
    talkUS("Logging out from your computer")
    os.system("shutdown /l")

def desk_wallpaper():
    comp_name = os.path.expanduser('~')
    with open(r'C:\Users\{}\Desktop\VoiceAssistant\userDatas\userData.txt'.format(comp_name[9:]), 'r+', encoding='utf-8') as f:
        wallpaper_path = [line.strip() for line in f]

    my_wallpaper = random.choice(os.listdir(r"{}".format(wallpaper_path[-1])))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"{}".format(wallpaper_path[-1])+r'\\'+my_wallpaper, 0)
    talkUS("I changed your desktop wallpaper.")


def create_folder():
    comp_name = os.path.expanduser('~')
    os.mkdir(r"C:\Users\{}\Desktop\AssistantFolder".format(comp_name[9:]))
    talkUS("Your folder is created on your desktop")

def open_games():

    #You can add your steam games here with an app id.

    if command.lower() in commandss.steam_games[:3]:
        try: subprocess.run("start steam://run/730", shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")

    elif command.lower() in commandss.steam_games[4:7]:
        try: subprocess.run("start steam://run/880940", shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")

    elif command.lower() in commandss.steam_games[8:12]:
        try: subprocess.run("start steam://run/107410", shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")

    elif command.lower() in commandss.steam_games[13:17]:
        try: subprocess.run("start steam://run/271590",shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")

    elif command.lower() in commandss.steam_games[18:23]:
        try: subprocess.run("start steam://run/227300",shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")

    elif command.lower() in commandss.steam_games[24:26]:
        try: subprocess.run("start steam://run/239140",shell=True)
        except: talkUS("Sorry bro, ı could not understand you or your game id is not defined to me.")



def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def cpu_inf():
    #get cpu info.
    print("="*20, "CPU İnformation", "="*20)
    print("Total CPUs:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Instant Ghz: {cpufreq.current:.2f}Mhz")
    print("Percentage of %CPU:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU usage: {psutil.cpu_percent()}%")
    time.sleep(5)


def hdd_inf():
    #get hdd info.
    partition_usage = psutil.disk_usage('/')
    print(f"  Total space: {get_size(partition_usage.total)}")
    print(f"  Using: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
    time.sleep(5)

def ram_inf():
    #get ram info
    svmem = psutil.virtual_memory()
    print("="*20, "Using of RAM", "="*20)
    print(f"Total: {get_size(svmem.total)}")
    print(f"Using: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    time.sleep(5)

def wb_cm():
    talkUS("Your web cam is opening")
    comp_name = os.path.expanduser('~')

    print("Press ESC for exit.")
    print("For save image press SPACE")

    faceCascade = cv2.CascadeClassifier(r'C:\Users\{}\Desktop\VoiceAssistant\haarcascade\haarcascade_frontalface_default.xml'.format(comp_name[9:]))

    video_capture = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k = cv2.waitKey(1)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('MyCamera', frame)

        if k%256 == 27: #ESC Pressed
            break

        elif k%256 == 32:
            # SPACE pressed
            img_name = "facedetect_webcam_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1


    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def havadurumu():
    # kyrenia (girne) weather report

    # talkUS("Please say to me where you are living now.")
    # city = listen()

    # ı used translate module for TR to EN
    translator = Translator()
    url = f"https://www.ntvhava.com/konum/girne/7-gunluk-hava-tahmini"
    #f"https://www.ntvhava.com/konum/{city}/7-gunluk-hava-tahmini"
    page = requests.get(url)
    source = page.content
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find_all('div', class_='summary seven-cols')
    hour = int(datetime.datetime.now().hour)

    if hour >= 1 and hour < 6:
        a = data[1].text.split()
        if a[2] == "Yağmurlu" or "Çoğunlukla Yağmurlu" in a[2:8]:
            info = translator.translate(' '.join(a[1:8]))
            uyari = " be careful and do not forget your umbrella " + chr(9730)
            talkUS(info.text + uyari)
        else:
            info = translator.translate(' '.join(a[1:4]))
            talkUS(info.text)

    elif hour >= 7 and hour <= 17:
        a = data[0].text.split()
        if a[2] == "Yağmurlu" or "Çoğunukla Yapmurlu" in a[2:8]:
            info = translator.translate(' '.join(a[1:8]))
            uyari = " be careful and do not forget your umbrella " + chr(9730)
            talkUS(info.text + uyari)
        else:
            info = translator.translate(' '.join(a[1:4]))
            talkUS(info.text + chr(9728))

    elif hour >= 18 and hour <= 24:
        a = data[1].text.split()
        if a[2] == "Yağmurlu" or "Çoğunlukla" in a[2:8]:
            info = translator.translate(' '.join(a[1:8]))
            uyari = " be careful and do not forget your umbrella " + chr(9730)
            talkUS(info.text + uyari)
        else:
            info = translator.translate(' '.join(a[1:4]))
            talkUS(info.text + chr(9728))
    else:
        a = data[0].text.split()
        if a[2] == "Yağmurlu" or "Çoğunlukla" in a[2:8]:
            info = translator.translate(' '.join(a[1:8]))
            uyari = " so be careful and if you going out side do not forget your umbrella " + chr(9730)
            talkUS(info.text + uyari)
        else:
            info = translator.translate(' '.join(a[1:4]))
            talkUS(info.text + chr(9728))


def yoltarifi():
    # more improvement will be coming.
    class YolTarif:
        def __init__(self):
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe", chrome_options=chrome_options)
            self.tarayici.maximize_window()
            self.tarayici.get('https://www.google.nl/maps/')
        def Islem(self):

            self.yol_butonu = WebDriverWait(self.tarayici,10).until(EC.element_to_be_clickable((By.ID, 'searchbox-directions')))
            self.yol_butonu.click()


            talkUS("Please say your start point") #Assistant ask for start point.
            self.baslangic = listen()
            self.baslangic_yeri = WebDriverWait(self.tarayici,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sb_ifc51"]/input')))
            self.baslangic_yeri.send_keys(self.baslangic)

            talkUS("Please say your end point") #Assistant ask for end point
            self.son_durak = listen()
            self.end_point = WebDriverWait(self.tarayici,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sb_ifc52"]/input')))
            self.end_point.click()
            self.end_point.send_keys(self.son_durak)
            self.end_point.send_keys(Keys.ENTER)

            talkUS("Just wait a second ı will tell you shortest way. Also you can see in your browser.")

            time.sleep(2)
            translator = Translator()
            source = self.tarayici.page_source
            soup = BeautifulSoup(source, 'html.parser')
            try:
                data = soup.find('h1', id='section-directions-trip-title-0')
                yol = data.text
                yol_info = translator.translate(yol) #I-80 through W43 to
                self.a = yol_info.text
            except:
                data2 = soup.find('h1', id='section-directions-trip-title-0')
                for item in data2:
                    items = item.find('span', jstcache='1020')
                    yol = items.text
                    yol_info = translator.translate(yol)
                    self.a = yol_info.text

            data1 = soup.find_all('div', class_='section-directions-trip-numbers')
            for item in data1:
                items = item.find('span')
                sure = items.text
                info = translator.translate(sure)
                talkUS("With a car from this road: " + self.a + info.text + " hours.")
                break
    yolTarif = YolTarif()
    yolTarif.Islem()




def wifi_passes():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
            'ISO-8859-1').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<20}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<20}|  {:<}".format(i, ""))

    talkUS("I print out already known wifi passwords")

def calendar_set():

    #there are some bugs but it will be fixed.
    # will be added more functionality.
    pyautogui.moveTo(1803, 1052)
    pyautogui.click()

    time.sleep(2)
    pyautogui.moveTo(1680, 758)
    pyautogui.click()
    talkUS("Please tell me something for event.")
    s = listen()
    lst = list(s)
    for i in lst:
        pyautogui.press(i)

    time.sleep(2)
    pyautogui.moveTo(1648, 947)
    pyautogui.click()

    talkUS("I set your event on default time.")

def write_code():

    user_id = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    url = "https://www.programiz.com/python-programming/examples"
    page = requests.get(url, headers=user_id)
    source = page.text
    soup = BeautifulSoup(source, 'lxml')

    data = soup.find_all('li')
    lst = []
    for item in data:
        items = item.find('a')
        try: lst.append("https://programiz.com" + items['href'])
        except: pass

    a = lst[:50]
    page = requests.get(choice(a))
    source = page.text
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find_all('div', class_='content')

    talkUS("I write basic python code.")

    for item in data:
        items = item.find('pre', class_='python-exec')
        print(items.text)



    talkUS("Here is the result of program")

    for item in data:
        items = item.find_all('pre')
        print(items[1].text)

def google_news():
    #Have some bugs but will be fixed.
    class GoogleNew:
        def __init__(self):
            self.user_id = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

            self.base_url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pIUWlnQVAB?hl=en-GB&gl=GB&ceid=GB%3Aen'
            self.NewsTitle = []
            self.NewsContent = []
            self.NewsUrl = []

        def Veri(self):
            page = requests.get(self.base_url, headers=self.user_id)
            source = page.text
            soup = BeautifulSoup(source, 'html.parser')

            data2 = soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')
            for item in data2:
                items = item.find('a')
                self.NewsTitle.append(items.text)

            a = len(self.NewsTitle)

            data = soup.find_all('a', class_='VDXfz')
            for item in data:
                self.NewsUrl.append("https://news.google.com/" + item['href'])
            del self.NewsUrl[a:]

            data3 = soup.find_all('h4', class_='ipQwMb ekueJc gEATFF RD0gLb')
            for item in data3:
                items = item.find('a')
                self.NewsContent.append(items.text)
            del self.NewsContent[a:]

            talkUS("I will read news headline and content")
            talkUS(self.NewsTitle[0])
            talkUS(self.NewsContent[0])
            talkUS("For more details shell ı open in your browser?")
            answer = listen()
            ans_lst = ['yes', "yes yes", "yes please", "please yes","open it","please open", "open please", "open in browser", "yeah open","yeah","yeah yeah"]
            if answer in ans_lst:
                webbrowser.open(self.NewsUrl[0])
            else:
                talkUS("Okey ı will not open in your browser.")

    google = GoogleNew()
    google.Veri()

def facebook_login():
    username = "facebook_user_mail"
    password = "facook_pass"
    class FacebookLog:
        def __init__(self,username,password):
            self.username = username
            self.password = password
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)

            self.browser = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe", chrome_options=chrome_options)
            self.browser.maximize_window()
            self.browser.get("https://www.facebook.com/")
        def Giris(self):

            user_name = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, 'email')))
            user_name.send_keys(self.username)

            user_pass = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, 'pass')))
            user_pass.send_keys(self.password)
            user_pass.send_keys(Keys.ENTER)

    facebook = FacebookLog(username,password)
    facebook.Giris()
def twit_login():
    usernm = "twit email/nickname"
    password2 = "twitpassword"
    class twitter:
        def __init__(self, usernm, password2):
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.browser = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe", chrome_options=chrome_options)

            self.usernm = usernm
            self.password2 = password2

        def twittSing(self):
            self.browser.get("https://twitter.com/login")
            self.browser.maximize_window()

            try:
                usernameInput = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.NAME,
                                                                                                        "session[username_or_email]")))
                usernameInput.send_keys(self.usernm)

                passwordInput = self.browser.find_element_by_name(
                    "session[password]")

                passwordInput.send_keys(self.password2, Keys.ENTER)
            except:
                print("Your login information is not true!")

    twit = twitter(usernm, password2)
    twit.twittSing()
