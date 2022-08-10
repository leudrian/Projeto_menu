from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE

# importando pillow
from PIL import Image, ImageTk


# chamando a biblioteca random
import random

# cores
co0 = "#444466"  # preto
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelha

# criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_fundo = Frame(janela, width=550, height=310, relief='flat')
frame_fundo.grid(row=1, column=0)

#Abrindo imagem
imagem_fundo = Image.open("Projeto_menu/imagens/dmc_wallpaper.jpg")
imagem_fundo = imagem_fundo.resize((550, 310))
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

#inserindo imagem no Frame
tela_fundo = Label(frame_fundo, image= imagem_fundo)
tela_fundo.place(x=0, y=0)

#criando botões
b_novo_jogo = Button(janela,text='Novo Jogo', width=25,
                 relief='raised', overrelief=RIDGE, compound=CENTER, anchor=CENTER, padx=5, font=('Verdana 20'), bg=co0, fg=co1)
b_novo_jogo.place(x=50, y=320)

b_Continue = Button(janela,text='Continue', width=25,
                 relief='raised', overrelief=RIDGE, compound=CENTER, anchor=CENTER, padx=5, font=('Verdana 20'), bg=co0, fg=co1)
b_Continue.place(x=50, y=380)

b_sair = Button(janela,text='Sair', width=25,
                 relief='raised', overrelief=RIDGE, compound=CENTER, anchor=CENTER, padx=5, font=('Verdana 20'), bg=co0, fg=co1)
b_sair.place(x=50, y=440)

janela['bg'] = "#000000"

janela.mainloop()