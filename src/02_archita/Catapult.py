from manim import *
from math import *

class Catapult(Scene):
    def construct(self):
        axes = Axes((-10, 60, 10), (0, 100, 10), 10, 5)
        rectangle = Rectangle(DARK_BROWN, 1.5, 2)
        rectangle.move_to(axes.get_origin()).shift(UP*rectangle.height/2)
        
        catapultTriangle = Triangle(color=RED).scale(0.3).next_to(rectangle, UP, buff=0).shift(RIGHT*0.25)
        catapultLine = Line((0, 0, 0), (1, 0, 0)).move_to(catapultTriangle.get_center())
        
        square = Square(0.3, color=RED).next_to(catapultLine.get_start(), direction=DOWN, buff=-0.3) 
        numbers = []
        for i in range(1, 4):
            numbers.append(Text(f"{i}", font_size=20).move_to(square.get_center()).add_updater(lambda n: n.move_to(square.get_center())))

        numberedSquare = VGroup(square)
        
        catapult = VGroup(catapultTriangle, catapultLine, numberedSquare)
        
        f1 = lambda x: -0.1*x**2 + 4*x + 40
        f1Display = axes.plot(f1, (0, 48.28, 1)).set_color(GREEN)
        f2 = lambda x: -0.0168*x**2 + 40
        f2Display = axes.plot(f2, (0, 48.28, 1)).set_color(TEAL)
        f3 = lambda x: -0.058*x**2 + 2*x + 40
        f3Display = axes.plot(f3, (0, 48.28, 1)).set_color(MAROON)
        
        ship1 = Triangle(color=WHITE).move_to(f1Display.get_end()).shift(UP*0.5).scale(0.5)
        ship2 = Triangle(color=WHITE).move_to(f1Display.get_end()).shift(LEFT, UP*0.5).scale(0.5)
        
        self.play(Create(axes.plot(lambda x: sin(x), color=BLUE)))
        self.play(GrowFromEdge(rectangle, DOWN), GrowFromEdge(catapult, DOWN))
        self.play(GrowFromEdge(ship1, LEFT), GrowFromEdge(ship2, LEFT))
        self.play(Create(f1Display))
        self.play(numberedSquare.animate.scale(2).next_to(catapultLine.get_start(), direction=DOWN, buff=-0.6).shift(LEFT*0.2))
        self.wait()
        self.play(Create(f2Display))
        self.play(numberedSquare.animate.scale(1.5).next_to(catapultLine.get_start(), direction=DOWN, buff=-0.9).shift(LEFT*0.3))
        self.wait()
        self.play(Create(f3Display))
        self.wait()
                 