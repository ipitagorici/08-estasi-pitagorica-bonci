from manim import *
from src.custom_mobjects import BoheldText

class TempioPaestumIntro(Scene):
    def construct(self):
        paestum_img = ImageMobject("src/assets/imgs/tempio-nettuno.jpg")
        title = BoheldText(r"Tempio di Nettuno, Paestum")\
            .scale_to_fit_width(self.camera.frame_width - 5)
        self.play(FadeIn(paestum_img))
        self.wait()
        self.play(paestum_img.animate.scale(.75).shift(UP * .5))
        title.next_to(paestum_img, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(title))
        self.play(Circumscribe(title))