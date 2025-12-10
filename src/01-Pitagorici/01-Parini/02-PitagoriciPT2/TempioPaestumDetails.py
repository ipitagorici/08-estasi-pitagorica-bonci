from manim import *

class TempioPaestumDetails(MovingCameraScene):
    def construct(self):
        paestum_img = ImageMobject("../assets/tempio-nettuno.jpg").scale(.75).shift(UP * .5)
        title = Tex(r"\textsc{Tempio di Nettuno — Paestum}")
        title.next_to(paestum_img, DOWN, buff=.5).scale(1.4)
        self.add(paestum_img, title)
        self.camera.frame.save_state()
        upper_band = Rectangle(width=paestum_img.width, color=BLACK, height=1.75).set_opacity(1).to_edge(UP)
        lower_band = Rectangle(width=paestum_img.width, color=BLACK, height=4.5).set_opacity(1).to_edge(DOWN)
        self.play(
            FadeIn(upper_band), FadeIn(lower_band),
            self.camera.frame.animate.set(width=paestum_img.width * .4).shift(UP * 1.3)
        )
        metopa_pointer = Circle(radius=.25).shift(UP * 1.3 + RIGHT * .1).set_color(RED)
        triglifo_pointer = Circle(radius=.25).shift(UP * 1.3 + RIGHT * .95).set_color(GREEN)
        metopa_lbl = Tex("Metopa").set_color(RED).next_to(metopa_pointer, UP, buff=.1).scale(.6)
        triglifo_lbl = Tex("Triglifo").set_color(GREEN).next_to(triglifo_pointer, DOWN, buff=.1).scale(.6)
        self.play(Create(metopa_pointer), Write(metopa_lbl), run_time=2)
        self.wait()
        self.play(Create(triglifo_pointer), Write(triglifo_lbl), run_time=2)