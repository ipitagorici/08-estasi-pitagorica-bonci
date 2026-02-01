from manim import *
import cv2

class MovingPythagoras(Scene):
    def construct(self):
        cap = cv2.VideoCapture("src/assets/videos/04-moving-with-bg.mp4")
        flag = True
        frame_imgs: List[ImageMobject] = []
        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                frame_img.scale(2).center()
                frame_img.set_z_index(-1)
                frame_imgs.append(frame_img)
        cap.release()

        for _ in range(0, 1):
            frame_imgs.extend(reversed(frame_imgs))
             
        for frame_img in frame_imgs:
                self.add(frame_img)
                self.wait(0.06)
                self.remove(frame_img)