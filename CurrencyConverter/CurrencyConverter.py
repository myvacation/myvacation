import tkinter as tk
import requests

root = tk.Tk()

HEIGHT = 470
WIDTH = 470

def test_button(entry):
    print ("this is the entry" , entry)


def get_coversion(entry):
    #have to get your own access key
    your_access_key = "insert access key here"
    url = "http://api.currencylayer.com/live"
    params =  {"access_key" : your_access_key, "quotes" : "USD"}
    response= requests.get(url, params= params)
    conversions= (response.json())
    currency= (conversions["quotes"])
    labelausanswer["text"] = round(float(entry) * (currency["USDAUD"]), 2)
    labelbritishanswer["text"] = round(float(entry) * (currency["USDGBP"]) , 2)
    labeleuroanswer["text"] = round(float(entry) * (currency["USDEUR"]), 2)
    labelnzdanswer["text"] = round(float(entry) * (currency["USDNZD"]), 2)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_photo= tk.PhotoImage(file="pexels-sharon-mccutcheon-1566909.png")
background_label= tk.Label(root, image= background_photo)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root, bg="#00FF00")
frame.place(relx=.2, rely=.2, relwidth=.6, relheight=.6)

background_photo2= tk.PhotoImage(file="IMGP2041.png")
background_label2= tk.Label(frame, image= background_photo2)
background_label2.place(relwidth=1,relheight=1)


entry = tk.Entry(frame, bg="white", )
entry.place(relx=.5, rely=.2, relwidth=.30, relheight=.10)

button = tk.Button(frame, text="Convert!", bg="gray", fg="red", command= lambda: get_coversion(entry.get()))
button.place(relx= .8, rely= .20, relwidth=.20, relheight=.10)

label = tk.Label(frame, text="American Currency Converter", bg="silver", fg="blue")
label.place(relx=.20, rely=0, relwidth=.60, relheight=.10)

label1 = tk.Label(frame, text="Enter U.S. Dollar Amount", bg="silver")
label1.place(relx=0, rely=.2, relwidth=.50, relheight=.10)

labelaus = tk.Label(frame, text="Australian Dollars", bg="silver")
labelaus.place(relx=0, rely=.40, relwidth=.50, relheight=.10)

labelbritish = tk.Label(frame, text="British Pounds", bg="silver")
labelbritish.place(relx=0, rely=.52, relwidth=.50, relheight=.10)

labeleuro = tk.Label(frame, text="Euros", bg="silver")
labeleuro.place(relx=0, rely=.64, relwidth=.50, relheight=.10)

labelnzd = tk.Label(frame, text="New Zealand Dollars", bg="silver")
labelnzd.place(relx=0, rely=.76, relwidth=.50, relheight=.10)

labelausanswer = tk.Label(frame, text="", bg="white")
labelausanswer.place(relx=.5, rely=.40, relwidth=.30, relheight=.10)

labelbritishanswer = tk.Label(frame, text="", bg="white")
labelbritishanswer.place(relx=.50, rely=.52, relwidth=.30, relheight=.10)

labeleuroanswer = tk.Label(frame, text="", bg="white")
labeleuroanswer.place(relx=.50, rely=.64, relwidth=.30, relheight=.10)

labelnzdanswer = tk.Label(frame, text="", bg="white")
labelnzdanswer.place(relx=.50, rely=.76, relwidth=.30, relheight=.10)



root.mainloop()
