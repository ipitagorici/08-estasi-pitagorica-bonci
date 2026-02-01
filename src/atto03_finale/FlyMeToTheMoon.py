from manim import *

class FlyMeToTheMoon(Scene):
    def construct(self):
        frase = Paragraph("Fly me to the moon\n" +
                    "Let me play among the stars\n" +
                    "And let me see what spring is like\n" +
                    "On a-Jupiter and Mars", line_spacing=MED_LARGE_BUFF, alignment="right")\
            .to_edge(UR, buff=MED_LARGE_BUFF)\
            .scale(.75)

        # Load the image and stretch it to fill the entire frame
        bg = ImageMobject("src/assets/imgs/upscaled-sfondoSpazio(flymetothemoon).jpg")\
            .move_to(ORIGIN)

        self.add(bg)
        self.wait(2)
        self.play(bg.animate.set_opacity(.3), run_time=4)
        self.wait()
        self.play(Write(frase, run_time=10))
        
        self.wait(5)