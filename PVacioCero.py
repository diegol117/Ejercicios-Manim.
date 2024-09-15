from manim import *

class PVacioCero(Scene):
    def construct(self):
    
        ejemplo_2 = Tex(
            r"Proposición. $P(\varnothing)=0$."
            ).scale(0.8).to_edge(UP).set_color(GOLD) 
        self.play(Write(ejemplo_2))
        self.wait(2)
        
        ejemplo_3 = Tex(
            r"Demostración. Tomando $A_{1}=A_{2}=\cdots=\varnothing$ en el tercer axioma, "
            ).scale(0.8).next_to(ejemplo_2, DOWN)
        self.play(Write(ejemplo_3))
        self.wait(0)
        
        ejemplo_4 = Tex(
            r"$P\left(\bigcup_{k=1}^{\infty} A_{k}\right)=\sum_{k=1}^{\infty} P\left(A_{k}\right)$ (con $A_{1}, A_{2}, \cdots$ independientes)."
            ).scale(0.8).next_to(ejemplo_3, DOWN)
        self.play(Write(ejemplo_4))
        self.wait(0)

        rectanguloA1 = SurroundingRectangle(ejemplo_4, color=YELLOW, buff=0.2)
        self.play(Create(rectanguloA1, run_time=2))

        ejemplo_5 = Tex(
            r"Tenemos que, $P(\varnothing)=P(\varnothing)+P(\varnothing)+\cdots$"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(2)
        
        ejemplo_6 = Tex(
            r"La única solución de esta ecuación es: "
            ).scale(0.8).next_to(ejemplo_5, DOWN)
        self.play(Write(ejemplo_6))
        self.wait(2)
        
        ejemplo_7 = Tex(
            r"$$P(\varnothing)=0.$$"
            ).scale(0.8).next_to(ejemplo_6, DOWN)
        self.play(Write(ejemplo_7))
        self.wait(2)
        

        rectanguloA = SurroundingRectangle(ejemplo_7, color=YELLOW, buff=0.2)
        self.play(Create(rectanguloA), run_time=2)
    

        self.play(FadeOut(VGroup(ejemplo_2, ejemplo_3, ejemplo_4, rectanguloA1, ejemplo_5, ejemplo_6, ejemplo_7, rectanguloA)))
    

