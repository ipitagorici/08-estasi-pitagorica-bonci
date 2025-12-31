from manim import *

class TempioPaestumIntro(Scene):
    def construct(self):
        paestum_img = ImageMobject("../assets/tempio-nettuno.jpg")
        title = Tex(r"\textsc{Tempio di Nettuno — Paestum}")
        self.play(FadeIn(paestum_img))
        self.wait()
        self.play(paestum_img.animate.scale(.75).shift(UP * .5))
        title.next_to(paestum_img, DOWN, buff=.5).scale(1.4)
        self.play(Write(title))
        self.play(Circumscribe(title))