from tkinter import *
import tkinter as tt

root = Tk()
v=tt.IntVar()
root.geometry('600x600')
l = Label(root, text='LOGIN PAGE')
l.pack()

#new window
def window():
    root1=Tk()
    value=v.get()
    root1.geometry("500x500")
    l2 =Label(root1,text="Name")
    l3=Label(root1,text="Password")
    l2.grid(row=0,column=1,sticky=E)
    l3.grid(row=1,column=1,sticky=E)
    entry1=Entry(root1)
    entry2=Entry(root1)
    entry1.grid(row=0,column=2)
    entry2.grid(row=1,column=2)
    def store():
        name1=entry1.get()
        password1 =entry2.get()
        fileName = name1 + ".txt"
        try:
            existingfile = open(fileName)
            #print("Account with same name exists,try using different Name")
            l4=Label(root1,text="Account with same name exists,try using different name")
            l4.grid(rowspan=4,columnspan=2,row=30,column=1)
            existingfile.close()
        except:
            # creating a File
            File1 = open(fileName, 'w')
            File1.write(password1)
            File1.close()
            l5=Label(root1,text="Account Successfully created!")
            l5.grid(rowspan=4,columnspan=2,row=30,column=1)

    def login():
        name1=entry1.get()
        password1 =entry2.get()
        File2 = name1 + '.txt'
        while True:
            try:
                file3 = open(File2)
                cont = file3.read()
                passowrd = password1
                if cont == passowrd:
                    l6=Label(root1,text="Successfully logged in!")
                    l6.grid(rowspan=4,columnspan=2,row=30,column=1)
                    file3.close()
                    break
                else:
                    l7 = Label(root1,text="Incorrect password!")
                    l7.grid(rowspan=4,columnspan=2,row=30,column=1)
                    file3.close()
                    break

            except:
                l8 = Label(root1,text="Account doesn't exist!")
                l8.grid(rowspan=4,columnspan=2,row=30,column=1)
                break
    if value == 0:
        button3 = Button(root1,text="Create",bg="blue",fg="white",command=lambda:store())
        button3.grid(columnspan=2, rowspan=2, row=2, column=2)
    else:
        button4=Button(root1,text="Login", bg="blue", fg="white", command=lambda : login())
        button4.grid(columnspan=2, rowspan=2,row=2,column=2)
    root1.mainloop()

b1 = Radiobutton(root, variable=v, value=0, text="Sign up", command=window)
b2 = Radiobutton(root, variable=v, value=1, text="Sign In", command=window)
b1.pack()
b2.pack()

root.mainloop()