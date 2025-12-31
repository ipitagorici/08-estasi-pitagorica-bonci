from manim import *

class Sqrt2Decimals(Scene):
    def construct(self):
        customTemplate = TexTemplate()
        customTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        sqrt2 = Tex(r"$\sqrt{2} = 1.414$").scale(3).set_color(GREEN)
        self.play(Write(sqrt2), run_time=2)