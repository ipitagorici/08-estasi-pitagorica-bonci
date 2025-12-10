from manim import *

class T3(Scene):
    def construct(self):
        title = Title(r"\textsc{Ringraziamenti}", font_size=90)

        def get_par(title: str, *argv: tuple[str]):
            return VGroup(
                Tex(r"\textsc{" + title + "}").scale(1.5).set_color(YELLOW),
                *[Tex(p) for p in argv]
            ).arrange_in_grid(cols=1)

        all = VGroup(
            title,
            get_par("Relatori", 
                    "prof. Emanuele Parini",
                    "Nikolas Panterini",
                    "Luca Brasini"),
            get_par("Pitagorici", 
                "Marco Caprili",
                "Nicolas Moltrasio",
                "Nicola Fersurella"),
            get_par("Accompagnamento Musicale", 
                    "prof. Francesco Filomena"),
            get_par("Beatbox", 
                    "Azel"),
            get_par("Grafici",
                    "Marco Cottignoli",
                    "Michele De Paola",
                    "Edoardo Zanzani",
                    "Nicholas Magi",
                    "Elettra Ventura"
            ),
            get_par("Riprese Video",
                    "Daniele Broccoli"
            )
        ).arrange_in_grid(cols=1, buff=(0, 3)).shift(DOWN * 22)

        for i in range(0, 1000):
            self.play(all.animate.shift(UP * .1))
            