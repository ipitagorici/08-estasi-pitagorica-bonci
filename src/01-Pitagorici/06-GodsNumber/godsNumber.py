from manim import *

class GodsNumber(Scene):
    def construct(self):
        godsNumber = Tex(r"God's Number \\ Numero di Dio", font_size=200)

        self.play(Write(godsNumber))


        self.wait(2)