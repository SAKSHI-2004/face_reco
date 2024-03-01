from tkinter import*
from  tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector




class student_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x850+0+0")
        self.root.title("face Recognition System")
        self.root.config(bg="#0e2433")


        # comments
        self.var_department= StringVar()
        self.var_course= StringVar()
        self.var_semester= StringVar()
        self.var_studentid= StringVar()
        self.var_rollno= StringVar()
        self.var_year= StringVar()
        self.var_name= StringVar()
        self.var_dob= StringVar()
        self.var_phoneno= StringVar()
        self.var_gender= StringVar()
        self.var_emailid= StringVar()
        self.var_address= StringVar()
             
        

        #upper images
        self.phone_image1=ImageTk.PhotoImage(file="file/student img 1.png")
        self.lbl_Phone_image1=Label(self.root,image=self.phone_image1,bd=0).place(x=0,y=0,width=203,height=135)
        self.phone_image2=ImageTk.PhotoImage(file="file/student img 2.png")
        
        self.lbl_Phone_image2=Label(self.root,image=self.phone_image2,bd=0).place(x=203,y=0,width=203,height=135)
        self.phone_image3=ImageTk.PhotoImage(file="file/student img 3.png")
        self.lbl_Phone_image3=Label(self.root,image=self.phone_image3,bd=0).place(x=406,y=0,width=193,height=135)
        self.phone_image4=ImageTk.PhotoImage(file="file/student img 4.png")
        self.lbl_Phone_image4=Label(self.root,image=self.phone_image4,bd=0).place(x=599,y=0,width=216,height=135)
        self.phone_image5=ImageTk.PhotoImage(file="file/student img 5.png")
        self.lbl_Phone_image5=Label(self.root,image=self.phone_image5,bd=0).place(x=815,y=0,width=240,height=135)
        self.phone_image8=ImageTk.PhotoImage(file="file/student img 8.png")
        self.lbl_Phone_image8=Label(self.root,image=self.phone_image8,bd=0).place(x=1055,y=0,width=186,height=135)
        self.phone_image6=ImageTk.PhotoImage(file="file/student img 7.png")
        self.lbl_Phone_image6=Label(self.root,image=self.phone_image6,bd=0).place(x=1241,y=0,width=172,height=135)
        self.phone_image7=ImageTk.PhotoImage(file="file/student img 6.png")
        self.lbl_Phone_image7=Label(self.root,image=self.phone_image7,bd=0).place(x=1413,y=0,width=117,height=135)


         #background image 
        self.bg_image=ImageTk.PhotoImage(file="file/bg image 2.png")
        self.lbl_bg_image=Label(self.root,image=self.bg_image,bd=0).place(x=0,y=135,width=1530,height=720)


        


        #title lable
        title_lbl=Label(text="STUDENT   MANAGEMENT    SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=135,width=1530,height=45)


        #frame
        main_frame=Frame( self.root,bd=2,bg="white")
        main_frame.place(x=10,y=188,width=1505,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=620)

        #img 
        self.student_info=ImageTk.PhotoImage(file="file/stu info.png")
        self.lbl_student_info=Label(Left_frame,image=self.student_info,bd=0).place(x=10,y=0,width=740,height=130)


        # current course label
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=730,height=130)

        #dept 
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable = self.var_department,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer science","Information Technology","ECE","Civil","Mechanical","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #courses
        course_label=Label(current_course_frame,text="Courses :",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=3,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable =self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Courses","Computer science","Information Technology","ECE","Civil","Mechanical","Chemical")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=5,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame,text="Year :",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable =self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        #semester
        sem_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=3,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable =self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=4,padx=5,pady=10,sticky=W)

        #.. class student information  label frame..
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=270,width=730,height=310)

        #studentid
        enrollment_label=Label(class_student_frame,text="StudentID No :",font=("times new roman",12,"bold"),bg="white")
        enrollment_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        enrollment_entry=ttk.Entry(class_student_frame,textvariable =self.var_studentid,width=20,font=("times new roman",12,"bold"))
        enrollment_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        sname_label=Label(class_student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        sname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        sname_entry=ttk.Entry(class_student_frame,textvariable =self.var_name,width=20,font=("times new roman",12,"bold"))
        sname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #roll no
        roll_label=Label(class_student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(class_student_frame,textvariable =self.var_rollno,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #dob
        
        dob_label=Label(class_student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable =self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # phoneno 
        phone_label=Label(class_student_frame,text="Phone No. :",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable =self.var_phoneno,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #gender 
        gender_label=Label(class_student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable =self.var_gender,font=("times new roman",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        

        #email 
        email_label=Label(class_student_frame,text="Email ID  :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable =self.var_emailid,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # address
        address_label=Label(class_student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable =self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5)

         # radio buttons
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio2,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5)

      #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=180,width=700,height=40)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0,padx=5,pady=1)

        update_btn=Button(btn_frame,text="UPDATE",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1,padx=5,pady=1)

        delete_btn=Button(btn_frame,text="DELETE",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2,padx=5,pady=1)

        reset_btn=Button(btn_frame,text="RESET",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3,padx=5,pady=1)


         #button2 frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=225,width=700,height=40)


        addphoto_btn=Button(btn_frame1,text="ADD PHOTO SAMPLE",font=("times new roman",12,"bold"),bg="blue",fg="white",width=35)
        addphoto_btn.grid(row=0,column=0,padx=5,pady=1)

        updatephoto_btn=Button(btn_frame1,text="UPDATE PHOTO SAMPLE",font=("times new roman",12,"bold"),bg="blue",fg="white",width=35)
        updatephoto_btn.grid(row=0,column=1,padx=5,pady=1)





        #....right lable frame...
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=730,height=620)

         #img 
        self.student_details=ImageTk.PhotoImage(file="file/stu details.png")
        self.lbl_student_details=Label(Right_frame,image=self.student_details,bd=0).place(x=10,y=0,width=740,height=130)

        #........search system......
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="VIEW STUDENT DETAILS  &  SEARCH SYSTEM ",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

         # search bar 
        search_label=Label(search_frame,text="Search By :",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select","Roll_No.","Phone_No.","name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=1,sticky=W)


        search_btn=Button(search_frame,text="SEARCH",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        search_btn.grid(row=0,column=3,padx=5,pady=1)

        showall_btn=Button(search_frame,text="SHOW ALL",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        showall_btn.grid(row=0,column=4,padx=5,pady=1)


        #........table frame system......
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=720,height=350)

       #.....scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dept","course","year","sem","roll no","name","gender","id","DOB","email","phone no","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll no",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
    

    #function-------------
    def add_data(self) :
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_studentid.get()=="":
             messagebox.showerror(" Error", "All Fields are mandatory",parent=self.root)
        else:
            messagebox.showinfo("Success","Welcome!")
             
        

         

        
        









        


















if __name__ == "__main__":
        root=Tk()
        obj1=student_System(root)
        root.mainloop()








        
















