from manim import *

class PT4(Scene):
    def construct(self):
        prev = MathTex(r"\frac{q^2}{2} = p^2").scale(3)
        self.add(prev)
        text = MathTex(r"p = 2k").scale(3)
        self.play(Transform(prev, text))