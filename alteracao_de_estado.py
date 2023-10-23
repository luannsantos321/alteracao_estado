import pyautogui
import pandas as pd
import time
from plyer import notification
from tkinter import *

	
def adicionando_cliques():
	'''Adiciona numa planilha todas as posições de da tela para atender diferentes dimensões de tela e
 atender o requisitos da empresa em que trabalho.'''
		add = 0
		global posicoes
		posicoes = []
		while add < 7:
			time.sleep(10)
			parametro = pyautogui.position()
			add +=1
			notification.notify(title= 'Notificação', message =f'Adicionado {add}', timeout= 0.5 )
			posicoes.append(parametro)
			
			
			print(posicoes)

		pos = pd.DataFrame(posicoes,columns=['x','y'])
		pos.to_excel('Posições.xlsx', index=False)



def alternado_estado():
	'''Pega os dados das posições, os numeros de série e retorna a ação da automação'''
	numero_serie = pd.read_excel('Numeros de série.xlsx')
	print(numero_serie)
	pos = pd.read_excel('Posições.xlsx')
	print(pos)
	for alterando in numero_serie.values:
		print(alterando[0])
		pyautogui.click(x=pos.iloc[0,0],y=pos.iloc[0,1], clicks=2)
		time.sleep(2)
		pyautogui.write(alterando[0])
		pyautogui.click(x=pos.iloc[1,0],y=pos.iloc[1,1])
		time.sleep(4)
		pyautogui.click(x=pos.iloc[2,0],y=pos.iloc[2,1])
		time.sleep(4)
		pyautogui.click(x=pos.iloc[3,0],y=pos.iloc[3,1])
		time.sleep(4)
		pyautogui.click(x=pos.iloc[4,0],y=pos.iloc[4,1])
		time.sleep(4)
		pyautogui.click(x=pos.iloc[5,0],y=pos.iloc[5,1])
		time.sleep(4)
		pyautogui.click(x=pos.iloc[6,0],y=pos.iloc[6,1])
		time.sleep(4)
window = Tk()
window.title('AAA')

botao_posicao = Button(window,text='Pegando posições', command=adicionando_cliques)
botao_posicao.pack(expand=True)
botao_alterado_estado= Button(window,text='GO!', command=alternado_estado)
botao_alterado_estado.pack(expand=True)


window.geometry('170x170')
window.mainloop()
