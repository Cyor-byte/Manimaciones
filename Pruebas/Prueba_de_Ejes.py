from manim import * 
from math import *
class PlotAxes(Scene):
    def construct(self):
        ax = Axes(x_range=(-10, 10), y_range=(-10, 10), tips=0)
        sineWave = ax.plot(lambda x: (1/x), color= WHITE)
        cosineWave = ax.plot(lambda x: cos(x), color= RED)
        area = ax.get_area(sineWave, color = (BLUE, GREEN))
        self.play(Create(ax), run_time=2)
        self.play(Create(sineWave), run_time = 5)
        #self.play(Create(cosineWave), run_time = 5)
        #self.play(Create(area), run_time = 4)

#class Grouping(Scene):
    #def construct(self):


