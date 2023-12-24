import tkinter

window = tkinter.Tk()
window.title("Mile to Km Unit Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

entry = tkinter.Entry()
entry.grid(column=1, row=0)

label = tkinter.Label(text="Miles")
label.grid(column=2, row=0)

label_2 = tkinter.Label(text="is equal to:")
label_2.grid(column=0, row=1)

converted_num = ""

answer = 0


def convert_to_km():
    answer = float(entry.get()) * 1.609
    answer_label.config(text=f"{answer}")


answer_label = tkinter.Label(text="**")
answer_label.grid(column=1, row=1)

label_3 = tkinter.Label(text="is equal to")
label_3.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
