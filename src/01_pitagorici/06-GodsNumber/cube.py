from manim import *

class Cube(Scene):
    def construct(self):
        cube = ImageMobject("../../assets/rubiks-cube.jpg").scale(2)

        self.play(FadeIn(cube))