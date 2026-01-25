from manim import *
from src.custom_mobjects import BoheldText

class QuattroLettere(Scene):
    def construct(self):
        phrase = [
            VGroup(
                Tex(r"$\Omega$", font_size=200), 
                BoheldText(r"Parametro di densità").scale(.5), 
            ),
            VGroup(
                Tex(r"\textsc{k}", font_size=200), 
                BoheldText("Curvatura").scale(.5),
            ),
            VGroup(
                Tex(r"\textsc{H}", font_size=200), 
                BoheldText("Costante di Hubble").scale(.5), 
            ),
            VGroup(
                Tex(r"$\Lambda$", font_size=200), 
                BoheldText("Costante cosmologica").scale(.5)
            )
        ]
        
        for group in phrase:
            group.arrange_in_grid(cols=1)
        
        phrases = VGroup(
            *[ph for ph in phrase]
        ).arrange_in_grid(cols=2, rows=2, buff=1.5)
        
        change = False
        for idx, direction in enumerate([UP, LEFT, RIGHT, DOWN]):
            phrase[idx][0].set_color(GREEN if not change else BLUE)
            self.play(GrowFromEdge(phrase[idx], direction))
            self.play(Circumscribe(phrase[idx]))
            change = not change