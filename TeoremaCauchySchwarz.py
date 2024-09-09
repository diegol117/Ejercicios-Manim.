from manim import *

class TeoremaCauchySchwarz(Scene):
    def construct(self):
        # Lamina 1 - Parte 1: Introducción del teorema
        texto_parte_1 = Tex(
            r"Teorema (Desigualdad de Cauchy-Schwarz)\\",
            r"Sean $a_1, a_2, \dots, a_n$ y $b_1, b_2, \dots, b_n$ números reales."
        ).scale(0.8).set_color(GOLD) 
        texto_parte_1.to_edge(UP)

        # Lamina 1 - Parte 2: Primera expresión matemática
        texto_parte_2 = MathTex(
            r"\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right) \geq\left(\sum_{i=1}^n a_i b_i\right)^2"
        ).scale(0.8).next_to(texto_parte_1, DOWN).set_color(GOLD) 

        # Lamina 1 - Parte 3: Segunda expresión matemática
        texto_parte_3 = MathTex(
            r"\left(a_1^2+a_2^2+\cdots+a_n^2\right)\left(b_1^2+b_2^2+\cdots+b_n^2\right) \geq\left(a_1 b_1+a_2 b_2+\cdots+a_n b_n\right)^2"
        ).scale(0.8).next_to(texto_parte_2, DOWN).set_color(GOLD) 

        # Lamina 1 - Parte 4: Condición de igualdad
        texto_parte_4 = Tex(
            r"La igualdad ocurre si y solo si las secuencias $(a_1, a_2, \dots, a_n)$ \\",
            r"y $(b_1, b_2, \dots, b_n)$ son proporcionales, es decir,\\",
            r"$\frac{a_1}{b_1}=\frac{a_2}{b_2}=\cdots=\frac{a_n}{b_n}$."
        ).scale(0.8).next_to(texto_parte_3, DOWN).set_color(GOLD) 

        # Mostrar cada parte de la lamina 1 con 3 segundos entre ellas
        self.play(Write(texto_parte_1), run_time=3)
        self.wait(3)
        self.play(Write(texto_parte_2), run_time=3)
        self.wait(3)
        self.play(Write(texto_parte_3), run_time=3)
        self.wait(3)
        self.play(Write(texto_parte_4), run_time=3)
        self.wait(3)

        # Transición a Lamina 2
        self.play(FadeOut(VGroup(texto_parte_1, texto_parte_2, texto_parte_3, texto_parte_4)))
        
        # Lamina 2 - Parte 1: Demostración, trinomio cuadrático
        texto_parte_5 = Tex(
            r"Demostración. Consideremos el trinomio cuadrático"
        ).scale(0.8)
        texto_parte_5.to_edge(UP)

        texto_parte_6 = MathTex(
            r"\sum_{i=1}^n\left(a_i x-b_i\right)^2 = \sum_{i=1}^n\left(a_i^2 x^2 - 2 a_i b_i x + b_i^2\right)\\",
            r"    = x^2 \sum_{i=1}^n a_i^2 - 2x \sum_{i=1}^n a_i b_i + \sum_{i=1}^n b_i^2"
        ).scale(0.8).next_to(texto_parte_5, DOWN)

        # Mostrar la parte 1 de la lamina 2
        self.play(Write(texto_parte_5), run_time=3)
        self.wait(3)
        self.play(Write(texto_parte_6), run_time=3)
        self.wait(3)

        # Lamina 2 - Parte 2: Expresión del discriminante
        texto_parte_7 = Tex(
            r"Este trinomio es no negativo para todo $x \in \mathbb{R}$, \\",
            r"por lo que su discriminante no es positivo, es decir:"
        ).scale(0.8)
        texto_parte_7.next_to(texto_parte_6, DOWN)

        texto_parte_8 = MathTex(
            r"4\left(\sum_{i=1}^n a_i b_i\right)^2 - 4\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right) \leq 0\\",
            r"\Leftrightarrow \left(\sum_{i=1}^n a_i b_i\right)^2 \leq \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)"
        ).scale(0.8).next_to(texto_parte_7, DOWN)

        # Mostrar la parte 2 de la lamina 2
        self.play(Write(texto_parte_7), run_time=3)
        self.wait(3)
        self.play(Write(texto_parte_8), run_time=3)
        self.wait(3)

        # Transición a Lamina 3
        self.play(FadeOut(VGroup(texto_parte_5, texto_parte_6, texto_parte_7, texto_parte_8)))

        # Lamina 3 - Parte 1: Condición de igualdad
        texto_parte_9 = Tex(
            r"La igualdad se cumple si y solo si $a_i x - b_i = 0$, para $i = 1, 2, \dots, n$, \\",
            r"es decir, $\frac{a_1}{b_1} = \frac{a_2}{b_2} = \dots = \frac{a_n}{b_n}$."
        ).scale(0.8)

        # Mostrar la parte 1 y parte 2 de la lamina 3
        self.play(Write(texto_parte_9), run_time=3)
        self.wait(3)

        # Finalización
        self.play(FadeOut(texto_parte_9))
