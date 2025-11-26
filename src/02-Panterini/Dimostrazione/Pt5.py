from manim import *

class PT5(Scene):
    def construct(self):
        prev = MathTex(r"p = 2k").scale(3)
        self.add(prev)
        text = MathTex(r"p^2 = 4k^2").scale(3)
        self.play(Transform(prev, text))