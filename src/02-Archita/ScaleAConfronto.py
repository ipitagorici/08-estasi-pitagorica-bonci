from manim import *

class ScaleAConfronto(Scene):
    def construct(self):
        def highlight(table, idx, color = RED):
            self.play(Create(
                SurroundingRectangle(
                    table.get_columns()[idx], 
                    color=color
                ).set_fill(color=color, opacity=.1))
            )
        
        font_size = 100
        first_row = [
            Tex(r"\textsc{Scala \\ Pitagorica}").scale(2),
            Tex(r"$1$", font_size=font_size),
            Tex(r"$\frac{9}{8}$", font_size=font_size),
            Tex(r"$\frac{81}{64}$", font_size=font_size),
            Tex(r"$\frac{4}{3}$", font_size=font_size),
            Tex(r"$\frac{3}{2}$", font_size=font_size),
            Tex(r"$\frac{27}{16}$", font_size=font_size),
            Tex(r"$\frac{243}{128}$", font_size=font_size),
            Tex(r"$2$", font_size=font_size)
        ]
        middle_row = [
            Tex(""),
            Tex(r"\textsc{Do}", font_size=font_size),
            Tex(r"\textsc{Re}", font_size=font_size),
            Tex(r"\textsc{Mi}", font_size=font_size),
            Tex(r"\textsc{Fa}", font_size=font_size),
            Tex(r"\textsc{Sol}", font_size=font_size),
            Tex(r"\textsc{La}", font_size=font_size),
            Tex(r"\textsc{Si}", font_size=font_size),
            Tex(r"\textsc{Do}", font_size=font_size),
        ]
        last_row = [
            Tex(r"\textsc{Scala \\ Naturale}").scale(2),
            Tex(r"$1$", font_size=font_size),
            Tex(r"$\frac{9}{8}$", font_size=font_size),
            Tex(r"$\frac{5}{4}$", font_size=font_size),
            Tex(r"$\frac{4}{3}$", font_size=font_size),
            Tex(r"$\frac{3}{2}$", font_size=font_size),
            Tex(r"$\frac{5}{3}$", font_size=font_size),
            Tex(r"$\frac{15}{8}$", font_size=font_size),
            Tex(r"$2$", font_size=font_size)
        ]
        
        data = [ first_row, middle_row, last_row ]
        table = MobjectTable(data).scale_to_fit_width(self.camera.frame_width - 1)
        
        def create_frac(f1, f2):
            frac = VGroup()
            frac.add(MathTex(f1))
            frac.add(MathTex(f2))
            frac.arrange_in_grid(cols=1, cell_alignment=LEFT, buff=(0, .7))
            return frac
            
        fracs = VGroup()
        frac1 = create_frac(r"\frac{81}{64} = 1.265625", r"\frac{5}{4} = 1.25")
        frac2 = create_frac(r"\frac{27}{16} = 1.6875", r"\frac{5}{3} = 1.6666")
        frac3 = create_frac(r"\frac{243}{128} = 1.8984", r"\frac{15}{8} = 1.875")
        fracs.add(frac1, frac2, frac3).arrange_in_grid(rows=1, buff=(1, 0))
        fracs.next_to(table, DOWN, .75)
        all = VGroup(table, fracs).center()

        self.play(table.create(), run_time=3)

        idxs = [ (3, YELLOW), (6, GREEN), (7, RED) ]
        for step, idx in enumerate(idxs):
            highlight(table, idx[0], idx[1])
            self.wait()
            self.play(Write(fracs[step].set_color(idx[1])))

        
        