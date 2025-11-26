from manim import *
from pythagoras_rules import rulesSet_pt1 as rulesSet, rulesSet_pt2

class RegolePT2(Scene):
    def construct(self):
        # BEGIN Previous scene setup
        title = Tex(r"\textsc{Le $\mathbb{R}$egole $\mathbb{P}$itagoriche}").scale(2)
        self.add(title.scale(.75).to_edge(UP, .75))
        rules = VGroup()
        change = False
        for rule in rulesSet.rules:
            rules.add(Tex(rule).set_color(YELLOW if change else ORANGE))
            change = not change
        rules.next_to(title, direction=DOWN, buff=3).arrange_in_grid(cols=1, cell_alignment=LEFT).scale(.95)
        source = Tex(r"\textit{" + rulesSet.source + "}").scale(.80).set_color(YELLOW).next_to(rules, DOWN).align_to(rules, RIGHT)
        self.add(rules, source)
        # END Previous scene setup

        self.play(AnimationGroup(*[Unwrite(rule) for rule in rules], Unwrite(source)))
        rules = VGroup()
        change = False
        for rule in rulesSet_pt2.rules:
            rules.add(Tex(rule, tex_environment="flushleft").set_color(YELLOW if change else ORANGE))
            change = not change
        rules.next_to(title, direction=DOWN, buff=2.15).arrange_in_grid(cols=1, cell_alignment=LEFT).scale(.95)
        source = Tex(r"\textit{" + rulesSet_pt2.source + "}").scale(.80).set_color(YELLOW).next_to(rules, DOWN, buff=1).align_to(rules, RIGHT)

        for rule in rules:
            self.play(Write(rule), run_time=.7)

        self.play(Write(source))