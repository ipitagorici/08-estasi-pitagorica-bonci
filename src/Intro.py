from manim import *
from random import randint, random
import cv2

class Intro(Scene):
    def construct(self):
        cap = cv2.VideoCapture("src/assets/SLOWStelleOrbitanti.mp4")
        flag = True
        frame_imgs = []

        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                frame_img.fade(.4).set_z_index(-1).center().scale_to_fit_width(self.camera.frame_width)
                frame_imgs.append(frame_img)
        cap.release()

        for frame_img in frame_imgs:
            self.add(frame_img)
            self.wait(0.08)
            self.remove(frame_img)
        
        self.wait(4)
        
        title = Tex(r"$\mathbb{N}$\textsc{otte }$\mathbb{P}$\textsc{itagorica}").scale(2.5).set_color(YELLOW).set_z_index(1)
        title_shadow = title.copy().shift(DR * .05).set_color(RED).set_opacity(.7)
        subtitle = Tex(r"\textsc{l'eterno spettacolo \\ della Matematica}").scale(1.4).next_to(title, DOWN, .5).set_color(YELLOW).set_z_index(1)
        subtitle_shadow = subtitle.copy().shift(DR * .05).set_color(RED).set_opacity(.7)
        logo = ImageMobject("src/assets/logo_BP_CLEAN.png").scale(.25).next_to(title, UP, .3).set_color(WHITE)
        text = Group(title, subtitle, title_shadow, subtitle_shadow, logo).center()

        background = ImageMobject("src/assets/background.png")
        background.scale_to_fit_width(self.camera.frame_width).set_z_index(-3).set_opacity(.5)
        castle = ImageMobject("src/assets/castello-longiano.png").set_z_index(0).scale_to_fit_width(self.camera.frame_width).to_edge(DOWN, -1)
        pythagoras = ImageMobject("src/assets/pythagoras_nobg.png").set_z_index(-1).scale(.85).shift(UP * 1.5 + RIGHT * 3.5)
        self.play(FadeIn(background), FadeIn(castle), run_time=5)
        self.wait(3)
        self.play(FadeIn(title), FadeIn(title_shadow), FadeIn(logo), run_time=6)
        self.play(Write(subtitle), Write(subtitle_shadow), run_time=2)
        self.wait(2)
        self.play(FadeIn(pythagoras), run_time=7)
        self.wait(10)
        self.play(FadeOut(pythagoras), FadeOut(background), run_time=1)
        self.play(FadeOut(*self.mobjects), run_time=2)