from manim import *
import random

def generate_random_point_inside_screen():
    frame_width = config.frame_width 
    frame_height = config.frame_height
    
    while True:
        # Generate random point within screen boundaries (with 3-unit padding)
        x = random.uniform(-frame_width / 2 + 4, frame_width / 2 - 4)
        y = random.uniform(-frame_height / 2 + 1, frame_height / 2 - 1)
        
        # Check if point is inside the 2x2 square centered at (0,0)
        if abs(x) <= 1.5 and abs(y) <= 1.5:
            # Point is inside the 2x2 square, so continue loop to regenerate
            continue
        # Point is outside the 2x2 square, return it
        return [x, y, 0]


class Parola1(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Universi Possibili", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))

        
class Parola2(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Si Espandono", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola3(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Si Contraggono", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola4(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Ruotano come trottole", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))

class Parola5(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Totalmente Caotici", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))



class Parola6(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Omogenei", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola7(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Grumosi", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola8(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Agitati", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola9(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Maree Cosmiche", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola10(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Eternità", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola11(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Senza vita", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola12(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Tumultuoso futuro", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola13(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Infinite cose", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola14(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Evolva La Vita", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola15(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Menti Consapevoli", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola16(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Esplosione", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola17(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Lamento", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola18(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Non Finiscono", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola19(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Dimensioni Nascoste", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola20(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Universi Eterni", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola21(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Buchi Neri", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola22(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("In Collisione", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola23(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Dal Nulla", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola24(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("L'Unico", color=YELLOW, font_size=90) 
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola25(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Universo Possibile", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola26(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Molti Universi Possibili", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola27(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Leggi Di Natura", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen()) 
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola28(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Mere Possibilità", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola29(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Voi e Me", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))


class Parola30(Scene):
    def construct(self):
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        bg.scale_to_fit_height(config.frame_height)
        bg.move_to(ORIGIN)
        self.add(bg)

        parola = Tex("Qui e Ora", color=YELLOW, font_size=90)
        parola.move_to(generate_random_point_inside_screen())
        self.add(parola)
        self.play(FadeIn(parola, run_time=2))