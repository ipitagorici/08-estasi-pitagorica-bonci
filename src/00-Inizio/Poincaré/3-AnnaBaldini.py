from manim import *

class AnnaBaldini(Scene):
    def construct(self):
        poem3 = Tex("Intendo invece parlare di quella bellezza più riposta\\\\" +
                        "che deriva dall’ordine armonioso delle parti\\\\" +
                        "e che può essere colta dalla pura intelligenza.",
                        font_size=55)

        self.play(Write(poem3))

        self.wait(2)