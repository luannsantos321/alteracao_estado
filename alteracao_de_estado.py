import pyautogui
import pandas as pd
import time
import webbrowser
#from plyer import notification
from tkinter import *
from pynotifier import Notification
	
def adicionando_cliques():
		add = 0
		global posicoes
		posicoes = []
		while add < 2:
			time.sleep(5)
			parametro = pyautogui.position()
			add += 1
			#notification.notify(title= 'NotificaÃ§Ã£o', message =f'Adicionado {add}', timeout= 0.5 )
			Notification(
	title='PosiÃ§Ã£o do clique',
	description=f'Adicionou posiÃ§Ã£o {add}',
	duration=2,                                   # Duration in seconds
	urgency='normal'
	).send()
			posicoes.append(parametro)
			print(posicoes)
		pos = pd.DataFrame(posicoes,columns=['x','y'])
		pos.to_excel('PosiÃ§Ãµes.xlsx', index=False)



def alternado_estado():
	sheets = pd.read_csv('https://docs.google.com/spreadsheets/d/1b1gnPbBe-elIOwO3JmGQd-3NVFCKbwyk/export?format=csv')
	print(sheets)
	pos = pd.read_excel('PosiÃ§Ãµes.xlsx')
	print(pos)
	for contagem,alterando in enumerate(sheets.values):
		print(alterando[0])
		contagem = contagem + 1
		
		
		link = f'https://estoque.brisanet.net.br/#/estoque/itens/item/estado/alterar/{alterando[0]}'
		webbrowser.open(link)
		time.sleep(6)
		pyautogui.click(x=pos.iloc[0,0],y=pos.iloc[0,1])
		time.sleep(2)
		pyautogui.click(x=pos.iloc[1,0],y=pos.iloc[1,1])
		time.sleep(2)
		pyautogui.hotkey('ctrl','w')
		time.sleep(2)
		print(contagem)
	print('Finalizada a alteraÃ§Ã£o')

window = Tk()
window.title('AAA')

botao_posicao = Button(window,text='Pegando posiÃ§Ãµes', command=adicionando_cliques)
botao_posicao.pack(expand=True)
botao_alterado_estado= Button(window,text='GO!', command=alternado_estado)
botao_alterado_estado.pack(expand=True)


window.geometry('170x170')
window.mainloop()
