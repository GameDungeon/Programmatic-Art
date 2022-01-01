from manim import *
from PIL import Image, ImageOps
import numpy as np
import random as r
from tqdm import tqdm

img = Image.open("cat.jpg")
dot_map = np.zeros(img.size)
size = img.size[0]
img = np.array(ImageOps.grayscale(img))
img = img.T[:,::-1]

count = 125000

class Dots(Scene):
    def construct(self):
        dots = []
        for i in tqdm(range(count)):
            test = True
            while test:
                x = r.randint(0, size-1)
                y = r.randint(0, size-1)

                if dot_map[x,y] == 0:
                    test = False
                else:
                    dot_map[x,y] = 1

            d = Dot([(x/size)*10-5,(y/size)*10-5,0], 0.01)

            dots.append(Succession(FadeIn(d, runtime=0.1), FadeToColor(d, "#" + hex(img[x,y])[2:]*3, run_time=3)))

        self.play(AnimationGroup(*dots, lag_ratio=0.00005))
        self.wait(5)
