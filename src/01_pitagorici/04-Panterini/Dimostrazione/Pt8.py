from manim import *

class PT8(Scene):
    def construct(self):
        prev = MathTex(r"2k^2 = q^2").scale(3)
        self.add(prev)
        text = MathTex(r"k^2 = \frac{q^2}{2}").scale(3)
        self.play(Transform(prev, text))