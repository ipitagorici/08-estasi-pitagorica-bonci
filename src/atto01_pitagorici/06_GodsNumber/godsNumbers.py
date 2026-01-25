from manim import *
from src.custom_mobjects import BoheldText

class GodsNumbers(Scene):
    def construct(self):
        def cell_content(img_path, title_text, caption_text):
            img = ImageMobject(img_path).scale(.7)
            title = BoheldText(title_text)
            caption = Tex(caption_text)
            return Group(img, title, caption).arrange_in_grid(cols=1)
        
        cube2 = "src/assets/imgs/rubiks-cube2x2.png"
        title2 = "2 x 2"
        caption2 = r"\textsc{11 mosse}"
        cell2 = cell_content(cube2, title2, caption2)

        cube3 = "src/assets/imgs/rubiks-cube3x3.png"
        title3 = "3 x 3"
        caption3 = r"\textsc{20 mosse}"
        cell3 = cell_content(cube3, title3, caption3)
        
        cube4 = "src/assets/imgs/rubiks-cube4x4.png"
        title4 = "4 x 4"
        caption4 = r"\textsc{??? mosse}"
        cell4 = cell_content(cube4, title4, caption4)

        target_height = min([cell2[0].height, cell3[0].height, cell4[0].height])
        for cube in [ cell2, cell3, cell4 ]:
            cube.scale_to_fit_height(target_height)

        row = Group(cell2, cell4.scale(2), cell3).arrange_in_grid(rows=1, buff=LARGE_BUFF).center()
        self.play(FadeIn(row[0]))
        self.play(FadeIn(row[2]))
        self.play(GrowFromCenter(row[1]))