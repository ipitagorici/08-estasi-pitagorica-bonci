from manim import *

class ZeusAConfronto(Scene):
    def construct(self):
        def get_in_between_point(mobject_left, mobject_right):
            x_coord = (mobject_left.get_right()[0] + mobject_right.get_left()[0]) / 2
            y_coord = (mobject_left.get_center()[1] + mobject_right.get_center()[1]) / 2
            return (x_coord, y_coord, 0)


        from_edge_distance = 1
        teatro = ImageMobject("../assets/Teatro_Comunale_Alessandro_Bonci.jpg")\
            .scale(1.5)\
            .to_edge(LEFT)\
            .shift(RIGHT*from_edge_distance)
        zeus = ImageMobject("../assets/zeus_bianco-nobg.png")\
            .to_edge(RIGHT)\
            .shift(LEFT*from_edge_distance)
        zeus.shift(DOWN*(zeus.get_bottom()[1]-teatro.get_bottom()[1]))

        zeus_height_indicator = Line(
            start=(zeus.get_bottom()[0], zeus.get_bottom()[1]-.5, 0), 
            end=(zeus.get_top()[0], zeus.get_top()[1]-.5, 0))\
                .next_to(zeus, RIGHT)
        zeus_height = Tex(r"18\ m")\
            .next_to(zeus_height_indicator, RIGHT)\
            .scale(1.2)

        elements = Group(teatro, zeus, zeus_height_indicator, zeus_height)
        
        zeus_height_operation = MathTex(r"4\ \text{cubiti}\ \times ")
        tetraktys = ImageMobject("../assets/tetraktys_nowriting.png")\
            .scale(.15)\
            .next_to(zeus_height_operation, RIGHT)
        equal_to = MathTex(r"= 40\ \text{cubiti}")\
            .next_to(tetraktys, RIGHT)

        operation = Group(zeus_height_operation, tetraktys, equal_to)\
            .move_to([0, -config.frame_height/2.5, 0])
         
        self.play(FadeIn(teatro))
        self.wait(2)

        self.play(FadeIn(zeus), GrowFromEdge(zeus_height_indicator, DOWN), Write(zeus_height), Circumscribe(zeus_height))
        self.wait(2)

        self.play(elements.animate.shift(UP*0.75))
        
        self.play(Write(zeus_height_operation))
        self.play(FadeIn(tetraktys))
        self.play(Write(equal_to), Circumscribe(equal_to))


