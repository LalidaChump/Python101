from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()#หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดของโปรแกรม

L1 = Label(GUI,text='โปรมแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

def Button2(): #การเก็บคำสั่งหลายๆคำสั่ง
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบันชี',text) #การสร้างMsb Showeror,showinfo

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาที่เรียน 10-20 ก.พ.',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=80)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()
