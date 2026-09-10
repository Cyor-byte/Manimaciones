from manim import *

class PIRotations(Scene):
    def construct(self):
        square = Square()
        square.set_stroke(color=WHITE, opacity=1.0)
        texRotacion = Tex(r"\text{Rotaciones de} \(\pi\)", font_size=46)
        texCero = Tex(r"\text{0}", font_size=46)
        texPI8 = Tex(r"\(\frac{\pi}{8}\)", font_size=46)
        texPI4 = Tex(r"\(\frac{\pi}{4}\)", font_size=46)
        tex3PI8 = Tex(r"\(\frac{3\pi}{8}\)", font_size=46)
        texPI2 = Tex(r"\(\frac{\pi}{2}\)", font_size=46)
        texInf = Tex(r"\(\infty\)", font_size=46)
        texRotacion.next_to(square, UP, 0.8)

        tasa_rot = 4 * PI

        def update_rotation(mobj, dt):
            # rotate by rotate_rate * dt radians this frame, about its center
            mobj.rotate(tasa_rot * dt, about_point=mobj.get_center())

        self.add(texRotacion)
        self.play(Create(square))
        self.wait(0.5)
        self.play(Create(texCero))
        self.wait(0.5)
        self.play(TransformMatchingTex(texCero, texPI8))
        self.play(Rotate(square, PI/8))
        self.wait(0.2)
        self.play(TransformMatchingTex(texPI8, texPI4))
        self.play(Rotate(square, PI/8))
        self.wait(0.2)
        self.play(TransformMatchingTex(texPI4, tex3PI8))
        self.play(Rotate(square, PI/8))
        self.wait(0.2)
        self.play(TransformMatchingTex(tex3PI8, texPI2))
        self.play(Rotate(square, PI/8))
        self.wait(0.2)
        self.play(TransformMatchingTex(texPI2, texInf))
        self.wait(0.1)
        # add updater directly (don't use the .animate proxy)
        square.add_updater(update_rotation)

        # let it spin for 2 seconds
        self.wait(2)

        # stop spinning if you want
        square.remove_updater(update_rotation)
        self.wait(0.5)



        