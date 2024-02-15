# Notepad

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import ctypes

try:
	ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
	pass

root = Tk()
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\part2\lesson15(Завершение программы блокнот)\686112.ico')
root.title('notepad')

root.geometry('400x400+1000+300')

main_menu = Menu(root) # создаём экземпляр класса меню
root.config(menu=main_menu)

# Опишем функцию которая будет выводить информацию о программе
def about_program():
	messagebox.showinfo('About notepad', 'Программа Notepad Version 0.0.1')

# Создадим функцию для переключения тем
def change_theme(theme):
	t['bg'] = theme_colors[theme]['text_bg']
	t['fg'] = theme_colors[theme]['text_fg']

# Создадим функцию для выхода из программы
def notepad_quit():
	answer = messagebox.askyesno('Выход из программы', 'Вы уверенны, что хотите закрыть программу?')
	if answer:
		root.destroy()

# Реализуем функцию открытия файла
def open_file():
	file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы', '*.txt'), ('Все файлы', '*.*')))
	if file_path:
		t.delete('1.0', END)
		t.insert('1.0', open(file_path, encoding='utf-8').read())

# Теперь сделаем функцию для сохранения файла
def save_file():
	file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы', '*.txt'), ('Все файлы', '*.*')))
	f = open(file_path, 'w', encoding='utf-8')
	text = t.get('1.0', END)
	f.write(text)
	f.close()
	if f:
		messagebox.showinfo('Сохранить', 'Файл успешно сохранён!')

# Если нам нужно однострочное меню то это можно сделать следующим образом
# main_menu.add_command(label='File') 

# А что если нужно выпадающее меню?
file_menu = Menu(main_menu, tearoff=0) # Привязываем пункт к нашему меню
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator() 
file_menu.add_command(label='Выход', command=notepad_quit)
main_menu.add_cascade(label="Файл", menu=file_menu) # Добавляем имя выпадающей менюшки и привязываем её к file_menu

# Создадим меню для переключения тем в блакноте
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light theme', command=lambda: change_theme('light'))
theme_menu_sub.add_command(label='Dark theme', command=lambda: change_theme('dark'))
theme_menu.add_cascade(label='Оформление', menu=theme_menu_sub)
theme_menu.add_command(label='О программе', command=about_program)
main_menu.add_cascade(label='Разное', menu=theme_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# Создадим слоаврь где сохраним настройки для тёмной и светлой тем

theme_colors = {
	'dark': {
		'text_bg':'#343D46', 'text_fg': "#fff"
	},
	'light': {
		'text_bg':'#fff', 'text_fg': "#000"
	}
}

# Создадим виджет Text
t = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10, wrap=WORD, 
spacing3=10, width=30) # С помощью параметра wrap сделаем так чтобы при переносе строки переносилось целое слово
# С помощью spacing3 мы можем установить отступы строк друг от ддруга
t.pack(fill=BOTH, expand=1, side=LEFT)

# Теперь создадим scrollbar

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()






































