from manim import *
from src.custom_mobjects import BoheldText

class Emma(Scene):
    def construct(self):
        emma = ImageMobject("src/assets/imgs/emma.jpg")\
            .scale(0.5).to_edge(LEFT)
        name = BoheldText("Emma Castelnuovo")\
            .next_to(emma, RIGHT, .15)\
            .scale(.9)
        life = Tex("1913 - 2014")\
            .next_to(name, DOWN, .5)

        all = Group(emma, name, life).center()
        emma_shadow = Rectangle(color=name.get_shadow().get_color(), height=emma.height, width=emma.width)\
            .move_to(emma)\
            .shift(DL * .050)\
            .set_z_index(-1)\
            .set_fill(name.get_shadow().get_color(), opacity=1)
        
        self.play(FadeIn(emma), FadeIn(emma_shadow))
        self.play(Write(name), Write(life))
        self.play(Circumscribe(name))
        
        self.wait()