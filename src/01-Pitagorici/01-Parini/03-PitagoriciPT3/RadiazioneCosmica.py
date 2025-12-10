from manim import *

class RadiazioneCosmica(Scene):
    def construct(self):
        title = Title(r"\textsc{Onda Radiazione Cosmica di Fondo}")
        img = ImageMobject("../assets/PowerSpectrumExt.png").scale_to_fit_height(self.camera.frame_height - title.height).scale(.80).shift(DOWN * .7)
        self.play(Write(title), run_time=.6)
        self.play(FadeIn(img), Circumscribe(img))
        self.wait()