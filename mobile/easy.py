'''
02-12-2022
WINTER HACK - FOCUS MOBILE APP

Aromal Pradeep
Arjun Jins
Adithya Kartha
Alan George Mathews
'''

import random

# GUI : kivy
import kivy
from kivy.app import App
from kivy.core.window import Window

from kivy.properties import ObjectProperty,StringProperty,NumericProperty

# UIX
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.animation import Animation

# Profiling
import cProfile

import os                              # OS controls
from hashlib import md5                # md5 hashing
from random import randint             # random
import requests                        # to verify mail
import ssl                             # to sent otp
import smtplib
from email.mime.text import MIMEText
import time                            # to sleep :)
import speech_recognition as speech    # Voice Recognition
from PIL import Image                  # to open image files
import subprocess                      # to open file location
from gtts import gTTS

import pygame
pygame.init()
pygame.mixer.init()

class OTP(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    count = 3
    # snext = 'screen0'
    
    def on_pre_enter(self, *args):
        
        global email
        
        # if admin : bypass otp
        if email == 'admin':
            #email = 'admin'
            self.manager.current = 'screen3'
            return
        
    
    def on_enter(self, *args):
        
        global email
        
        # generate OTP
        self.otp = ''
        for i in range(6):
            self.otp+=str(randint(0, 9))                # simple AES
        
        try:        

            # senting otp as mail
            '''
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"               # Server
            sender_email = "focusapp@zohomail.in"   # program mail
            receiver_email = email
            password = "focusapp"                       # program mail password
            
            message = """Subject: OTP for image encryption/decryption
            
            Your OTP is """ + str(self.otp)
            '''
            
            sender = 'focusapp@zohomail.in'
            recipient = email
            
            # Create message
            msg = MIMEText("Message text" + str(self.otp))
            msg['Subject'] = "OTP for Focus App"
            msg['From'] = sender
            msg['To'] = recipient
            
            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.in', 465)
            
            # Perform operations via server
            server.login('focusapp@zohomail.in', 'FOCUS@123')
            server.sendmail(sender, [recipient], msg.as_string())
            server.quit()
            
            '''
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                '''
        
        except :

            self.serror = "No Internet Connection."
        
        return
    
    def confirm(self):
        
        if self.ids.otp.text != self.otp:
            
            self.count-=1
            self.serror = str(self.count)+" Attempts left."
            
            if self.count < 1:
                
                self.serror += "Exiting..."

                # self.snext = 'screen0'
                self.manager.current = 'screen0'
            
            return
        
        # self.snext = 'screen3'
        self.manager.current = 'screen3'
        
        return
    
    def on_pre_leave(self, *args):

        # resetting
        self.ids.otp.text = ''
        self.serror = ''
        self.shint = ''
        self.count = 3

        # self.snext = 'screen0'
        
        return

class OTPS(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    count = 3
    # snext = 'screen0'
    
    def on_pre_enter(self, *args):
        
        global email
        
        # if admin : bypass otp
        if email == 'admin':
            #email = 'admin'
            self.manager.current = 'screen3'
            return
        
    
    def on_enter(self, *args):
        
        global email
        global user
        
        # generate OTP
        self.otp = ''
        for i in range(6):
            self.otp+=str(randint(0, 9))
        
        try:        

            # senting otp as mail
            
            sender = 'focusapp@zohomail.in'
            recipient = email
            
            # Create message
            msg = MIMEText("OTP : " + str(self.otp))
            msg['Subject'] = "OTP for Focus App"
            msg['From'] = sender
            msg['To'] = recipient
            
            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.in', 465)
            
            # Perform operations via server
            server.login('focusapp@zohomail.in', 'FOCUS@123')
            server.sendmail(sender, [recipient], msg.as_string())
            server.quit()
        
        except :

            self.serror = "No Internet Connection."
        
        return
    
    def confirm(self):
        
        if self.ids.otp.text != self.otp:
            
            self.count-=1
            self.serror = str(self.count)+" Attempts left."
            
            if self.count < 1:
                
                self.serror += "Account creation failed. Exiting..."
                
                '''
                global email
                
                if os.path.exists("data/private/"+email+".oec"):
                    os.remove("data/private/"+email+".oec")                
                '''
                
                os.remove("data/private/temp.oec")
                
                # self.snext = 'screen0'
                self.manager.current = 'screen0'
            
            return
        
        # create account
        global user
        with open("data/private/"+ user +".oec","w") as f:
            with open("data/private/temp.oec","r") as p:
                f.write(p.read())
        
        os.remove("data/private/temp.oec")
        
        # self.snext = 'screen_temp'
        self.manager.current = 'screen3'
        
        return
    
    def on_pre_leave(self, *args):

        # resetting
        self.ids.otp.text = ''
        self.serror = ''
        self.shint = ''
        self.count = 3

        # self.snext = 'screen0'
        
        return

# Screen_0 : Loading
class ScreenZero(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def on_pre_enter(self, *args):
        
        quotes = ["The body achieves what the mind believes.",
                  "Tough times don’t last. Tough people do.",
                  "No more excuses."]
        
        self.shint = random.choice(quotes)
        return

# Screen_1 : Log_in
class ScreenOne(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def password(self):
        
        # verifies entered mail and password
        if not os.path.exists("data/private/"+self.ids.einput.text+".oec"):
            self.serror = "Account does not exist."
            return
        
        with open("data/private/"+self.ids.einput.text+".oec","r") as f:
            passw = f.read()
        
        # verifies password
        if md5(self.ids.pinput.text.encode()).hexdigest() == passw:
            
            self.manager.current = 'screen3' 
            
        else:
            self.serror = "Invalid credentials"
            
        return
    
    def on_pre_enter(self, *args):
        
        #time.sleep(2)
        
        # resetting
        self.ids.einput.text = ''
        self.ids.pinput.text = ''
        self.serror = ''
        self.shint = ''
        
# Screen_2 : Sign_up
class ScreenTwo(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def test(self):
        
        # verifies entered mail and password
        if os.path.exists("data/private/"+self.ids.einput.text+".oec"):
            self.serror = "Account exists."
            return
        
        if os.path.exists("data/private/"+self.ids.uinput.text+".oec"):
            self.serror = "Account exists."
            return
    
    def password(self):
        
        # check if account exist
        if os.path.exists("data/private/"+self.ids.einput.text+".oec"):
            self.serror = "Account exists."
            return
        
        # check if valid mail id
        try:
            response = requests.get(
                "https://isitarealemail.com/api/email/validate",
                params = {'email': self.ids.einput.text})
            
            status = response.json()['status']
            if status == 'invalid':
                self.serror = "Invalid mail id."
                return
        
        except:
            self.serror = "No internet connection."
            return
    
        with open("data/private/temp.oec","w") as f:
            f.write(md5(self.ids.pinput.text.encode()).hexdigest())
            
        # email
        global email
        global user
        email = self.ids.einput.text
        user = self.ids.uinput.text
            
        self.serror = 'Creating account.'            
        self.manager.current = 'OTPS' # OTP

        return
    
    def on_pre_enter(self, *args):
        
        #time.sleep(2)
        
        # resetting
        self.ids.einput.text = ''
        self.ids.pinput.text = ''
        self.ids.uinput.text = ''
        self.serror = ''
        self.shint = ''
        return
    
# Screen_3 : Menu - focus / task
class ScreenThree(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def on_pre_enter(self, *args):
        
        self.shint = user
        return
    
    
# Screen_4 : Focus 
class ScreenFour(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    a = NumericProperty(100)
    
    def play(self, *args):      
        pygame.mixer.music.stop()
        return
    
    def playl(self, *args):  
        file = 'data/music/lofi.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
        return
    
    def playr(self, *args):      
        file = 'data/music/rain.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
        return
    
    def playrr(self, *args):      
        file = 'data/music/morerain.mp3'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
        return
    
# Screen_5 : Task
class ScreenFive(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def on_pre_leave(self, *args):

        # resetting
        self.serror = ''
        self.shint = ''

        return
    
    def f(self, fid,*args):   
        return
    
    def sets(self, *args):
        
        if self.ids.o1.text:
            mytext = self.ids.o1.text  
            mytext = 'you have set reminder, '+mytext
            myobj = gTTS(text=mytext, lang='en', slow=False)
            file = 'temp1.mp3'
            myobj.save(file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pygame.event.wait()

        if self.ids.o2.text:
            mytext = self.ids.o2.text  
            myobj = gTTS(text=mytext, lang='en', slow=False)
            file = 'temp2.mp3'
            myobj.save(file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pygame.event.wait()
        
        if self.ids.o3.text:
            mytext = self.ids.o3.text  
            myobj = gTTS(text=mytext, lang='en', slow=False)
            file = 'temp3.mp3'
            myobj.save(file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pygame.event.wait()
        
        if self.ids.o4.text:
            mytext = self.ids.o4.text  
            myobj = gTTS(text=mytext, lang='en', slow=False)
            file = 'temp4.mp3'
            myobj.save(file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            pygame.event.wait()
        
        return
    
    def clears(self, *args):
        return
    

# Screen_6 : Profile [Avatar,Pet,Reward points,logout]
class ScreenSix(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    sselect = StringProperty()
    
    def on_pre_enter(self, *args):
        
        global user
        self.ids.shint.text = user
    
    def on_pre_leave(self, *args):

        # resetting
        self.serror = ''
        self.shint = ''
        self.sselect = ''

        return


# Screen_7 : Community [page]
class ScreenSeven(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    def on_pre_enter(self, *args):
        
        self.shint = ""
        
    def f(self): # About us
        
        self.shint = ""
    
    def k(self): # About project
        
        self.shint = ""   


# Screen_8 : Settings [Theme,sounds,about us,about project]
class ScreenEight(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    pass

# Screen_9 : Settings [Theme,sounds,about us,about project]
class ScreenNine(Screen):
    
    serror = StringProperty()
    shint = StringProperty()
    
    pass

# screen manager
class Manager(ScreenManager):
    
    screen_zero = ObjectProperty(None)

class easyApp(App):
        
    def build(self):
        
        # Window
        self.title = 'Focus'
        self.icon = 'static/icon.png'
        Window.size = (360,640)
        
        #Clock.schedule_interval(lambda dt: self.update_time(), 1)
        
        return Manager()
    
    def on_start(self):

        # Profile
        self.profile = cProfile.Profile()
        self.profile.enable()

        return
    
    def stop(self):
        
        # Profile
        self.profile.disable()
        self.profile.dump_stats('data/profile/lastrun.profile')
        
        # kivy
        Window.close()
        
        return
    
    def update_time(self):
        
        return

if __name__ == "__main__":
    
    user = ""
    email = ''
    
    # App start
    main = easyApp()
    main.run()