from manim import *
from src.custom_mobjects import BoheldText, Tetraktys

class Intro(Scene):
    
    def construct(self):
        fg_color = ManimColor("#e4c8c8")
        shadow_color = ManimColor("#82001e")

        title_fg = BoheldText("Estasi Pitagorica", color=fg_color)\
            .scale(1.5)
        title_shadow = title_fg.get_shadow(shadow_color)
        
        title = VGroup(title_fg, title_shadow)

        subtitle_fg = BoheldText("L'eterno spettacolo della matematica", color=fg_color)\
            .next_to(title, DOWN)\
            .scale_to_fit_width(self.camera.frame_width - 2.0)

        subtitle_shadow = subtitle_fg.get_shadow(shadow_color)
        
        subtitle = VGroup(subtitle_fg, subtitle_shadow)

        tetraktys = Tetraktys()

        t_triangle = tetraktys.get_triangle()
        n_triangles = 30
        triangles = VGroup()
        
        last_height = -1
        triangles.add(t_triangle.scale_to_fit_height(self.camera.frame_height + 20).center())
        for i in range(1, n_triangles):
            prev = triangles[i - 1]
            new_height = prev.height - .7 * (i * .1)
            if (new_height < 0):
                break
            triangles.add(t_triangle.copy()\
                        .scale_to_fit_height(new_height)\
                        .center())
        
        triangles.remove(triangles[-1])
        last_height = triangles[-1].height
        triangles.remove(triangles[-1])
        
        self.play(AnimationGroup(*[Broadcast(t, lag_ratio=.1, initial_opacity=0, final_opacity=1, remover=False, n_mobs=20) for t in triangles], lag_ratio=.2))
        self.play(FadeIn(tetraktys\
                        .scale_to_fit_height(last_height)\
                        .center()
        ))
        # self.mobjects -> [Group, Tetraktys] 

        for t in triangles:
            self.add(t)

        print(self.mobjects)
        # self.mobjects -> [Group, Tetraktys, Polygon, Polygon, Polygon, ...]
        
        self.mobjects.pop(0)
        print(self.mobjects)
        # self.mobjects -> [Tetraktys, Polygon, Polygon, Polygon, ...]

        self.mobjects.reverse()
        print(self.mobjects)
        # self.mobjects -> [Polygon, Polygon, Polygon, ..., Tetraktys]

        to_play = []
        while (len(self.mobjects) > 1):
            n = len(self.mobjects) - 1
            for i in range(n - 1, -1, -1):
                current = self.mobjects[i]
                prev = self.mobjects[i - 1]
                to_play.append(current.animate\
                            .scale_to_fit_height(prev.height)\
                            .center())
            to_play.append(FadeOut(self.mobjects[0]))
            self.mobjects.remove(self.mobjects[0])

        self.play(AnimationGroup(to_play, lag_ratio=.05))
        self.wait()
        self.play(Wiggle(tetraktys, scale_value=1.3))
        self.play(FadeOut(tetraktys))
        self.wait(3)
        self.play(FadeIn(title), run_time=3)
        self.wait()
        self.play(Write(subtitle_fg), Write(subtitle_shadow), run_time=3)

        pascal_logo = ImageMobject(r"src/assets/imgs/loghi/pascal-white-logo-no-bg.png")
        times = MathTex(r"\times")
        pitagorici_logo = ImageMobject(r"src/assets/imgs/loghi/pitagorici-logo.png")
        logo_header = Tex("Un'iniziativa di:")
        logo_row = Group(pascal_logo, times, pitagorici_logo)
        logos = Group(logo_row, logo_header)
        pitagorici_logo.scale_to_fit_width(pascal_logo.width)
        times.next_to(pitagorici_logo, RIGHT)
        pascal_logo.next_to(times, RIGHT)
        logo_row.center()
        logo_header\
            .scale(.8)\
            .next_to(logo_row, UP, buff=MED_LARGE_BUFF)
        logos.center()

        self.wait(5)
        self.play(FadeOut(*self.mobjects))

        self.play(Write(logo_header))
        self.play(FadeIn(logo_row))

        self.wait(5)
        self.play(FadeOut(*self.mobjects))