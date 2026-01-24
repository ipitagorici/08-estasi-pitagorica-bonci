from manim import *
from src.custom_mobjects import BoheldText

class PerfectNumbers(ZoomedScene):
    def construct(self):
        numbers = [BoheldText("6").to_edge(UP),
                   BoheldText("28"),
                   BoheldText("496"),
                   BoheldText("8128", font_size=70),
                   BoheldText("33550336", font_size=70),
                   BoheldText("8589869056", font_size=70),
                   BoheldText("137438691328", font_size=100),
                   BoheldText("2305843008139952128", font_size=100),
                   BoheldText("2658455991569831744654692615953842176", font_size=100),
                   BoheldText("191561942608236107294793378084303638130997321548169216", font_size=150)
        ]
        
        for i in range(0, len(numbers)):
            if i % 3 !=  0:
                if i != 0:
                    self.play(Write(numbers[i]))
                else:
                    numbers[i].next_to(numbers[i-1], DOWN)
                    self.play(Write(numbers[i]))
            else:
                self.camera.width *= 2