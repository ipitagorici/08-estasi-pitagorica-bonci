from manim import *

class Infinitum(Scene):
    def construct(self):
        text = Tex(r"$\mathbb{I}$\textsc{nfinitum}").scale_to_fit_width(self.camera.frame_width - 2)
        self.play(Write(text))