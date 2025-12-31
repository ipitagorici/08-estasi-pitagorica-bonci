from manim import *

class Fractal(MovingCameraScene):
    def construct(self):
        radiusRatio = 0.42
        
        colors = [RED, ORANGE, YELLOW, GREEN, PURPLE, BLUE]
        
        def innerRadius(star):
            return np.linalg.norm(star.get_vertices()[0] - star.get_center())*radiusRatio
                    
        def CreateStars(startingStar, depth=0):            
            if innerRadius(startingStar) < 0.01:
                return 
            
            smallerStar = Star(outer_radius=innerRadius(startingStar), stroke_width=startingStar.stroke_width*radiusRatio)
                
            if depth%2 == 0:
                smallerStar.rotate(PI, about_point=ORIGIN)
            
            smallerInnerPentagon = RegularPolygon(5, radius=innerRadius(smallerStar), stroke_width=smallerStar.stroke_width)

            if depth%2 == 1:
                smallerInnerPentagon.rotate(PI, about_point=ORIGIN)
                
            smallerStar.set_color(colors[depth%len(colors)])
            smallerInnerPentagon.set_color(colors[depth%len(colors)])
            
            self.play(Create(smallerStar), Create(smallerInnerPentagon))
            
            if innerRadius(smallerStar) > 0.08 and innerRadius(smallerStar) < 0.5:
                self.play(self.camera.frame.animate.set(width = 0.5))
            elif innerRadius(smallerStar) < 0.08:
                self.play(self.camera.frame.animate.set(width = 0.1))
            
            print(innerRadius(smallerStar))
            return CreateStars(smallerStar, depth+1)
        
        
        star = Star(5, outer_radius=4, color=WHITE)
        innerPentagon = RegularPolygon(5, radius=innerRadius(star), color=WHITE)
        innerPentagon.rotate(PI, about_point=ORIGIN)
        self.play(DrawBorderThenFill(star), DrawBorderThenFill(innerPentagon))
        pythagoreanStar = VGroup(star, innerPentagon)
        self.wait()
        CreateStars(star)