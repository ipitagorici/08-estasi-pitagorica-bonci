from manim import *

class PT1(Scene):
    def construct(self):
        text = MathTex(r"\frac{q}{p} = \sqrt{2}").scale(3)
        self.play(Write(text))