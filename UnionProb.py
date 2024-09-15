from manim import *

class UnionProb(Scene):
    def construct(self):
    
        ejemplo_2 = Tex(
            r"Proposición. Para cualesquiera eventos $A$ y $B$, se cumple"
            ).scale(0.8).to_edge(UP).set_color(GOLD)
        self.play(Write(ejemplo_2))
        self.wait(0)
        
        ejemplo_3 = Tex(
            r"$$P(A \cup B)=P(A)+P(B)-P(A \cap B)$$"
            ).scale(0.8).next_to(ejemplo_2, DOWN).set_color(GOLD)
        self.play(Write(ejemplo_3))
        self.wait(2)
        
        ejemplo_4 = Tex(
            r"Demostración. Note que si $A \cap B \subseteq A$,  se cumple"
            ).scale(0.8).next_to(ejemplo_3, DOWN)
        self.play(Write(ejemplo_4))
        self.wait(0)
        
        ejemplo_5 = Tex(
            r"$$A-B=A-(A \cap B)$$"
            ).scale(0.8).next_to(ejemplo_4, DOWN)
        self.play(Write(ejemplo_5))
        self.wait(1)
        
        ejemplo_6 = Tex(
            r"Esto implica que, $$P(A-(A \cap B))=P(A)-P(A \cap B).$$"
            ).scale(0.8).next_to(ejemplo_5, DOWN)
        self.play(Write(ejemplo_6))
        self.wait(2)
        
        self.play(FadeOut(VGroup(ejemplo_2, ejemplo_3, ejemplo_4, ejemplo_5, ejemplo_6)))

    
        ejemplo_12 = Tex(
            r"Escribimos $A \cup B$ como la unión disjunta de los siguientes eventos:"
            ).scale(0.8).to_edge(UP)
        self.play(Write(ejemplo_12))
        self.wait(0)
        
        ejemplo_13 = Tex(
            r"$$ \begin{aligned} A \cup B & =(A-B) \cup(A \cap B) \cup(B-A) \\ & =(A-(A \cap B)) \cup(A \cap B) \cup(B-(A \cap B)) . \end{aligned} $$"
            ).scale(0.8).next_to(ejemplo_12, DOWN)
        self.play(Write(ejemplo_13))
        self.wait(2)
        
        ejemplo_14 = Tex(
            r"Aplicando la probabilidad (y el tercer axioma)"
            ).scale(0.8).next_to(ejemplo_13, DOWN)
        self.play(Write(ejemplo_14))
        self.wait(0)
        
        # Usando MathTex para mantener la alineación y animando por partes
        ejemplo_15 = MathTex(
            r"P(A \cup B) &=P(A-(A \cap B))+P(A \cap B)+P(B-(A \cap B))",  # Primera línea
            r"\\ &=P(A)-P(A \cap B)+P(A \cap B)+P(B)-P(A \cap B)",        # Segunda línea
            r"\\ &=P(A)+P(B)-P(A \cap B)"                                # Tercera línea
        ).scale(0.8).next_to(ejemplo_14, DOWN)

        # Animaciones por partes con esperas
        self.play(Write(ejemplo_15[0]))  # Primera parte
        self.wait(2)
        self.play(Write(ejemplo_15[1]))  # Segunda parte
        self.wait(2)
        self.play(Write(ejemplo_15[2]))  # Tercera parte
        self.wait(3)

        self.play(FadeOut(VGroup(ejemplo_12, ejemplo_13, ejemplo_14, ejemplo_15)))
    