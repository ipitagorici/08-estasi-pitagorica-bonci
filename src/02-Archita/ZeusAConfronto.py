from manim import *

class ZeusAConfronto(Scene):
    def construct(self):
        zeus = ImageMobject("../assets/zeus_bianco-nobg.png")
        santuario = ImageMobject("../assets/santuario-santissimo-crocifisso.jpg").scale(.8)
        zeus.next_to(santuario, RIGHT).scale(1.5).shift(UP * .4)
        both = Group(zeus, santuario).move_to(ORIGIN).scale(.8).shift(UP * .5)
        zeus_height_indicator = Line(
            start=(zeus.get_bottom()[0], zeus.get_bottom()[1] - .75, 0), 
            end=(zeus.get_top()[0], zeus.get_top()[1] - .75, 0)).next_to(zeus, RIGHT, buff=-.2).set_color(YELLOW).shift(DOWN * .1)
        zeus_height = Tex(r"18\ m").next_to(zeus_height_indicator, RIGHT, buff=.5).scale(1.2)
        zeus_height_operation = MathTex(r"4\ \text{cubiti}\ \times ")
        tetraktys = ImageMobject("../assets/tetraktys_nowriting.png").scale(.16)
        equal_to = MathTex(r"= 40\ \text{cubiti}")
        operation = Group(zeus_height_operation, tetraktys, equal_to).arrange_in_grid(rows=1).next_to(both, DOWN, buff=.2)
        # self.add(operation, zeus_height_indicator, zeus_height)
        # self.add(both)
        self.play(FadeIn(santuario))
        self.wait(2)
        self.play(FadeIn(zeus), GrowFromEdge(zeus_height_indicator, DOWN), Write(zeus_height), Circumscribe(zeus_height))
        self.wait(2)
        self.play(Write(zeus_height_operation))
        self.play(FadeIn(tetraktys))
        self.play(Write(equal_to), Circumscribe(equal_to))