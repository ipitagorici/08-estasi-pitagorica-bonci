from manim import *
from src.custom_mobjects import BoheldText

class Amore(Scene):
    def construct(self):
        amore = BoheldText("Amore").scale(4)
        self.play(Write(amore))