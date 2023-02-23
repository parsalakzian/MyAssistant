import speech_recognition as sr
import pyautogui
import screen_brightness_control as sbc
import datetime
import time
import webbrowser
import json
import os
import wolframalpha
import requests
import subprocess
from AppOpener import open, close
from googletrans import Translator
import flet as ft





wakeUpCall = ['ام جی','ان جی','سیستم','جی','اندی','حسین','انجیر','ال جی','ال','ام','ان','اینجا','اینجی']
exit_commands = ['خروج','تمام','خارج']

hi_commands = ['سلام']

prev_commands = ['قبلی','قبلیه']
next_commands = ['بعدی','بعدیه']
play_commands = ['پخش','پلی']
stop_commands = ['استاپ','قطع']

sound_commands = ['صدا','اهنگ','آهنگ','موسیقی']
sound_vol_down = ['کم','پایین']
sound_vol_up = ['زیاد','بالا']
sound_mute_commands = ['ببند','میوت']

bright_commands = ['نور']
bright_down_commands = ['کم','پایین']
bright_up_commands = ['زیاد','بالا']

appsname = {'Telegram':'Unigram','pictures':'Photos','Videos':'movies & tv','X Box':'xbox','Chrome':'Microsoft Edge','email':'Mail','Music':'media player'}






