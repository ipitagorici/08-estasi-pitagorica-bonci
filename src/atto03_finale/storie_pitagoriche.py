from manim import *
from src.custom_mobjects import Tetraktys

class StoriePitagoriche(Scene):
    def create_glow(self, vmobject: VMobject, rad=1, col=YELLOW):
        glow_group = VGroup()
        for idx in range(100):
            new_obj = vmobject.copy()
            new_obj\
                .scale(1 + (1.002 ** (idx**2))/400)\
                .set_stroke(opacity = 0)\
                .move_to(vmobject)
            if vmobject.get_color() is not None:
                new_obj\
                    .set_color(col)\
                    .set_opacity(0.2 - idx/300)
            if vmobject.get_stroke_color() is not None:
                new_obj\
                    .set_stroke(color = col, opacity = 0.2 - idx/300)
            glow_group.add(new_obj)
        return glow_group

    def construct(self):
        N_IMAGES = 20
        TOT_SEC = 90
        TETRAKTYS_TIME = 6
        CAROUSEL_QUANTUM = (TOT_SEC - TETRAKTYS_TIME) / N_IMAGES
        immagini_pitagoriche = Group()
        for img_idx in range(1, N_IMAGES + 1):
            immagini_pitagoriche.add(
                ImageMobject(f"src/assets/imgs/storie_pitagoriche/{img_idx}.jpg")\
                    .scale_to_fit_width(self.camera.frame_width - 4)
            )

        tetraktys = Tetraktys()
        dots, border = tetraktys.get_dots(), tetraktys.get_triangle()
        glows = VGroup()
        for row in dots:
            for circle in row:
                glows.add(self.create_glow(vmobject=circle, col=circle.get_color()))

        self.play(FadeIn(tetraktys), FadeIn(glows), run_time=TETRAKTYS_TIME/3)
        self.wait(TETRAKTYS_TIME/3)
        self.play(FadeOut(*self.mobjects), run_time=TETRAKTYS_TIME/3)

        for img in immagini_pitagoriche:
            self.play(FadeIn(img), run_time=CAROUSEL_QUANTUM/3)
            self.wait(CAROUSEL_QUANTUM/3)
            self.play(FadeOut(img), run_time=CAROUSEL_QUANTUM/3)