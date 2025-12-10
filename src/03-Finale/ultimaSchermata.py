from manim import *

class UltimaSchermata(Scene):
    def construct(self):
        frase = Text("Fly me to the moon\n" +
                    "Let me play among the stars\n" +
                    "Let me see what spring is like on\n" +
                    "A-Jupiter and Mars", font_size=30)\
            .to_edge(UR)\
            .shift(LEFT*1.3)
            

        # Load the image and stretch it to fill the entire frame
        bg = ImageMobject("src/Finale/sfondoSpazio.jpg")\
            .move_to(ORIGIN)
        bg.set_width(config.frame_width)
        bg.set_height(config.frame_height)

        self.add(bg)
        self.play(Write(frase, run_time=4))
        
        self.wait(5)