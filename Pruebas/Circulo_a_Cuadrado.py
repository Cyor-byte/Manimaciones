from manim import *

# class Square2Circle(Scene):
#     def construct(self):
#         circle = Circle() #crea un circulo
#         circle.set_stroke(color = WHITE, opacity = 1)
        

#         square = Square() #creo un cuadrado
#         square.rotate(PI/4) #lo roto 45 grados


#         self.play(Create(circle)) #creo el circulo
#         self.play(Transform(circle, square)) #convierto el circulo en un cuadrado
#         self.play(FadeOut(circle)) #transicion de salida de la escena


class Square2Circle(Scene):
    def construct(self):
        circle = Circle() #crea un circulo
        circle.set_stroke(color = WHITE, opacity = 1)
        

        square = Square() #creo un cuadrado
        square.rotate(PI/4) #lo roto 45 grados
        #square.next_to(circle, UP, buff = 1)

        self.play(Create(circle), Create(square)) #creo el circulo
        
        self.play(Transform(circle, square)) #convierto el circulo en un cuadrado
        self.play(Rotate(square, PI/4))
        self.play(Rotate(circle, PI/2))
        self.play(circle.animate.set_stroke(color = BLUE, opacity = 1))
        self.play(square.animate.set_stroke(color = DARK_BROWN, opacity = 1))
        
        #self.play(FadeOut(circle)) #transicion de salida de la escena



