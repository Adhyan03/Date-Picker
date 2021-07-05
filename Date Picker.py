from tkinter import *
from tkcalendar import *      # For Calendar

root = Tk()
root.title("Adhyan's Date Picker")
root.geometry("600x400")

#Calendar
cal = Calendar(root, selectmode="day" , year=2021 , month=4 , day=25)
cal.pack(pady = 20, fill = "both" , expand = True)

def grab_date():
    my_label.config(text = cal.get_date())


#Buttons
my_button = Button(root, text = 'Check Date' , height = 2, bg = '#3489eb' , fg = 'white', command = grab_date)
my_button.pack(pady = 15)

#Lable
my_label = Label(root , text = '')
my_label.pack(pady = 20)


root.mainloop()