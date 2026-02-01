from manim import *
from src.custom_mobjects import BoheldText

WIDTH_OFFSET = 6

class BohemianRhapsody(Scene):
    def construct(self):
        frasi = [
            ("Goodbye, everybody, I've got to go", "Arrivederci a tutti, devo andare"),
            ("Gotta leave you all behind and face the truth", "Devo lasciarvi indietro e affrontare la veritÀ"),
            ("I don't wanna die\\\I sometimes wish I'd never been born at all", "Non voglio morire,\nma a volte vorrei non essere mai nato"),
        ]

        f1, t1 = frasi[0]
        it1 = BoheldText(t1).scale_to_fit_width(self.camera.frame_width - WIDTH_OFFSET)
        eng1 = Tex(rf"\textit{{{f1}}}").scale_to_fit_width(it1.width - 2).set_opacity(.7)
        frase1 = VGroup(it1, eng1)\
            .arrange_in_grid(buff=SMALL_BUFF, cols=1, cell_alignment=LEFT)\
            .to_corner(UL, buff=LARGE_BUFF)
        # self.add(frase1)

        f2, t2 = frasi[1]
        it2 = BoheldText(t2).scale_to_fit_width(it1.width)
        eng2 = Tex(rf"\textit{{{f2}}}").scale_to_fit_width(it2.width - 2).set_opacity(.7)
        frase2 = VGroup(it2, eng2)\
            .arrange_in_grid(buff=SMALL_BUFF, cols=1, cell_alignment=RIGHT)\
            .to_edge(RIGHT, buff=LARGE_BUFF)
        # self.add(frase2)

        f3, t3 = frasi[2]
        it3 = BoheldText(t3).scale_to_fit_width(it1.width)
        eng31 = Tex(r"\textit{I don't wanna die}").scale_to_fit_width(it3.width - 5.5).set_opacity(.8)
        eng32 = Tex(r"\textit{I sometimes wish I'd never been born at all}").scale_to_fit_width(it3.width - 2).set_opacity(.7)
        frase3 = VGroup(it3, eng31, eng32)\
            .arrange_in_grid(buff=SMALL_BUFF, cols=1, cell_alignment=LEFT)\
            .to_corner(DL, buff=LARGE_BUFF)
        # self.add(frase3)        
        ippaso = Tex(r"$\textit{Ippaso}$").to_corner(DR, buff=LARGE_BUFF)
        
        self.play(Write(it1))
        self.play(FadeIn(eng1, shift=RIGHT))
        self.wait()
        self.play(Write(it2))
        self.play(FadeIn(eng2, shift=LEFT))
        self.wait()
        self.play(Write(it3))
        self.play(FadeIn(eng31, shift=RIGHT), FadeIn(eng32, shift=RIGHT))
        self.wait()
        self.play(Write(ippaso), run_time=5)
        
        # self.next_section()
        
        # self.play(FadeOut(translation1))

        # self.play(FadeIn(translation2))
        
        # self.next_section()
        
        # self.play(FadeOut(translation2))

        # self.play(FadeIn(pause))
        
        # self.next_section()
        
        # self.play(FadeOut(pause))

        # self.play(FadeIn(translation3))
        
        # self.next_section()
        
        # self.play(FadeIn(ippaso))

        # self.wait(2)   