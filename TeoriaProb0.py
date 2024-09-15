from manim import *

class TeoriaProb0(Scene):
    def construct(self):
    
        ejemplo_2 = Tex(
            r"Definición. Sea $A$ un subconjunto de un espacio muestral $\Omega$ de "
            ).scale(0.8).to_edge(UP)
        self.play(Write(ejemplo_2))
        self.wait(0)
        
        ejemplo_3 = Tex(
            r"cardinalidad finita. Se define la probabilidad clásica del evento $A$ como el cociente"
            ).scale(0.8).next_to(ejemplo_2, DOWN)
        self.play(Write(ejemplo_3))
        self.wait(1)
        
        ejemplo_4 = Tex(
            r"$$P(A)=\frac{\# A}{\# \Omega}$$"
            ).scale(0.8).next_to(ejemplo_3, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_4))
        self.wait(1)
        
        ejemplo_5 = Tex(
            r"\#A denota la cardinalidad o número de elementos del conjunto $A$.\\"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(2)
        
        ejemplo_6 = Tex(
            r"Esta definición de probabilidad puede aplicarse cuando:\\"
            ).scale(0.8).next_to(ejemplo_5, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_6))
        self.wait(2)
        
        ejemplo_7 = Tex(
            r"a) el espacio muestral es finito.\\"
            ).scale(0.8).next_to(ejemplo_6, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_7))
        self.wait(2)
        
        ejemplo_8 = Tex(
            r"b) todos los elementos del espacio muestral tienen el mismo 'peso'."
            ).scale(0.8).next_to(ejemplo_7, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_8))
        self.wait(2)
        
        self.play(FadeOut(VGroup(ejemplo_2, ejemplo_3, ejemplo_4, ejemplo_5, ejemplo_6, ejemplo_7, ejemplo_8)))

        ejemplo_A2 = Tex(
            r"Los siguientes tres postulados o axiomas fueron establecidos en 1933 por "
            ).scale(0.8).to_edge(UP)
        self.play(Write(ejemplo_A2))
        self.wait(0)
        
        ejemplo_A3 = Tex(
            r"el matemático ruso Andrey Nikolaevich Kolmogorov."
            ).scale(0.8).next_to(ejemplo_A2, DOWN)
        self.play(Write(ejemplo_A3))
        self.wait(2)
        
        ejemplo_A4 = Tex(
            r"$$P(A) \geqslant 0.$$"
            ).scale(0.8).next_to(ejemplo_A3, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_A4))
        self.wait(2)
        
        ejemplo_A5 = Tex(
            r"$$P(\Omega)=1.$$"
            ).scale(0.8).next_to(ejemplo_A4, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_A5))
        self.wait(2)
        
        ejemplo_A6 = Tex(
            r"$P\left(\bigcup_{k=1}^{\infty} A_{k}\right)=\sum_{k=1}^{\infty} P\left(A_{k}\right)$ (si $A_{1}, A_{2}, \cdots$ son independientes)."
            ).scale(0.8).next_to(ejemplo_A5, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_A6))
        self.wait(2)
        

        self.play(FadeOut(VGroup(ejemplo_A2, ejemplo_A3, ejemplo_A4, ejemplo_A5, ejemplo_A6)))





