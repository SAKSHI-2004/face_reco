from tkinter import*
from PIL import ImageTk
from studetails1 import student_System


class Dashboard_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x850+0+0")
        self.root.title("face Recognition System")
        self.root.config(bg="#0e2433")

        #upper 8 images 
        self.phone_image1=ImageTk.PhotoImage(file="file/new 1.png")
        self.lbl_Phone_image1=Label(self.root,image=self.phone_image1,bd=0).place(x=0,y=0,width=256,height=130)
        self.phone_image2=ImageTk.PhotoImage(file="file/new 2.png")
        
        self.lbl_Phone_image2=Label(self.root,image=self.phone_image2,bd=0).place(x=256,y=0,width=411,height=130)
        self.phone_image3=ImageTk.PhotoImage(file="file/new 3.png")
        self.lbl_Phone_image3=Label(self.root,image=self.phone_image3,bd=0).place(x=667,y=0,width=195,height=130)
        self.phone_image4=ImageTk.PhotoImage(file="file/new 4.png")
        self.lbl_Phone_image4=Label(self.root,image=self.phone_image4,bd=0).place(x=862,y=0,width=246,height=130)
        self.phone_image5=ImageTk.PhotoImage(file="file/new 5.png")
        self.lbl_Phone_image5=Label(self.root,image=self.phone_image5,bd=0).place(x=1108,y=0,width=215,height=130)
        self.phone_image6=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image6=Label(self.root,image=self.phone_image6,bd=0).place(x=1323,y=0,width=207,height=130)

        #background color 
        self.bg_image=ImageTk.PhotoImage(file="file/bg image 2.png")
        self.lbl_bg_image=Label(self.root,image=self.bg_image,bd=0).place(x=0,y=130,width=1530,height=720)


        


        #title lable
        title_lbl=Label(text=" BIOMETRIC   ATTENDANCE   SYSTEM   SOFTWARE ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)

        # 1student button img 
        self.phone_image7=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image7=Label(self.root,image=self.phone_image7,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 1
        b1=Button(image=self.lbl_Phone_image7,command=self.smart,cursor="hand2")
        b1.place(x=218,y=200, width=220,height=220)
        #button text,c
        b1_1=Button(text="STUDENTS DETAILS",command=self.smart,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=218,y=422, width=220,height=40)

         #2detect face  button img 
        self.phone_image8=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image8=Label(self.root,image=self.phone_image8,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 2
        b2=Button(image=self.lbl_Phone_image8,cursor="hand2")
        b2.place(x=656,y=200, width=220,height=220)
        #button 2 text
        b2_1=Button(text="FACE  RECOGNITION ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b2_1.place(x=656,y=422, width=220,height=40)

        #3button img 
        self.phone_image9=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image9=Label(self.root,image=self.phone_image9,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 3
        b3=Button(image=self.lbl_Phone_image7,cursor="hand2")
        b3.place(x=1094,y=200, width=220,height=220)
        #button 3 text
        b3_1=Button(text="EYE RECOGNITION ",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b3_1.place(x=1094,y=422, width=220,height=40)

      
        #4th button in 2nd row 
        self.phone_image10=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image10=Label(self.root,image=self.phone_image10,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 4
        b4=Button(image=self.lbl_Phone_image7,cursor="hand2")
        b4.place(x=218,y=500, width=220,height=220)
        #button text
        b4_1=Button(text="FACE PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b4_1.place(x=218,y=722, width=220,height=40)



        #5th button in 2nd row 
        self.phone_image10=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image10=Label(self.root,image=self.phone_image10,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 4
        b5=Button(image=self.lbl_Phone_image7,cursor="hand2")
        b5.place(x=656,y=500, width=220,height=220)
        #button text
        b5_1=Button(text="EYE PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b5_1.place(x=656,y=722, width=220,height=40)



         #6th button in 2nd row 
        self.phone_image10=ImageTk.PhotoImage(file="file/new 6.png")
        self.lbl_Phone_image10=Label(self.root,image=self.phone_image10,bd=0).place(x=1323,y=0,width=207,height=130)
        #button 6
        b6=Button(image=self.lbl_Phone_image7,cursor="hand2")
        b6.place(x=1094,y=500, width=220,height=220)
        #button text
        b6_1=Button(text="ATTENDENCE",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b6_1.place(x=1094,y=722, width=220,height=40)


        #EXIT BUTTON 
        b7=Button(text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b7.place(x=1300,y=800, width=100,height=30)





    def smart(self):
         self.new_window=Toplevel(self.root)
         self.app=student_System(self.new_window)
              










       

        



























if __name__ == "__main__":
        root=Tk()
        obj1=Dashboard_System(root)
        root.mainloop()
