from manim import *

class StoriePitagoriche(Scene):
    def construct(self):
        immagini_pitagoriche = Group(
            ImageMobject("assets/imgs/storie_pitagoriche/1.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/2.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/3.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/4.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/5.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/6.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/7.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/8.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/9.jpg"),
            ImageMobject("assets/imgs/storie_pitagoriche/10.jpg"),
        )
        
        for i in range(0,len(immagini_pitagoriche)):
            if i==0:
                self.play(FadeIn(immagini_pitagoriche[i], run_time=8))
            else:
                self.play(FadeOut(immagini_pitagoriche[i-1]), FadeIn(immagini_pitagoriche[i-1]), run_time=8)
                
        
        self.wait(2)