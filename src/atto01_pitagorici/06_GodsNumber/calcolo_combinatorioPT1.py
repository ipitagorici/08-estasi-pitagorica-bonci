from manim import *


class CalcoloCombinatorio(Scene):
    def construct(self):
        # --------------------- #
        #   DEFINING MOBJECTS   #
        # --------------------- #

        cube = ImageMobject("assets/imgs/rubiks-cube.png")

        # DEFINING PIECES OF THE CUBE
        s_text = Tex(r"$12 \times$ \textsc{Spigoli}")
        a_text = Tex(r"$8 \times$ \textsc{Angoli}")
        c_text = Tex(r"$6 \times$ \textsc{Centri}")
        
        s_img = ImageMobject("assets/imgs/spigoli.png").scale(0.1)
        a_img = ImageMobject("assets/imgs/angoli.png").scale_to_fit_height(s_img.height)
        c_img = ImageMobject("assets/imgs/centri.png").scale_to_fit_height(s_img.height)

        spigoli = Group(s_text, s_img)
        angoli = Group(a_text, a_img)
        centri = Group(c_text, c_img)
        
        # ARRANGING PIECES
        for g in [spigoli, angoli, centri]:
            g.arrange_in_grid(cols=1, buff=0.2)

        pieces = (
            Group(centri, angoli, spigoli)
            .arrange_in_grid(rows=1)
            .next_to(cube, DOWN, buff=0.5)
        )
        
        # NUMBERS FOR CALCULATIONS
        calcolo_centri = Tex(r"Posizione //// Costante").next_to(centri, RIGHT)
        calcolo_angoli = Tex(r"8! combinazioni //// $3^{8}$ colori").next_to(angoli, RIGHT)
        calcolo_spigoli = Tex(r"12! combinazioni //// $2^{12}$ colori").next_to(spigoli, RIGHT)
        
        totale_mosse = Tex(r"519.024.039.293.878.272.000 // (519 quintilioni)", font_size=70)
        
        
        
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
        self.play(pieces.animate.arrange_in_grid(cols=1, buff=0).center().to_edge(LEFT))
        
        calcolo_centri.next_to(centri, RIGHT)
        calcolo_angoli.next_to(angoli, RIGHT)
        calcolo_spigoli.next_to(spigoli, RIGHT)
         

        self.wait()


        self.next_section() # NEXT SECTION -------------------------------------------------------------

        
        self.play(FadeIn(calcolo_centri))

        
        self.next_section() # NEXT SECTION --------------------------------------------------------------
        
        
        self.play(FadeIn(calcolo_angoli))
         
         
        self.next_section() # NEXT SECTION -------------------------------------------------------------
         
         
        self.play(FadeIn(calcolo_spigoli))
        
        
        self.next_section() # NEXT SECTION --------------------------------------------------------------
        
        
        self.play(FadeOut(calcolo_centri), FadeOut(calcolo_angoli), FadeOut(calcolo_spigoli))
        self.play(FadeOut(pieces))
        self.play(FadeIn(totale_mosse))
        
        self.wait(2)