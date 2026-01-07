from manim import *

class Poem(Scene):
    def construct(self):
        # remember to render using the --save_sections option!
        
        self.next_section("AnnaRicci")

        poem1 = Tex("L’uomo di scienza non studia la natura perché ciò è utile;\\\\" +
                        "la studia perché ci prova gusto,\\\\" + 
                        "e ci prova gusto perché la natura è bella.\\\\"
                        "Se la natura non fosse bella,\\\\" +
                        "non varrebbe la pena conoscerla.\\\\" +
                        "né varrebbe la pena vivere la nostra vita.",
                        font_size=50)

        self.play(Write(poem1), run_time=4)

        self.wait(2)
        
        self.next_section("Ilaria")
        
        self.play(FadeOut(*self.mobjects), run_time=2)
        
        poem2 = Tex("Non intendo parlare, naturalmente,\\\\" +
                        "di quella bellezza che colpisce i sensi,\\\\" +
                        "della bellezza delle apparenze qualitative;\\\\" + 
                        "non che la che la disdegni, tutt’altro,\\\\" +
                        "ma essa non ha niente a che vedere con la scienza.",
                        font_size=55)

        self.play(Write(poem2))

        self.wait(2)

        self.next_section("AnnaBaldini")
        
        self.play(FadeOut(*self.mobjects), run_time=2)

        poem3 = Tex("Intendo invece parlare di quella bellezza più riposta\\\\" +
                        "che deriva dall’ordine armonioso delle parti\\\\" +
                        "e che può essere colta dalla pura intelligenza.",
                        font_size=55)

        self.play(Write(poem3))

        self.wait(2)

        self.next_section("Jessica")
        self.play(FadeOut(*self.mobjects), run_time=2)

        poem4 = Tex("Essa dà un corpo, uno scheletro per così dire,\\\\" +
                        "alle cangianti apparenze che deliziano i nostri sensi,\\\\" +
                        "e senza questo sostegno\\\\" +
                        "la bellezza di quei sogni fugaci non sarebbe che imperfetta,\\\\" +
                        "perché confusa e sempre fuggitiva",
                        font_size=50)

        self.play(Write(poem4))

        self.wait(2)