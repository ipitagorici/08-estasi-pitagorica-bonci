from manim import *

class ZeusAConfronto(Scene):
    def construct(self):
        def get_in_between_point(mobject1, mobject2):
            x_coord = (mobject1.get_center()[0] + mobject2.get_center()[0]) / 2
            y_coord = (mobject1.get_center()[1] + mobject2.get_center()[1]) / 2
            return (x_coord, y_coord, 0)


        
        teatro = ImageMobject("../assets/Teatro_Comunale_Alessandro_Bonci.jpg")\
            .to_edge(LEFT)
        zeus = ImageMobject("../assets/zeus_bianco-nobg.png")\
            .scale(1.5)\
            .to_edge(RIGHT)

        zeus_height_indicator = Line(
            start=(zeus.get_bottom()[0], zeus.get_bottom()[1]-.5, 0), 
            end=(zeus.get_top()[0], zeus.get_top()[1]-.5, 0))\
                .next_to(zeus, RIGHT)
        zeus_height = Tex(r"18\ m")\
            .next_to(zeus_height_indicator, RIGHT)\
            .scale(1.2)
        
        zeus_height_operation = MathTex(r"4\ \text{cubiti}\ \times ")\
            .move_to(get_in_between_point(teatro, zeus))
        
        tetraktys = ImageMobject("../assets/tetraktys_nowriting.png").scale(.16)
        
        equal_to = MathTex(r"= 40\ \text{cubiti}") 
        
        self.play(FadeIn(teatro))
        self.wait(2)
        self.play(FadeIn(zeus), GrowFromEdge(zeus_height_indicator, DOWN), Write(zeus_height), Circumscribe(zeus_height))
        self.wait(2)
        self.play(Write(zeus_height_operation))
        self.play(FadeIn(tetraktys))
        self.play(Write(equal_to), Circumscribe(equal_to))


