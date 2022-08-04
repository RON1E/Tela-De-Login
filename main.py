from tkinter import*
from tkinter import Tk, ttk


# cores ----------------------------------------------------------
cor0 = "#f0f3f5"  # preta
cor1 = "#feffff"  # branco
cor2 = "#3fb5a3"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra

# Criando a janela ------------------------------------------------
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Div Janela --------------------------------------------------------

frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor2, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#

janela.mainloop()
