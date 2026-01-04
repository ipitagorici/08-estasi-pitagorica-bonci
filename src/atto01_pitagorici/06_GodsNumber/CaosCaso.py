from manim import *

class Caos(Scene):
    def construct(self):
        caos = Tex("Caos", font_size=200)

        self.play(Write(caos))
        self.wait(2)
        
class CaosCaso(Scene):
    def construct(self):
        caos = Tex("Caos", font_size=200)
        caso = Tex("Caso", font_size=200)

        self.add(caos)
        self.play(Transform(caos, caso))
        self.wait(2)