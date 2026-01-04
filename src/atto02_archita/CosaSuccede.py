from manim import *

class CosaSuccede(Scene):
    def construct(self):
        text = Tex(r"Cosa succede se scaglio il mio bastone \\ verso il limite del Cosmo?").scale_to_fit_width(self.camera.frame_width - 2)
        self.play(Write(text))