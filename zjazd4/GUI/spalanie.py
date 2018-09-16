import tkinter
from tkinter import messagebox

def oblicz():
    try:
        a = float(a_entry.get()) # cena paliwa
        b = float(b_entry.get()) #Spalanie
        c = float(c_entry.get())/100 #dystans
        koszt = a * b* c

        wynik_label.configure(text=f"Wynik: {koszt}")
    except ValueError:
        tkinter.messagebox.showerror("Błędne dane", "Musisz poprawić dane!!!")

root = tkinter.Tk()
root.title("Koszt przejazdu")

# cena paliwa
a_Label = tkinter.Label(master=root, text="Cena paliwa")
a_Label.grid(row=0, column =0)

a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

# spalanie
b_Label = tkinter.Label(master=root, text="Spalanie")
b_Label.grid(row=1, column =0)

b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

# dystans

c_Label = tkinter.Label(master=root, text="Dystans")
c_Label.grid(row=3, column =0)

c_entry = tkinter.Entry(master=root)
c_entry.grid(row=3, column=1)



#oblicz
dodaj_button = tkinter.Button(master=root, text="Oblicz", command=oblicz )
dodaj_button.grid(row=4, column=0)

wynik_label = tkinter.Label(master=root, text = "Koszt:")
wynik_label.grid(row=4, column=1)



root.mainloop()