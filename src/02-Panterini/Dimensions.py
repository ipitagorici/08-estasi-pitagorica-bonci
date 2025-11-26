from manim import *

class Dimensions(ThreeDScene):
    def construct(self):
        cube = always_redraw(lambda: Cube()).set_color(RED)
        square = Square().set_color(YELLOW)
        line = Line().set_color(GREEN)
        dot = Dot().set_color(BLUE)
        
        dimensions = VGroup(Tex("2D"), Tex("1D"), Tex("0D"), Tex("?"))\
            .next_to(square, RIGHT)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        self.play(Create(cube))

        cube_height = ValueTracker(cube.height)
        phi_tracker = ValueTracker(75 * DEGREES)
        theta_tracker = ValueTracker(30 * DEGREES)

        # Function to update the camera orientation based on the trackers
        def update_camera(mob):
            self.set_camera_orientation(
                phi=phi_tracker.get_value(), 
                theta=theta_tracker.get_value()
            )

        dummy = always_redraw(lambda: Dot(radius=0.0000001).add_updater(update_camera))
        self.add(dummy)

        self.play(
            Transform(cube, square, replace_mobject_with_target_in_scene=True),
            phi_tracker.animate.set_value(0 * DEGREES),
            theta_tracker.animate.set_value(-90 * DEGREES),
            
            run_time=2
        )

        self.remove(dummy)  # Cleanup after camera movement is done
        
        self.play(Write(dimensions[0]))

        self.play(Transform(square, line, replace_mobject_with_target_in_scene=True, run_time=2.5), Transform(dimensions[0], dimensions[1], replace_mobject_with_target_in_scene=True, run_time=2.5))
        self.play(Transform(line, dot, replace_mobject_with_target_in_scene=True, run_time=2.5), Transform(dimensions[1], dimensions[2], replace_mobject_with_target_in_scene=True, run_time=2.5))
        
        self.wait(5)
        
        self.play(Flash(dot, color=WHITE), FadeOut(dot), Transform(dimensions[2], dimensions[3], replace_mobject_with_target_in_scene=True))
        self.play(dimensions[3].animate.move_to(ORIGIN))
        self.play(dimensions[3].animate.scale(3))
        

        self.wait(2)