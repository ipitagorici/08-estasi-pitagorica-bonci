from manim import *

class BigNumber(Scene):
    def construct(self):
        bigNumber = Tex("43.252.003.274.489.856.000", font_size=100)\
            .shift(UP*2)

        self.play(Write(bigNumber))

class UniverseAge(Scene):
    def construct(self):
        universeAge = Tex("13.7 miliardi di anni", font_size=100)\
            .shift(DOWN*2)

        self.play(Write(universeAge))

class Compare(Scene):
    def construct(self):
        bigNumber = Tex(r"43.252.003.274.489.856.000", font_size=100).to_edge(UP)
        universeAge = Tex(r"13.7 miliardi di anni", font_size=100).to_edge(DOWN)

        ageTransformationExplanation = Tex(r"13.Mi = 365 x 24 x60 x 60 x 13.700.000.000 =", font_size=100).to_edge(DOWN)

        numberScientific = Tex(r"4,32 x 10$^{19}$", font_size=100)
        ageScientific = Tex(r"4.32 x 10$^{17}$", font_size=100)

        fraction = Tex(r"$\frac{4.32 x 10^{19}}{4.32 x 10^{17}}$", font_size=200)
        fractionResult = Tex(r"100", font_size=200).next_to(fraction, RIGHT)


        self.play(FadeIn(bigNumber))
        self.play(FadeIn(universeAge))

        self.play(Transform(bigNumber, numberScientific, replace_mobject_with_target_in_scene=True))
        
        self.play(FadeOut(universeAge), FadeIn(ageTransformationExplanation))
        self.play(Transform(ageTransformationExplanation, ageScientific, replace_mobject_with_target_in_scene=True))

        self.play(FadeOut(numberScientific), FadeOut(ageScientific), GrowFromCenter(fraction))
        
        self.play(fraction.animate.shift(LEFT))
        self.play(Write(fractionResult))


        self.wait(2)