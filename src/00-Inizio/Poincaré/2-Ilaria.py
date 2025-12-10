from manim import *

class Ilaria(Scene):
    def construct(self):
        poem2 = Tex("Non intendo parlare, naturalmente,\\\\" +
                        "di quella bellezza che colpisce i sensi,\\\\" +
                        "della bellezza delle apparenze qualitative;\\\\" + 
                        "non che la che la disdegni, tutt’altro,\\\\" +
                        "ma essa non ha niente a che vedere con la scienza.",
                        font_size=55)

        self.play(Write(poem2))

        self.wait(2)
        