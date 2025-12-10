from manim import *

class TempioPaestumFourier(Scene):
    def construct(self):
        def fourier_series(x, steps):
            sum_terms = 1 / 2
            for n in range(steps, 0, -1):
                if (n % 2) == 0:
                    continue
                sum_terms += -(2 / (n * PI)) * np.sin(n * x)

            return sum_terms
        axes = Axes(
            x_range=[-7/2*PI, 7/2*PI, PI/8], 
            y_range=[0, 1.5],
            y_length=4,
            x_length=15,
            x_axis_config={
                "numbers_with_elongated_ticks": [
                    -3*PI, -2*PI, -PI, PI, 2*PI, 3*PI
                ]
            },
            y_axis_config={
                "include_numbers": True
            }
        )
        values_and_labels = [
            (r"$-3\pi$", -3*PI),
            (r"$-2\pi$", -2*PI),
            (r"$-\pi$", -PI),
            (r"$0$", 0),
            (r"$-\pi$", PI),
            (r"$2\pi$", 2*PI),
            (r"$3\pi$", 3*PI),
        ]
        toFadeOut = VGroup()
        toFadeOut.add(axes)
        for (label, x_val) in values_and_labels:
            labelDisplay = Tex(label).next_to(
                axes.c2p(x_val, 0),
                DOWN
            )
            toFadeOut.add(labelDisplay)
        self.play(Create(axes))
        self.play(*[Write(lbl) for lbl in toFadeOut], run_time=2)

        fn = axes.plot(lambda x: fourier_series(x, 61))
        fn.set_stroke(color=RED, width=7).set_z_index(2)
        paestum_img = ImageMobject("../assets/tempio-nettuno.jpg").scale(5).shift(DOWN * 6 + RIGHT * .4).set_opacity(.6).set_z_index(-1)
        self.play(Create(fn), run_time=5)
        self.play(FadeIn(paestum_img), FadeOut(toFadeOut), run_time=10)
        self.wait()