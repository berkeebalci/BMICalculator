import tkinter

def bmi_calculator():
    height = height_entry.get()
    weight = weight_entry.get()

    if height == "" or weight == "":
        result_label.config(text="Enter both weight and height! ")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text ="Enter a valid number")




screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.geometry("250x200")

height_label = tkinter.Label(text="Enter Your Height (cm)",)
height_label.pack()
height_entry = tkinter.Entry(fg="black",bg="white")
height_entry.pack()

weight_label = tkinter.Label(text="Enter Your Weight (kg)",)
weight_label.pack()
weight_entry = tkinter.Entry(fg="black",bg="white")
weight_entry.pack()

my_button = tkinter.Button(text="Calculate",command=bmi_calculator)
my_button.pack()

result_label = tkinter.Label(text="BMI : ")
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {bmi:.2f}. You are "
    if bmi <= 16:
        result_string += "Severely Thin!"
    elif 16 < bmi <= 17:
        result_string += "Moderately Thin!"
    elif 17 < bmi <= 18.5:
        result_string += "Mild Thin!"
    elif 18.5 < bmi <= 25:
        result_string += "Normal"
    elif 25 < bmi <= 30:
        result_string += "Overweight!"
    elif 30 < bmi <= 35:
        result_string += "Obese Class I "
    elif 35 < bmi <= 40:
        result_string += "Obese Class II "
    elif bmi > 40:
        result_string += "Obese Class III "
    return result_string









screen.mainloop()