from manim import *

class Sqrt2Decimals(Scene):
    def construct(self):
        customTemplate = TexTemplate()
        customTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        sqrt2 = Tex(r"$\sqrt{2} = 1.414$").scale(3).set_color(GREEN)
        self.add(sqrt2)
        eventDate, nrPascal, birthday = "05042025", "054722792", "24082006"
        sqrt2Complete = Tex(r"$\sqrt{2} = 1.414$21356237309504880168872420969807856967187535 "
            "769480731766797379907324784621070388503875343276415727 "
            "350138462309122970249248360558507372126441214970999358 "
            rf"3141322\dots{eventDate}\dots2557999505011527820605714701095599 "
            "716059702745345968620147285174186408891986095523292304 "
            rf"844308714321450839762603\dots{nrPascal}\dots6872533965463318 "
            "088296406206152583523950547457502877599617298355752203 "
            "375318570113543746034084988471603868999706990048150305 "
            rf"4\dots{birthday}\dots4247823068492936918621580578463111596668 "
            "130130156185689872372352885092648612494977154218334204 "
            r"285686060146824720771435854874155657069677653720226\dots ", 
            tex_template=customTemplate, 
            tex_environment="center", 
            substrings_to_isolate=[r"$\sqrt{2} = 1.414$", 
                rf"\dots{eventDate}\dots", 
                rf"\dots{nrPascal}\dots", 
                rf"\dots{birthday}\dots"])
        sqrt2Complete.set_color_by_tex(r"$\sqrt{2} = 1.414$", GREEN)
        self.play(TransformMatchingTex(sqrt2, sqrt2Complete), run_time=3)
        self.wait()
        self.play(sqrt2Complete.animate.set_color_by_tex(rf"\dots{eventDate}\dots", RED_C), run_time=1)
        self.play(sqrt2Complete.animate.set_color_by_tex(rf"\dots{nrPascal}\dots", YELLOW), run_time=1)
        self.play(sqrt2Complete.animate.set_color_by_tex(rf"\dots{birthday}\dots", TEAL), run_time=1)