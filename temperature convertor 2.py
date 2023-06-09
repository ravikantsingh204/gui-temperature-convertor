import tkinter
import customtkinter
from PIL import Image,ImageTk
import tkinter.messagebox


def switch_mode():
    s=switch_var.get()
    if s=="Dark":
        customtkinter.set_appearance_mode("dark")
    elif s=="Light":
        customtkinter.set_appearance_mode("light")


def clear():
    heading_label6.destroy()
    heading_label4.destroy()
    heading_label5.destroy()
    clear_button.destroy()
    convert_button.configure(state="normal")


def convert():
    convert_button.configure(state="normal")
    unit=temperature_unit_variable.get()
    value=temperature_entry.get()
    if value=="":
        tkinter.messagebox.showerror("Error","Please enter temperature")
    elif unit=="Select Unit":
        tkinter.messagebox.showerror("Error","Please select unit")
    else:
        convert_button.configure(state="disabled")
        
        global heading_label6
        heading_label6=customtkinter.CTkLabel(master=frame,text=" Converted temperature value:- ",font=("Century Gothic",30))
        heading_label6.place(x=50,y=500)
        
        global heading_label4
        global heading_label5
        
        if unit=="Celsius":
            c=float(value)
            f=round(((c*1.8)+32),3)
            k=round((c+273.15),3)
            heading_label4=customtkinter.CTkLabel(master=frame,text=" Kelvin :- "+str(k)+" Kelvin ",font=("Century Gothic",30))
            heading_label4.place(x=100,y=600)
            heading_label5=customtkinter.CTkLabel(master=frame,text=" Fahrenheit :- "+str(f)+" Fahrenheit ",font=("Century Gothic",30))
            heading_label5.place(x=100,y=650)
        elif unit=="Fahrenheit":
            f=float(value)
            c=round(((f-32)*(5/9)),3)
            k=round((c+273.15),3)
            heading_label4=customtkinter.CTkLabel(master=frame,text=" Celsius :- "+str(c)+" Celsius ",font=("Century Gothic",30))
            heading_label4.place(x=100,y=600)
            heading_label5=customtkinter.CTkLabel(master=frame,text=" Kelvin :- "+str(k)+" Kelvin ",font=("Century Gothic",30))
            heading_label5.place(x=100,y=650)
        elif unit=="Kelvin":
            k=float(value)
            c=round((k-273.15),3)
            f=round(((c*1.8)+32),3)
            heading_label4=customtkinter.CTkLabel(master=frame,text=" Celsius :- "+str(c)+" Celsius ",font=("Century Gothic",30))
            heading_label4.place(x=100,y=600)
            heading_label5=customtkinter.CTkLabel(master=frame,text=" Fahrenheit :- "+str(f)+" Fahrenheit ",font=("Century Gothic",30))
            heading_label5.place(x=100,y=650)
        
        global clear_button
        clear_button=customtkinter.CTkButton(master=frame,width=500,text="clear",corner_radius=6,font=("Century Gothic",30),height=50,hover_color="green",command=clear)
        clear_button.place(x=100,y=725)


window=customtkinter.CTk()
window.geometry("1920x1080")
window.title("Temperature Convertor")


image1=ImageTk.PhotoImage(Image.open("D:\\programming\\Bharat intern\\t2.jpg"))
background_frame1=customtkinter.CTkLabel(master=window,image=image1)
background_frame1.pack()


frame=customtkinter.CTkFrame(master=window,width=700,height=850,corner_radius=100)
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)


heading_label1=customtkinter.CTkLabel(master=frame,text=" Temperature Convertor ",font=("Century Gothic",50))
heading_label1.place(x=50,y=45)


heading_label2=customtkinter.CTkLabel(master=frame,text="------------------------------------",font=("Century Gothic",50))
heading_label2.place(x=50,y=100)


heading_label3=customtkinter.CTkLabel(master=frame,text=" Enter the temperature:- ",font=("Century Gothic",36))
heading_label3.place(x=50,y=200)


temperature_variable=customtkinter.DoubleVar()
temperature_entry=customtkinter.CTkEntry(master=frame,width=200,height=50,placeholder_text="0.0",font=("Century Gothic",20))
temperature_entry.place(x=100,y=275)


temperature_unit_variable=customtkinter.StringVar()
temperature_unit=customtkinter.CTkOptionMenu(master=frame,width=275,height=50,values=["Celsius","Fahrenheit","Kelvin"],font=("Century Gothic",20),dropdown_font=("Century Gothic",20),fg_color="grey",variable=temperature_unit_variable)
temperature_unit.place(x=325,y=275)
temperature_unit.set("Select Unit")


convert_button=customtkinter.CTkButton(master=frame,width=500,text="Convert",corner_radius=6,font=("Century Gothic",30),height=50,hover_color="green",command=convert)
convert_button.place(x=100,y=350)


switch_var = customtkinter.StringVar()
switch = customtkinter.CTkSwitch(master=frame,text="Dark Mode",variable=switch_var,onvalue="Dark",offvalue="Light",font=("Century Gothic",20),command=switch_mode)
switch.place(x=500,y=800)
switch.select()


window.mainloop()