from manim import *

class LanzaMoneda(Scene):
    def construct(self):
        ejemplo_2 = Tex(
            r"Ejemplo. Considere el experimento aleatorio de lanzar un dado equilibrado. "
            ).scale(0.8).to_edge(UP)
        self.play(Write(ejemplo_2))
        self.wait(2)
        
        ejemplo_3 = Tex(
            r"El espacio muestral es el conjunto $\Omega=\{1,2,3,4,5,6\}$. "
            ).scale(0.8).next_to(ejemplo_2, DOWN)
        self.play(Write(ejemplo_3))
        self.wait(2)
        
        ejemplo_4 = Tex(
            r"Si deseamos calcular la probabilidad (clásica) del evento $A$, correspondiente a "
            ).scale(0.8).next_to(ejemplo_3, DOWN)
        self.play(Write(ejemplo_4))
        self.wait(0)
        
        ejemplo_5 = Tex(
            r"obtener un número par, es decir, la probabilidad de $A=\{2,4,6\}$"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(0)
        
        ejemplo_6 = Tex(
            r"$$P(A)=\frac{\#\{2,4,6\}}{\#\{1,2,3,4,5,6\}}=\frac{3}{6}$$"
            ).scale(0.8).next_to(ejemplo_5, DOWN)
        self.play(Write(ejemplo_6))
        self.wait(2)
        
        ejemplo_7 = Tex(
            r"$$P(A)=\frac{1}{2}$$"
            ).scale(0.8).next_to(ejemplo_6, DOWN)
        self.play(Write(ejemplo_7))
        self.wait(0)
        
        rectanguloA = SurroundingRectangle(ejemplo_7, color=YELLOW, buff=0.2)
        self.play(Create(rectanguloA), run_time=2)
    
        self.play(FadeOut(VGroup(ejemplo_2, ejemplo_3, ejemplo_4, ejemplo_5, ejemplo_6, ejemplo_7, rectanguloA)))
    
