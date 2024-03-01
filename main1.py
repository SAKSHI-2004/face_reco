from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x850+0+0")
        self.root.title("face Recognition System")
        self.root.config(bg="#0e2433")

        self.bg_image=ImageTk.PhotoImage(file="file/bg img 3 (1).png")
        self.lbl_bg_image=Label(self.root,image=self.bg_image,bd=0).place(x=0,y=0,width=1530,height=850)

        #=====images=========
        self.phone_image=ImageTk.PhotoImage(file="image/faceimg.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=90)

        


        #=====login_frame========

        login_frame=Frame(self.root,bd=2,relief=RIDGE)
        login_frame.place(x=800,y=100,width=400,height=500)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold")).place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="#f1f3f2",fg="#040401").place(x=60,y=120)
        self.Username=StringVar()
        self.Password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.Username,font=("times new roman",15),bg="#c0c9c5").place(x=50,y=160,width=300)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="#f1f3f2",fg="#040401").place(x=60,y=200)
        txt_pass=Entry(login_frame,textvariable=self.Password,show="*",font=("times new roman",15),bg="#c0c9c5").place(x=50,y=240,width=300)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",cursor="hand2").place(x=50,y=300,width=300,height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=300,height=2)
        or_=Label(login_frame,text="OR",bg="#f1f3f2",fg="lightgray",font=("times new roman",15,"bold")).place(x=180,y=360)

        btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="#f1f3f2",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=135,y=400)

        #=====Frame 2=======

        register_frame=Frame(self.root,bd=2,relief=RIDGE)
        register_frame.place(x=800,y=630,width=400,height=60)
        
        lbl_reg=Label(register_frame,text="Don't have an account ?",font=("times new roman",13),bg="#f1f3f2").place(x=50,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="#f1f3f2",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=220,y=20)

       

        










    def login(self):
         if self.Username.get()=="" or self.Password.get()=="":
              messagebox.showerror("Error","All Fields are required")
         elif self.Username.get()!="Rangesh" or self.Password.get()!="123456":    #==see this thing in database===
              messagebox.showerror("Error","Invalid Username or Password\nTry again with correct  credentials")      
         else:
              messagebox.showinfo("Information",f"Welcome: {self.Username.get()}\nYour Password: {self.Password.get()}")



if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()

