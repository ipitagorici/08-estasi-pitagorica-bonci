from manim import *

class AnnaRicci(Scene):
    def construct(self):
        poem1 = Tex("L’uomo di scienza non studia la natura perché ciò è utile;\\\\" +
                        "la studia perché ci prova gusto,\\\\" + 
                        "e ci prova gusto perché la natura è bella.\\\\"
                        "Se la natura non fosse bella,\\\\" +
                        "non varrebbe la pena conoscerla.\\\\" +
                        "né varrebbe la pena vivere la nostra vita.",
                        font_size=50)

        self.play(Write(poem1))

        self.wait(2)  