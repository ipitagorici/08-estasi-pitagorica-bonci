from manim import *
from math import *

class AzelCreatoreDiMondi(Scene):
    def construct(self):
        # Letters for the 4 constants, the color will be the same for everything related to that letter
        omegaLetter = Tex(r"$\Omega$").set_color(RED)
        kLetter = Tex("k").set_color(YELLOW)
        hubbleConstantLetter = Tex("H").set_color(GREEN)
        lambdaLetter = Tex(r"$\Lambda$").set_color(BLUE)
        letters = VGroup(omegaLetter, kLetter, hubbleConstantLetter, lambdaLetter)
        
        # VGroups containing only the formulas (text) for the corresponding constant 
        # Array containing the VGroups of the various functions (text)
        omegaFunctions = [lambda x: sqrt(5) * 2**x-1, 
                          lambda x: (1-5**(-1.8*x)) * (1.1**(2.4*x-2)),
                          lambda x: sqrt(16*(x+0.1) - (x+0.1)**2 - 1.25) * (1.2**(-2*x-1)) if x>=0 and x<=15.8215 else 0,
                          lambda x: sqrt(4*x - x**2) if x >= 0 and x <= 4 else 0]
        kFunctions = [lambda x: (x-4) * ((1 - 3.5**(-x+4)) * (1.9**(1.2*x-7.8)) + 0.745),
                      lambda x: (1 - 2**(-6*x+24)) * (1.2**(1.8*x-9.2)),
                      lambda x: (1 - 2**(-2.8*x+11.2)) * (1.1**(2*x-10)),
                      lambda x: sqrt(0.867*(x-4)) if x >= 4 else 0]
        hubbleFunctions = [lambda x: sqrt(3.8*x + 12) - 4.58 if x >= -12/3.8 else 0,
                            lambda x: 0.01*x**2 + 0.1*x + 0.35,
                            lambda x: (1 - 2**(-6*x-24)) * (1.06**(1.8*(x+4)-2)) - 1.23]
        lambdaFunctions = [lambda x: (1 - 2**(2.8*x+11.2)) * (1.1**(1.8*x-5.2)) - 1.23,
                           lambda x: 0.2 * 3**(x-11.2) + 3.05,
                           lambda x: 6**(x-12.52) + 3.15,
                           lambda x: (1 - 5**(-1.8*x+15.21)) * (1.1**(2.8*x-25.66)) + 1.4]

        # Axes for the final plot
        axes = Axes((0, 18, 1), (0, 10, 1),
                    8, 4.5).shift(LEFT*0.5)
        
        omegaDrawnFunctions = VGroup(
                            axes.plot(omegaFunctions[0], x_range=[0, 4]),
                            axes.plot(omegaFunctions[1]),
                            axes.plot(omegaFunctions[2]),
                            axes.plot(omegaFunctions[3], x_range=[0, 4]))
        kDrawnFunctions = VGroup(
                            axes.plot(kFunctions[0], x_range=[4, 6]),
                            axes.plot(kFunctions[1], x_range=[4, 6]),
                            axes.plot(kFunctions[2]),
                            axes.plot(kFunctions[3], x_range=[4, 6]))
        hubbleDrawnFunctions = VGroup(
                                axes.plot(hubbleFunctions[0]),
                                axes.plot(hubbleFunctions[1]),
                                axes.plot(hubbleFunctions[2], x_range=[6, 12]))
        lambdaDrawnFunctions = VGroup(
                                axes.plot(lambdaFunctions[0]),
                                axes.plot(lambdaFunctions[1]),
                                axes.plot(lambdaFunctions[2]),
                                axes.plot(lambdaFunctions[3], x_range=[12, 18]))
        
        constantsDrawnFunctions = [ 
            omegaDrawnFunctions, 
            kDrawnFunctions, 
            hubbleDrawnFunctions, 
            lambdaDrawnFunctions
        ]
        
        # Text displayed for each drawn function
        functionsPhrases = VGroup(Tex("Close, Return to fire", font_size=30)\
                                    .next_to(omegaDrawnFunctions[3].get_end(), DOWN),
                                  Tex("Flat", font_size=30)\
                                    .next_to(kDrawnFunctions[3].get_end(), UP),
                                  Tex("Expansion", font_size=30)\
                                    .next_to(hubbleDrawnFunctions[2].get_end(), RIGHT).shift(DOWN*0.1),
                                  Tex("Accelerate", font_size=30)\
                                    .next_to(lambdaDrawnFunctions[3].get_end(), LEFT))
        
        lettersDescriptions = VGroup(Text("Parametro\ndi densità",
                                          font_size=letters[0].get_font_size()-15),
                                     Text("Curvatura",
                                          font_size=letters[1].get_font_size()-15),
                                     Text("Costante\ndi Hubble",
                                          font_size=letters[2].get_font_size()-15),
                                     Text("Costante\nCosmologica",
                                          font_size=letters[3].get_font_size()-15))\
                                              .arrange(DOWN, aligned_edge=LEFT)
                                              
        endingText = Tex("COSMOS COMPLETE")\
            .move_to(ORIGIN).shift(UL).shift(UP)\
                .set_color_by_gradient(RED, YELLOW, GREEN, BLUE)

        self.play(Create(axes))

        runtime = 0.7
        # Loop that:
        # 1) 
        # 2) 
        # 3) 
        # 4) 
        for i in range(0, len(letters)):
            self.play(Write(letters[i]))
            
            if i == 0:
                self.play(letters[i].animate.to_corner(UR))
            else:
                self.play(letters[i].animate.to_corner(UR).shift(DOWN*i*1.2))
                
            lettersDescriptions[i].next_to(letters[i]).shift(LEFT*2.5)
            self.play(letters[i].animate.shift(LEFT*2.5), GrowFromEdge(lettersDescriptions[i], RIGHT))

            end = len(constantsDrawnFunctions[i])
            runtime = 0.7
            for n in range(1, 3):
                self.play(Create(constantsDrawnFunctions[i][0]), run_time=runtime)
                for j in range(0, end-1):
                    self.play(Transform(
                        constantsDrawnFunctions[i][j], 
                        constantsDrawnFunctions[i][j + 1], 
                        replace_mobject_with_target_in_scene=True), 
                        run_time=runtime if n==1 else runtime*1.3)

            self.play(FadeToColor(
                constantsDrawnFunctions[i][end-1], letters[i].get_color()),
                Create(functionsPhrases[i]))
            
            self.play(Circumscribe(letters[i], Rectangle, color=DARK_BROWN, stroke_width=5))
        
        self.play(SpinInFromNothing(endingText))
        
        # self.wait
        self.wait(2)
        