import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import pyttsx3
import threading
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
import tkinter as tk
from PIL import Image


text_content = "...............things you can make me do .................\n\n 1.say Open google\n\n 2.say Open Youtube\n\n 3. say Play Music\n\n4. say open weather forecast \n\n 5. TAlk to me like a friend \n\n 6. say open code to open visual studio code \n\n 7.say Tell me a story\n\n 8. Search wikipedia\n\n9. and alot else you can make  me do for you..........."
text_content2 ="...............things you can make me do .................\n\n 1.say Open google\n\n 2.say Open Youtube\n\n 3. say Play Music\n\n4. say open weather forecast \n\n 5. TAlk to me like a friend \n\n 6. say open code to open visual studio code \n\n 7.say Tell me a story\n\n 8. Search wikipedia\n\n9. and alot else you can make  me do for you..........."
def start():
    count=0
    threading.Thread(target=MainExecution).start()
    
def update_wraplength(event=None):
    # Get the current screen width
    screen_width = text_window.winfo_screenwidth()

    # Set wraplength based on a percentage of the screen width
    wrap_percentage = 0.15  # You can adjust this percentage as needed
    wrap_length = int(screen_width * wrap_percentage)

    # Update wraplength for the label
    scrollable_label.config(wraplength=wrap_length)

def create_wrapped_label(master, text, wraplength):
    label = tk.Label(master, text=text, wraplength=wraplength,height=100,width=200)
    label.pack()a
    return label

def create_frame(master, side, color):
    frame = tk.Frame(master, width=20, height=10, bg=color)
    frame.pack(side=side, fill="both", expand=True)
    return frame

root = tk.Tk()
root.title("Ai_Companion")
root.geometry("1000x650")
left_frame = create_frame(root, "left", "blue")
mid_frame = create_frame(root, "left", "black")
#right_frame = create_frame(root, "right", "green")


def MainExecution():
    global text_content
    print("")
    print("NAMASTE welcome to ARASTU")
    text_content=text_content + "\n\nNAMASTE welcome to ARASTU. " # type: ignore
    scrollable_label.configure(text=text_content)
    print("")
    Speak("NAMASTE welcome to ARASTU, i am your virtual assistant.")


    while True:

        Data = MicExecution()
        Data = str(Data)
        getResponse(Data)


def getResponse(Data):
        DataLen = len(Data)

        if "introduce yourself" in Data:
           Speak("Hello! I am your dedicated digital assistant, poised to simplify your daily tasks, streamline your workflow, and enhance overall efficiency. Whether you need information, assistance, or just a friendly chat, I'm here to make your digital experience seamless and enjoyable.")
        elif int(DataLen)<=1:
            pass
        if 'wikipedia' in Data:
            Speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")
        elif 'open weather forecast' in Data:
            webbrowser.open("accuweather.com")

        elif 'open google' in Data:
            webbrowser.open("google.com")
        elif 'play music' in Data:
            music_dir = 'C:\\Users\\nandi\\Music\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in Data:
            codePath = "C:\\Users\\nandi\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'hello' in Data:
            Speak(" hello master,  , i am there to help you out , you can check my list on the left of the screen to check what i can do.")

        elif 'i am fine' in Data:
            Speak("happy to hear this nandini , hope you will recover from your anxiety soon")

        elif 'oh you care for me' in Data:
            Speak(" yes my lord, am there for you ")

        elif 'bye' in Data:
            Speak("bye sir hope to meet you soon ")

        elif 'thank you' in Data:
            Speak("most welcome sir")
        elif 'favourtie singer' in Data:
            Speak("my favourite singer is ASha bhosale")
        elif'tell me a story' in Data:
            Speak("Once there was a Lion in the jungle who used to kill 2-3 animals daily for his meal. All animals went to him to tell, that daily one of them will come to him for his meal.So, the Lion agreed and this started going for many days. One day, it was Rabbit’s turn. When he was on his way he saw a well.Now he plans to kill the lion and save himself. He went to the lion and told him that, there is another lion who claims to be more powerful than him.Then the lion asks the rabbit to take him to that lion. The rabbit takes him to the well and said he lives here. When the lion looked in the well he saw his own reflection and jumped in the well and dies.Moral: Wisdom wins might.")

        elif 'I am feeling alone and depressed' in Data:
            Speak("boss am there to help you out please do not feel lonely,share with me and light up your vibes")   

        else:
          r= requests.get("http://api.brainshop.ai/get?bid=171149&key=vUQ8EIQHjwgyJHYI&uid=[uid]&msg="+ Data)
          response_json = r.json()
          d = response_json["cnt"]  
          print(d)
          Speak(d)


