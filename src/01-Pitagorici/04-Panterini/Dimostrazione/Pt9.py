from manim import *

class PT9(Scene):
    def construct(self):
        text = Tex(r"p = pari \\ q = pari").scale(2)
        conclusion = Tex(r"\# Assurdo!").scale(2).next_to(text, DOWN, 1)
        all = VGroup(text, conclusion).center()
        self.play(Write(all))