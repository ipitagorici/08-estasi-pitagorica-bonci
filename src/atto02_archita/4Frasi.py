from manim import *
from src.custom_mobjects import BoheldText

class QuattroFrasi(Scene):
    def construct(self):
        phrase = [
            VGroup(
                BoheldText(r"Aritmetica", font_size=60), 
                Tex(r"numeri a riposo"), 
            ),
            VGroup(
                BoheldText(r"Geometria", font_size=60), 
                Tex("grandezze a riposo"),
            ),
            VGroup(
                BoheldText(r"Musica", font_size=60), 
                Tex("numeri in movimento"), 
            ),
            VGroup(
                BoheldText(r"Astronomia", font_size=60), 
                Tex("grandezze in movimento")
            )
        ]
        
        for group in phrase:
            group.arrange_in_grid(cols=1)
        
        phrases = VGroup(
            *[ph for ph in phrase]
        ).arrange_in_grid(cols=2, rows=2, buff=1.5)
        
        change = False
        for idx, direction in enumerate([UP, LEFT, RIGHT, DOWN]):
            self.play(GrowFromEdge(phrase[idx], direction))
            self.play(Circumscribe(phrase[idx]))
            change = not change