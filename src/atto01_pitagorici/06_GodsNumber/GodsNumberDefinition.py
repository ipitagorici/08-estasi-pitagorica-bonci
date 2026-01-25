from manim import *
from src.custom_mobjects import BoheldText

class GodsNumber(Scene):
    def construct(self):
        title = BoheldText("God's Number", font_size=100)
        subtitle = Tex(r"\textsc{Numero di Dio}").next_to(title, DOWN, MED_LARGE_BUFF)
        VGroup(title, subtitle).center()

        self.play(Write(title))
        self.play(Wiggle(title))
        self.play(Write(subtitle))
        self.wait(2)