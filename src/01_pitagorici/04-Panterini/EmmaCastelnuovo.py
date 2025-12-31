from manim import *

class Emma(Scene):
    def construct(self):
        emma = ImageMobject("../assets/emma.jpg")\
            .scale(0.5).to_edge(LEFT)
        name = Tex(r"\textsc{Emma Castelnuovo}\\")\
            .scale(1.2)\
            .next_to(emma, RIGHT, 1)
        life = Tex("1913 - 2014")\
            .next_to(name, DOWN, .5)

        all = Group(emma, name, life).center()

        self.play(FadeIn(emma))
        self.play(Write(name), Write(life))
        self.play(Circumscribe(name))
        
        self.wait()