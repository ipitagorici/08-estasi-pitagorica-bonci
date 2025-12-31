from manim import *

class BohemianRhapsody(Scene):
    def construct(self):
        translation1 = Tex("Arrivederci a tutti, devo andare",
                            font_size=75)
        translation2 = Tex("Devo lasciarvi indietro e affrontare la verità",
                            font_size=65)
        pause = Tex("(...)", font_size=100)
        translation3 = Tex("Non voglio morire,\\\\ma a volte vorrei non essere mai nato",
                            font_size=75)
        ippaso = Tex(r"$\textit{Ippaso}$", font_size=80).to_corner(DR)

        self.play(FadeIn(translation1))
        self.wait(4)
        self.play(FadeOut(translation1))

        self.play(FadeIn(translation2))
        self.wait(6)
        self.play(FadeOut(translation2))

        self.play(FadeIn(pause))
        self.wait(4)
        self.play(FadeOut(pause))

        self.play(FadeIn(translation3))
        self.wait(8)
        self.play(FadeIn(ippaso))

        self.wait(2)   