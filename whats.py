from kivy.app import App
from kivy.core.window import Window
import webbrowser

Window.clearcolor = (108/255, 52/255, 176/255, 1 )
#Window.size = (300,300)

class whats(App):
	def set_text(self):
		#setas
			numero = self.root.ids.numero.text
			label = self.root.ids.label
			check = self.root.ids.check
			if check.active == True:
				label.text = ('http://wa.me/{}{}'.format(5595, numero))
				webbrowser.open('http://wa.me/{}{}'.format(5595, numero))
			else:
				label.text = ('http://wa.me/{}'.format(numero))
				webbrowser.open('http://wa.me/{}'.format(numero))
			pass
	
whats().run()