#Functions
#Speak  
def Speak(Text):
    global text_content
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"You : {Text}.")
    print("")
    text_content=text_content+"\n\nArastu: "+Text # type: ignore
    scrollable_label.configure(text=text_content)
    engine.say(Text)
    engine.runAndWait()

# 1. listen 
def Listen():
    global text_content
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        text_content=text_content+"\n\nListening..." # type: ignore
        scrollable_label.configure(text=text_content)
        r.energy_threshold=4000
        r.pause_threshold = 1
        audio = r.listen(source,8,None) # Listening Mode.....

    try:
        print("Recognizing...")
        text_content=text_content+"\n\nRecognizing..."
        scrollable_label.configure(text=text_content)
        query = r.recognize_google(audio,language="hi") # type: ignore
        

    except:
        return ""

    query = str(query).lower()
    text_content=text_content+"\n\nYou:"+query # type: ignore
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text #  type: ignore
    print(f"You : {data}.")
    # text_content=text_content+"\n\n YOU:"
    # scrollable_label.configure(text=text_content)
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data


file = "C:\\Users\\gcb\\ZENITH\\templates\\giphy.gif"
info = Image.open(file)
frames = info.n_frames
print(frames)

im = [tk.PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
gif_label = tk.Label(mid_frame, image="")
gif_label.configure(background='black')
gif_label.pack()

entry_frame= tk.Frame(mid_frame,width=250,height=30,bg="black")
entry_frame.pack()
entry_frame_var=tk.StringVar()
entry=tk.Entry(entry_frame,width=30,textvariable=entry_frame_var)
entry.grid(row=0,column=0)

def sendQuery():
    global entry_frame_var
    getResponse(entry_frame_var.get())

sendBtn=tk.Button(entry_frame,text="SEND",command=sendQuery)
sendBtn.grid(row=0,column=1)

b1 = tk.Button(mid_frame, text="Wake Up Me", fg="white", background="black", font=("Helvetica", 15),
              command=start)
b1.pack(pady=10)

# Create a canvas for the scrollable text
canvas = tk.Canvas(left_frame, bg="black", width=20, height=10)
canvas.pack(fill="both", expand=True)
'''
canvas2= tk.Canvas(right_frame, bg="black", width=400, height=10)
canvas2.pack(fill="both", expand=True)
'''

# Create a window within the canvas to hold the text
text_window = tk.Frame(canvas, bg="black", width=20, height=10)
canvas.create_window((100, 5), window=text_window, anchor="nw")
'''
text_window2 = tk.Frame(canvas2, bg="black", width=200, height=10)
canvas2.create_window((100, 5), window=text_window2, anchor="nw")
'''
custom_font = ("Arial", 12, "bold italic")
# Add the text to the text window
scrollable_label = tk.Label(text_window,justify="center" ,text=text_content, wraplength=200,  bg="black", fg="white",font=custom_font)
scrollable_label.pack()

'''scrollable_label2 = tk.Label(text_window2,justify="center", text=text_content2, wraplength=400,  bg="black", fg="white",font=custom_font)
scrollable_label2.pack()
'''
# scrollbar=tk.Scrollbar(left_frame,orient='vertical',command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')

'''scrollbar2=tk.Scrollbar(right_frame,orient='vertical',command=canvas2.yview)
canvas2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.place(relx=0.03,rely=0,relheight=1,anchor='ne')
'''
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
# Bind the mouse wheel event to enable scrolling
canvas.bind("<MouseWheel>", on_mousewheel)

# Update the canvas scrolling region
text_window.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
'''
text_window2.update_idletasks()
canvas2.config(scrollregion=canvas2.bbox("all"))
'''

def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0

    root.after(50, lambda: animation(count))
threading.Thread(target=animation(0)).start()

root.bind("<Configure>", update_wraplength)
root.mainloop()
