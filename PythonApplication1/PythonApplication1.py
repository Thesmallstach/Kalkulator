import tkinter as tk
symbole = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0', ',', '%', '+']


def start0okienka() :
    root = tk.Tk()
    root.configure(background = 'white')
    root.geometry('463x400')
    root.title('Kalkulatorek :D')
    return root

def ekran0do0wyświetlania(root): 
    
    ekran = [tk.Label(root, background='#C0CBCB', width = 65, anchor = 'w', borderwidth = 2) for i in range(3)] 

    for i in range(len(ekran)) :
        ekran[i].grid(row = i, columnspan = 6, ipady = 15, ipadx = 1)

    return ekran

def okienko0do0pisania(root, ekran):
    pole_na_dane = tk.Entry(root, borderwidth = 0, background= 'light grey', highlightcolor = 'light grey', highlightbackground = 'light grey')
    pole_na_dane.grid(row = len(ekran), columnspan = 6, ipadx = 170, ipady = 10)

    informacje = tk.Label(root, background = 'light grey', width = 65, anchor = 'w', borderwidth = 2)
    informacje.grid(row = len(ekran) + 1, columnspan = 6, ipady = 15, ipadx = 1)

    return pole_na_dane

def przyciskixD(root, ekran):
    przyciski = [tk.Button(root, text = symbol, background = 'white', border = 0) for symbol in symbole]
    
    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1

        margin = 28 if len(symbole[i]) == 1 else 10
        przyciski[i].grid(row = j, column = i % 6, ipady = 5, ipadx = margin)

    return przyciski
if __name__ == '__main__' : 
    root = start0okienka() 
    
    ekran = ekran0do0wyświetlania(root)

    pole_na_dane = okienko0do0pisania(root, ekran)

    przyciski = przyciskixD(root, ekran)
    
    root.mainloop()
