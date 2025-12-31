from manim import *

class GodsNumbers(Scene):
    def construct(self):
        cube2 = ImageMobject("../../assets/rubiks-cube2x2.png").scale(0.5).to_edge(LEFT)
        mosse2 = Tex(r"2x2 \\ 11 mosse").next_to(cube2, DOWN)

        cube3 = ImageMobject("../../assets/rubiks-cube3x3.jpg").move_to(ORIGIN)
        mosse3 = Tex(r"3x3 \\ 20 mosse").next_to(cube3, DOWN)

        cube4 = ImageMobject("../../assets/rubiks-cube4x4.jpg").scale(0.5).to_edge(RIGHT)
        mosse4 = Tex(r"4x4 \\ ??? mosse").next_to(cube4, DOWN)


        self.play(FadeIn(cube2), Write(mosse2))

        self.play(FadeIn(cube3), Write(mosse3))

        self.play(FadeIn(cube4), Write(mosse4))
    