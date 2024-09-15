from manim import *
class ComplementoProb(Scene):
    def construct(self):
    
        ejemplo_1 = Tex(
            r"Proposición. Para cualquier evento $A$,"
            ).scale(0.8).to_edge(UP).set_color(GOLD)
        self.play(Write(ejemplo_1))
        self.wait(2)
        
        ejemplo_2 = Tex(
            r"$$P\left(A^{c}\right)=1-P(A).$$"
            ).scale(0.8).next_to(ejemplo_1, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_2))
        self.wait(2)
        

        ejemplo_3 = Tex(
            r"Demostración. De la teoría elemental de conjuntos tenemos que \\"
            ).scale(0.8).next_to(ejemplo_2, DOWN)
        self.play(Write(ejemplo_3))
        self.wait(0)
        
        ejemplo_4 = Tex(
            r"$\Omega= A \cup A^{c}$, en donde $A$ y $A^{c}$ son eventos ajenos. "
            ).scale(0.8).next_to(ejemplo_3, DOWN)
        self.play(Write(ejemplo_4))
        self.wait(2)
        
        ejemplo_5 = Tex(
            r"Aplicando el tercer axioma tenemos que"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(1)
        
        ejemplo_6 = Tex(
            r"$$ \begin{aligned} 1 & =P(\Omega) \\ & =P\left(A \cup A^{c}\right) \\ & =P(A)+P\left(A^{c}\right) \end{aligned} $$"
            ).scale(0.8).next_to(ejemplo_5, DOWN)
        self.play(Write(ejemplo_6))
        self.wait(2)
        
        self.play(FadeOut(VGroup(ejemplo_1, ejemplo_2, ejemplo_3, ejemplo_4, ejemplo_5, ejemplo_6)))
