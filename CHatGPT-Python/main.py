from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class ChatGPTApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        
        # Crear título
        title = Label(text="[color=00ff00][b]ChatGPT API en Python[/b][/color]", markup=True)
        layout.add_widget(title)
        
        # Crear tabla
        comando_label = Label(text="[b]Comando[/b]", markup=True)
        descripcion_label = Label(text="[b]Descripcion[/b]", markup=True)
        layout.add_widget(comando_label)
        layout.add_widget(descripcion_label)
        
        layout.add_widget(Label(text="exit"))
        layout.add_widget(Label(text="Salir de la aplicacion"))
        
        layout.add_widget(Label(text="new"))
        layout.add_widget(Label(text="Crear una nueva conversacion"))
        
        return layout

if __name__ == '__main__':
    ChatGPTApp().run()
