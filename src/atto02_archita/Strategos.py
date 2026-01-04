from manim import *

class Strategos(Scene):
    def construct(self):
        # Στρατεγός
        strategos = Text(r"Στρατεγός", font_size=150).set_color(GREEN)
        strategos_it = Tex('"Stratego"', font_size=80).next_to(strategos, DOWN, .5)

        all = VGroup(strategos, strategos_it).center()
        self.play(Write(strategos), run_time=1)
        self.play(Write(strategos_it))
        self.wait()