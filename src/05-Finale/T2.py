from manim import *

class T2(Scene):
    def construct(self):
        def get_path(filename):
            loghi_path = "../assets/loghi/"
            return loghi_path + filename
        
        patrocinio = Group()
        patrocinio_logos = Group()
        patrocinio_text = Title(r"\textsc{con il patrocinio di}")
        
        er = Group(ImageMobject(get_path("rer.png")).scale(.5))
        # er.add(Rectangle(WHITE, er.height, er.width + 1).set_fill(WHITE, 1).set_z_index(-1))

        longiano = Group(ImageMobject(get_path("longiano.png")))
        longiano.add(Tex(r"\textsc{Comune di\\Longiano}").scale(3.5).next_to(longiano, RIGHT))

        first_row = Group(er, longiano)
        for obj in first_row:
            obj.scale_to_fit_height(first_row.height)

        patrocinio_logos.add(longiano, er).arrange_in_grid(cols=1, buff=(1.5, 2.5)).scale_to_fit_width(self.camera.frame_width - 2).center()
        patrocinio.add(patrocinio_logos, patrocinio_text).center()

        self.play(Write(patrocinio_text))
        for obj in patrocinio_logos:
            self.play(FadeIn(obj))