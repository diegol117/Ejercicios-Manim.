from manim import *

class Ejercicio(Scene):
    def construct(self):
        # Lamina 1: Ejercicio 4.7
        texto_lamina_1_parte_1 = Tex(
            r"Ejercicio. Sea $a, b, c \in \mathbb{R}^{+}$\\"
        ).scale(0.8).set_color(GOLD) 
        self.play(Write(texto_lamina_1_parte_1), run_time=3)
        self.wait(1)

        texto_lamina_1_parte_2 = MathTex(
            r"\text{Demuestra la desigualdad: } \frac{a}{b+2c} + \frac{b}{c+2a} + \frac{c}{a+2b} \geq 1"
        ).scale(0.8).next_to(texto_lamina_1_parte_1, DOWN).set_color(GOLD) 

        # Mostrar texto en la Lamina 1

        self.play(Write(texto_lamina_1_parte_2), run_time=3)
        self.wait(3)

        # Transición a la Lamina 2
        self.play(FadeOut(texto_lamina_1_parte_1, texto_lamina_1_parte_2))

        # Lamina 2: Solución (parte 1)
        texto_lamina_2_parte_1 = Tex(
            r"Solución: Aplicando la desigualdad de Cauchy-Schwarz obtenemos"
        ).scale(0.8)

        # Mostrar la primera parte de la solución
        self.play(Write(texto_lamina_2_parte_1), run_time=3)
        self.wait(3)

        # Lamina 2: Solución (parte 2)
        texto_lamina_2_parte_2 = MathTex(
            r"\left(\frac{a}{b+2c} + \frac{b}{c+2a} + \frac{c}{a+2b}\right)(a(b+2c)+b(c+2a)+c(a+2b)) \geq (a+b+c)^2"
        ).scale(0.8).next_to(texto_lamina_2_parte_1, DOWN)

        # Mostrar la segunda parte de la solución
        self.play(Write(texto_lamina_2_parte_2), run_time=3)
        self.wait(3)

        # Lamina 2: Solución (parte 3)
        texto_lamina_2_parte_3 = Tex(
            r"Por lo tanto,"
        ).scale(0.8).next_to(texto_lamina_2_parte_2, DOWN)

        texto_lamina_2_parte_4 = MathTex(
            r"\frac{a}{b+2c} + \frac{b}{c+2a} + \frac{c}{a+2b} \geq \frac{(a+b+c)^2}{3(ab + bc + ca)}"
        ).scale(0.8).next_to(texto_lamina_2_parte_3, DOWN)

        # Mostrar la tercera parte de la solución
        self.play(Write(texto_lamina_2_parte_3), run_time=3)
        self.play(Write(texto_lamina_2_parte_4), run_time=3)
        self.wait(3)

        # Transición a la Lamina 3
        self.play(FadeOut(texto_lamina_2_parte_1, texto_lamina_2_parte_2, texto_lamina_2_parte_3, texto_lamina_2_parte_4))

        # Lamina 3: Parte 1
        texto_lamina_3_parte_1 = Tex(
            r"Entonces, basta con mostrar que"
        ).scale(0.8)

        self.play(Write(texto_lamina_3_parte_1), run_time=3)
        self.wait(3)

        # Lamina 3: Parte 2
        texto_lamina_3_parte_2 = MathTex(
            r"\frac{(a+b+c)^2}{3(ab + bc + ca)} \geq 1, \quad \text{es decir,} \quad (a+b+c)^2 \geq 3(ab + bc + ca)"
        ).scale(0.8).next_to(texto_lamina_3_parte_1, DOWN)

        self.play(Write(texto_lamina_3_parte_2), run_time=3)
        self.wait(3)

        # Lamina 3: Parte 3
        texto_lamina_3_parte_3 = Tex(
            r"lo que es equivalente a $a^2 + b^2 + c^2 \geq ab + bc + ca$, y claramente se cumple."
        ).scale(0.8).next_to(texto_lamina_3_parte_2, DOWN)

        texto_lamina_3_parte_4 = Tex(
            r"La igualdad ocurre si y solo si $a = b = c$."
        ).scale(0.8).next_to(texto_lamina_3_parte_3, DOWN)

        self.play(Write(texto_lamina_3_parte_3), run_time=3)
        self.play(Write(texto_lamina_3_parte_4), run_time=3)
        self.wait(3)

        # Finalización
        self.play(FadeOut(texto_lamina_3_parte_1, texto_lamina_3_parte_2, texto_lamina_3_parte_3, texto_lamina_3_parte_4))
