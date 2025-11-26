from manim import *

class Sqrt2DecimalsNikolas(Scene):
    def construct(self):

        def highlight(table, idx, change = False):
            self.play(
                Create(SurroundingRectangle(
                    table.get_columns()[idx], 
                    color=YELLOW if not change else TEAL
                ))
            )
        
        customTemplate = TexTemplate()
        customTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        nameCode = [ 13, 8, 10, 14, 11, 0, 18 ]
        encodedName = "".join([str(code) for code in nameCode])
        sqrt2Complete = Tex(r"\dots 325142566908780256366504399364323429587433403882 "
            " 287962848285758752341071805593570366530436653045304 "
            " 764947836564078696980855454208174012078501207850785 "
            " 810411215480461614178499741653525049361304936133613 "
            f" 98027959803490{encodedName}5861769399585839958585858 "
            " 037058606868404951942318169717076155671015567106710 "
            " 828048336531921493320922072547282506580450658045804 "
            r" 244933460316227830824270117378514539904453990399 \dots ",
            tex_template=customTemplate, 
            tex_environment="center",
            substrings_to_isolate=[encodedName])
        # 
        alphabet = [ chr(idx).capitalize() for idx in range(97, 97 + 26) ]
        alphabetTable = Table([
            [*alphabet], 
            [*[str(idx) for idx, _ in enumerate(alphabet)]]
        ]).scale_to_fit_width(self.camera.frame_width).scale(.97).to_edge(UP)
        # hLines = alphabetTable.get_horizontal_lines().set_opacity(0)
        vLines = alphabetTable.get_vertical_lines().set_opacity(0)
        name = Tex(r"\textsc{Nikolas}").scale(2).next_to(alphabetTable, DOWN)
        sqrt2Complete.next_to(name, DOWN, buff=.5)
        self.play(Write(sqrt2Complete))
        self.wait(.75)
        self.play(Write(name))
        self.play(Circumscribe(name))
        self.play(alphabetTable.create(), run_time=3)
        self.wait()
        for code in nameCode: 
            highlight(alphabetTable, code)
        self.wait()
        self.play(sqrt2Complete.animate.set_color_by_tex(encodedName, YELLOW))