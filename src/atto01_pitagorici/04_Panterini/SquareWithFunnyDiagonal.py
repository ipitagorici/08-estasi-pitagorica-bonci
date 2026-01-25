from manim import *

class Square(Scene):
    def construct(self):
        funnySquare = Rectangle(WHITE, 4, 4)
        funnyDiagonal = Line(funnySquare.get_corner(UR), funnySquare.get_corner(DL))

        lengths = [Text("1"), Tex(r"Teorema di Pitagora\\$a^2 + b^2 = c^2$"), Tex(r"$1^2 + 1^2 = 2$\\Quindi l'ipotenusa è uguale a $\sqrt{2}$"), Tex("$\sqrt{2}$")]
        lengths[0].next_to(funnySquare.get_edge_center(LEFT), LEFT)
        lengths[1].shift(RIGHT * 2.7).scale(1.8)
        lengths[2].scale(1.1).to_edge(RIGHT).shift(DOWN*2)
        
        self.play(LaggedStart(Create(funnySquare), Write(lengths[0]), lag_ratio=0.5))
        self.play(Create(funnyDiagonal))

        mainSquare = VGroup(funnySquare, funnyDiagonal, lengths[0])
        self.play(mainSquare.animate.to_edge(LEFT))

        self.play(GrowFromCenter(lengths[1]))
        self.wait(2)
        self.play(lengths[1].animate.scale(0.7))
        self.play(lengths[1].animate.to_corner(UR))

        self.play(GrowFromEdge(lengths[2], RIGHT))
        self.wait(1)

        lengths[3].move_to((funnyDiagonal.get_x()-0.5, funnyDiagonal.get_y()+0.5, 0)).set_color(RED)
        self.play(LaggedStart(FadeToColor(funnyDiagonal, RED), Write(lengths[3]), lag_ratio=0.5))
        self.wait(2)


