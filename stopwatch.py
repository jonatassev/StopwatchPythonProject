from tkinter import *
from write import Write


global count
count = 0

class Stopwatch():
    
    def start(self):
        global count
        count = 0
        self.bt1['state'] = 'disabled'
        self.bt2['state'] = 'normal'
        self.timer()

    def pause(self):
        global count
        count = 1
        self.bt1['state'] = 'normal'
        self.bt2['state'] = 'disabled'


    def write(self):
        global count
        count = 1
        wr = Write(self.root)


    def reset(self):
        global count
        count = 1
        self.t.set('00:00:00')
    
    def close(self):
        self.root.destroy()

    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m = int(m)
            s = int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)

    def getTime(self):
        return self.t

    def __init__(self):
        self.root=Tk()
        self.root.title("OSTEC Projetos")
        self.root.minsize(width=260, height=70)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Arial 40 bold"))
        self.bt1 = Button(self.root,text="Iniciar",command=self.start,font=("Arial 12 bold"),bg=("green"))
        self.bt2 = Button(self.root,text="Pausar",command=self.pause,font=("Arial 12 bold"),bg=("red"))
        self.bt3 = Button(self.root,text="Gravar",command=self.write,font=("Arial 12 bold"),bg=("orange"))
        self.bt4 = Button(self.root,text="Resetar",command=self.reset,font=("Arial 12 bold"),bg=("orange"))
        self.bt5 = Button(self.root, text="Sair", command=self.close,font=("Arial 12 bold"),bg=("yellow"))
        self.lb.pack(anchor = 'center',pady=20)
        self.bt1.pack(side="left",pady=5)
        self.bt2.pack(side ="left",pady=5)
        self.bt3.pack(side="left",pady=5)
        self.bt4.pack(side="left",pady=5)
        self.bt5.pack(side="left",pady=5)

        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.mainloop()
