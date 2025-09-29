from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder

# Este es un placeholder simplificado del juego completo.
# Aquí iría todo el flujo de preguntas, vidas, puntajes y minijuegos adaptados a Kivy.

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    usuario = StringProperty("")
    vidas = NumericProperty(5)
    puntaje = NumericProperty(0)
    mensaje = StringProperty("Bienvenido al cuestionario de inglés")

    def start_game(self, nombre):
        self.usuario = nombre
        self.vidas = 5
        self.puntaje = 0
        self.mensaje = f"Hola {self.usuario}, ¡empezamos!"

class GameOverScreen(Screen):
    mensaje_final = StringProperty("")

    def final_score(self, score):
        self.mensaje_final = f"Juego terminado. Puntaje final: {score}"

class InglesApp(App):
    def build(self):
        Builder.load_file("main.kv")
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(GameOverScreen(name="gameover"))
        return sm

if __name__ == "__main__":
    InglesApp().run()
