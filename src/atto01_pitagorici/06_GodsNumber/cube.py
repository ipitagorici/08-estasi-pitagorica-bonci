from manim import *

class Cube(Scene):
    def construct(self):
        cube = ImageMobject("../src/assets/imgsrubiks-cube.png").scale(2)

        self.play(FadeIn(cube))