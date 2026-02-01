import random
from manim import *
from src.custom_mobjects import BoheldText

class PoppingWords(Scene):

    def generate_random_point_inside_screen(self, word: BoheldText):
        frame_width = config.frame_width 
        frame_height = config.frame_height
        
        while True:
            x = random.uniform(-(frame_width - word.width) / 2 + 4, (frame_width - word.width) / 2 - 4)
            y = random.uniform(-(frame_height - word.height) / 2 + 1, (frame_height - word.height) / 2 - 1)
            
            return [x, y, 0]

    def construct(self):
        words = [
            "Universi possibili", 
            "Si espandono", 
            "Si Contraggono", 
            "Ruotano come trottole", 
            "Totalmente Caotici", 
            "Omogenei", 
            "Grumosi", 
            "Agitati", 
            "Maree Cosmiche", 
            "EternitÀ", 
            "Senza vita", 
            "Tumultuoso futuro", 
            "Infinite cose", 
            "Evolva La Vita", 
            "Menti Consapevoli", 
            "Esplosione", 
            "Lamento", 
            "Non Finiscono", 
            "Dimensioni Nascoste", 
            "Universi Eterni", 
            "Buchi Neri", 
            "In Collisione", 
            "Dal Nulla", 
            "L'Unico", 
            "Universo Possibile", 
            "Molti Universi Possibili", 
            "Leggi Di Natura", 
            "Mere PossibilitÀ", 
            "Voi e Me", 
            "Qui e Ora"
        ]

        bg = ImageMobject("src/assets/imgs/sfondoSpazio.jpg")\
            .scale_to_fit_width(self.camera.frame_width)\
            .set_z_index(-2)
        self.add(bg)
        def update_bg(bg, dt):
            bg.scale(1 + 0.005 * dt)
        
        bg.add_updater(update_bg)
        self.play(bg.animate.set_opacity(.5))
        self.wait()
        for word in words:
            parola = BoheldText(word)
            parola.move_to(self.generate_random_point_inside_screen(parola))
            self.play(Write(parola), run_time=.5)
            self.wait()
            self.next_section(word)
            self.play(Unwrite(parola))
            self.wait()