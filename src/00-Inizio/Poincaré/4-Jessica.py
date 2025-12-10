from manim import *

class Jessica(Scene):
    def construct(self):
        poem4 = Tex("Essa dà un corpo, uno scheletro per così dire,\\\\" +
                        "alle cangianti apparenze che deliziano i nostri sensi,\\\\" +
                        "e senza questo sostegno\\\\" +
                        "la bellezza di quei sogni fugaci non sarebbe che imperfetta,\\\\" +
                        "perché confusa e sempre fuggitiva",
                        font_size=50)

        self.play(Write(poem4))

        self.wait(2)