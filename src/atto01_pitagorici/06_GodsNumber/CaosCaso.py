from manim import *
from src.custom_mobjects import BoheldText

class CaosCaso(Scene):
    def construct(self):
        caos = BoheldText("Caos", font_size=200)
        self.play(Write(caos))

        self.next_section("CaosToCaso")
        
        caso = BoheldText("Caso", font_size=200)
        self.play(Transform(caos, caso))