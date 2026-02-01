from manim import *
from src.custom_mobjects import Tetraktys

class Interleave(Scene):
    def create_glow(self, vmobject: VMobject, rad=1, col=YELLOW):
        glow_group = VGroup()
        for idx in range(100):
            new_obj = vmobject.copy()
            new_obj\
                .scale(1 + (1.002 ** (idx**2))/400)\
                .set_stroke(opacity = 0)\
                .move_to(vmobject)
            if vmobject.get_color() is not None:
                new_obj\
                    .set_color(col)\
                    .set_opacity(0.2 - idx/300)
            if vmobject.get_stroke_color() is not None:
                new_obj\
                    .set_stroke(color = col, opacity = 0.2 - idx/300)
            glow_group.add(new_obj)
        return glow_group

    def construct(self):
        tetraktys = Tetraktys()
        circles = tetraktys.get_dots()
        border = tetraktys.get_triangle()
        self.play(AnimationGroup(
            *[SpiralIn(circle_row) for circle_row in circles],
            lag_ratio=.27
        ), run_time=4)
        glows = VGroup()
        for row in circles:
            for circle in row:
                glows.add(self.create_glow(vmobject=circle, col=circle.get_color()))
        self.wait()
        self.play(
            DrawBorderThenFill(border), 
        )
        self.play(AnimationGroup(
                FadeIn(*[glow for glow in glows]), 
                Broadcast(border, focal_point=border.get_center())
            )
        )