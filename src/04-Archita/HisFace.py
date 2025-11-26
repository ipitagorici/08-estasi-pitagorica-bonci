from manim import *

class HisFace(Scene):
    def construct(self):
        face = ImageMobject("../assets/archita-da-taranto.jpg")
        face.scale(1.2)
        self.play(FadeIn(face), run_time=1.5)
        self.play(face.animate.scale(.65).to_edge(UP, buff=.7))
        name = Tex(r"$\mathbb{A}$\textsc{rchita}").scale(2.5)
        name.next_to(face, DOWN)
        birth_place = Tex(r"\textbf{Taranto}")
        death_place = Tex(r"\textbf{Mattinata}")
        birth_day = Tex("428 a.C.")
        death_day = Tex("360 a.C.")
        info = VGroup(birth_place, birth_day, death_place, death_day)
        info.arrange_in_grid(rows=2, cols=2, cell_alignment=RIGHT, buff=(.75, MED_SMALL_BUFF))
        info.next_to(name, DOWN, .35).scale(.8)
        
        self.play(Write(name), run_time=2)
        self.play(Circumscribe(name))
        self.play(Write(info))