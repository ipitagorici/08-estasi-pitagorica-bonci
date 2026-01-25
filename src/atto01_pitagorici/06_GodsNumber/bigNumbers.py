from manim import *
from src.custom_mobjects import BoheldText

SCREEN_WIDTH_OFFSET = 3

class BigNumbers(Scene):
    def construct(self):
        self.next_section("BigNumber")
        bigNumber = BoheldText("43.252.003.274.489.856.000")\
            .scale_to_fit_width(self.camera.frame_width - SCREEN_WIDTH_OFFSET)
        subtitle = Tex(r"\textsc{Possibili configurazioni}").next_to(bigNumber, DOWN)
        
        VGroup(bigNumber, subtitle).center()
        self.play(Write(bigNumber))
        self.play(Write(subtitle))
        
        self.next_section("UniverseAge")
        
        self.play(FadeOut(*self.mobjects))
        
        universeAge = BoheldText("13.7 miliardi di anni")\
            .scale_to_fit_width(self.camera.frame_width - SCREEN_WIDTH_OFFSET)
        subtitle = Tex(r"\textsc{Età dell'universo}").next_to(universeAge, DOWN)

        VGroup(universeAge, subtitle).center()
        self.play(Write(universeAge))
        self.play(Write(subtitle))

        self.next_section("Comparison")
        self.play(FadeOut(subtitle))
        
        scientificBigNumber = MathTex(r"4.32 \times 10^{19}").set_color(YELLOW)
        scientificUniverseAge = MathTex(r"4.32 \times 10^{17}").set_color(GREEN)
        
        self.play(universeAge.animate\
                .scale(.9)\
                .shift(UP * .5))
        ageTransformationExplanation = MathTex(r"= 365 \times 24 \times 60 \times 60 \times 13.700.000.000 =")\
            .scale_to_fit_width(universeAge.width - 1)\
            .next_to(universeAge, DOWN, MED_LARGE_BUFF)
        self.play(Write(ageTransformationExplanation))
        self.play(Write(scientificUniverseAge.copy()\
                    .scale(2)\
                    .next_to(ageTransformationExplanation, DOWN, MED_LARGE_BUFF)))
        self.play(Circumscribe(self.mobjects[-1], color=ORANGE))

        self.play(FadeOut(*self.mobjects))
        self.play(Write(bigNumber))
        self.play(bigNumber.animate\
                .scale(.9)\
                .shift(UP * .5))
        scientificBigNumberExplanation = MathTex(r"= 4.32 \times 10^{19} = ")\
            .scale_to_fit_width(ageTransformationExplanation.width - 6)\
            .next_to(bigNumber, DOWN, MED_LARGE_BUFF)
        self.play(Write(scientificBigNumberExplanation))
        scientificBigNumberNormalized = MathTex(r"4.32 \times 10^{17} \times 10^2", substrings_to_isolate=[r"10^2"])\
            .scale_to_fit_width(bigNumber.width - 1)\
            .next_to(scientificBigNumberExplanation, DOWN, MED_LARGE_BUFF)\
            .set_color(GREEN)\
            .set_color_by_tex(r"10^2", RED)
        self.play(Write(scientificBigNumberNormalized))
        self.play(Circumscribe(scientificBigNumberNormalized, color=ORANGE))
        
        self.play(FadeOut(*self.mobjects))

        initialFraction = MathTex(r"\frac{4.32 \times 10^{17} \times 10^2}{4.32 \times 10^{17}}")
        initialFraction[0][0:9].set_color(GREEN)
        initialFraction[0][10:13].set_color(RED)
        initialFraction[0][14:].set_color(GREEN)
        equalsToResult = MathTex(r"= 10^2 = 100", substrings_to_isolate=[r"10^2", "100"])\
                .set_color_by_tex("10^2", RED)\
                .set_color_by_tex("100", RED)
        
        self.play(Write(initialFraction))
        self.play(initialFraction.animate.shift(LEFT))
        equalsToResult.next_to(initialFraction, RIGHT)
        self.play(Write(equalsToResult))

