from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
root = Tk()
root.geometry('650x400')
root.title('Translator - Tanish')
root.iconbitmap('icon.ico')
root.resizable(False, False)
root.configure(bg='turquoise1')
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
###################################################################
def tt(e):
    try:
        word3 = TextBlob(varname1.get())
        lan = word3.detect_language()
        lan_todict = languages.get()
        lan_to = lang_dict[lan_todict]
        word3 = word3.translate(from_lang=lan, to=lan_to)
        label3.configure(text=word3)
        varname2.set(word3)
    except:
        print('Try another word...')
def main_exit():
    rr = messagebox.askyesnocancel('Notification', 'do you want to exit', parent=root)
    if(rr == TRUE):
        root.destroy()
def on_enterentry1(e):
    entry1["bg"] = "springgreen"
def on_enterentry2(e):
    entry2["bg"] = "springgreen"
def on_leaveentry1(e):
    entry1["bg"] = "yellow"
def on_leaveentry2(e):
    entry2["bg"] = "yellow"
def on_enterbtn1(e):
    btn1["bg"] = "springgreen"
    pass
def on_leavebtn1(e):
    btn1["bg"] = "yellow"
    pass
def on_enterbtn2(e):
    btn2["bg"] = "springgreen"

def on_leavebtn2(event = None):
    btn2["bg"] = "yellow"


#===================Combo box======================
languages = StringVar()
font_box = Combobox(root,width=40, textvariable=languages, state='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=400, y=0)
#===================Entry Box======================
varname1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varname1, font=('times', 20, 'italic bold'), bd=10)
entry1.place(x=170, y=50)

varname2 = StringVar()
entry2 = Entry(root, width=30, textvariable=varname2, font=('times', 20, 'italic bold'), bd=10)
entry2.place(x=170, y=130)

#======================= Labels ========================
label1 = Label(root, text='Enter words:', font=('times', 20, 'italic bold'), bg='turquoise1')
label1.place(x=10, y=50)
label2 = Label(root, text='Translated:', font=('times', 20, 'italic bold'), bg='turquoise1')
label2.place(x=10, y=130)
label3 = Label(root, text='', font=('times', 20, 'italic bold'), bg='turquoise1')
label3.place(x=10, y=170)
label4 = Label(root, text='@ Tanish Gupta', font=('times', 20, 'italic bold'), bg='turquoise1')
label4.place(x=400, y=350)

#==================== buttons -------------------
btn1 = Button(root, text='Click', bd=10, bg='yellow', activebackground='red',
              width=10, font=('times', 15, 'italic bold'), command=tt)
btn1.place(x=100, y=240)

btn2 = Button(root, text='Exit', bd=10, bg='yellow', activebackground='red', width=10,
              font=('times', 15, 'italic bold'), command =main_exit)
btn2.place(x=400, y=240)
root.bind('<Return>', tt)
########################### Binding #################
entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

btn1.bind('<Enter>', on_enterbtn1)
btn1.bind('<Leave>', on_leavebtn1)

btn2.bind('<Enter>', on_enterbtn2)
btn2.bind('<Leave>', on_leavebtn2)

root.mainloop()
