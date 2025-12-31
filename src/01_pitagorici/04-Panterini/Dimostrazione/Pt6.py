from manim import *

class PT6(Scene):
    def construct(self):
        prev = MathTex(r"p^2 = 4k^2").scale(3)
        self.add(prev)
        text = MathTex(r"\frac{4k^2}{2} = q^2").scale(3)
        self.play(Transform(prev, text))