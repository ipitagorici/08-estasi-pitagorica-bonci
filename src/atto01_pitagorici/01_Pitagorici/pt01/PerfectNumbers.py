from manim import *
from src.custom_mobjects import BoheldText

class PerfectNumbers(MovingCameraScene):
    def construct(self):
        pitagorici=Tex(r"\textsc{Pitagorici}")
        eulero=Tex(r"\textsc{Eulero, 1772}")
        numbers = VGroup(
            VGroup(BoheldText("6", font_size=70), pitagorici.copy()).arrange_in_grid(rows=2),
            VGroup(BoheldText("28", font_size=70), pitagorici.copy()).arrange_in_grid(rows=2),
            VGroup(BoheldText("496", font_size=70), pitagorici.copy()).arrange_in_grid(rows=2),
            VGroup(BoheldText("8.128", font_size=70), pitagorici.copy()).arrange_in_grid(rows=2),
            BoheldText("33.550.336", font_size=100),
            BoheldText("8.589.869.056", font_size=100),
            BoheldText("137.438.691.328", font_size=125),
            BoheldText("2.305.843.008.139.952.128", font_size=125),
            VGroup(BoheldText("2.658.455.991.569.831.744.654.692.615.953.842.176", font_size=125), eulero.copy().scale(3.25)).arrange_in_grid(rows=2, buff=LARGE_BUFF),
            BoheldText("191.561.942.608.236.107.294.793.378.084.303.638.130.997.321.548.169.216", font_size=150)
        )

        # Initial setup: Put the first number at the center
        current_number = numbers[0]
        self.play(Write(current_number))

        # We keep track of the numbers already on screen
        displayed_numbers = VGroup(current_number)

        for i in range(1, len(numbers)):
            # 1. Transition: Move old numbers up and scale them down
            # Simultaneously zoom the camera out
            self.play(
                displayed_numbers.animate.shift(UP * 2.5).scale(0.7),
                self.camera.frame.animate.scale(1.2),
                run_time=1
            )

            # 2. Add the next number at the center of the NEW frame
            next_num = numbers[i]
            # Ensure it appears at the center of the camera's current view
            next_num.move_to(self.camera.frame.get_center())
            
            self.play(FadeIn(next_num, shift=UP * 0.5))

            # Add the new number to our group so it moves in the next iteration
            displayed_numbers.add(next_num)

        self.wait(2)