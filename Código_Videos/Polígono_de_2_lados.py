from manim import *
import numpy as np

class Sides(ThreeDScene):
    def construct(self):
        c = Circle(radius=1)
        c.set_stroke(color=WHITE)

        p100 = RegularPolygon(n=100).set_stroke(PINK)
        p10 = RegularPolygon(n=10).set_stroke(RED)
        p9 = RegularPolygon(n=9).set_stroke(ORANGE)
        p8 = RegularPolygon(n=8).set_stroke(YELLOW)
        p7 = RegularPolygon(n=7).set_stroke(GREEN)
        p6 = RegularPolygon(n=6).set_stroke(PURPLE)
        p5 = RegularPolygon(n=5).set_stroke(DARK_BLUE)
        p4 = RegularPolygon(n=4).set_stroke(BLUE)
        p3 = RegularPolygon(n=3).set_stroke(WHITE)

        LadosInf = Tex(r"\text{Lados:} \(\infty\)").shift(2 * DOWN)
        Lados100 = Tex(r"\text{Lados:} \text{100}").shift(2 * DOWN)
        Lados10 = Tex(r"\text{Lados:} \text{10}").shift(2 * DOWN)
        Lados9  = Tex(r"\text{Lados:} \text{9}").shift(2 * DOWN)
        Lados8  = Tex(r"\text{Lados:} \text{8}").shift(2 * DOWN)
        Lados7  = Tex(r"\text{Lados:} \text{7}").shift(2 * DOWN)
        Lados6  = Tex(r"\text{Lados:} \text{6}").shift(2 * DOWN)
        Lados5  = Tex(r"\text{Lados:} \text{5}").shift(2 * DOWN)
        Lados4  = Tex(r"\text{Lados:} \text{4}").shift(2 * DOWN)
        Lados3  = Tex(r"\text{Lados:} \text{3}").shift(2 * DOWN)
        Lados2  = Tex(r"\text{Lados:} \text{2}").shift(2 * DOWN)
        pI = Tex(r"\text{?}"); pI.next_to(Lados2, RIGHT, buff=0.1)
        pD = Tex(r"\text{¿}"); pD.next_to(Lados2, LEFT,  buff=0.1)

        self.play(Create(c), FadeIn(LadosInf), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingTex(LadosInf, Lados100), run_time=0.2)
        self.play(ReplacementTransform(c, p100), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados100, Lados10), run_time=0.2)
        self.play(ReplacementTransform(p100, p10), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados10, Lados9), run_time=0.2)
        self.play(ReplacementTransform(p10, p9), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados9, Lados8), run_time=0.2)
        self.play(ReplacementTransform(p9, p8), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados8, Lados7), run_time=0.2)
        self.play(ReplacementTransform(p8, p7), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados7, Lados6), run_time=0.2)
        self.play(ReplacementTransform(p7, p6), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados6, Lados5), run_time=0.2)
        self.play(ReplacementTransform(p6, p5), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados5, Lados4), run_time=0.2)
        self.play(ReplacementTransform(p5, p4), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados4, Lados3), run_time=0.2)
        self.play(ReplacementTransform(p4, p3), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Lados3, Lados2), run_time=0.2)
        self.wait(0.5)

     
        self.play(Indicate(p3, 1.1, RED), run_time=0.3)
        self.wait(1)
        self.play(Indicate(p3, 1.1, RED), run_time=0.3)
        self.wait(1)
        self.play(Indicate(p3, 1.1, RED), run_time=0.3)

       
        self.play(FadeIn(pI), FadeIn(pD))
        self.wait(0.4)

        
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=2.0)
        self.wait(0.3)

     
        axes = ThreeDAxes(x_length=3, y_length=3, z_length=3)
        axes.set_opacity(0.9)
        self.play(FadeIn(axes), run_time=1.0)
        self.wait(0.2)

        
        self.play(Indicate(axes.x_axis, scale_factor=1.1), run_time=0.45)
        self.play(Indicate(axes.y_axis, scale_factor=1.1), run_time=0.45)
        self.play(Indicate(axes.z_axis, scale_factor=1.1), run_time=0.45)
        self.wait(0.2)

      
        A = np.array([1.0, 0.0, 0.0])
        B = np.array([-1.0, 0.0, 0.0])

      
        arc3d_xy = ParametricFunction(
            lambda t: np.array([np.cos(t), np.sin(t), 0.0]),
            t_range = np.array([0, PI]),
        ).set_stroke(WHITE, width=6)

       
        arc3d_xz = ParametricFunction(
            lambda t: np.array([np.cos(t), 0.0, np.sin(t)]),
            t_range = np.array([0, PI]),
        ).set_stroke(WHITE, width=6)

        p2 = VGroup(arc3d_xy, arc3d_xz)
        self.play(TransformMatchingTex(Lados3, Lados2), run_time=0.2)

       
        self.play(FadeOut(p3), run_time=0.6)
        self.wait(0.1)
        self.play(Create(p2), run_time=1.2) 
        self.wait(0.2)

        
        self.play(Indicate(arc3d_xy, scale_factor=1.08, color=RED), run_time=0.45)
        self.play(Indicate(arc3d_xz, scale_factor=1.08, color=RED), run_time=0.45)

   
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3.0)
        self.stop_ambient_camera_rotation()

        self.wait(0.6)