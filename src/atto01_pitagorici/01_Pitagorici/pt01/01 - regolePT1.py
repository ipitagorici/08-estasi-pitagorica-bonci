from manim import *
from pythagoras_rules import rulesSet_pt1 as rulesSet

class RegolePT1(Scene):
    def construct(self):
        title = Tex(r"\textsc{Le $\mathbb{R}$egole $\mathbb{P}$itagoriche}").scale(2)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.scale(.75).to_edge(UP, .75))
        rules = VGroup()
        change = False
        for rule in rulesSet.rules:
            rules.add(Tex(rule).set_color(YELLOW if change else ORANGE))
            change = not change
        
        rules.next_to(title, direction=DOWN, buff=3).arrange_in_grid(cols=1, cell_alignment=LEFT).scale(.95)
        source = Tex(r"\textit{" + rulesSet.source + "}").scale(.80).set_color(YELLOW).next_to(rules, DOWN).align_to(rules, RIGHT)
        
        for rule in rules:
            self.play(Write(rule), run_time=.7)

        self.play(Write(source))