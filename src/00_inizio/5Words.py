from manim import *
from src.custom_mobjects import BoheldText

class FiveWords(Scene):
    def construct(self):
        words = [
            ("Emozione", UL, DR),
            ("Matematica", UR, DL),
            ("Cosmo", DR, UL),
            ("Bellezza", DL, UR),
        ]

        caosDisplay = BoheldText("caos").scale(2)
        lines = VGroup()
        for word, pos, opp in words:
            wordDisplay = Tex(fr"\textsc{{{word}}}")
            wordDisplay.to_corner(pos, buff=LARGE_BUFF)
            line = Line(
                start=wordDisplay.get_corner(opp), 
                end=caosDisplay.get_corner(pos),
                buff=MED_SMALL_BUFF
            ).set_color(ManimColor("#82001e")).set_opacity(.5)
            self.play(FadeIn(wordDisplay, shift=pos))
            self.play(Indicate(wordDisplay))
            lines.add(line)

        self.play(Create(lines))
        self.play(GrowFromCenter(caosDisplay))