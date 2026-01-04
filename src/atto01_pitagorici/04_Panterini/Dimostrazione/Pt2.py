from manim import *

class PT2(Scene):
    def construct(self):
        prev = MathTex(r"\frac{q}{p} = \sqrt{2}").scale(3)
        self.add(prev)
        text = MathTex(r"\frac{q^2}{p^2} = 2").scale(3)
        self.play(Transform(prev, text))