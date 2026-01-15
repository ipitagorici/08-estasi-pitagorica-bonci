from manim import *

class CalcoloCombinatorio(Scene):
    def construct(self):
        cube = ImageMobject("assets/imgs/rubiks-cube.png")
        self.play(FadeIn(cube))
        self.play(cube.animate.scale(.3).to_edge(UP))

        s_text = Tex(r"$12 \times$ \textsc{Spigoli}")
        a_text = Tex(r"$8 \times$ \textsc{Angoli}")
        c_text = Tex(r"$6 \times$ \textsc{Centri}")

        s_img = ImageMobject("assets/imgs/spigoli.png").scale(0.1)
        a_img = ImageMobject("assets/imgs/angoli.png").scale_to_fit_height(s_img.height)
        c_img = ImageMobject("assets/imgs/centri.png").scale_to_fit_height(s_img.height)
        
        spigoli = Group(s_text, s_img)
        angoli = Group(a_text, a_img)
        centri = Group(c_text, c_img)

        for g in [ spigoli, angoli, centri ]:
            g.arrange_in_grid(cols=1, buff=.2)

        row = Group(centri, angoli, spigoli)\
            .arrange_in_grid(rows=1)\
            .next_to(cube, DOWN, buff=.5)
        
        for g in row:
            self.play(FadeIn(g))
            
            
        self.wait()
        
        
        self.next_section()
        
        
        self.play(FadeOut(cube))
        
        self.play(row.animate.scale(0.6))
        text_fade_out = AnimationGroup(
            FadeOut(row[0][0]),
            FadeOut(row[1][0]),
            FadeOut(row[2][0])
        )
        
        self.play(row.animate.arrange_in_grid(cols=1, buff=0).center().to_edge(LEFT))        
        self.play(text_fade_out)

        
        self.wait(2)
        
        
        self.next_section()
        
        
        