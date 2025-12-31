from manim import *

class Approx1(Scene):
    def construct(self):
        title = Title(r"YBC 7289 — Babilonia, $\approx$ 1800-1600 a.C.")
        text = MathTex(r"\sqrt{2} \approx \frac{305470}{216000} = 1 + \frac{24}{60} + \frac{51}{60^2} + \frac{10}{60^3}", font_size=70)
        res = MathTex(r"\frac{305470}{216000} = \mathbf{1.41421}", r"\overline{296}", font_size=70, substrings_to_isolate=["1.41421"]).next_to(text, DOWN, 1)
        res.set_color_by_tex(r"1.41421", GREEN)
        body = VGroup(text, res).center()
        self.play(Write(title))
        self.play(Write(text))
        self.play(Write(res))
    
class Approx2(Scene):
    def construct(self):
        title = Title(r"Sulbasutras — India, $\approx$ 800-200 a.C.")
        text = MathTex(r"\sqrt{2}", r"\approx \frac{577}{408} = 1 + \frac{1}{3} + \frac{1}{3 \times 4} + \frac{1}{3 \times 4 \times 34}", font_size=70)
        res = MathTex(r"\frac{577}{408} = 1.41421", r"\overline{56862745098039}", font_size=70, substrings_to_isolate=["1.41421"]).next_to(text, DOWN, 1)
        res.set_color_by_tex("1.41421", GREEN)
        body = VGroup(text, res).center()
        self.play(Write(title))
        self.play(Write(text))
        self.play(Write(res))

class Approx3(Scene):
    def construct(self):
        title = Title(r"Metodo delle tangenti — Newton")
        text = MathTex(r"\begin{cases} a_0 = 1 \\ a_{n+1} = \frac12\left(a_n + \dfrac{2}{a_n}\right)=\frac{a_n}{2}+\frac{1}{a_n} \end{cases}", font_size=50)
        res = MathTex(r"a_1 = \frac{3}{2} = \mathbf{1}.5", 
            r"a_2 = \frac{17}{12} = \mathbf{1.41}6 \dots", 
            r"a_3 = \frac{577}{408} = \mathbf{1.4142}15 \dots", 
            font_size=40).next_to(text, DOWN, 1.5).arrange_in_grid(cols=1, cell_alignment=LEFT, buff=(0,.25)).to_edge(LEFT)
        
        body = VGroup(text, res).next_to(title, DOWN, .8)
        text.center().shift(UP * 1.3)
        self.play(Write(title))
        self.play(Write(text))
        self.wait()
        for step in res:
            self.play(Write(step), run_time=.8)
        