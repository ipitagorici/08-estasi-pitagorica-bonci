from manim import *
import math as m

class GodsNumber(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[1980, 2010, 1], 
            y_range=[0, 60, 5], 
            x_length=10, y_length=5, 
            x_axis_config={
                "numbers_with_elongated_ticks": [ 1980, 1990, 2000, 2010 ],
                "numbers_to_include": [ 1980, 1990, 2000, 2010 ]
            },
            y_axis_config={
                "numbers_with_elongated_ticks": list(range(0, 60, 10)),
                "numbers_to_include": list(range(0, 60, 10))
            },
            axis_config={
                'tip_shape': StealthTip
            }
        )

        def higherLimitFunction(x):
            if x < 1990:
                return 55
            if x >= 1990 and x <= 1991:
                return 47
            if x > 1991 and x <= 1994:
                return 45
            if x > 1994 and x < 1995:
                return 37
            if x >= 1995 and x < 2008:
                return 30
            if x >= 2008 and x < 2010:
                return 25
            if x >= 2010:
                return 20
            
        def lowerLimitFunction(x):
            if x < 1994:
                return 18
            if x >= 1994 and x < 1995:
                return x
            if x >= 1995:
                return 20

        higherLimit = axes.plot(
            function=lambda x: higherLimitFunction(x), 
            discontinuities=[1990, 1991, 1994, 1995, 2008, 2010]
        ).set_color(RED)

        lowerLimit = axes.plot(
            function=lambda x: lowerLimitFunction(x),
            discontinuities=[1994, 1995]
        ).set_color(BLUE_D)

        def get_segment(p1, p2):
            return DashedLine(p1, p2)

        # Terribile ma funziona
        segments = VGroup()
        segments.add(get_segment(axes.coords_to_point(1990, 55), axes.coords_to_point(1990, 47)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(1991, 47), axes.coords_to_point(1991, 45)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(1994, 45), axes.coords_to_point(1994, 37)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(1995, 37), axes.coords_to_point(1995, 30)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(2008, 30), axes.coords_to_point(2008, 25)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(2010, 25), axes.coords_to_point(2010, 20)).set_color(RED))
        segments.add(get_segment(axes.coords_to_point(1994, 18), axes.coords_to_point(1995, 20)).set_color(BLUE_D))

        endOfHigherLimit = Dot(higherLimit.get_end())
        endOfLowerLimit = Dot(lowerLimit.get_end())

        pointersValueTracker = ValueTracker(1980)
        upperDot = always_redraw(lambda: Dot(point = axes.c2p(pointersValueTracker.get_value(), higherLimitFunction(pointersValueTracker.get_value()))).set_color(RED))
        upperLabel = always_redraw(lambda: Text(f"{higherLimitFunction(pointersValueTracker.get_value())}")).add_updater(lambda label: label.next_to(upperDot, UR))
        lowerDot = always_redraw(lambda: Dot(point = axes.c2p(pointersValueTracker.get_value(), lowerLimitFunction(pointersValueTracker.get_value()))).set_color(BLUE_D))
        lowerLabel = always_redraw(lambda: Text(f"{lowerLimitFunction(pointersValueTracker.get_value())}")).add_updater(lambda label: label.next_to(lowerDot, UR))
        yProjection = always_redraw(lambda: axes.get_vertical_line(point=axes.c2p(pointersValueTracker.get_value(), higherLimitFunction(pointersValueTracker.get_value())), line_func=DashedLine).set_opacity(.8).set_color(GRAY))
        self.play(LaggedStart(GrowFromCenter(axes), Write(axes.get_axis_labels("Anni", r"\# Mosse")), lag_ratio=0.5))
        self.play(Create(lowerLimit), Create(higherLimit), run_time=5)
        self.play(Create(segments))
        self.play(Create(upperDot), Create(lowerDot), Create(yProjection), Write(upperLabel), Write(lowerLabel))
        self.play(pointersValueTracker.animate.set_value(2010), run_time=5)

        self.camera.frame.save_state()
        circle = Circle(3).shift((4.5, 0, 0))

        self.wait(2)
        self.play(self.camera.frame.animate.set(width = 10.8).move_to(circle))

        dot = Dot((endOfLowerLimit.get_x(), endOfLowerLimit.get_y() + ((endOfHigherLimit.get_y() - endOfLowerLimit.get_y())/2), 0), color=GOLD)
        self.play(Flash(dot), lowerDot.animate.set_color(GOLD), lowerLabel.animate.set_color(GOLD))
