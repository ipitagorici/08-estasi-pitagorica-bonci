from manim import *

class Square(Scene):
    def construct(self):
        funnySquare = Rectangle(WHITE, 4, 4)
        funnyDiagonal = Line(funnySquare.get_corner(UR), funnySquare.get_corner(DL))

        lenghts = [Text("1"), Tex(r"Teorema di Pitagora:\\$a^2 + b^2 = c^2$"), Tex(r"$1^2 + 1^2 = 2$\\Quindi l'ipotenusa è uguale a $\sqrt{2}$"), Tex("$\sqrt{2}$")]
        lenghts[0].next_to(funnySquare.get_edge_center(LEFT), LEFT)
        lenghts[1].shift(RIGHT*2.7).scale(1.8)
        lenghts[2].scale(1.1).to_edge(RIGHT).shift(DOWN*2)
        
        self.play(LaggedStart(Create(funnySquare), Write(lenghts[0]), lag_ratio=0.5))
        self.play(Create(funnyDiagonal))

        mainSquare = VGroup(funnySquare, funnyDiagonal, lenghts[0])
        self.play(mainSquare.animate.to_edge(LEFT))

        self.play(GrowFromCenter(lenghts[1]))
        self.wait(2)
        self.play(lenghts[1].animate.scale(0.7))
        self.play(lenghts[1].animate.to_corner(UR))

        self.play(GrowFromEdge(lenghts[2], RIGHT))
        self.wait(1)

        lenghts[3].move_to((funnyDiagonal.get_x()-0.5, funnyDiagonal.get_y()+0.5, 0)).set_color(RED)
        self.play(LaggedStart(FadeToColor(funnyDiagonal, RED), Write(lenghts[3]), lag_ratio=0.5))
        self.wait(2)


