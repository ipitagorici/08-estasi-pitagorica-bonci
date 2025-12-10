from manim import *

class QuattroFrasi(Scene):
    def construct(self):
        phrase = [
            VGroup(
                Tex(r"\textsc{Aritmetica}", font_size=80), 
                Tex(r"numeri a riposo"), 
            ),
            VGroup(
                Tex(r"\textsc{Geometria}", font_size=80), 
                Tex("grandezze a riposo"),
            ),
            VGroup(
                Tex(r"\textsc{Musica}", font_size=80), 
                Tex("numeri in movimento"), 
            ),
            VGroup(
                Tex(r"\textsc{Astronomia}", font_size=80), 
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
            phrase[idx][0].set_color(LIGHT_BROWN if not change else BLUE)
            self.play(GrowFromEdge(phrase[idx], direction))
            self.play(Circumscribe(phrase[idx]))
            change = not change