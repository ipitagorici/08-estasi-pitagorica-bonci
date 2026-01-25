from manim import *

class Cube(Scene):
    def construct(self):
        cube = ImageMobject("src/assets/imgs/rubiks-cube.png").scale(.8)

        self.play(FadeIn(cube))