def main(page: ft.page):
    page.title = "My Assistant"
    page.window_height = 300
    page.window_width = 500
    page.theme_mode = ft.ThemeMode.SYSTEM
    pg = ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")






    def wishMe():
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            print("سلام صبح بخیر")
            text = "سلام صبح بخیر"
            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
            page.add(lbl)
            time.sleep(3)
            page.remove(lbl)
            text = ("")
        elif hour>=12 and hour<18:
            print("سلام ظهر بخیر")
            text = "سلام ظهر بخیر"
            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
            page.add(lbl)
            time.sleep(3)
            page.remove(lbl)
            text = ("")
        else:
            print("سلام شبت بخیر")
            text = "سلام شبت بخیر"
            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
            page.add(lbl)
            time.sleep(3)
            page.remove(lbl)
            text = ("")



    print("در حال آماده سازی ...")
    text = "... در حال آماده سازی"
    lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
    page.add(lbl , pg)
    time.sleep(3)
    page.remove(lbl , pg)
    text = ("")



    def voiceRec():
        r = sr.Recognizer()
        mic = sr.Microphone()
        while True:
            print("چه کاری از دستم بر میاد ؟")
            text = "چه کاری از دستم بر میاد ؟"
            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
            page.add(lbl)
            time.sleep(2)
            page.remove(lbl)
            text = ("")
            try:
                with mic as source:
                    audio = r.listen(source)
                    command = r.recognize_google (audio, language='fa-IR').lower()
                    if any(item in command for item in wakeUpCall):      
                        if any(item in command for item in hi_commands):
                            wishMe()
                        elif any(item in command for item in exit_commands):
                            print('...در حال خارج شدن')
                            text = '...در حال خارج شدن'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl , pg)
                            time.sleep(5)
                            page.remove(lbl , pg)
                            text = ("")
                            page.window_close()
                            break

                        elif any(item in command for item in prev_commands):
                            pyautogui.press('prevtrack')
                            print('زدم قبلی')
                            text = 'زدم قبلی'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")

                        elif any(item in command for item in next_commands):
                            pyautogui.press('nexttrack')
                            print('زدم بعدی')
                            text = 'زدم بعدی'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")

                        elif any(item in command for item in play_commands):
                            pyautogui.press('playpause')
                            print('پخش کردم')
                            text = 'پخش کردم'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")

                        elif any(item in command for item in stop_commands):
                            pyautogui.press('playpause')
                            print('قطع کردم')
                            text = 'قطع کردم'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")

                        elif any(item in command for item in sound_commands):
                            if any(item in command for item in sound_mute_commands):
                                pyautogui.press('volumemute')
                                print('میوت کردم')
                                text = 'میوت کردم'
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(2)
                                page.remove(lbl)
                                text = ("")
                            elif any(item in command for item in sound_vol_down):
                                pyautogui.press('volumedown', presses=10)
                                print('کم کردم')
                                text = 'کم کردم'
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(2)
                                page.remove(lbl)
                                text = ("")
                            elif any(item in command for item in sound_vol_up):
                                pyautogui.press('volumeup', presses=10)
                                print('زیاد کردم')
                                text = 'زیاد کردم'
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(2)
                                page.remove(lbl)
                                text = ("")

                        elif any(item in command for item in bright_commands):
                            if any(item in command for item in bright_up_commands):
                                sbc.set_brightness(100)
                                print('زیاد کردم')
                                text = 'زیاد کردم'
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(2)
                                page.remove(lbl)
                                text = ("")
                            elif any(item in command for item in bright_down_commands):
                                sbc.set_brightness(-10)
                                print('کم کردم')
                                text = 'کم کردم'
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(2)
                                page.remove(lbl)
                                text = ("")

                        elif 'یوتیوب' in command:
                            webbrowser.open_new_tab("https://www.youtube.com")
                            print("باز کردم")
                            text = "باز کردم"
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")
                            time.sleep(5)

                        elif 'گوگل' in command:
                            webbrowser.open_new_tab("https://www.google.com")
                            print("باز کردم")
                            text = "باز کردم"
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")
                            time.sleep(5)

                        elif 'جیمیل' in command:
                            webbrowser.open_new_tab("gmail.com")
                            print("باز کردم")
                            text = "باز کردم"
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")
                            time.sleep(5)

                        elif "هوا" in command:
                            api_key="8ef61edcf1c576d65d836254e11ea420"
                            base_url="https://api.openweathermap.org/data/2.5/weather?"
                            city_name="fardis"
                            complete_url=base_url+"appid="+api_key+"&q="+city_name+"&units=metric"
                            response = requests.get(complete_url)
                            x=response.json()
                            if x["cod"]!="404":
                                y=x["main"]
                                current_temperature = y["temp"]
                                current_humidiy = y["humidity"]
                                z = x["weather"]
                                weather_description = z[0]["description"]
                                ci = z[0]["icon"]
                                print(
                                    str(current_temperature) +
                                    " = دمای هوا" +
                                    "\n" +
                                    str(current_humidiy) + "%" +
                                    " = رطوبت هوا" +
                                    "\n" +
                                    str(weather_description) +
                                    " = هوا" )
                                text = str(current_temperature) + " = دمای هوا" + "\n" + str(current_humidiy) + "%" + " = رطوبت هوا" + "\n" + str(weather_description) + " = هوا" 
                                lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                                page.add(lbl)
                                time.sleep(5)
                                page.remove(lbl)
                                text = ("")

                        elif 'ساعت' in command:
                            strTime=datetime.datetime.now().strftime("%H:%M:%S")
                            print(f"است {strTime} ساعت")
                            text = f"ساعت {strTime} است"
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(3)
                            page.remove(lbl)
                            text = ("")

                        elif 'کی هستی' in command or 'چه کار' in command:
                            print('من دستیار شخصی شما هستم و میتوانم کار هایی همچون باز کردن برنامه ها و تغییر اهنگ و صدا و نور صفحه ، بررسی آب و هوا ، اعلام ساعت و انواع کار های درخواستی شما را انجام دهم .')
                            text = 'من دستیار شخصی شما هستم و میتوانم کار هایی همچون باز کردن برنامه ها و تغییر اهنگ و صدا و نور صفحه ، بررسی آب و هوا ، اعلام ساعت و انواع کار های درخواستی شما را انجام دهم .'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(10)
                            page.remove(lbl)
                            text = ("")

                        elif "چه کسی تو را ساخته" in command or "چه کسی تو رو ساخته" in command or "ساخته" in command:
                            print('من ساخته شده و طراحی شده به دست پارسا لکزیان هستم .')
                            text = 'من ساخته شده و طراحی شده به دست پارسا لکزیان هستم .'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(7)
                            page.remove(lbl)
                            text = ("")

                        elif 'سرچ'  in command:
                            new = command.replace("سرچ","")
                            new = new.replace("کن","")
                            new = new.replace("سیستم","")
                            new = new.replace("رو","")
                            new = new.replace("را","")
                            webbrowser.open_new_tab(new)
                            time.sleep(5)

                        elif "خاموش" in command or "بخواب" in command:
                            print("دارم خاموش میکنم ")
                            text = "دارم خاموش میکنم "
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl , pg)
                            time.sleep(10)
                            page.remove(lbl , pg)
                            text = ("")
                            subprocess.call(["shutdown", "/h"])

                        elif "باز کن" in command:
                            delc = ['سیستم','باز','کن','رو','را']
                            command = command.split()
                            if delc[0] in command:
                                command.remove(delc[0])
                            if delc[1] in command:
                                command.remove(delc[1])
                            if delc[2] in command:
                                command.remove(delc[2])
                            if delc[3] in command:
                                command.remove(delc[3])
                            if delc[4] in command:
                                command.remove(delc[4])
                            command = ' '.join([str(elem) for elem in command])
                            tr = Translator()
                            trt = tr.translate(command)
                            trt = trt.text
                            if trt in appsname:
                                appname = appsname.get(trt)
                            else:
                                appname = trt
                            open(appname)

                        elif "ببند" in command:
                            delc = ['سیستم','باز','کن','رو','را']
                            command = command.split()
                            if delc[0] in command:
                                command.remove(delc[0])
                            if delc[1] in command:
                                command.remove(delc[1])
                            if delc[2] in command:
                                command.remove(delc[2])
                            if delc[3] in command:
                                command.remove(delc[3])
                            if delc[4] in command:
                                command.remove(delc[4])
                            command = ' '.join([str(elem) for elem in command])
                            tr = Translator()
                            trt = tr.translate(command)
                            trt = trt.text
                            if trt in appsname:
                                appname = appsname.get(trt)
                            else:
                                appname = trt
                            close(appname)


                        else:
                            print('متوجه نشدم ؟')
                            text = 'متوجه نشدم ؟'
                            lbl = ft.Text(text , weight=400 , color = "Yellow" , size=35 , text_align = ft.TextAlign.CENTER )
                            page.add(lbl)
                            time.sleep(2)
                            page.remove(lbl)
                            text = ("")
            except Exception as e:
                print(e)
                r = sr.Recognizer()
                continue
            
        time.sleep(7)
        voiceRec()





    voiceRec()


    
    page.update()


ft.app(target=main , view=ft.WEB_BROWSER)
