from manim import *

class Istogram(Scene):
    def construct(self):
        # strategus = [Tex("Στρατεγός", font_size=80), Tex("Strategos", font_size=100)]
        # strategusText = Text(strategus[0].get_text() + " " + strategus[1].get_tex_string(), color=BLUE, font_size=40).to_corner(UL)
        
        graph = BarChart((29000, 30000, 1200, 3000),
                         ("", "", "", ""),
                         (0, 35000, 5000),
                         6, 5,
                         ("#ee6f55", "#e6f542", "#ee6f55", "#e6f542"))

        text = [MarkupText(f'<span fgcolor="{RED_C}">Rosso</span> = Atene\n<span fgcolor="{YELLOW}">Giallo</span> = Taranto', font_size=40),
                Text("Fanti", font_size=40),
                Text("Cavalieri", font_size=40)]
        text[0].to_corner(UR)
        text[1].next_to(graph, DOWN).shift(LEFT)
        text[2].next_to(graph, DOWN).shift(RIGHT*2)

        # self.play(Write(strategus[0]))
        # self.wait(1)
        # self.play(LaggedStart(strategus[0].animate.shift(UP), Write(strategus[1]), lag_ratio=0.5))
        # self.wait(2)
        # self.play(FadeOut(strategus[0], run_time=0.3), FadeOut(strategus[1], run_time=0.3))
        # self.play(Write(strategusText))
        self.play(DrawBorderThenFill(graph.axes))
        self.play(Write(text[0]))
        self.play(Write(text[1]), Write(text[2]))
        self.wait(3)
        self.play(GrowFromEdge(graph.bars[0], edge=DOWN), GrowFromEdge(graph.bars[2], edge=DOWN))
        self.wait()
        self.play(GrowFromEdge(graph.bars[1], edge=DOWN), GrowFromEdge(graph.bars[3], edge=DOWN))
        self.play(Write(graph.get_bar_labels(font_size=30)))