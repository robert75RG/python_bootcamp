import tkinter
from zjazd4.praca_z_siecia.pogoda import get_location_id, get_location_weather, present_results

def szukaj():
    lokalizacja = city_E.get()
    lokalizacja_id = get_location_id(lokalizacja)
    pogoda = get_location_weather(lokalizacja_id)
    output = present_results(pogoda)
    pogoda_L.configure(text=output)

root = tkinter.Tk()
root.title("Pogoda")

city_L = tkinter.Label(master=root, text="Miasto")
city_L.grid(row=0, column =0)
city_E = tkinter.Entry(master=root)
city_E.grid(row=0, column=1)


szukaj_button = tkinter.Button(master=root, text="Szukaj", command=szukaj)
szukaj_button.grid(row=2, column=0)

pogoda_L = tkinter.Label(master=root, text = ' ')
pogoda_L.grid(row=3, column=0)








root.mainloop()