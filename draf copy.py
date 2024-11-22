import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from PIL import Image
from tabulate import tabulate
from tkinter import messagebox
import webbrowser
while True:
    book1=0
    book2=0
    book3=0
    book4=0
    book5=0
    book6=0
    book7=0
    book8=0
    book9=0
    book10=0
    book11=0
    book12=0
    book13=0
    book14=0
    book15=0
    book16=0
    book17=0
    book18=0
    book19=0
    book20=0
    book21=0
    book22=0
    book23=0
    book24=0
    book25=0
    book26=0
    book27=0

    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql', database='books')
    cursor = mydb.cursor(buffered=True)
    cursor.execute('select*from books')

    ID = ['w12', 'r32', 't67', '56e']
    window=tk.Tk()
    window.title("étagère à livres")
    window.geometry("600x400")
    window.geometry("+400+250")
    window.configure(bg="#BF3EFF")
    img=tk.PhotoImage(file="/Users/garimagrover/Desktop/avatar.png")
    img1=tk.Label(window,image=img,bg="#BF3EFF")
    img1.place(x=32,y=127)
    label1=tk.Label(window,text="USER LOGIN",bg="#BF3EFF",)
    label1.config(font=("Courier", 45))
    label1.place(x=160,y=50)
    logo0=Image.open("/Users/garimagrover/Desktop/logo.png")
    rlogo=logo0.resize((68,75))
    logo=ImageTk.PhotoImage(rlogo)
    lab8=tk.Label(window,image=logo,bg="#BF3EFF")
    lab8.image=logo
    lab8.place(x=517,y=2)

    def official():
        window.destroy()
        root = tk.Tk()
        #root.configure(bg="#87CEFA")
        root.title("OFFICIAL  INTERFACE")
        root.geometry("700x400")
        root.geometry("+390+250")
        image = Image.open("/Users/garimagrover/Desktop/librvec.png")
        resize = image.resize((300, 400))
        img = ImageTk.PhotoImage(resize)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=0, y=0)
        label1 = tk.Label(root, text="OFFICIAL ID" )
        label1.config(font=("Courier", 40))
        label1.place(x=360, y=30)
        label2 = tk.Label(root,text="Enter your Official ID")
        label2.config(font=("Courier", 27))
        label2.place(x=320,y=135)
        enter=tk.Entry(root,width=27,relief="sunken")
        enter.config(highlightbackground="blue", highlightcolor="blue")
        enter.place(x=380,y=220)

        def official1():
            a=enter.get()
            if a in ID:
                root.destroy()
                frame=tk.Tk()
                frame.geometry("750x400")
                frame.geometry("+390+250")
                frame.config(bg="#FFEFD5")
                frame.title("STAFF  SECTION")

                def view_rec():
                    l = []
                    l1 = ['SNO', 'B_ID', 'B_NAME', 'B_CODE', 'QTY', 'AUTHOR', 'COST', 'GENRE']
                    l.append(l1)
                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql', database='books')
                    cursor = mydb.cursor(buffered=True)
                    cursor.execute('select*from books')
                    for i in cursor:
                        l.append(i)
                    l=tabulate(l,headers='firstrow', tablefmt='fancy_grid')
                    rec_scrn=tk.Tk()
                    rec_scrn.title("RECORDS")
                    rec_scrn.geometry("885x745")
                    rec_scrn.configure(bg='black')
                    text=tk.Text(rec_scrn,height=50,width=110)
                    text.insert(tk.END,l)
                    text.config(font=("Courier", 13),bg='black',fg='white')
                    text.pack(side=tk.LEFT)
                    def ok1():
                        rec_scrn.destroy()
                        mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                        cursor = mydb.cursor(buffered=True)
                        cursor.execute('select*from books')

                    ok=tk.Button(rec_scrn,text="BACK",command=ok1,height=2,width=8,fg='black')
                    ok.place(x=150,y=710)
                    rec_scrn.mainloop()
                def delete():
                    del_scrn=tk.Toplevel()
                    del_scrn.title("DELETE")
                    del_scrn.geometry("590x340")
                    del_scrn.geometry("+400+250")
                    del_scrn.config(bg="#03A89E")
                    i=tk.PhotoImage(file="/Users/garimagrover/Desktop/pile.png")
                    label10=tk.Label(del_scrn,image=i)
                    label10.image=i
                    label10.place(x=0,y=0)
                    label9=tk.Label(del_scrn,text="Enter the book name",bg="#03A89E")
                    label9.config(font=("Courier", 21))
                    label9.place(x=305,y=70)
                    enter1=tk.Entry(del_scrn)
                    enter1.place(x=332,y=131)

                    def next():
                        b=enter1.get()
                        mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                        cursor = mydb.cursor(buffered=True)
                        cursor.execute('select*from books')
                        for i in cursor:
                            if b.title()==i[2].title():
                                mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                cursor = mydb.cursor(buffered=True)
                                cursor.execute('select*from books')
                                SQ = "Delete from books where b_name='{}'".format(b.title())
                                cursor.execute(SQ)
                                mydb.commit()
                                msg1= 'DONE '+"\U0001F44D"
                                messagebox.showinfo(message=msg1)

                    bt4=tk.Button(del_scrn,text="DELETE",height=1,width=8,command=next)
                    bt4.config(font=("Courier", 21))
                    bt4.place(x=387,y=190)
                    del_scrn.mainloop()

                def update():
                    updt_scrn=tk.Toplevel()
                    updt_scrn.geometry("795x600")
                    updt_scrn.geometry("+400+160")
                    updt_scrn.config(bg="#4169E1")
                    updt_scrn.title("UPDATE")
                    ima=tk.PhotoImage(file="/Users/garimagrover/Desktop/bst.png")
                    l1=tk.Label(updt_scrn,image=ima,bg="#4169E1")
                    l1.image=ima
                    l1.pack(side=tk.LEFT)
                    cmb = ttk.Combobox(updt_scrn)
                    cmb['values'] = ('Quantity', 'Cost')
                    cmb.config(font=("Courier", 15))
                    cmb.place(x=545,y=100)
                    def update1():
                        if cmb.get()=="Cost":
                            bt0.destroy()
                            ent=tk.Entry(updt_scrn)
                            ent1= tk.Entry(updt_scrn)
                            l0=tk.Label(updt_scrn,text="Book name -:",bg="#4169E1")
                            l0.config(font=("Courier", 18))
                            l0.place(x=550,y=190)
                            l3 = tk.Label(updt_scrn, text="New cost -:", bg="#4169E1")
                            l3.config(font=("Courier", 18))
                            l3.place(x=550, y=260)
                            ent.place(x=555,y=220)
                            ent1.place(x=555, y=290)
                            def update2():
                                mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                cursor = mydb.cursor(buffered=True)
                                cursor.execute('select*from books')
                                c=ent.get()
                                d=ent1.get()
                                for i in cursor:
                                    if c.title()==i[2].title():
                                        SQ = "update books set cost={} where b_name='{}'".format(d, c)
                                        cursor.execute(SQ)
                                        mydb.commit()
                                        msg = 'DONE '+"\U0001F44D"
                                        messagebox.showinfo(message=msg)

                            bt5 = tk.Button(updt_scrn, text="UPDATE", height=2, width=11, command=update2)
                            bt5.place(x=600, y=350)

                        if cmb.get() == "Quantity":
                            bt0.destroy()
                            ent = tk.Entry(updt_scrn)
                            ent1 = tk.Entry(updt_scrn)
                            l0 = tk.Label(updt_scrn, text="Book name -:", bg="#4169E1")
                            l0.config(font=("Courier", 18))
                            l0.place(x=550, y=190)
                            l3 = tk.Label(updt_scrn, text="Quantity -:", bg="#4169E1")
                            l3.config(font=("Courier", 18))
                            l3.place(x=550, y=260)
                            ent.place(x=555, y=220)
                            ent1.place(x=555, y=290)

                            def update3():
                                mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                cursor = mydb.cursor(buffered=True)
                                cursor.execute('select*from books')
                                c = ent.get()
                                d = ent1.get()
                                for i in cursor:
                                    if c.title() == i[2].title():
                                        SQ = "update books set Qty={} where b_name='{}'".format(d, c)
                                        cursor.execute(SQ)
                                        mydb.commit()
                                        msg = 'DONE ' + "\U0001F44D"
                                        messagebox.showinfo(message=msg)

                            bt5 = tk.Button(updt_scrn, text="UPDATE", height=2, width=11, command=update3)
                            bt5.place(x=600, y=350)
                            bt5 = tk.Button(updt_scrn, text="UPDATE", height=2, width=11, command=update4)
                            bt5.place(x=600, y=350)

                    bt0=tk.Button(updt_scrn,text="OK",height=2,width=5,command=update1)
                    bt0.place(x=635,y=160)
                    updt_scrn.mainloop()

                def add():
                    ad=tk.Toplevel()
                    ad.geometry("760x600")
                    ad.geometry("+400+150")
                    ad.title("ADD RECORD")
                    ad.config(bg="black")
                    img0=tk.PhotoImage(file="/Users/garimagrover/Desktop/gradient1.png")
                    lab0=tk.Label(ad,image=img0,bg="black")
                    lab0.image=img0
                    lab0.pack()
                    a1=0
                    for i in cursor:
                        a1+=1
                    a1+1

                    la1=tk.Label(ad,text="ID",bg="black",fg="white")
                    la1.config(font=("Courier", 25))
                    la1.place(x=50,y=50)
                    la2 = tk.Label(ad, text="Name", bg="black", fg="white")
                    la2.config(font=("Courier", 25))
                    la2.place(x=50, y=130)
                    la3 = tk.Label(ad, text="Code", bg="black", fg="white")
                    la3.config(font=("Courier", 25))
                    la3.place(x=50, y=210)
                    la4 = tk.Label(ad, text="Quantity", bg="black", fg="white")
                    la4.config(font=("Courier", 25))
                    la4.place(x=50, y=290)
                    la5 = tk.Label(ad, text="Author", bg="black", fg="white")
                    la5.config(font=("Courier", 25))
                    la5.place(x=50, y=360)
                    la6 = tk.Label(ad, text="Cost", bg="black", fg="white")
                    la6.config(font=("Courier", 25))
                    la6.place(x=50, y=430)
                    la7 = tk.Label(ad, text="Genre", bg="black", fg="white")
                    la7.config(font=("Courier", 25))
                    la7.place(x=50, y=500)
                    e1=tk.Entry(ad)
                    e1.place(x=410,y=50)
                    e2 = tk.Entry(ad)
                    e2.place(x=410, y=130)
                    e3 = tk.Entry(ad)
                    e3.place(x=410, y=210)
                    e4 = tk.Entry(ad)
                    e4.place(x=410, y=290)
                    e5 = tk.Entry(ad)
                    e5.place(x=410, y=360)
                    e6 = tk.Entry(ad)
                    e6.place(x=410, y=430)
                    e7 = tk.Entry(ad)
                    e7.place(x=410, y=500)

                    def a_rec():
                        mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                        cursor = mydb.cursor(buffered=True)
                        cursor.execute('select*from books')
                        g1 = e1.get()
                        g2 = e2.get()
                        g3 = e3.get()
                        g4 = e4.get()
                        g5 = e5.get()
                        g6 = e6.get()
                        g7 = e7.get()
                        SQ = "insert into books values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        val=(a1,g1.title(),g2,g3,g4,g5,g6,g7)
                        cursor.execute(SQ,val)
                        mydb.commit()
                        msg = 'DONE ' + "\U0001F44D"
                        messagebox.showinfo(message=msg)
                        ad.destroy()


                    b=tk.Button(ad,text="ADD",command=a_rec,height=2,width=5)
                    b.place(x=300,y=550)

                    ad.mainloop()



                rad1 = tk.Radiobutton(frame, text='UPDATE',bg="#FFEFD5",command=update)
                rad2 = tk.Radiobutton(frame, text='DELETE',bg="#FFEFD5",command=delete)
                rad3 = tk.Radiobutton(frame, text='VIEW BOOKS',bg="#FFEFD5",command=view_rec)
                rad4 = tk.Radiobutton(frame, text='ADD RECORD', bg="#FFEFD5",command=add)
                rad1.place(x=270,y=150)
                rad1.config(font=("Courier", 35))
                rad2.place(x=270, y=210)
                rad2.config(font=("Courier", 35))
                rad3.place(x=270, y=270)
                rad3.config(font=("Courier", 35))
                rad4.place(x=270, y=330)
                rad4.config(font=("Courier", 35))
                image = Image.open("/Users/garimagrover/Desktop/bookvec.png")
                resize = image.resize((200, 400))
                img = ImageTk.PhotoImage(resize)
                label1 = tk.Label(image=img,bg="#FFEFD5")
                label1.image = img
                label1.place(x=0, y=0)
                label6=tk.Label(frame,text='"I have always imagined that Paradise \n \n will be a kind of library"',bg="#FFEFD5")
                label6.config(font=("Courier", 23))
                def show():
                    label6.place(x=210, y=40)
                frame.after(220,show)

                frame.mainloop()





        bt3 = tk.Button(root, text="Proceed",command=official1,activeforeground='cyan')
        bt3.config(font=("Courier", 20))
        bt3.place(x=540,y=290,height=40,width=100)

        root.mainloop()
    def shop():
        window.destroy()
        custom = tk.Tk()
        custom.geometry("920x650")
        custom.geometry("+330+80")
        custom.config(bg="#F0F0F0")
        custom.title("WELCOME")
        i9 = tk.PhotoImage(file="/Users/garimagrover/Desktop/v3.png")
        labe1 = tk.Label(custom, image=i9, bg="#F0F0F0")
        labe1.image = i9
        labe1.place(x=40, y=65)
        labe2 = tk.Label(custom, text="étagère  à  livres", bg="#F0F0F0")
        labe2.config(font=("Chalkduster", 85, "bold"))
        labe2.place(x=31, y=17)

        def customer():
            custom.destroy()
            cust = tk.Tk()
            cust.title("SHOP")
            cust.geometry("1450x900")
            cust.config(bg="#FFFFE0")
            l3 = tk.Label(cust, text="étagère à livres", bg="#FFFFE0")
            l3.config(font=("Chalkduster", 30, "bold"))
            l3.place(x=17, y=5)
            logo0=Image.open("/Users/garimagrover/Desktop/logo.png")
            rlogo=logo0.resize((55,55))
            logo=ImageTk.PhotoImage(rlogo)
            lab8=tk.Label(cust,image=logo,bg="#FFFFE0")
            lab8.image=logo
            lab8.place(x=305,y=0)

            def kill8():
                kill_scn = tk.Toplevel()
                kill_scn.title("The Killing Tide")
                kill_scn.geometry("600x400")
                kill_scn.geometry("+400+150")
                kill_scn.config(bg="black")
                kill00 = Image.open("/Users/garimagrover/Desktop/killing.png")
                rkill0 = kill00.resize((180, 275))
                kill_0 = ImageTk.PhotoImage(rkill0)
                killl0 = tk.Label(kill_scn, image=kill_0, bg="black")
                killl0.image = kill_0
                killl0.place(x=7, y=30)
                la2 = tk.Label(kill_scn,text="The Killing Tide\n BY \n Dany Pettrey \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                m0 = 'select cost from books where b_code ="KT/430"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(kill_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=300, y=230)

                def cart0():
                    global book2
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book2 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(kill_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.danipettrey.com/the-killing-tide")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(kill_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def kill_des():
                    kill_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(kill_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=kill_des)
                back02.place(x=15, y=330)
                kill_scn.mainloop()

            def kots8():
                kots_scn = tk.Toplevel()
                kots_scn.title("Kafka on the Shore")
                kots_scn.geometry("600x400")
                kots_scn.geometry("+400+250")
                kots_scn.config(bg="black")
                kots00 = Image.open("/Users/garimagrover/Desktop/kots.png")
                rkots0 = kots00.resize((180, 275))
                kots_0 = ImageTk.PhotoImage(rkots0)
                kotsl0 = tk.Label(kots_scn, image=kots_0, bg="black")
                kotsl0.image = kots_0
                kotsl0.place(x=7, y=30)
                la2 = tk.Label(kots_scn,text="Kafka on the Shore\n BY \n Haruki Murakami \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=255, y=50)
                m0 = 'select cost from books where b_code ="KS/021"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(kots_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=300, y=230)

                def cart0():
                    global book3
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book3 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(kots_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.harukimurakami.com/reading_guide/kafka-on-the-shore-readers-guide")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(kots_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def kots_des():
                    kots_scn.destroy()

                back3 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback3 = back3.resize((90, 60))
                back_3 = ImageTk.PhotoImage(rback3)
                back03 = tk.Button(kots_scn, image=back_3, height=55, width=80, highlightbackground="black",
                                   command=kots_des)
                back03.place(x=15, y=330)
                kots_scn.mainloop()

            def edu8():
                edu_scn = tk.Toplevel()
                edu_scn.title("Educated")
                edu_scn.geometry("600x400")
                edu_scn.geometry("+400+150")
                edu_scn.config(bg="black")
                edu00 = Image.open("/Users/garimagrover/Desktop/educated.png")
                redu0 = edu00.resize((180, 275))
                edu_0 = ImageTk.PhotoImage(redu0)
                edul0 = tk.Label(edu_scn, image=edu_0, bg="black")
                edul0.image = edu_0
                edul0.place(x=7, y=30)
                la1 = tk.Label(edu_scn, text="  Educated \n BY \n Tara Westover \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la1.config(font=("Courier", 27, "bold"))
                la1.place(x=280, y=50)
                m0 = 'select cost from books where b_code ="ET/504"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(edu_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=300, y=230)

                def cart0():
                    global book1
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book1 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(edu_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open_new("https://www.sparknotes.com/lit/educated/summary/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(edu_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def edu_des():
                    edu_scn.destroy()

                back1 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback1 = back1.resize((90, 60))
                back_1 = ImageTk.PhotoImage(rback1)
                back01 = tk.Button(edu_scn, image=back_1, height=55, width=80, highlightbackground="black",command=edu_des)
                back01.place(x=15, y=330)
                edu_scn.mainloop()

            def ttp8():
                ttp_scn = tk.Toplevel()
                ttp_scn.title("Train to Pakistan")
                ttp_scn.geometry("600x400")
                ttp_scn.geometry("+400+150")
                ttp_scn.config(bg="black")
                ttp00 = Image.open("/Users/garimagrover/Desktop/ttp.png")
                rttp0 = ttp00.resize((180, 275))
                ttp_0 = ImageTk.PhotoImage(rttp0)
                ttpl0 = tk.Label(ttp_scn, image=ttp_0, bg="black")
                ttpl0.image = ttp_0
                ttpl0.place(x=7, y=30)
                la2 = tk.Label(ttp_scn, text="Train to Pakistan\n BY \n Khushwant Singh \n \n  \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=255, y=50)
                m0 = 'select cost from books where b_code ="TP/062"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(ttp_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=300, y=230)

                def cart0():
                    global book4
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book4 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(ttp_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Train_to_Pakistan")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(ttp_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def ttp_des():
                    ttp_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(ttp_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=ttp_des)
                back02.place(x=15, y=330)
                ttp_scn.mainloop()

            def mart8():
                mart_scn = tk.Toplevel()
                mart_scn.title("The Martian")
                mart_scn.geometry("600x400")
                mart_scn.geometry("+400+150")
                mart_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/martian.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(mart_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(mart_scn, text="The Martian\n BY \n Andy Weir \n \n \u2B50 \u2B50 \u2B50 \u2B50 \u2B50",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="M/897"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(mart_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book5
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book5 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(mart_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/The_Martian_(film)")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(mart_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def mart_des():
                    mart_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(mart_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=mart_des)
                back02.place(x=15, y=330)
                mart_scn.mainloop()

            def thief8():
                thief_scn = tk.Toplevel()
                thief_scn.title("The Thief")
                thief_scn.geometry("600x400")
                thief_scn.geometry("+400+150")
                thief_scn.config(bg="black")
                thief00 = Image.open("/Users/garimagrover/Desktop/thief.png")
                rthief0 = thief00.resize((180, 275))
                thief_0 = ImageTk.PhotoImage(rthief0)
                thiefl0 = tk.Label(thief_scn, image=thief_0, bg="black")
                thiefl0.image = thief_0
                thiefl0.place(x=7, y=30)
                la2 = tk.Label(thief_scn, text="The Thief\n BY \nFuminori Nakamura \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=265, y=50)
                m0 = 'select cost from books where b_code ="TT/780"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(thief_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book7
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book7 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(thief_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.mysterytribune.com/good-read-review-thief-fuminori-nakamura/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(thief_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def thief_des():
                    thief_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(thief_scn, image=back_2, height=55, width=80, highlightbackground="black",command=thief_des)
                back02.place(x=15, y=330)
                thief_scn.mainloop()

            def bec8():
                bec_scn = tk.Toplevel()
                bec_scn.title("Becoming")
                bec_scn.geometry("600x400")
                bec_scn.geometry("+400+150")
                bec_scn.config(bg="black")
                bec00 = Image.open("/Users/garimagrover/Desktop/becoming.png")
                rbec0 = bec00.resize((185, 275))
                bec_0 = ImageTk.PhotoImage(rbec0)
                becl0 = tk.Label(bec_scn, image=bec_0, bg="black")
                becl0.image = bec_0
                becl0.place(x=7, y=30)
                la2 = tk.Label(bec_scn,text="Becoming\n BY \n  Michelle Obama \n \n \u2B50 \u2B50 \u2B50 \u2B50 \u2B50",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="BM/061"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(bec_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=295, y=230)

                def cart0():
                    global book6
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book6 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(bec_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/Becoming_(book)")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(bec_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def bec_des():
                    bec_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(bec_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=bec_des)
                back02.place(x=15, y=330)
                bec_scn.mainloop()

            def malgudi8():
                malgudi_scn = tk.Toplevel()
                malgudi_scn.title("Malgudi Days")
                malgudi_scn.geometry("600x400")
                malgudi_scn.geometry("+400+150")
                malgudi_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/malgudi.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(malgudi_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(malgudi_scn, text="Malgudi Days\n BY \n R.K.Narayan \n \n \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="MD/094"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(malgudi_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book8
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book8 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(malgudi_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.supersummary.com/malgudi-days/summary/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(malgudi_scn, image=info_1, height=55, width=70, highlightbackground="black",
                                command=web)
                ib1.place(x=280, y=320)

                def malgudi_des():
                    malgudi_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(malgudi_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=malgudi_des)
                back02.place(x=15, y=330)
                malgudi_scn.mainloop()

            def tres8():
                tres_scn = tk.Toplevel()
                tres_scn.title("Treasure Island")
                tres_scn.geometry("600x400")
                tres_scn.geometry("+400+150")
                tres_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/treasure.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(tres_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(tres_scn,text="Treasure Island\n BY \nRobert Louis Stevenson \n \n \u2B50 \u2B50 \u2B50 \u2B50 \u2B50",bg="black", fg="white")
                la2.config(font=("Courier", 25, "bold"))
                la2.place(x=230, y=50)
                m0 = 'select cost from books where b_code ="TI/783"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(tres_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book9
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book9 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(tres_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.lancsngfl.ac.uk/curriculum/literacy/lit_site/html/fiction/treasure_is/story.htm")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(tres_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def tres_des():
                    tres_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(tres_scn, image=back_2, height=55, width=80, highlightbackground="black",command=tres_des)
                back02.place(x=15, y=330)
                tres_scn.mainloop()

            def mal8():
                mal_scn = tk.Toplevel()
                mal_scn.title("Malibu Rising")
                mal_scn.geometry("600x400")
                mal_scn.geometry("+400+150")
                mal_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/malibu.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(mal_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(mal_scn, text="Malibu Rising\n BY \n Taylor Jenkins \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="MR/523"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(mal_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book10
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book10 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(mal_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://the-bibliofile.com/malibu-rising/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(mal_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def mal_des():
                    mal_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(mal_scn, image=back_2, height=55, width=80, highlightbackground="black",command=mal_des)
                back02.place(x=15, y=330)
                mal_scn.mainloop()

            def train8():
                train_scn = tk.Toplevel()
                train_scn.title("The girl on the train")
                train_scn.geometry("600x400")
                train_scn.geometry("+400+150")
                train_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/train.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(train_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(train_scn,text="The girl on the train\n BY \n Paula Hawkins \n \n \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=230, y=50)
                m0 = 'select cost from books where b_code ="GT/302"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(train_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book11
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book11 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(train_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/The_Girl_on_the_Train_(novel)")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(train_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def train_des():
                    train_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(train_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=train_des)
                back02.place(x=15, y=330)
                train_scn.mainloop()

            def vin8():
                vin_scn = tk.Toplevel()
                vin_scn.title("Da Vinci Code")
                vin_scn.geometry("600x400")
                vin_scn.geometry("+400+150")
                vin_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/vinci.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(vin_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(vin_scn, text="Da Vinci Code\n BY \n Dan Brown \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=280, y=50)
                m0 = 'select cost from books where b_code ="DV/579"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(vin_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book12
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book12 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(vin_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.supersummary.com/the-da-vinci-code/summary/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(vin_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def vin_des():
                    vin_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(vin_scn, image=back_2, height=55, width=80, highlightbackground="black",command=vin_des)
                back02.place(x=15, y=330)
                vin_scn.mainloop()

            def gst8():
                gst_scn = tk.Toplevel()
                gst_scn.title("The Guest List")
                gst_scn.geometry("600x400")
                gst_scn.geometry("+400+250")
                gst_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/guest.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(gst_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(gst_scn, text="The Guest List\n BY \n Lucy Foley \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="LF/222"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(gst_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book13
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book13 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(gst_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://the-bibliofile.com/the-guest-list/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(gst_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def gst_des():
                    gst_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(gst_scn, image=back_2, height=55, width=80, highlightbackground="black",command=gst_des)
                back02.place(x=15, y=330)
                gst_scn.mainloop()

            def lord8():
                lord_scn = tk.Toplevel()
                lord_scn.title("The Lord of the Rings")
                lord_scn.geometry("600x400")
                lord_scn.geometry("+400+150")
                lord_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/lord.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(lord_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(lord_scn,text="The Lord of the Rings\n BY \n J.R.R.Talkien \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=210, y=50)
                m0 = 'select cost from books where b_code ="LR/043"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(lord_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book15
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book15 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(lord_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.britannica.com/topic/The-Lord-of-the-Rings")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(lord_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def lord_des():
                    lord_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(lord_scn, image=back_2, height=55, width=80, highlightbackground="black",command=lord_des)
                back02.place(x=15, y=330)
                lord_scn.mainloop()

            def kl8():
                kl_scn = tk.Toplevel()
                kl_scn.title("Klara and the Sun")
                kl_scn.geometry("600x400")
                kl_scn.geometry("+400+250")
                kl_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/klara.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(kl_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(kl_scn, text="Klara and the Sun\n BY \n Kazuo Ishiguro \n \n \u2B50 \u2B50 \u2B50  ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=275, y=50)
                m0 = 'select cost from books where b_code ="KR/413"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(kl_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book14
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book14 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(kl_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://the-bibliofile.com/klara-and-the-sun/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(kl_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def kl_des():
                    kl_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(kl_scn, image=back_2, height=55, width=80, highlightbackground="black",command=kl_des)
                back02.place(x=15, y=330)
                kl_scn.mainloop()

            def hate8():
                hate_scn = tk.Toplevel()
                hate_scn.title("The Hating Game")
                hate_scn.geometry("600x400")
                hate_scn.geometry("+400+150")
                hate_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/hate.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(hate_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(hate_scn, text="The Hating Game\n BY \n Sally Thorne \n \n \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="HT/333"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(hate_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book16
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book16 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(hate_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.bookbrowse.com/bb_briefs/detail/index.cfm/ezine_preview_number/11670/the-hating-game")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(hate_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def hate_des():
                    hate_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(hate_scn, image=back_2, height=55, width=80, highlightbackground="black",command=hate_des)
                back02.place(x=15, y=330)
                hate_scn.mainloop()

            def mgc8():
                mgc_scn = tk.Toplevel()
                mgc_scn.title("Love, Hope and Magic")
                mgc_scn.geometry("600x400")
                mgc_scn.geometry("+400+150")
                mgc_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/magic.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(mgc_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(mgc_scn,text="Love, Hope and Magic\n BY \n Ashish Bagrecha\n \n \u2B50 \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=238, y=50)
                m0 = 'select cost from books where b_code ="LH/650"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(mgc_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book17
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book17 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(mgc_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.frontlist.in/books/love-hope-and-magic-by-ashish-bagrecha/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(mgc_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def mgc_des():
                    mgc_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(mgc_scn, image=back_2, height=55, width=80, highlightbackground="black",command=mgc_des)
                back02.place(x=15, y=330)
                mgc_scn.mainloop()

            def tm8():
                tm_scn = tk.Toplevel()
                tm_scn.title("The Time Machine")
                tm_scn.geometry("600x400")
                tm_scn.geometry("+400+150")
                tm_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/time.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(tm_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(tm_scn, text="The Time Machine\n BY \n H.G. Wells \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="TM/968"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(tm_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=293, y=230)

                def cart0():
                    global book18
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book18 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(tm_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.sparknotes.com/lit/timemachine/summary/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(tm_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def tm_des():
                    tm_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(tm_scn, image=back_2, height=55, width=80, highlightbackground="black",command=tm_des)
                back02.place(x=15, y=330)
                tm_scn.mainloop()

            def end8():
                end_scn = tk.Toplevel()
                end_scn.title("It Ends with Us")
                end_scn.geometry("600x400")
                end_scn.geometry("+400+150")
                end_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/ends.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(end_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(end_scn,text="It Ends with Us\n BY \n Collen Hoover \n \n\u2B50 \u2B50 \u2B50 \u2B50 \u2B50",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="IU/459"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(end_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book19
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book19 = +1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(end_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://scan.lancastersu.co.uk/2017/08/23/book-review-it-ends-with-us/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(end_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def end_des():
                    end_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(end_scn, image=back_2, height=55, width=80, highlightbackground="black",command=end_des)
                back02.place(x=15, y=330)
                end_scn.mainloop()

            def mkt8():
                mkt_scn = tk.Toplevel()
                mkt_scn.title("The Three Musketeers")
                mkt_scn.geometry("600x400")
                mkt_scn.geometry("+400+150")
                mkt_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/musket.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(mkt_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(mkt_scn,text="The Three Musketeers\n BY \n Alexandre Dumas \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=235, y=50)
                m0 = 'select cost from books where b_code ="TM/212"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(mkt_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book20
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book20 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(mkt_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.britannica.com/topic/The-Three-Musketeers")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(mkt_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def mkt_des():
                    mkt_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(mkt_scn, image=back_2, height=55, width=80, highlightbackground="black",
                                   command=mkt_des)
                back02.place(x=15, y=330)
                mkt_scn.mainloop()

            def sct8():
                sct_scn = tk.Toplevel()
                sct_scn.title("The Secrets we keep")
                sct_scn.geometry("600x400")
                sct_scn.geometry("+400+150")
                sct_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/secret.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(sct_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(sct_scn, text="The Secrets we keep\n BY \n Sudeep Nagarkar \n \n \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=235, y=50)
                m0 = 'select cost from books where b_code ="SK/970"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(sct_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book21
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book21 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(sct_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.thehindu.com/books/books-authors/sudeep-nagarkar-on-his-latest-book-the-secrets-we-keep/article27160146.ece")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(sct_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def sct_des():
                    sct_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(sct_scn, image=back_2, height=55, width=80, highlightbackground="black",command=sct_des)
                back02.place(x=15, y=330)
                sct_scn.mainloop()

            def nb8():
                nb_scn = tk.Toplevel()
                nb_scn.title("The Notebook")
                nb_scn.geometry("600x400")
                nb_scn.geometry("+400+150")
                nb_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/ntb.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(nb_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(nb_scn, text="The Notebook\n BY \n Nicholas Sparks \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=275, y=50)
                m0 = 'select cost from books where b_code ="N/541"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(nb_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=295, y=230)

                def cart0():
                    global book22
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book22 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(nb_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/The_Notebook")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(nb_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def nb_des():
                    nb_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(nb_scn, image=back_2, height=55, width=80, highlightbackground="black",command=nb_des)
                back02.place(x=15, y=330)
                nb_scn.mainloop()

            def ed8():
                ed_scn = tk.Toplevel()
                ed_scn.title("The Edge of the Grave")
                ed_scn.geometry("600x400")
                ed_scn.geometry("+400+150")
                ed_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/edge.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(ed_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(ed_scn,text="The Edge of the Grave\n BY \n Robbie Morrison \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=230, y=50)
                m0 = 'select cost from books where b_code ="EG/643"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(ed_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book23
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book23 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(ed_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.panmacmillan.com/authors/robbie-morrison/edge-of-the-grave/9781529054019")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(ed_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def ed_des():
                    ed_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(ed_scn, image=back_2, height=55, width=80, highlightbackground="black",command=ed_des)
                back02.place(x=15, y=330)
                ed_scn.mainloop()

            def clr8():
                clr_scn = tk.Toplevel()
                clr_scn.title("The Colour of Magic")
                clr_scn.geometry("600x400")
                clr_scn.geometry("+400+150")
                clr_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/colour.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(clr_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(clr_scn,text="The Colour of Magic\n BY \n Terry Pratchett \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=235, y=50)
                m0 = 'select cost from books where b_code ="CM/566"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(clr_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book24
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book24 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(clr_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://www.britannica.com/topic/The-Colour-of-Magic")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(clr_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def clr_des():
                    clr_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(clr_scn, image=back_2, height=55, width=80, highlightbackground="black",command=clr_des)
                back02.place(x=15, y=330)
                clr_scn.mainloop()

            def dgt8():
                dgt_scn = tk.Toplevel()
                dgt_scn.title("Daughters of Night")
                dgt_scn.geometry("600x400")
                dgt_scn.geometry("+400+150")
                dgt_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/night.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(dgt_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(dgt_scn,text="Daughters of Night\n BY \n Laura Shepherd Robinson \n \n \u2B50 \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 25, "bold"))
                la2.place(x=217, y=50)
                m0 = 'select cost from books where b_code ="DN/660"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(dgt_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=293, y=230)

                def cart0():
                    global book25
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book25 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(dgt_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://shereadsnovels.com/2021/03/08/daughters-of-night-by-laura-shepherd-robinson/")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(dgt_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def dgt_des():
                    dgt_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(dgt_scn, image=back_2, height=55, width=80, highlightbackground="black",command=dgt_des)
                back02.place(x=15, y=330)
                dgt_scn.mainloop()

            def dn8():
                dn_scn = tk.Toplevel()
                dn_scn.title("Dune")
                dn_scn.geometry("600x400")
                dn_scn.geometry("+400+150")
                dn_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/dune.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(dn_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(dn_scn, text=" Dune \n BY \n Frank Herbert \n \n \u2B50 \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="DU/740"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2 = tk.Label(dn_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=290, y=230)

                def cart0():
                    global book26
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book26 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(dn_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/Dune_(novel)")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(dn_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def dn_des():
                    dn_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(dn_scn, image=back_2, height=55, width=80, highlightbackground="black", command=dn_des)
                back02.place(x=15, y=330)
                dn_scn.mainloop()

            def ot8():
                ot_scn = tk.Toplevel()
                ot_scn.title("Outlanders")
                ot_scn.geometry("600x400")
                ot_scn.geometry("+400+150")
                ot_scn.config(bg="black")
                mart00 = Image.open("/Users/garimagrover/Desktop/out.png")
                rmart0 = mart00.resize((180, 275))
                mart_0 = ImageTk.PhotoImage(rmart0)
                martl0 = tk.Label(ot_scn, image=mart_0, bg="black")
                martl0.image = mart_0
                martl0.place(x=7, y=30)
                la2 = tk.Label(ot_scn, text=" Outlanders \n BY \n Diana Gabaldon \n \n \u2B50 \u2B50 \u2B50 ",bg="black", fg="white")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=277, y=50)
                m0 = 'select cost from books where b_code ="OT/210"'
                cursor.execute(m0)
                m = 0
                for x in cursor:
                    y = str(x)
                    y = y[1:4]
                    m = "M.R.P: ₹" + y
                la2.place(x=255, y=50)
                la2 = tk.Label(ot_scn, text=m, fg="white", bg="black")
                la2.config(font=("Courier", 27, "bold"))
                la2.place(x=293, y=230)

                def cart0():
                    global book27
                    msg0 = "+1 📚"
                    messagebox.showinfo(message=msg0)
                    book27 += 1

                c0 = Image.open("/Users/garimagrover/Desktop/bag1.png")
                res0 = c0.resize((80, 60))
                sh = ImageTk.PhotoImage(res0)
                bu6 = tk.Button(ot_scn, image=sh, height=50, width=60, highlightbackground="black", command=cart0)
                bu6.place(x=470, y=320)

                def web():
                    webbrowser.open("https://en.wikipedia.org/wiki/Outlander_(novel)")

                info1 = Image.open("/Users/garimagrover/Desktop/info1.png")
                rinfo1 = info1.resize((80, 60))
                info_1 = ImageTk.PhotoImage(rinfo1)
                ib1 = tk.Button(ot_scn, image=info_1, height=55, width=70, highlightbackground="black", command=web)
                ib1.place(x=280, y=320)

                def ot_des():
                    ot_scn.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(ot_scn, image=back_2, height=55, width=80, highlightbackground="black",command=ot_des)
                back02.place(x=15, y=330)
                ot_scn.mainloop()

            def temp_txt(e):
                e1.delete(0,"end")
            e1 = tk.Entry(cust, width=30)
            e1.insert(0,"  Search")
            e1.bind("<FocusIn>", temp_txt)
            e1.config(highlightcolor="blue",highlightbackground="lightskyblue")
            e1.place(x=620, y=14)
            def srch():
                s=e1.get()
                if s.lower()=="the killing tide":
                   kill8()
                if s.lower()=="kafka on the shore":
                    kots8()
                if s.lower()=="Educated".lower():
                    edu8()
                if s.lower()=="train to pakistan":
                    ttp8()
                if s.lower()=="the martian":
                    mart8()
                if s.lower()=="the thief":
                    thief8()
                if s.lower()=="becoming":
                    bec8()
                if s.lower()=="malgudi days":
                    malgudi8()
                if s.lower()=="treasure island":
                    tres8()
                if s.lower()=="malibu rising":
                    mal8()
                if s.lower()=="the girl on the train":
                    train8()
                if s.lower()=="da vinci code":
                    vin8()
                if s.lower()=="the guest list":
                    gst8()
                if s.lower()=="lord of the rings":
                    lord8()
                if s.lower()=="klara and the sun":
                    kl8()
                if s.lower()=="the hating game":
                    hate8()
                if s.lower()=="love, hope and magic":
                    mgc8()
                if s.lower()=="the time machine":
                    tm8()
                if s.lower()=="it ends with us":
                    end8()
                if s.lower()=="the three musketeers":
                    mkt8()
                if s.lower()=="the secrets we keep":
                    sct8()
                if s.lower()=="the notebook":
                    nb8()
                if s.lower()=="the edge of the grave":
                    ed8()
                if s.lower()=="the colour of magic":
                    clr8()
                if s.lower()=="daughters of night":
                    dgt8()
                if s.lower()=="dune":
                    dn8()
                if s.lower()=="outlanders":
                    ot8()

            bimg = Image.open("/Users/garimagrover/Desktop/search.png")
            rimg = bimg.resize((32, 25))
            b_img = ImageTk.PhotoImage(rimg)
            but = tk.Button(cust, text="Search",highlightbackground="#FFFFE0",image=b_img,width=32,height=27,command=srch)
            but.config(font=("Courier", 19))
            but.place(x=902, y=12)

            edu=Image.open("/Users/garimagrover/Desktop/educated.png")
            redu=edu.resize((75,100))
            edu1=ImageTk.PhotoImage(redu)
            edul=tk.Label(cust,image=edu1,bg="#FFFFE0")
            edul.image=edu1
            edul.place(x=302,y=110)
            edu_bt=tk.Button(cust,text="Educated",height=2,width=11,bg="#FFFFE0",command=edu8)
            edu_bt.config(font=("Courier", 12,"bold"))
            edu_bt.place(x=302,y=218)

            killing=Image.open("/Users/garimagrover/Desktop/killing.png")
            rkill=killing.resize((75,100))
            kill1=ImageTk.PhotoImage(rkill)
            kill=tk.Label(cust,image=kill1,bg="#FFFFE0")
            kill.image=kill1
            kill.place(x=422,y=110)
            kill_bt=tk.Button(cust,text="Killing \n Tide",width=11,command=kill8)
            kill_bt.config(font=("Courier", 11,"bold"))
            kill_bt.place(x=422, y=218)

            kots = Image.open("/Users/garimagrover/Desktop/kots.png")
            rkots = kots.resize((75, 100))
            kots1 = ImageTk.PhotoImage(rkots)
            kots2 = tk.Label(cust, image=kots1, bg="#FFFFE0")
            kots2.image = kots1
            kots2.place(x=537, y=110)
            kots_bt = tk.Button(cust, text=" Kafka on \n the shore",height=2,width=11,command=kots8)
            kots_bt.config(font=("Courier", 11, "bold"))
            kots_bt.place(x=537, y=218)

            ttp = Image.open("/Users/garimagrover/Desktop/ttp.png")
            rttp = ttp.resize((75, 100))
            ttp1 = ImageTk.PhotoImage(rttp)
            ttp2 = tk.Label(cust, image=ttp1, bg="#FFFFE0")
            ttp2.image = ttp1
            ttp2.place(x=652, y=110)
            ttp_bt = tk.Button(cust, text="Train to \n Pakistan",width=11,command=ttp8)
            ttp_bt.config(font=("Courier", 11, "bold"))
            ttp_bt.place(x=652, y=218)

            mart = Image.open("/Users/garimagrover/Desktop/martian.png")
            rmart = mart.resize((75, 100))
            mart1 = ImageTk.PhotoImage(rmart)
            mart2 = tk.Label(cust, image=mart1, bg="#FFFFE0")
            mart2.image = mart1
            mart2.place(x=772, y=110)
            mart_bt = tk.Button(cust, text="The \n Martian", width=11,command=mart8)
            mart_bt.config(font=("Courier", 11, "bold"))
            mart_bt.place(x=772, y=215)

            become = Image.open("/Users/garimagrover/Desktop/becoming.png")
            rbec = become.resize((75, 100))
            bec1 = ImageTk.PhotoImage(rbec)
            bec2 = tk.Label(cust, image=bec1, bg="#FFFFE0")
            bec2.image = bec1
            bec2.place(x=892, y=110)
            bec_bt = tk.Button(cust, text="Becoming", height=2,width=11,command=bec8)
            bec_bt.config(font=("Courier", 12, "bold"))
            bec_bt.place(x=892, y=215)

            thief = Image.open("/Users/garimagrover/Desktop/thief.png")
            rthief = thief.resize((75, 100))
            thief1 = ImageTk.PhotoImage(rthief)
            thief2 = tk.Label(cust, image=thief1, bg="#FFFFE0")
            thief2.image = thief1
            thief2.place(x=300, y=310)
            thief_bt = tk.Button(cust, text="The \n Thief", width=11,command=thief8)
            thief_bt.config(font=("Courier", 12, "bold"))
            thief_bt.place(x=300, y=415)

            malgudi = Image.open("/Users/garimagrover/Desktop/malgudi.png")
            rmalgudi = malgudi.resize((75, 100))
            malgudi1 = ImageTk.PhotoImage(rmalgudi)
            malgudi2 = tk.Label(cust, image=malgudi1, bg="#FFFFE0")
            malgudi2.image = malgudi1
            malgudi2.place(x=420, y=310)
            malgudi_bt = tk.Button(cust, text="Malgudi \n Days", width=11,command=malgudi8)
            malgudi_bt.config(font=("Courier", 12, "bold"))
            malgudi_bt.place(x=420, y=415)

            treasure = Image.open("/Users/garimagrover/Desktop/treasure.png")
            rtreasure = treasure.resize((75, 100))
            treasure1 = ImageTk.PhotoImage(rtreasure)
            treasure2 = tk.Label(cust, image=treasure1, bg="#FFFFE0")
            treasure2.image = treasure1
            treasure2.place(x=535, y=310)
            treasure_bt = tk.Button(cust, text="Treasure \n Island", width=11,command=tres8)
            treasure_bt.config(font=("Courier", 12, "bold"))
            treasure_bt.place(x=535, y=415)

            malibu = Image.open("/Users/garimagrover/Desktop/malibu.png")
            rmalibu = malibu.resize((75, 100))
            malibu1 = ImageTk.PhotoImage(rmalibu)
            malibu2 = tk.Label(cust, image=malibu1, bg="#FFFFE0")
            malibu2.image = malibu1
            malibu2.place(x=650, y=310)
            malibu_bt = tk.Button(cust, text="Malibu \n Rising", width=11,command=mal8)
            malibu_bt.config(font=("Courier", 12, "bold"))
            malibu_bt.place(x=650, y=415)

            train = Image.open("/Users/garimagrover/Desktop/train.png")
            rtrain = train.resize((75, 100))
            train1 = ImageTk.PhotoImage(rtrain)
            train2 = tk.Label(cust, image=train1, bg="#FFFFE0")
            train2.image = train1
            train2.place(x=770, y=310)
            train_bt = tk.Button(cust, text=" The Girl on \n the Train", width=11,command=train8)
            train_bt.config(font=("Courier", 12, "bold"))
            train_bt.place(x=770, y=415)

            vinci = Image.open("/Users/garimagrover/Desktop/vinci.png")
            rvinci = vinci.resize((75, 100))
            vinci1 = ImageTk.PhotoImage(rvinci)
            vinci2 = tk.Label(cust, image=vinci1, bg="#FFFFE0")
            vinci2.image = vinci1
            vinci2.place(x=890, y=310)
            vinci_bt = tk.Button(cust, text="Da Vinci \n Code", width=11,command=vin8)
            vinci_bt.config(font=("Courier", 12, "bold"))
            vinci_bt.place(x=890, y=415)

            guest = Image.open("/Users/garimagrover/Desktop/guest.png")
            rguest = guest.resize((75, 100))
            guest1 = ImageTk.PhotoImage(rguest)
            guest2 = tk.Label(cust, image=guest1, bg="#FFFFE0")
            guest2.image = guest1
            guest2.place(x=1012, y=310)
            guest_bt = tk.Button(cust, text="The Guest \n List", width=11,command=gst8)
            guest_bt.config(font=("Courier", 12, "bold"))
            guest_bt.place(x=1012, y=415)

            klara = Image.open("/Users/garimagrover/Desktop/klara.png")
            rklara = klara.resize((75, 100))
            klara1 = ImageTk.PhotoImage(rklara)
            klara2 = tk.Label(cust, image=klara1, bg="#FFFFE0")
            klara2.image = klara1
            klara2.place(x=1130, y=310)
            klara_bt = tk.Button(cust, text="Klara and \n the Sun", width=11,command=kl8)
            klara_bt.config(font=("Courier", 12, "bold"))
            klara_bt.place(x=1130, y=415)

            lord = Image.open("/Users/garimagrover/Desktop/lord.png")
            rlord = lord.resize((75, 100))
            lord1 = ImageTk.PhotoImage(rlord)
            lord2 = tk.Label(cust, image=lord1, bg="#FFFFE0")
            lord2.image = lord1
            lord2.place(x=300, y=510)
            lord_bt = tk.Button(cust, text="The Lord of \n the Rings", width=11,command=lord8)
            lord_bt.config(font=("Courier", 12, "bold"))
            lord_bt.place(x=300, y=620)

            hate = Image.open("/Users/garimagrover/Desktop/hate.png")
            rhate = hate.resize((75, 100))
            hate1 = ImageTk.PhotoImage(rhate)
            hate2 = tk.Label(cust, image=hate1, bg="#FFFFE0")
            hate2.image = lord1
            hate2.place(x=420, y=510)
            hate_bt = tk.Button(cust, text=" The Hating \n Game", width=11,command=hate8)
            hate_bt.config(font=("Courier", 12, "bold"))
            hate_bt.place(x=420, y=620)

            magic = Image.open("/Users/garimagrover/Desktop/magic.png")
            rmagic = magic.resize((75, 100))
            magic1 = ImageTk.PhotoImage(rmagic)
            magic2 = tk.Label(cust, image=magic1, bg="#FFFFE0")
            magic2.image = magic1
            magic2.place(x=535, y=510)
            magic_bt = tk.Button(cust, text=" Love, Hope \n and Magic", width=11,command=mgc8)
            magic_bt.config(font=("Courier", 12, "bold"))
            magic_bt.place(x=535, y=620)

            machine = Image.open("/Users/garimagrover/Desktop/time.png")
            rmachine = machine.resize((75, 100))
            machine1 = ImageTk.PhotoImage(rmachine)
            machine2 = tk.Label(cust, image=machine1, bg="#FFFFE0")
            machine2.image = machine1
            machine2.place(x=652, y=510)
            machine_bt = tk.Button(cust, text=" The Time \n Machine", width=11,command=tm8)
            machine_bt.config(font=("Courier", 12, "bold"))
            machine_bt.place(x=652, y=620)

            ends = Image.open("/Users/garimagrover/Desktop/ends.png")
            rends = ends.resize((75, 100))
            ends1 = ImageTk.PhotoImage(rends)
            ends2 = tk.Label(cust, image=ends1, bg="#FFFFE0")
            ends2.image = ends1
            ends2.place(x=770, y=510)
            ends_bt = tk.Button(cust, text=" It ends \n with us", width=11,command=end8)
            ends_bt.config(font=("Courier", 12, "bold"))
            ends_bt.place(x=770, y=620)

            musket = Image.open("/Users/garimagrover/Desktop/musket.png")
            rmusket = musket.resize((75, 100))
            musket1 = ImageTk.PhotoImage(rmusket)
            musket2 = tk.Label(cust, image=musket1, bg="#FFFFE0")
            musket2.image = musket1
            musket2.place(x=890, y=510)
            musket_bt = tk.Button(cust, text=" The Three \n Musketeers", width=11,command=mkt8)
            musket_bt.config(font=("Courier", 12, "bold"))
            musket_bt.place(x=890, y=620)

            secret = Image.open("/Users/garimagrover/Desktop/secret.png")
            rsecret = secret.resize((75, 100))
            secret1 = ImageTk.PhotoImage(rsecret)
            secret2 = tk.Label(cust, image=secret1, bg="#FFFFE0")
            secret2.image = secret1
            secret2.place(x=1010, y=510)
            secret_bt = tk.Button(cust, text=" The Secrets \n we keep", width=11,command=sct8)
            secret_bt.config(font=("Courier", 12, "bold"))
            secret_bt.place(x=1010, y=620)

            ntb = Image.open("/Users/garimagrover/Desktop/ntb.png")
            rntb = ntb.resize((75, 100))
            ntb1 = ImageTk.PhotoImage(rntb)
            ntb2 = tk.Label(cust, image=ntb1, bg="#FFFFE0")
            ntb2.image = ntb1
            ntb2.place(x=1130, y=510)
            ntb_bt = tk.Button(cust, text=" The \n Notebook", width=11,command=nb8)
            ntb_bt.config(font=("Courier", 12, "bold"))
            ntb_bt.place(x=1130, y=620)

            edge = Image.open("/Users/garimagrover/Desktop/edge.png")
            redge = edge.resize((75, 100))
            edge1 = ImageTk.PhotoImage(redge)
            edge2 = tk.Label(cust, image=edge1, bg="#FFFFE0")
            edge2.image = edge1
            edge2.place(x=1015, y=110)
            edge_bt = tk.Button(cust, text=" The Edge of \n the Grave", width=11,command=ed8)
            edge_bt.config(font=("Courier", 12, "bold"))
            edge_bt.place(x=1015, y=215)

            colour = Image.open("/Users/garimagrover/Desktop/colour.png")
            rcolour = colour.resize((75, 100))
            colour1 = ImageTk.PhotoImage(rcolour)
            colour2 = tk.Label(cust, image=colour1, bg="#FFFFE0")
            colour2.image = colour1
            colour2.place(x=1132, y=110)
            colour_bt = tk.Button(cust, text=" The Colour \n of Magic", width=11,command=clr8)
            colour_bt.config(font=("Courier", 12, "bold"))
            colour_bt.place(x=1132, y=215)

            night = Image.open("/Users/garimagrover/Desktop/night.png")
            rnight = night.resize((75, 100))
            night1 = ImageTk.PhotoImage(rnight)
            night2 = tk.Label(cust, image=night1, bg="#FFFFE0")
            night2.image = night1
            night2.place(x=1250, y=310)
            night_bt = tk.Button(cust, text=" Daughters \n of Night", width=11,command=dgt8)
            night_bt.config(font=("Courier", 12, "bold"))
            night_bt.place(x=1250, y=415)

            dune = Image.open("/Users/garimagrover/Desktop/dune.png")
            rdune = dune.resize((75, 100))
            dune1 = ImageTk.PhotoImage(rdune)
            dune2 = tk.Label(cust, image=dune1, bg="#FFFFE0")
            dune2.image = dune1
            dune2.place(x=1250, y=510)
            dune_bt = tk.Button(cust, text=" Dune", width=10,height=2,command=dn8)
            dune_bt.config(font=("Courier", 13, "bold"))
            dune_bt.place(x=1250, y=620)

            out = Image.open("/Users/garimagrover/Desktop/out.png")
            rout = out.resize((75, 100))
            out1 = ImageTk.PhotoImage(rout)
            out2 = tk.Label(cust, image=out1, bg="#FFFFE0")
            out2.image = out1
            out2.place(x=1250, y=113)
            out_bt = tk.Button(cust, text="Outlander", width=10, height=2,command=ot8)
            out_bt.config(font=("Courier", 13, "bold"))
            out_bt.place(x=1250, y=221)

            def home1():
                cust.destroy()
            n = Image.open("/Users/garimagrover/Desktop/home.png")
            re = n.resize((110, 70))
            home = ImageTk.PhotoImage(re)
            b5 = tk.Button(cust, image=home, height=60, width=90,command=home1,highlightbackground="#FFFFE0")
            b5.place(x=1335, y=705)

            def cart00():
                crt=tk.Toplevel()
                crt.geometry("870x650")
                crt.geometry("+330+80")
                crt.title("CART")
                crt.config(bg="black")
                if book1>0:
                    lb1=tk.Label(crt,text="Educated",fg="white",bg="black")
                    lb1.config(font=("Courier",25,"bold"))
                    lb1.pack()
                if book2>0:
                    lb2=tk.Label(crt,text="The Killing Tide",fg="white",bg="black")
                    lb2.config(font=("Courier", 25, "bold"))
                    lb2.pack()
                if book3>0:
                    lb3=tk.Label(crt,text="Kafka on the Shore",fg="white",bg="black")
                    lb3.config(font=("Courier", 25, "bold"))
                    lb3.pack()
                if book4 > 0:
                    lb4 = tk.Label(crt, text="Train to Pakistan", fg="white", bg="black")
                    lb4.config(font=("Courier", 25, "bold"))
                    lb4.pack()
                if book5>0:
                    lb5=tk.Label(crt,text="The Martian",fg="white",bg="black")
                    lb5.config(font=("Courier", 25, "bold"))
                    lb5.pack()
                if book6>0:
                    lb6=tk.Label(crt,text="Becoming",fg="white",bg="black")
                    lb6.config(font=("Courier", 25, "bold"))
                    lb6.pack()
                if book7>0:
                    lb7=tk.Label(crt,text="The Thief",fg="white",bg="black")
                    lb7.config(font=("Courier", 25, "bold"))
                    lb7.pack()
                if book8>0:
                    lb8=tk.Label(crt,text="Malgudi Days",fg="white",bg="black")
                    lb8.config(font=("Courier", 25, "bold"))
                    lb8.pack()
                if book9>0:
                    lb9=tk.Label(crt,text="Treasure Island",fg="white",bg="black")
                    lb9.config(font=("Courier", 25, "bold"))
                    lb9.pack()
                if book10>0:
                    lb10=tk.Label(crt,text="Malibu Rising",fg="white",bg="black")
                    lb10.config(font=("Courier", 25, "bold"))
                    lb10.pack()
                if book11>0:
                    lb11=tk.Label(crt,text="The Girl on the Train",fg="white",bg="black")
                    lb11.config(font=("Courier", 25, "bold"))
                    lb11.pack()
                if book12>0:
                    lb12=tk.Label(crt,text="Da Vinci Code",fg="white",bg="black")
                    lb12.config(font=("Courier", 25, "bold"))
                    lb12.pack()
                if book13>0:
                    lb13=tk.Label(crt,text="The guest List",fg="white",bg="black")
                    lb13.config(font=("Courier", 25, "bold"))
                    lb13.pack()
                if book14>0:
                    lb14=tk.Label(crt,text="Klara and the Sun",fg="white",bg="black")
                    lb14.config(font=("Courier", 25, "bold"))
                    lb14.pack()
                if book15>0:
                    lb15=tk.Label(crt,text="The lord of the rings",fg="white",bg="black")
                    lb15.config(font=("Courier", 25, "bold"))
                    lb15.pack()
                if book16>0:
                    lb16=tk.Label(crt,text="The Hating Game",fg="white",bg="black")
                    lb16.config(font=("Courier", 25, "bold"))
                    lb16.pack()
                if book17>0:
                    lb17=tk.Label(crt,text="Love, Hope and Magic",fg="white",bg="black")
                    lb17.config(font=("Courier", 27, "bold"))
                    lb17.pack()
                if book18>0:
                    lb18=tk.Label(crt,text="The Time Machine",fg="white",bg="black")
                    lb18.config(font=("Courier", 25, "bold"))
                    lb18.pack()
                if book19>0:
                    lb19=tk.Label(crt,text="It ends with us",fg="white",bg="black")
                    lb19.config(font=("Courier", 25, "bold"))
                    lb19.pack()
                if book20>0:
                    lb20=tk.Label(crt,text="The Three Musketeers",fg="white",bg="black")
                    lb20.config(font=("Courier", 25, "bold"))
                    lb20.pack()
                if book21>0:
                    lb21=tk.Label(crt,text="The Secrets we keep",fg="white",bg="black")
                    lb21.config(font=("Courier", 25, "bold"))
                    lb21.pack()
                if book22>0:
                    lb22=tk.Label(crt,text="The Notebook",fg="white",bg="black")
                    lb22.config(font=("Courier", 25, "bold"))
                    lb22.pack()
                if book23>0:
                    lb23=tk.Label(crt,text="The Edge of the Grave",fg="white",bg="black")
                    lb23.config(font=("Courier", 27, "bold"))
                    lb23.pack()
                if book24>0:
                    lb24=tk.Label(crt,text="The Colour of the Magic",fg="white",bg="black")
                    lb24.config(font=("Courier", 25, "bold"))
                    lb24.pack()
                if book25>0:
                    lb25=tk.Label(crt,text="Daughters of Night",fg="white",bg="black")
                    lb25.config(font=("Courier", 25, "bold"))
                    lb25.pack()
                if book26>0:
                    lb26=tk.Label(crt,text="Dune",fg="white",bg="black")
                    lb26.config(font=("Courier", 25, "bold"))
                    lb26.pack()
                if book27>0:
                    lb27=tk.Label(crt,text="Outlander",fg="white",bg="black")
                    lb27.config(font=("Courier", 25, "bold"))
                    lb27.pack()

                def crt_des():
                    crt.destroy()

                back2 = Image.open("/Users/garimagrover/Desktop/back.png")
                rback2 = back2.resize((90, 60))
                back_2 = ImageTk.PhotoImage(rback2)
                back02 = tk.Button(crt, image=back_2, height=55, width=80, highlightbackground="black",command=crt_des)
                back02.place(x=15, y=580)

                bk = Image.open("/Users/garimagrover/Desktop/book2.png")
                rbk = bk.resize((220, 260))
                bk_2 = ImageTk.PhotoImage(rbk)
                bk02 = tk.Label(crt, image=bk_2,bg="black")
                bk02.place(x=30, y=180)

                def buy1():
                    buy0=tk.Toplevel()
                    buy0.geometry("400x300")
                    buy0.geometry("+330+60")
                    buy0.title("BUY")
                    buy0.config(bg="black")

                    def cash():
                        msg0="Your order is placed !!!"
                        messagebox.showinfo(message=msg0)
                        global book1
                        if book1>=1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Educated"
                                if i[2] == g:
                                    c = i[4]
                                    d = c - book1
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book1-=1
                        global book2
                        if book2 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Killing Tide"
                                if i[2] == g:
                                    c = i[4]
                                    d = c - book2
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book2-= 1
                        global book3
                        if book3 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Kafka on the Shore"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book3
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book3 -= 1
                        global book4
                        if book4 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Train to Pakistan"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book4
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book4 -= 1
                        global book5
                        if book5 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Martian"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book5
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book5 -= 1
                        global book6
                        if book6 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Becoming"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book6
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book6 -= 1
                        global book7
                        if book7 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Thief"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book7
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book7 -= 1
                        global book8
                        if book8 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Malgudi Days"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book8
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book8 -= 1
                        global book9
                        if book9 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Treasure Island"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book9
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book9 -= 1
                        global book10
                        if book10 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Malibu Rising"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book10
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book10 -= 1
                        global book11
                        if book11 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The girl on the train"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book11
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book11 -= 1
                        global book12
                        if book12 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Da Vinci Code"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book12
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book12 -= 1
                        global book13
                        if book13 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Guest List"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book13
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book13 -= 1
                        global book14
                        if book14 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Klara and the Sun"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book14
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book14 -= 1
                        global book15
                        if book15 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Lord of the Rings"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book15
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book15 -= 1
                        global book16
                        if book16 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Hating Game"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book16
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book16 -= 1
                        global book17
                        if book17 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Love, Hope and Magic"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book17
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book17 -= 1
                        global book18
                        if book18 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',
                                                           database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The time machine"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book18
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book18 -= 1
                        global book19
                        if book19 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "It ends with us"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book19
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book19 -= 1
                        global book20
                        if book20 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Three Musketeers"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book20
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book20 -= 1
                        global book21
                        if book21 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Secrets we keep"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book21
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book21 -= 1
                        global book22
                        if book22 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Notebook"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book22
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book22 -= 1
                        global book23
                        if book23 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Edge of the Grave"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book23
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book23 -= 1
                        global book24
                        if book24 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "The Colour of Magic"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book24
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book24 -= 1
                        global book25
                        if book25 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Daughters of Night"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book25
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book25 -= 1
                        global book26
                        if book26 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Dune"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book26
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book26 -= 1
                        global book27
                        if book27 >= 1:
                            mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                            cursor = mydb.cursor(buffered=True)
                            cursor.execute('select * from books')
                            for i in cursor:
                                g = "Outlanders"
                                if i[2].lower() == g.lower():
                                    c = i[4]
                                    d = c - book27
                                    SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                    cursor.execute(SQ)
                                    mydb.commit()
                            book27-= 1
                        buy0.destroy()
                        crt.destroy()

                    by1=tk.Button(buy0,text="Cash on Delivery",height=2,width=20,command=cash)
                    by1.config(font=("Courier",17,"bold"))
                    by1.place(x=90,y=60)

                    def card():
                        pay=tk.Toplevel()
                        pay.geometry("600x400")
                        pay.geometry("+500+250")
                        pay.title("PAYMENT")
                        pay.config(bg="black")

                        def temp1_txt(e):
                            e_1.delete(0, "end")

                        e_1 = tk.Entry(pay, width=30)
                        e_1.insert(0, "  Enter Card number")
                        e_1.bind("<FocusIn>", temp1_txt)
                        e_1.place(x=170,y=80)

                        def temp2_txt(e):
                            e_2.delete(0, "end")

                        e_2 = tk.Entry(pay, width=30)
                        e_2.insert(0, "  Enter CVV")
                        e_2.bind("<FocusIn>", temp2_txt)
                        e_2.place(x=170,y=160)

                        def temp3_txt(e):
                            e_3.delete(0, "end")

                        e_3 = tk.Entry(pay, width=30)
                        e_3.insert(0, "  Enter your name")
                        e_3.bind("<FocusIn>", temp3_txt)
                        e_3.place(x=170,y=260)

                        def bought():
                            h=e_1.get()
                            if len(h)!=16:
                                msg0="Wrong Details"
                                messagebox.showinfo(message=msg0)
                            else:
                                msg00="Thankyou for shopping !!!"
                                messagebox.showinfo(message=msg00)
                                global book1
                                if book1 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g="Educated"
                                        if i[2] == g:
                                            c=i[4]
                                            d=c-book1
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book1 -= 1
                                global book2
                                if book2 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Killing Tide"
                                        if i[2] == g:
                                            c = i[4]
                                            d = c - book2
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book2 -= 1
                                global book3
                                if book3 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Kafka on the Shore"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book3
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book3 -= 1
                                global book4
                                if book4 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Train to Pakistan"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book4
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book4 -= 1
                                global book5
                                if book5 >= 1:
                                     mydb = mysql.connector.connect(host='127.0.0.1', user='root',password='garimasql', database='books')
                                     cursor = mydb.cursor(buffered=True)
                                     cursor.execute('select * from books')
                                     for i in cursor:
                                         g = "The Martian"
                                         if i[2].lower() == g.lower():
                                             c = i[4]
                                             d = c - book5
                                             SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                             cursor.execute(SQ)
                                             mydb.commit()
                                     book5 -= 1
                                global book6
                                if book6 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Becoming"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book6
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book6 -= 1
                                global book7
                                if book7 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Thief"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book7
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book7 -= 1
                                global book8
                                if book8 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Malgudi Days"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book8
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book8 -= 1
                                global book9
                                if book9 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Treasure Island"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book9
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book9 -= 1
                                global book10
                                if book10 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Malibu Rising"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book10
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book10 -= 1
                                global book11
                                if book11 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The girl on the train"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book11
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book11 -= 1
                                global book12
                                if book12 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Da Vinci Code"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book12
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book12 -= 1
                                global book13
                                if book13 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Guest List"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book13
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book13 -= 1
                                global book14
                                if book14 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Klara and the Sun"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book14
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book14 -= 1
                                global book15
                                if book15 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Lord of the Rings"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book15
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book15 -= 1
                                global book16
                                if book16 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Hating Game"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book16
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book16 -= 1
                                global book17
                                if book17 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Love, Hope and Magic"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book17
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book17 -= 1
                                global book18
                                if book18 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The time machine"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book18
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book18 -= 1
                                global book19
                                if book19 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "It ends with us"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book19
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book19 -= 1
                                global book20
                                if book20 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Three Musketeers"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book20
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book20 -= 1
                                global book21
                                if book21 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Secrets we keep"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book21
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book21 -= 1
                                global book22
                                if book22 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Notebook"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book22
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book22 -= 1
                                global book23
                                if book23 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Edge of the Grave"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book23
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book23 -= 1
                                global book24
                                if book24 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "The Colour of Magic"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book24
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book24 -= 1
                                global book25
                                if book25 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Daughters of Night"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book25
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book25 -= 1
                                global book26
                                if book26 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Dune"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book26
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book26 -= 1
                                global book27
                                if book27 >= 1:
                                    mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='garimasql',database='books')
                                    cursor = mydb.cursor(buffered=True)
                                    cursor.execute('select * from books')
                                    for i in cursor:
                                        g = "Outlanders"
                                        if i[2].lower() == g.lower():
                                            c = i[4]
                                            d = c - book27
                                            SQ = "update books set Qty={} where b_name='{}'".format(d, g)
                                            cursor.execute(SQ)
                                            mydb.commit()
                                    book27 -= 1
                                buy0.destroy()
                                crt.destroy()
                                pay.destroy()
                        b_1=tk.Button(pay,text="PAY",command=bought)
                        b_1.config(font=("Courier",21,"bold"))
                        b_1.place(x=300,y=350)
                        pay.mainloop()
                    by2=tk.Button(buy0,text="Card Payment",height=2,width=20,command=card)
                    by2.config(font=("Courier", 17, "bold"))
                    by2.place(x=90,y=160)
                    buy0.mainloop()
                c_bt=tk.Button(crt,text="BUY",highlightbackground="black",height=2,width=6,command=buy1)
                c_bt.config(font=("Courier", 20, "bold"))
                c_bt.place(x=770,y=590)
                crt.mainloop()
            c = Image.open("/Users/garimagrover/Desktop/bag.png")
            re4 = c.resize((62,52))
            cart = ImageTk.PhotoImage(re4)
            b6 = tk.Button(cust, image=cart, height=50, width=60,highlightbackground="#FFFFE0",command=cart00)
            b6.place(x=1360, y=12)
            labe3=tk.Label(cust,text="Genre -:",bg="#FFFFE0")
            labe3.config(font=("Courier", 23, "bold"))
            labe3.place(x=18,y=132)

            var1 = tk.IntVar()
            var2 = tk.IntVar()
            var3 = tk.IntVar()
            var4 = tk.IntVar()
            var5 = tk.IntVar()
            var6 = tk.IntVar()
            var7 = tk.IntVar()
            var8 = tk.IntVar()
            var9 = tk.IntVar()
            var10 = tk.IntVar()

            def myst1():
                if var1.get()==1:
                    myst=tk.Toplevel()
                    myst.config(bg="black")
                    myst.geometry("600x400")
                    myst.geometry("+300+250")
                    myst.title("MYSTERY")

                    edge = Image.open("/Users/garimagrover/Desktop/edge.png")
                    redge = edge.resize((77, 105))
                    edge1 = ImageTk.PhotoImage(redge)
                    edge2 = tk.Label(myst, image=edge1, bg="#FFFFE0")
                    edge2.image = edge1
                    edge2.place(x=100, y=30)
                    edge_bt = tk.Button(myst, text=" The Edge of \n the Grave ", width=11, command=ed8)
                    edge_bt.config(font=("Courier", 12, "bold"))
                    edge_bt.place(x=100, y=150)

                    vinci = Image.open("/Users/garimagrover/Desktop/vinci.png")
                    rvinci = vinci.resize((75, 100))
                    vinci1 = ImageTk.PhotoImage(rvinci)
                    vinci2 = tk.Label(myst, image=vinci1, bg="black")
                    vinci2.image = vinci1
                    vinci2.place(x=350, y=30)
                    vinci_bt = tk.Button(myst, text="Da Vinci \n Code", width=11, command=vin8)
                    vinci_bt.config(font=("Courier", 12, "bold"))
                    vinci_bt.place(x=350, y=150)

                    guest = Image.open("/Users/garimagrover/Desktop/guest.png")
                    rguest = guest.resize((75, 100))
                    guest1 = ImageTk.PhotoImage(rguest)
                    guest2 = tk.Label(myst, image=guest1, bg="black")
                    guest2.image = guest1
                    guest2.place(x=225, y=205)
                    guest_bt = tk.Button(myst, text="The Guest \n List", width=11, command=gst8)
                    guest_bt.config(font=("Courier", 12, "bold"))
                    guest_bt.place(x=225, y=317)

                    malibu = Image.open("/Users/garimagrover/Desktop/malibu.png")
                    rmalibu = malibu.resize((75, 100))
                    malibu1 = ImageTk.PhotoImage(rmalibu)
                    malibu2 = tk.Label(myst, image=malibu1, bg="black")
                    malibu2.image = malibu1
                    malibu2.place(x=470, y=205)
                    malibu_bt = tk.Button(myst, text="Malibu \n Rising", width=11, command=mal8)
                    malibu_bt.config(font=("Courier", 12, "bold"))
                    malibu_bt.place(x=470, y=315)
                    myst.mainloop()
            ch1 = tk.Checkbutton(cust, text='Mystery', variable=var1, onvalue=1, offvalue=0,bg="#FFFFE0",command=myst1)
            ch1.config(font=("Courier", 18))
            ch1.place(x=18,y=170)

            def fant1():
                if var2.get() == 1:
                    fant=tk.Toplevel()
                    fant.config(bg="black")
                    fant.title("FANTASY")
                    fant.geometry("500x300")
                    fant.geometry("+300+250")

                    colour = Image.open("/Users/garimagrover/Desktop/colour.png")
                    rcolour = colour.resize((75, 100))
                    colour1 = ImageTk.PhotoImage(rcolour)
                    colour2 = tk.Label(fant, image=colour1, bg="black")
                    colour2.image = colour1
                    colour2.place(x=100, y=60)
                    colour_bt = tk.Button(fant, text=" The Colour \n of Magic", width=11, command=clr8)
                    colour_bt.config(font=("Courier", 12, "bold"))
                    colour_bt.place(x=100, y=170)

                    lord = Image.open("/Users/garimagrover/Desktop/lord.png")
                    rlord = lord.resize((75, 100))
                    lord1 = ImageTk.PhotoImage(rlord)
                    lord2 = tk.Label(fant, image=lord1, bg="black")
                    lord2.image = lord1
                    lord2.place(x=320, y=60)
                    lord_bt = tk.Button(fant, text=" The Lord of\n the Rings", width=11, command=lord8)
                    lord_bt.config(font=("Courier", 12, "bold"))
                    lord_bt.place(x=320, y=170)
                    fant.mainloop()
            ch2 = tk.Checkbutton(cust, text='Fantasy', variable=var2, onvalue=1, offvalue=0,bg="#FFFFE0",command=fant1)
            ch2.config(font=("Courier", 18))
            ch2.place(x=18, y=200)

            def scifi1():
                if var3.get()==1:
                    sifi=tk.Toplevel()
                    sifi.config(bg="black")
                    sifi.geometry("600x400")
                    sifi.geometry("+300+250")
                    sifi.title("Sci-Fi")

                    dune = Image.open("/Users/garimagrover/Desktop/dune.png")
                    rdune = dune.resize((75, 100))
                    dune1 = ImageTk.PhotoImage(rdune)
                    dune2 = tk.Label(sifi, image=dune1, bg="black")
                    dune2.image = dune1
                    dune2.place(x=100, y=30)
                    dune_bt = tk.Button(sifi, text=" Dune", width=9, height=2, command=dn8)
                    dune_bt.config(font=("Courier", 13, "bold"))
                    dune_bt.place(x=102, y=150)

                    klara = Image.open("/Users/garimagrover/Desktop/klara.png")
                    rklara = klara.resize((75, 100))
                    klara1 = ImageTk.PhotoImage(rklara)
                    klara2 = tk.Label(sifi, image=klara1, bg="black")
                    klara2.image = klara1
                    klara2.place(x=350, y=30)
                    klara_bt = tk.Button(sifi, text="Klara and \n the Sun", width=11, command=kl8)
                    klara_bt.config(font=("Courier", 12, "bold"))
                    klara_bt.place(x=350, y=150)

                    mart = Image.open("/Users/garimagrover/Desktop/martian.png")
                    rmart = mart.resize((75, 100))
                    mart1 = ImageTk.PhotoImage(rmart)
                    mart2 = tk.Label(sifi, image=mart1, bg="black")
                    mart2.image = mart1
                    mart2.place(x=225, y=205)
                    mart_bt = tk.Button(sifi, text="The \n Martian", width=11, command=mart8)
                    mart_bt.config(font=("Courier", 11, "bold"))
                    mart_bt.place(x=225, y=317)

                    machine = Image.open("/Users/garimagrover/Desktop/time.png")
                    rmachine = machine.resize((75, 100))
                    machine1 = ImageTk.PhotoImage(rmachine)
                    machine2 = tk.Label(sifi, image=machine1, bg="black")
                    machine2.image = machine1
                    machine2.place(x=470, y=205)
                    machine_bt = tk.Button(sifi, text=" The Time \n Machine", width=11, command=tm8)
                    machine_bt.config(font=("Courier", 12, "bold"))
                    machine_bt.place(x=470, y=317)
                    sifi.mainloop()
            ch3 = tk.Checkbutton(cust, text='Sci-Fi', variable=var3, onvalue=1, offvalue=0,bg="#FFFFE0",command=scifi1)
            ch3.config(font=("Courier", 18))
            ch3.place(x=18, y=230)

            def adv1():
                if var4.get()==1:
                    adv=tk.Toplevel()
                    adv.config(bg="black")
                    adv.title("ADVENTURE")
                    adv.geometry("500x300")
                    adv.geometry("+300+250")

                    musket = Image.open("/Users/garimagrover/Desktop/musket.png")
                    rmusket = musket.resize((75, 100))
                    musket1 = ImageTk.PhotoImage(rmusket)
                    musket2 = tk.Label(adv, image=musket1, bg="black")
                    musket2.image = musket1
                    musket2.place(x=100, y=60)
                    musket_bt = tk.Button(adv, text=" The Three \n Musketeers", width=11, command=mkt8)
                    musket_bt.config(font=("Courier", 12, "bold"))
                    musket_bt.place(x=100, y=170)

                    treasure = Image.open("/Users/garimagrover/Desktop/treasure.png")
                    rtreasure = treasure.resize((75, 100))
                    treasure1 = ImageTk.PhotoImage(rtreasure)
                    treasure2 = tk.Label(adv, image=treasure1, bg="black")
                    treasure2.image = treasure1
                    treasure2.place(x=320, y=60)
                    treasure_bt = tk.Button(adv, text="Treasure \n Island", width=11, command=tres8)
                    treasure_bt.config(font=("Courier", 12, "bold"))
                    treasure_bt.place(x=320, y=170)
                    adv.mainloop()
            ch4 = tk.Checkbutton(cust, text='Adventure', variable=var4, onvalue=1, offvalue=0,bg="#FFFFE0",command=adv1)
            ch4.config(font=("Courier", 18))
            ch4.place(x=18, y=260)

            def fic1():
                if var5.get()==1:
                    fic=tk.Toplevel()
                    fic.config(bg="black")
                    fic.title("FICTION")
                    fic.geometry("500x300")
                    fic.geometry("+300+250")

                    kots = Image.open("/Users/garimagrover/Desktop/kots.png")
                    rkots = kots.resize((75, 100))
                    kots1 = ImageTk.PhotoImage(rkots)
                    kots2 = tk.Label(fic, image=kots1, bg="black")
                    kots2.image = kots1
                    kots2.place(x=100, y=60)
                    kots_bt = tk.Button(fic, text=" Kafka on \n the shore", height=2, width=11, command=kots8)
                    kots_bt.config(font=("Courier", 11, "bold"))
                    kots_bt.place(x=100, y=170)

                    malgudi = Image.open("/Users/garimagrover/Desktop/malgudi.png")
                    rmalgudi = malgudi.resize((75, 100))
                    malgudi1 = ImageTk.PhotoImage(rmalgudi)
                    malgudi2 = tk.Label(fic, image=malgudi1, bg="#FFFFE0")
                    malgudi2.image = malgudi1
                    malgudi2.place(x=320, y=60)
                    malgudi_bt = tk.Button(fic, text="Malgudi \n Days", width=11, command=malgudi8)
                    malgudi_bt.config(font=("Courier", 12, "bold"))
                    malgudi_bt.place(x=320, y=175)
                    fic.mainloop()
            ch5 = tk.Checkbutton(cust, text='Fiction', variable=var5, onvalue=1, offvalue=0,bg="#FFFFE0",command=fic1)
            ch5.config(font=("Courier", 18))
            ch5.place(x=18, y=290)

            def bio1():
                if var6.get()==1:
                    bio=tk.Toplevel()
                    bio.config(bg="black")
                    bio.title("BIOGRAPHY")
                    bio.geometry("500x300")
                    bio.geometry("+300+250")

                    become = Image.open("/Users/garimagrover/Desktop/becoming.png")
                    rbec = become.resize((75, 100))
                    bec1 = ImageTk.PhotoImage(rbec)
                    bec2 = tk.Label(bio, image=bec1, bg="black")
                    bec2.image = bec1
                    bec2.place(x=100, y=60)
                    bec_bt = tk.Button(bio, text="Becoming", height=2, width=11, command=bec8)
                    bec_bt.config(font=("Courier", 12, "bold"))
                    bec_bt.place(x=100, y=170)

                    edu = Image.open("/Users/garimagrover/Desktop/educated.png")
                    redu = edu.resize((75, 100))
                    edu1 = ImageTk.PhotoImage(redu)
                    edul = tk.Label(bio, image=edu1, bg="black")
                    edul.image = edu1
                    edul.place(x=320, y=60)
                    edu_bt = tk.Button(bio, text="Educated", height=2, width=11, bg="#FFFFE0", command=edu8)
                    edu_bt.config(font=("Courier", 12, "bold"))
                    edu_bt.place(x=320, y=170)
                    bio.mainloop()
            ch6 = tk.Checkbutton(cust, text='Biography', variable=var6, onvalue=1, offvalue=0,bg="#FFFFE0",command=bio1)
            ch6.config(font=("Courier", 18))
            ch6.place(x=18, y=320)

            def rom1():
                if var7.get()==1:
                    rom=tk.Toplevel()
                    rom.config(bg="black")
                    rom.title("ROMANCE")
                    rom.geometry("600x400")
                    rom.geometry("+300+250")

                    hate = Image.open("/Users/garimagrover/Desktop/hate.png")
                    rhate = hate.resize((75, 100))
                    hate1 = ImageTk.PhotoImage(rhate)
                    hate2 = tk.Label(rom, image=hate1, bg="black")
                    hate2.image = lord1
                    hate2.place(x=135, y=40)
                    hate_bt = tk.Button(rom, text=" The Hating \n Game", width=11, command=hate8)
                    hate_bt.config(font=("Courier", 12, "bold"))
                    hate_bt.place(x=135, y=150)

                    ends = Image.open("/Users/garimagrover/Desktop/ends.png")
                    rends = ends.resize((75, 100))
                    ends1 = ImageTk.PhotoImage(rends)
                    ends2 = tk.Label(rom, image=ends1, bg="black")
                    ends2.image = ends1
                    ends2.place(x=20, y=222)
                    ends_bt = tk.Button(rom, text=" It ends \n with us", width=11, command=end8)
                    ends_bt.config(font=("Courier", 12, "bold"))
                    ends_bt.place(x=20, y=335)

                    ntb = Image.open("/Users/garimagrover/Desktop/ntb.png")
                    rntb = ntb.resize((75, 100))
                    ntb1 = ImageTk.PhotoImage(rntb)
                    ntb2 = tk.Label(rom, image=ntb1, bg="black")
                    ntb2.image = ntb1
                    ntb2.place(x=353, y=40)
                    ntb_bt = tk.Button(rom, text=" The \n Notebook", width=11, command=nb8)
                    ntb_bt.config(font=("Courier", 12, "bold"))
                    ntb_bt.place(x=353, y=150)

                    out = Image.open("/Users/garimagrover/Desktop/out.png")
                    rout = out.resize((75, 100))
                    out1 = ImageTk.PhotoImage(rout)
                    out2 = tk.Label(rom, image=out1, bg="#FFFFE0")
                    out2.image = out1
                    out2.place(x=475, y=222)
                    out_bt = tk.Button(rom, text="Outlander", width=10, height=2, command=ot8)
                    out_bt.config(font=("Courier", 13, "bold"))
                    out_bt.place(x=475, y=335)

                    secret = Image.open("/Users/garimagrover/Desktop/secret.png")
                    rsecret = secret.resize((75, 100))
                    secret1 = ImageTk.PhotoImage(rsecret)
                    secret2 = tk.Label(rom, image=secret1, bg="black")
                    secret2.image = secret1
                    secret2.place(x=240, y=222)
                    secret_bt = tk.Button(rom, text=" The Secrets \n we keep", width=11, command=sct8)
                    secret_bt.config(font=("Courier", 12, "bold"))
                    secret_bt.place(x=240, y=335)
                    rom.mainloop()
            ch7 = tk.Checkbutton(cust, text='Romance', variable=var7, onvalue=1, offvalue=0,bg="#FFFFE0",command=rom1)
            ch7.config(font=("Courier", 18))
            ch7.place(x=18, y=350)

            def his1():
                if var8.get():
                    his=tk.Toplevel()
                    his.title("HISTORICAL")
                    his.config(bg="black")
                    his.geometry("300x200")
                    his.geometry("+300+250")

                    ttp = Image.open("/Users/garimagrover/Desktop/ttp.png")
                    rttp = ttp.resize((76, 105))
                    ttp1 = ImageTk.PhotoImage(rttp)
                    ttp2 = tk.Label(his, image=ttp1, bg="black")
                    ttp2.image = ttp1
                    ttp2.place(x=115, y=20)
                    ttp_bt = tk.Button(his, text="Train to \n Pakistan", width=11, command=ttp8)
                    ttp_bt.config(font=("Courier", 11, "bold"))
                    ttp_bt.place(x=115, y=140)
                    his.mainloop()
            ch8 = tk.Checkbutton(cust, text='Historical', variable=var8, onvalue=1, offvalue=0,bg="#FFFFE0",command=his1)
            ch8.config(font=("Courier", 18))
            ch8.place(x=18, y=380)

            def pty1():
                if var9.get()==1:
                    pty=tk.Toplevel()
                    pty.title("POETRY")
                    pty.config(bg="black")
                    pty.geometry("300x200")
                    pty.geometry("+300+250")

                    magic = Image.open("/Users/garimagrover/Desktop/magic.png")
                    rmagic = magic.resize((77, 106))
                    magic1 = ImageTk.PhotoImage(rmagic)
                    magic2 = tk.Label(pty, image=magic1, bg="black")
                    magic2.image = magic1
                    magic2.place(x=115, y=20)
                    magic_bt = tk.Button(pty, text=" Love, Hope \n and Magic", width=11, command=mgc8)
                    magic_bt.config(font=("Courier", 12, "bold"))
                    magic_bt.place(x=115, y=140)
                    pty.mainloop()
            ch9 = tk.Checkbutton(cust, text='Poetry', variable=var9, onvalue=1, offvalue=0,bg="#FFFFE0",command=pty1)
            ch9.config(font=("Courier", 18))
            ch9.place(x=18, y=410)

            def crm1():
                if var10.get()==1:
                    crm=tk.Toplevel()
                    crm.config(bg="black")
                    crm.title("CRIME")
                    crm.geometry("600x400")
                    crm.geometry("+300+250")

                    night = Image.open("/Users/garimagrover/Desktop/night.png")
                    rnight = night.resize((75, 100))
                    night1 = ImageTk.PhotoImage(rnight)
                    night2 = tk.Label(crm, image=night1, bg="black")
                    night2.image = night1
                    night2.place(x=100, y=30)
                    night_bt = tk.Button(crm, text=" Daughters \n of Night", width=11, command=dgt8)
                    night_bt.config(font=("Courier", 12, "bold"))
                    night_bt.place(x=100, y=150)

                    train = Image.open("/Users/garimagrover/Desktop/train.png")
                    rtrain = train.resize((75, 100))
                    train1 = ImageTk.PhotoImage(rtrain)
                    train2 = tk.Label(crm, image=train1, bg="#FFFFE0")
                    train2.image = train1
                    train2.place(x=350, y=30)
                    train_bt = tk.Button(crm, text=" The Girl on \n the Train", width=11, command=train8)
                    train_bt.config(font=("Courier", 12, "bold"))
                    train_bt.place(x=350, y=150)

                    killing = Image.open("/Users/garimagrover/Desktop/killing.png")
                    rkill = killing.resize((75, 100))
                    kill1 = ImageTk.PhotoImage(rkill)
                    kill = tk.Label(crm, image=kill1, bg="black")
                    kill.image = kill1
                    kill.place(x=225, y=205)
                    kill_bt = tk.Button(crm, text="Killing \n Tide", width=11, command=kill8)
                    kill_bt.config(font=("Courier", 11, "bold"))
                    kill_bt.place(x=225, y=317)

                    thief = Image.open("/Users/garimagrover/Desktop/thief.png")
                    rthief = thief.resize((75, 100))
                    thief1 = ImageTk.PhotoImage(rthief)
                    thief2 = tk.Label(crm, image=thief1, bg="black")
                    thief2.image = thief1
                    thief2.place(x=470, y=205)
                    thief_bt = tk.Button(crm, text="The \n Thief", width=11, command=thief8)
                    thief_bt.config(font=("Courier", 12, "bold"))
                    thief_bt.place(x=470, y=315)
                    crm.mainloop()
            ch10 = tk.Checkbutton(cust, text='Crime', variable=var10, onvalue=1, offvalue=0,bg="#FFFFE0",command=crm1)
            ch10.config(font=("Courier", 18))
            ch10.place(x=18, y=440)

            labe4 = tk.Label(cust, text="Cost -:", bg="#FFFFE0")
            labe4.config(font=("Courier", 23, "bold"))
            labe4.place(x=18, y=500)

            cm = ttk.Combobox(cust, width=18)
            cm['values'] = ('100-300','300-600','600-1000')
            cm.config(font=("Courier", 17))
            cm.place(x=15, y=540)

            def filter():
                if cm.get()=='100-300':
                    filt=tk.Toplevel()
                    filt.config(bg='black')
                    filt.title("SHOP")
                    filt.geometry("610x400")
                    filt.geometry("+400+250")

                    colour = Image.open("/Users/garimagrover/Desktop/colour.png")
                    rcolour = colour.resize((75, 100))
                    colour1 = ImageTk.PhotoImage(rcolour)
                    colour2 = tk.Label(filt, image=colour1, bg="black")
                    colour2.image = colour1
                    colour2.place(x=45, y=20)
                    colour_bt = tk.Button(filt, text=" The Colour \n of Magic", width=11, command=clr8)
                    colour_bt.config(font=("Courier", 12, "bold"))
                    colour_bt.place(x=45, y=130)

                    edu = Image.open("/Users/garimagrover/Desktop/educated.png")
                    redu = edu.resize((75, 100))
                    edu1 = ImageTk.PhotoImage(redu)
                    edul = tk.Label(filt, image=edu1, bg="black")
                    edul.image = edu1
                    edul.place(x=154, y=20)
                    edu_bt = tk.Button(filt, text="Educated", height=2, width=11, bg="#FFFFE0", command=edu8)
                    edu_bt.config(font=("Courier", 12, "bold"))
                    edu_bt.place(x=154, y=130)

                    train = Image.open("/Users/garimagrover/Desktop/train.png")
                    rtrain = train.resize((75, 100))
                    train1 = ImageTk.PhotoImage(rtrain)
                    train2 = tk.Label(filt, image=train1, bg="black")
                    train2.image = train1
                    train2.place(x=263, y=20)
                    train_bt = tk.Button(filt, text=" The Girl on \n the Train", width=11, command=train8)
                    train_bt.config(font=("Courier", 12, "bold"))
                    train_bt.place(x=263, y=130)

                    magic = Image.open("/Users/garimagrover/Desktop/magic.png")
                    rmagic = magic.resize((75, 100))
                    magic1 = ImageTk.PhotoImage(rmagic)
                    magic2 = tk.Label(filt, image=magic1, bg="black")
                    magic2.image = magic1
                    magic2.place(x=374, y=20)
                    magic_bt = tk.Button(filt, text=" Love, Hope \n and Magic", width=11, command=mgc8)
                    magic_bt.config(font=("Courier", 12, "bold"))
                    magic_bt.place(x=374, y=130)

                    mart = Image.open("/Users/garimagrover/Desktop/martian.png")
                    rmart = mart.resize((75, 100))
                    mart1 = ImageTk.PhotoImage(rmart)
                    mart2 = tk.Label(filt, image=mart1, bg="black")
                    mart2.image = mart1
                    mart2.place(x=485, y=20)
                    mart_bt = tk.Button(filt, text="The \n Martian", width=11, command=mart8)
                    mart_bt.config(font=("Courier", 11, "bold"))
                    mart_bt.place(x=485, y=130)

                    malgudi = Image.open("/Users/garimagrover/Desktop/malgudi.png")
                    rmalgudi = malgudi.resize((75, 100))
                    malgudi1 = ImageTk.PhotoImage(rmalgudi)
                    malgudi2 = tk.Label(filt, image=malgudi1, bg="black")
                    malgudi2.image = malgudi1
                    malgudi2.place(x=90, y=210)
                    malgudi_bt = tk.Button(filt, text="Malgudi \n Days", width=11, command=malgudi8)
                    malgudi_bt.config(font=("Courier", 12, "bold"))
                    malgudi_bt.place(x=90, y=320)

                    ntb = Image.open("/Users/garimagrover/Desktop/ntb.png")
                    rntb = ntb.resize((75, 100))
                    ntb1 = ImageTk.PhotoImage(rntb)
                    ntb2 = tk.Label(filt, image=ntb1, bg="black")
                    ntb2.image = ntb1
                    ntb2.place(x=210, y=210)
                    ntb_bt = tk.Button(filt, text=" The \n Notebook", width=11, command=nb8)
                    ntb_bt.config(font=("Courier", 12, "bold"))
                    ntb_bt.place(x=210, y=320)

                    musket = Image.open("/Users/garimagrover/Desktop/musket.png")
                    rmusket = musket.resize((75, 100))
                    musket1 = ImageTk.PhotoImage(rmusket)
                    musket2 = tk.Label(filt, image=musket1, bg="black")
                    musket2.image = musket1
                    musket2.place(x=330, y=210)
                    musket_bt = tk.Button(filt, text=" The Three \n Musketeers", width=11, command=mkt8)
                    musket_bt.config(font=("Courier", 12, "bold"))
                    musket_bt.place(x=330, y=320)

                    ttp = Image.open("/Users/garimagrover/Desktop/ttp.png")
                    rttp = ttp.resize((75, 100))
                    ttp1 = ImageTk.PhotoImage(rttp)
                    ttp2 = tk.Label(filt, image=ttp1, bg="black")
                    ttp2.image = ttp1
                    ttp2.place(x=450, y=210)
                    ttp_bt = tk.Button(filt, text="Train to \n Pakistan", width=11, command=ttp8)
                    ttp_bt.config(font=("Courier", 11, "bold"))
                    ttp_bt.place(x=450, y=320)
                    filt.mainloop()

                if cm.get()=="300-600":
                    filt=tk.Toplevel()
                    filt.config(bg="black")
                    filt.title("SHOP")
                    filt.geometry("610x550")
                    filt.geometry("+400+150")

                    night = Image.open("/Users/garimagrover/Desktop/night.png")
                    rnight = night.resize((75, 100))
                    night1 = ImageTk.PhotoImage(rnight)
                    night2 = tk.Label(filt, image=night1, bg="black")
                    night2.image = night1
                    night2.place(x=60, y=20)
                    night_bt = tk.Button(filt, text=" Daughters \n of Night", width=11, command=dgt8)
                    night_bt.config(font=("Courier", 12, "bold"))
                    night_bt.place(x=60, y=135)

                    vinci = Image.open("/Users/garimagrover/Desktop/vinci.png")
                    rvinci = vinci.resize((75, 100))
                    vinci1 = ImageTk.PhotoImage(rvinci)
                    vinci2 = tk.Label(filt, image=vinci1, bg="black")
                    vinci2.image = vinci1
                    vinci2.place(x=170, y=20)
                    vinci_bt = tk.Button(filt, text="Da Vinci \n Code", width=11, command=vin8)
                    vinci_bt.config(font=("Courier", 12, "bold"))
                    vinci_bt.place(x=170, y=135)

                    edge = Image.open("/Users/garimagrover/Desktop/edge.png")
                    redge = edge.resize((75, 100))
                    edge1 = ImageTk.PhotoImage(redge)
                    edge2 = tk.Label(filt, image=edge1, bg="black")
                    edge2.image = edge1
                    edge2.place(x=282, y=20)
                    edge_bt = tk.Button(filt, text=" The Edge of \n the Grave", width=11, command=ed8)
                    edge_bt.config(font=("Courier", 12, "bold"))
                    edge_bt.place(x=282, y=135)

                    hate = Image.open("/Users/garimagrover/Desktop/hate.png")
                    rhate = hate.resize((75, 100))
                    hate1 = ImageTk.PhotoImage(rhate)
                    hate2 = tk.Label(filt, image=hate1, bg="black")
                    hate2.image = hate1
                    hate2.place(x=400, y=20)
                    hate_bt = tk.Button(filt, text=" The Hating \n Game", width=11, command=hate8)
                    hate_bt.config(font=("Courier", 12, "bold"))
                    hate_bt.place(x=400, y=135)

                    klara = Image.open("/Users/garimagrover/Desktop/klara.png")
                    rklara = klara.resize((75, 100))
                    klara1 = ImageTk.PhotoImage(rklara)
                    klara2 = tk.Label(filt, image=klara1, bg="black")
                    klara2.image = klara1
                    klara2.place(x=100, y=200)
                    klara_bt = tk.Button(filt, text="Klara and \n the Sun", width=11, command=kl8)
                    klara_bt.config(font=("Courier", 12, "bold"))
                    klara_bt.place(x=100, y=315)

                    kots = Image.open("/Users/garimagrover/Desktop/kots.png")
                    rkots = kots.resize((75, 100))
                    kots1 = ImageTk.PhotoImage(rkots)
                    kots2 = tk.Label(filt, image=kots1, bg="black")
                    kots2.image = kots1
                    kots2.place(x=220, y=200)
                    kots_bt = tk.Button(filt, text=" Kafka on \n the shore", height=2, width=11, command=kots8)
                    kots_bt.config(font=("Courier", 11, "bold"))
                    kots_bt.place(x=220, y=315)

                    killing = Image.open("/Users/garimagrover/Desktop/killing.png")
                    rkill = killing.resize((75, 100))
                    kill1 = ImageTk.PhotoImage(rkill)
                    kill = tk.Label(filt, image=kill1, bg="black")
                    kill.image = kill1
                    kill.place(x=340, y=200)
                    kill_bt = tk.Button(filt, text="Killing \n Tide", width=11, command=kill8)
                    kill_bt.config(font=("Courier", 11, "bold"))
                    kill_bt.place(x=340, y=315)

                    guest = Image.open("/Users/garimagrover/Desktop/guest.png")
                    rguest = guest.resize((75, 100))
                    guest1 = ImageTk.PhotoImage(rguest)
                    guest2 = tk.Label(filt, image=guest1, bg="black")
                    guest2.image = guest1
                    guest2.place(x=460, y=200)
                    guest_bt = tk.Button(filt, text="The Guest \n List", width=11, command=gst8)
                    guest_bt.config(font=("Courier", 12, "bold"))
                    guest_bt.place(x=460, y=315)

                    secret = Image.open("/Users/garimagrover/Desktop/secret.png")
                    rsecret = secret.resize((75, 100))
                    secret1 = ImageTk.PhotoImage(rsecret)
                    secret2 = tk.Label(filt, image=secret1, bg="black")
                    secret2.image = secret1
                    secret2.place(x=60, y=380)
                    secret_bt = tk.Button(filt, text=" The Secrets \n we keep", width=11, command=sct8)
                    secret_bt.config(font=("Courier", 12, "bold"))
                    secret_bt.place(x=60, y=495)

                    treasure = Image.open("/Users/garimagrover/Desktop/treasure.png")
                    rtreasure = treasure.resize((75, 100))
                    treasure1 = ImageTk.PhotoImage(rtreasure)
                    treasure2 = tk.Label(filt, image=treasure1, bg="black")
                    treasure2.image = treasure1
                    treasure2.place(x=180, y=380)
                    treasure_bt = tk.Button(filt, text="Treasure \n Island", width=11, command=tres8)
                    treasure_bt.config(font=("Courier", 12, "bold"))
                    treasure_bt.place(x=180, y=495)

                    machine = Image.open("/Users/garimagrover/Desktop/time.png")
                    rmachine = machine.resize((75, 100))
                    machine1 = ImageTk.PhotoImage(rmachine)
                    machine2 = tk.Label(filt, image=machine1, bg="black")
                    machine2.image = machine1
                    machine2.place(x=300, y=380)
                    machine_bt = tk.Button(filt, text=" The Time \n Machine", width=11, command=tm8)
                    machine_bt.config(font=("Courier", 12, "bold"))
                    machine_bt.place(x=300, y=495)

                    thief = Image.open("/Users/garimagrover/Desktop/thief.png")
                    rthief = thief.resize((75, 100))
                    thief1 = ImageTk.PhotoImage(rthief)
                    thief2 = tk.Label(filt, image=thief1, bg="black")
                    thief2.image = thief1
                    thief2.place(x=420, y=380)
                    thief_bt = tk.Button(filt, text="The \n Thief", width=11, command=thief8)
                    thief_bt.config(font=("Courier", 12, "bold"))
                    thief_bt.place(x=420, y=495)

                    filt.mainloop()
                if cm.get()=="600-1000":
                    filt = tk.Toplevel()
                    filt.config(bg='black')
                    filt.title("SHOP")
                    filt.geometry("500x400")
                    filt.geometry("+400+250")

                    become = Image.open("/Users/garimagrover/Desktop/becoming.png")
                    rbec = become.resize((75, 100))
                    bec1 = ImageTk.PhotoImage(rbec)
                    bec2 = tk.Label(filt, image=bec1, bg="black")
                    bec2.image = bec1
                    bec2.place(x=60, y=20)
                    bec_bt = tk.Button(filt, text="Becoming", height=2, width=11, command=bec8)
                    bec_bt.config(font=("Courier", 12, "bold"))
                    bec_bt.place(x=60, y=135)

                    dune = Image.open("/Users/garimagrover/Desktop/dune.png")
                    rdune = dune.resize((75, 100))
                    dune1 = ImageTk.PhotoImage(rdune)
                    dune2 = tk.Label(filt, image=dune1, bg="black")
                    dune2.image = dune1
                    dune2.place(x=180, y=20)
                    dune_bt = tk.Button(filt, text=" Dune", width=10, height=2, command=dn8)
                    dune_bt.config(font=("Courier", 13, "bold"))
                    dune_bt.place(x=180, y=135)

                    ends = Image.open("/Users/garimagrover/Desktop/ends.png")
                    rends = ends.resize((75, 100))
                    ends1 = ImageTk.PhotoImage(rends)
                    ends2 = tk.Label(filt, image=ends1, bg="black")
                    ends2.image = ends1
                    ends2.place(x=300, y=20)
                    ends_bt = tk.Button(filt, text=" It ends \n with us", width=11, command=end8)
                    ends_bt.config(font=("Courier", 12, "bold"))
                    ends_bt.place(x=300, y=135)

                    lord = Image.open("/Users/garimagrover/Desktop/lord.png")
                    rlord = lord.resize((75, 100))
                    lord1 = ImageTk.PhotoImage(rlord)
                    lord2 = tk.Label(filt, image=lord1, bg="black")
                    lord2.image = lord1
                    lord2.place(x=60, y=210)
                    lord_bt = tk.Button(filt, text="The Lord of \n the Rings", width=11, command=lord8)
                    lord_bt.config(font=("Courier", 12, "bold"))
                    lord_bt.place(x=60, y=320)

                    malibu = Image.open("/Users/garimagrover/Desktop/malibu.png")
                    rmalibu = malibu.resize((75, 100))
                    malibu1 = ImageTk.PhotoImage(rmalibu)
                    malibu2 = tk.Label(filt, image=malibu1, bg="black")
                    malibu2.image = malibu1
                    malibu2.place(x=180, y=210)
                    malibu_bt = tk.Button(filt, text="Malibu \n Rising", width=11, command=mal8)
                    malibu_bt.config(font=("Courier", 12, "bold"))
                    malibu_bt.place(x=180, y=320)

                    out = Image.open("/Users/garimagrover/Desktop/out.png")
                    rout = out.resize((75, 100))
                    out1 = ImageTk.PhotoImage(rout)
                    out2 = tk.Label(filt, image=out1, bg="black")
                    out2.image = out1
                    out2.place(x=300, y=210)
                    out_bt = tk.Button(filt, text="Outlander", width=10, height=2, command=ot8)
                    out_bt.config(font=("Courier", 13, "bold"))
                    out_bt.place(x=300, y=320)
                    filt.mainloop()

            but9 = tk.Button(cust, text="Filter", width=9, highlightbackground="#FFFFE0",command=filter)
            but9.config(font=("Courier", 15))
            but9.place(x=81, y=585)

            def new1():
                new = tk.Toplevel()
                new.config(bg='black')
                new.title("NEW RELEASES")
                new.geometry("400x200")
                new.geometry("+400+250")

                become = Image.open("/Users/garimagrover/Desktop/becoming.png")
                rbec = become.resize((75, 100))
                bec1 = ImageTk.PhotoImage(rbec)
                bec2 = tk.Label(new, image=bec1, bg="black")
                bec2.image = bec1
                bec2.place(x=100, y=20)
                bec_bt = tk.Button(new, text="Becoming", height=2, width=11, command=bec8)
                bec_bt.config(font=("Courier", 12, "bold"))
                bec_bt.place(x=100, y=140)

                kots = Image.open("/Users/garimagrover/Desktop/kots.png")
                rkots = kots.resize((75, 100))
                kots1 = ImageTk.PhotoImage(rkots)
                kots2 = tk.Label(new, image=kots1, bg="black")
                kots2.image = kots1
                kots2.place(x=230, y=20)
                kots_bt = tk.Button(new, text=" Kafka on \n the shore", height=2, width=11, command=kots8)
                kots_bt.config(font=("Courier", 11, "bold"))
                kots_bt.place(x=230, y=140)
                new.mainloop()
            rad0=tk.Radiobutton(cust,text="New Releases",bg="#FFFFE0",command=new1)
            rad0.config(font=("Courier", 20,"bold"))
            rad0.place(x=15,y=660)
            cust.mainloop()

        b5 = tk.Button(custom, text="LEAF  THROUGH", height=2, width=43, activeforeground="darkorchid1",highlightbackground="brown", command=customer)
        b5.config(font=("Courier", 15, "bold"))
        b5.place(x=263, y=530)
        custom.mainloop()

    bt1=tk.Button(window,text="OFFICIAL",command=official,activeforeground='darkorchid1',highlightbackground="darkorchid1",)
    bt2=tk.Button(window,text="CUSTOMER",activeforeground='darkorchid1',highlightbackground="darkorchid1",command=shop)
    bt1.config(font=("Courier", 30))
    bt2.config(font=("Courier", 30))
    bt1.place(x=320,y=148,height=50,width=200)
    bt2.place(x=320,y=258,height=50,width=200)

    window.mainloop()