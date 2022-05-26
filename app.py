from tkinter import *
from tkinter import messagebox
import requests
import json
type = 'sports'
apiKey = '3407ffcb23974d4fb528724ddcaa2d8d'
BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey


class NewsApp:
	global apiKey, type

	def __init__(self, root):
		self.root = root
		self.root.geometry('1350x700+0+0')
		self.root.title("News app")

		#====variables========#
		self.newsCatButton = []
		self.newsCat = ["sports", "Entertainment",
						"business", "general", "health","technology"]

		#========title frame===========#
		bg_color = "#F4BFBF"
		text_area_bg = "#CDF0EA"
		basic_font_color = "#3E2C41"
		title = Label(self.root, text="Latest News Updates", font=("roboto", 30, "bold"),
					pady=2, bd=12, relief=GROOVE, bg=bg_color, fg=basic_font_color).pack(fill=X)

		F1 = LabelFrame(self.root, text="select category", font=(
			"consolas", 20, "bold"), bg=bg_color, fg=basic_font_color, bd=10, relief=GROOVE)
		F1.place(x=0, y=80, width=300, relheight=0.88)

		for i in range(len(self.newsCat)):
			b = Button(F1, text=self.newsCat[i].upper(
			), width=20, bd=7, font="roboto 15 bold")
			b.grid(row=i, column=0, padx=10, pady=5)
			b.bind('<Button-1>', self.Newsarea)
			self.newsCatButton.append(b)

		#=======news frame=======#
		F2 = Frame(self.root, bd=7, relief=GROOVE)
		F2.place(x=320, y=80, relwidth=0.7, relheight=0.8)
		news_title = Label(F2, text=f"This news is brought to u by newsapi.org", font=(
			"roboto", 20, "bold"), bd=7, relief=GROOVE).pack(fill=X)
		scroll_y = Scrollbar(F2, orient=VERTICAL)
		self.txtarea = Text(F2, yscrollcommand=scroll_y.set, font=(
			"roboto", 15, "bold"), bg=text_area_bg, fg="#000000")
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_y.config(command=self.txtarea.yview)
		self.txtarea.insert(
			END, "PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES AND PLEASE BE PATIENT IT DEPENDS ON UR INTERNET CONNECTIONS!!!!")
		self.txtarea.pack(fill=BOTH, expand=1)

	def Newsarea(self, event):
		type = event.widget.cget('text').lower()
		BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey
		self.txtarea.delete("1.0", END)
		self.txtarea.insert(END, f"\n {type}\n")
		self.txtarea.insert(
			END, "--------------------------------------------------------------------\n")
		try:
			articles = (requests.get(BASE_URL).json())['articles']
			if(articles != 0):
				for i in range(len(articles)):
					self.txtarea.insert(END, f"{articles[i]['title']}\n")
					self.txtarea.insert(
						END, f"{articles[i]['description']}\n\n")
					self.txtarea.insert(END, f"{articles[i]['content']}\n\n")
					self.txtarea.insert(
						END, f"read more...{articles[i]['url']}\n")
					self.txtarea.insert(
						END, "--------------------------------------------------------------------\n")
					self.txtarea.insert(
						END, "--------------------------------------------------------------------\n")
			else:
				self.txtarea.insert(END, "Sorry no news available")
		except Exception as e:
			messagebox.showerror(
				'ERROR', "Sorry cant connect to internet or some issues with newsapp :'(")


root = Tk()
obj = NewsApp(root)
root.mainloop()
