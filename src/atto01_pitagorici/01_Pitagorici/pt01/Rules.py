from manim import *
from pythagoras_rules import rulesSet_pt1, rulesSet_pt2
from src.custom_mobjects import BoheldText

class Rules(Scene):
    def construct(self):
        
        self.next_section("pt1")
        title = BoheldText(r"Le Regole Pitagoriche")\
            .scale_to_fit_width(self.camera.frame_width - 2)
        
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate\
                .scale(.75)\
                .to_edge(UP, .75))
        
        rules = VGroup()
        change = False
        for rule in rulesSet_pt1.rules:
            rules.add(Paragraph(rule, alignment="left").set_color(YELLOW if change else ORANGE))
            change = not change
        
        rules.arrange_in_grid(cols=1, cell_alignment=LEFT, buff=MED_LARGE_BUFF)\
            .scale_to_fit_width(self.camera.frame_width - 5)\
            .center()

        source = Tex(r"\textit{" + rulesSet_pt1.source + "}")\
            .scale(.80)\
            .set_color(YELLOW)\
            .to_corner(DR, MED_LARGE_BUFF)
        
        for rule in rules:
            self.play(Write(rule), run_time=.7)

        self.play(Write(source))

        self.wait()
        self.next_section("pt2")

        self.play(Uncreate(rules))
        self.play(Uncreate(source))

        rules = VGroup()
        for rule in rulesSet_pt2.rules:
            rules.add(Paragraph(rule, alignment="left").set_color(YELLOW if change else ORANGE))
            change = not change
        
        rules.arrange_in_grid(cols=1, cell_alignment=LEFT, buff=MED_LARGE_BUFF)\
            .scale_to_fit_width(self.camera.frame_width - 5)\
            .center()

        source = Tex(r"\textit{" + rulesSet_pt2.source + "}")\
            .scale(.80)\
            .set_color(YELLOW)\
            .to_corner(DR, MED_LARGE_BUFF)
        
        for rule in rules:
            self.play(Write(rule), run_time=.7)

        self.play(Write(source))
