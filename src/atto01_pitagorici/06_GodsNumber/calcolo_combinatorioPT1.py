from manim import *
from src.custom_mobjects import BoheldText

class CalcoloCombinatorio(Scene):
    def construct(self):
        # --------------------- #
        #   DEFINING MOBJECTS   #
        # --------------------- #

        cube = ImageMobject("src/assets/imgs/rubiks-cube.png")

        # DEFINING PIECES OF THE CUBE
        s_text = MathTex(r"12 \times \textsc{Spigoli}", substrings_to_isolate=["12"])\
            .set_color_by_tex("12", YELLOW)
        a_text = MathTex(r"8 \times \textsc{Angoli}", substrings_to_isolate=["8"])\
            .set_color_by_tex("8", TEAL)
        c_text = MathTex(r"6 \times \textsc{Centri}", substrings_to_isolate=["6"])\
            .set_color_by_tex("6", GREEN)
        
        s_img = ImageMobject("src/assets/imgs/spigoli.png").scale(0.4)
        a_img = ImageMobject("src/assets/imgs/angoli.png").scale_to_fit_height(s_img.height)
        c_img = ImageMobject("src/assets/imgs/centri.png").scale_to_fit_height(s_img.height)

        spigoli = Group(s_text, s_img)
        angoli = Group(a_text, a_img)
        centri = Group(c_text, c_img)
        
        # ARRANGING PIECES
        for g in [ spigoli, angoli, centri ]:
            g.arrange_in_grid(cols=1, cell_alignment=ORIGIN, buff=0.25)

        pieces = (
            Group(centri, angoli, spigoli)
                .arrange_in_grid(rows=1)
                .align_to(cube, DOWN)
        )
        
        # NUMBERS FOR CALCULATIONS
        calcolo_centri = Tex(r"Posizione costante")
        calcolo_angoli = VGroup(
            MathTex(r"8!\ \text{ posizioni }", substrings_to_isolate=[r"8"])\
                .set_color_by_tex(r"8", TEAL),
            Tex(r"$ \times $"),
            MathTex(r"3^8 \text{ colori}", substrings_to_isolate=[r"8"])\
                .set_color_by_tex(r"8", TEAL)
        ).arrange_in_grid(rows=1)
        calcolo_spigoli = VGroup(
            MathTex(r"12! \text{ posizioni}", substrings_to_isolate=[r"12"])\
                .set_color_by_tex("12", YELLOW),
            Tex(r"$ \times $"),
            MathTex(r"2^{12} \text{ colori}", substrings_to_isolate=[r"12"])\
                .set_color_by_tex("12", YELLOW)
        ).arrange_in_grid(rows=1)

        totale_mosse = Group(
            BoheldText(r"519.024.039.293.878.272.000").scale_to_fit_width(self.camera.frame_width - 3),
            Tex(r"(519 \textsc{quintilioni})", font_size=50)
        ).arrange_in_grid(cols=1).center()
        
        # -------------- #
        #   ANIMATIONS   #
        # -------------- #

        self.play(FadeIn(cube))
        self.play(cube.animate.scale(0.3).to_edge(UP))
        
        for piece in pieces:
            self.play(FadeIn(piece))
            print(piece.get_x(), piece.get_y())

        self.wait()

        self.next_section() # NEXT SECTION --------------------------------------------------------------

        self.play(FadeOut(cube))

        self.play(pieces.animate.scale(0.6))
        self.play(pieces.animate.arrange_in_grid(cols=1, buff=0.1)\
                .center()\
                .to_edge(LEFT))

        calcoli = Group(
            centri, calcolo_centri, 
            angoli, calcolo_angoli, 
            spigoli, calcolo_spigoli)\
            .arrange_in_grid(rows=3, cell_alignment=LEFT, buff=(LARGE_BUFF, MED_SMALL_BUFF))
        
        # ARRANGING PIECES — again
        for g in [ spigoli, angoli, centri ]:
            g.arrange_in_grid(cols=1, cell_alignment=ORIGIN, buff=0.25)

        self.wait()
        self.next_section() # NEXT SECTION -------------------------------------------------------------

        # -------------- #
        #     NUMERI     #
        # -------------- #
        for text_idx in range(1, len(calcoli), 2):
            self.play(FadeIn(calcoli[text_idx]))
            self.next_section() # NEXT SECTION --------------------------------------------------------------
        
        self.play(FadeOut(calcolo_centri), FadeOut(calcolo_angoli), FadeOut(calcolo_spigoli))
        self.play(FadeOut(pieces))
        self.wait()
        self.play(Write(totale_mosse[0]))
        self.play(FadeIn(totale_mosse[1]))
        
        self.wait(2)