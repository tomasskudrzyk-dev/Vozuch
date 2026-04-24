import tkinter as tk

#nastavení barev
SIRKA, VYSKA = 600, 600
CERNA = "#000000"
BILA = "#FFFFFF"
SEDA = "#808080"
ZELENA = "#00FF00"
CERVENA = "#FF0000"
TMAVE_SEDA = "#404040"

barva_pozadi = CERNA
barva_tlacitek = SEDA
barva_textu = BILA
barva_hover = TMAVE_SEDA

#okno
okno = tk.Tk()
okno.title("Kalkulačka")
okno.geometry(f"{SIRKA}x{VYSKA}")
pismo = ("Arial", 24)

#funkce pro kliknutí na tlačítko
def klik(text):
    if text == "=":
        try:
            vysledek = eval(vstup.get())
            vstup.delete(0, tk.END)
            vstup.insert(tk.END, str(vysledek))
        except Exception as e:
            vstup.delete(0, tk.END)
            vstup.insert(tk.END, "Chyba")
    elif text == "C":
        vstup.delete(0, tk.END)
    elif text == "DEL":
        obsah = vstup.get()
        if len(obsah) > 0:
            vstup.delete(len(obsah)-1, tk.END)
    else:
        vstup.insert(tk.END, text)

#funkce pro podsvícení tlačítka
def hover(e, t):
    e.widget.config(bg=barva_hover)

def unhover(e, t):
    e.widget.config(bg=barva_tlacitek)


#vstup
vstup = tk.Entry(okno, font=pismo, justify="right", width=15)
vstup.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#tlačítka
tlacitka = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("DEL", 5, 1),
]

for (text, row, col) in tlacitka:
    tlacitko = tk.Button(okno, text=text, font=pismo, bg=barva_tlacitek, fg=barva_textu, width=5, height=2)
    tlacitko.grid(row=row, column=col, padx=5, pady=5)
    tlacitko.bind("<Button-1>", lambda e, t=text: klik(t))
    tlacitko.bind("<Enter>", lambda e, t=text: hover(e, t))
    tlacitko.bind("<Leave>", lambda e, t=text: unhover(e, t))

okno.bind("<BackSpace>", lambda e: vstup.delete(len(vstup.get())-1, tk.END))
okno.mainloop()