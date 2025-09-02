#IMPORTAÇÃO DA BIBLIOTECA TKINTER
from tkinter import *
from types import LambdaType

#from tkinter.ttk import *

#IMPORTANDO TKCALENDAR
from tkcalendar import DateEntry
from datetime import date

#IMPORTANDO DATEUTIL
from dateutil.relativedelta import relativedelta


janela = Tk()
janela.title('Calculadora de Idade')
janela.geometry('310x400')

#CORES UTILIZADAS

cor1 = "#153441"
cor2 = "#345C6B"
cor3 = "#BDDDEA"
cor4 = "#628796"
cor5 = "#9EB6C0"

#-------CRIANDO FRAMES-------

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, background=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, background=cor1)
frame_baixo.grid(row=1, column=0)

#-------LABELS NO FRAME DE CIMA-------

l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Ivi 15 bold'), background=cor2, foreground="#ffffff")
l_calculadora.place(x=0, y=30)

l_calculadora = Label(frame_cima, text="DE IDADE", width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Arial 15 bold'), background=cor2, foreground="#082733")
l_calculadora.place(x=0, y=70)

#-------LABELS NO FRAME DE BAIXO-------

l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11'), background=cor1, foreground="#ffffff")
l_data_inicial.place(x=30, y=30)

cal_1 = DateEntry(frame_baixo, width=13, background=cor2, foreground="#ffffff", borderwidth=2, date_pattern='dd/mm/yyyy', year=2025)
cal_1.place(x=185, y=30)

#-------FUNÇÃO CALCULAR IDADE-------

def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    # CONVERTENDO OS VALORES EM FORMATO DATE/DATETIME
    dia_1, mes_1, ano_1 = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1, mes_1, dia_1)

    dia_2, mes_2, ano_2 = [int(f) for f in termino.split('/')]
    data_nascimento = date(ano_2, mes_2, dia_2)

    # CALCULANDO IDADE
    diferenca = relativedelta(data_inicial, data_nascimento)
    anos = diferenca.years
    meses = diferenca.months
    dias = diferenca.days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias

l_calendario = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, relief=FLAT, anchor=NW, font=('Ivi 11'), background=cor1, foreground="#ffffff")
l_calendario.place(x=30, y=60)

cal_2 = DateEntry(frame_baixo, width=13, background=cor2, foreground="#ffffff", borderwidth=2, date_pattern='dd/mm/yyyy', year=2025)
cal_2.place(x=185, y=60)

#-------LABELS DOS ANOS, MESES E DIAS-------

l_app_anos = Label(frame_baixo, text="-", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 25 bold'), background=cor1, foreground="#ffffff")
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 11 bold'), background=cor1, foreground="#ffffff")
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text="-", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 25 bold'), background=cor1, foreground="#ffffff")
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 11 bold'), background=cor1, foreground="#ffffff")
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text="-", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 25 bold'), background=cor1, foreground="#ffffff")
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, relief=FLAT, anchor="center", font=('Ivi 11 bold'), background=cor1, foreground="#ffffff")
l_app_dias_nome.place(x=220, y=175)

#-------CRIANDO BOTÃO CALCULAR-------

b_calcular = Button(frame_baixo, command= lambda: calcular(), text="Calcular", width=20, height=1, padx=0, relief=RAISED, overrelief=RIDGE, font=('Ivi 10 bold'), background=cor1, foreground="#ffffff")
b_calcular.place(x=65, y=218)

calcular()
janela.mainloop()