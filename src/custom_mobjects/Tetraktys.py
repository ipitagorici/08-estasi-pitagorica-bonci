from manim import *

class Tetraktys(Mobject):
    def __init__(self):
        super().__init__()
        colors = [ManimColor("#ffe680"), GREEN, TEAL, ORANGE]
        circles = VGroup()
        
        for i in range(0, 4):
            layer = VGroup()
            for _ in range(0, i + 1):
                new_circ = Circle(color=colors[i])
                new_circ.set_fill(colors[i], opacity=1) 
                layer.add(new_circ)

            layer.arrange_in_grid(rows=1, buff=1)
            circles.add(layer)

        circles.arrange_in_grid(cols=1)\
            .move_to(ORIGIN)\
            .scale(.5)
        
        triangle = Polygon(
            circles.get_top(), 
            circles.get_right() + DOWN * 2, 
            circles.get_left() + DOWN * 2)\
                .scale(1.5)\
                .shift(UP * .35)\
                .set_stroke(color=MAROON)
        
        self.triangle = triangle
        self.dots = circles

        tetraktys = VGroup(circles, triangle).scale(.8)
        self.add(tetraktys)

    def get_triangle(self):
        return self.triangle.copy()
    
    def get_dots(self):
        return self.dots.copy()