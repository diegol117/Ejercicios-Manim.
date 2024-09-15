from manim import *
class EventosInd(Scene):
    def construct(self):
    
        ejemplo_2 = Tex(
            r"Proposición. Sea $A_{1}, A_{2}, \cdots, A_{n}$ una colección finita de eventos independientes. "
            ).scale(0.8).to_edge(UP).set_color(GOLD)
        self.play(Write(ejemplo_2))
        self.wait(0)
        
        ejemplo_3 = Tex(
            r"Entonces $P\left(\bigcup_{k=1}^{n} A_{k}\right)=\sum_{k=1}^{n} P\left(A_{k}\right)$"
            ).scale(0.8).next_to(ejemplo_2, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_3))
        self.wait(2)
        
        ejemplo_4 = Tex(
            r"Demostración. Definiendo $A_{n+1}=A_{n+2}=\cdots=\varnothing$, se verifica que esta sucesión infinita sigue siendo ajena dos a dos y por lo tanto, usando el tercer axioma, tenemos que"
            ).scale(0.8).next_to(ejemplo_3, DOWN)
        self.play(Write(ejemplo_4))
        self.wait(3)
        
        ejemplo_5 = Tex(
            r"$$\begin{aligned}P\left(\bigcup_{k=1}^{n} A_{k}\right) & =P\left(\bigcup_{k=1}^{\infty} A_{k}\right) \\& =\sum_{k=1}^{\infty} P\left(A_{k}\right) \\& =\sum_{k=1}^{n} P\left(A_{k}\right)\end{aligned}$$"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(1)
        
        self.play(FadeOut(VGroup(ejemplo_2, ejemplo_3, ejemplo_4, ejemplo_5)))
    
        ejemplo_12 = Tex(
            r"De esta manera, el tercer axioma incluye tanto el caso de sucesiones  "
            ).scale(0.8).to_edge(UP)
        self.play(Write(ejemplo_12))
        self.wait(0)
        
        ejemplo_13 = Tex(
            r"infinitas de eventos ajenos dos a dos como el caso de sucesiones finitas. \\"
            ).scale(0.8).next_to(ejemplo_12, DOWN)
        self.play(Write(ejemplo_13))
        self.wait(2)
        
        ejemplo_14 = Tex(
            r"En particular, cuando sólo tenemos dos eventos $A$ y $B$ con "
            ).scale(0.8).next_to(ejemplo_13, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_14))
        self.wait(0)
        
        ejemplo_15 = Tex(
            r"$A \cap B=\varnothing$, se cumple la identidad:"
            ).scale(0.8).next_to(ejemplo_14, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_15))
        self.wait(0)
        
        ejemplo_16 = Tex(
            r"$$P(A \cup B)=P(A)+P(B)$$"
            ).scale(0.8).next_to(ejemplo_15, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_16))
        self.wait(2)
        
        self.play(FadeOut(VGroup(ejemplo_12, ejemplo_13, ejemplo_14, ejemplo_15, ejemplo_16)))
