import tkinter

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.geometry("220x160")

def bmi_calculator():

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight * (height ** 2)
        print(bmi)
    except:
        print("Please Enter Your Weight and Height ")

weight_label = tkinter.Label()
weight_label.config(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = tkinter.Entry(bg="white",width=18)
weight_entry.pack()

height_label = tkinter.Label()
height_label.config(text="Enter Your Weight (cm)")
height_label.pack()

height_entry= tkinter.Entry(bg="white",width=18)
height_entry.config()
height_entry.pack()

bmi_calculator()




screen.mainloop()
