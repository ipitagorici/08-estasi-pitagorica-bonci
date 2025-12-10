from manim import *

class T1(Scene):
    def construct(self):
        def get_path(filename):
            loghi_path = "../assets/loghi/"
            return loghi_path + filename
        
        collab = Group()
        collab_logos = Group()
        collab_text = Title(r"\textsc{con la collaborazione di}")
        
        petrella = Group(ImageMobject(get_path("petrella.jpg")).scale(.75))
        petrella.add(Rectangle(WHITE, petrella.height, petrella.width + 1).set_fill(WHITE, 1).set_z_index(-1))

        romagna_iniziative = Group(ImageMobject(get_path("romagna-iniziative.png")))
        romagna_iniziative.add(Rectangle(WHITE, romagna_iniziative.height + 1, romagna_iniziative.width + 1).set_fill(WHITE, 1).set_z_index(-1))

        orogel = Group(ImageMobject(get_path("orogel.png")).scale(.5))
        fam = Group(ImageMobject(get_path("famila.png")))
        credit = Group(ImageMobject(get_path("credit.png")))

        centro_usato = Group(ImageMobject(get_path("centro-usato.png")).scale(2))
        centro_usato.add(Tex("CENTRO USATO S.R.L. - www.centrousato.net").next_to(centro_usato, DOWN))
        
        first_row = Group(fam, credit, centro_usato, orogel).arrange()
        for obj in first_row:
            obj.scale_to_fit_height(first_row.height)
        
        second_row = Group(romagna_iniziative, petrella).arrange().next_to(first_row, UP)
        for obj in second_row:
            obj.scale_to_fit_height(second_row.height)

        collab_logos.add(romagna_iniziative, petrella, orogel, centro_usato, credit, fam).arrange_in_grid(cols=3, row=2, buff=(0, 1)).scale_to_fit_width(self.camera.frame_width - 2).center()
        collab.add(collab_logos, collab_text).center()

        self.play(Write(collab_text))
        for obj in collab_logos:
            self.play(FadeIn(obj))