from manim import *

class EcuacionesDiferenciales(Scene):
    def construct(self):
        # Lamina 1: Título en grande y en dorado
        titulo_1 = Text(
            "Ecuaciones diferenciales de variables separables", 
            font_size=28, color=GOLD
        ).to_edge(UP, buff=1)

        # Mostrar la Lamina 1
        self.play(Write(titulo_1), run_time=3)
        self.wait(2)

        # Lamina 2 Parte 1: Texto normal con saltos de línea
        texto_2_1 = Paragraph(
            "El primer tipo de ED que presentamos es el de variables separables,\n"
            "porque con frecuencia se intenta separar las variables de las\n"
            "ecuaciones de dos variables.\n\n",
            alignment="center",
            line_spacing=0.75,
            font_size=28
        ).scale(0.8).next_to(titulo_1, DOWN)
        

        # Mostrar Lamina 2 Parte 1


        # Lamina 2 Parte 2: Texto en dorado
        ejemplo_2_2_1 = Text(
            "Ejemplo. Separar las variables de la siguiente ecuación algebraica", 
            font_size=25, color=GOLD
        ).next_to(texto_2_1, DOWN, buff=0.5)

        ecuacion_2_2_1 = MathTex(
            r"\left(x^2-x\right)\left(y^2+3\right)=2xy",
            color=GOLD
        ).scale(0.8).next_to(ejemplo_2_2_1, DOWN)

        # Mostrar Lamina 2 Parte 2
        self.play(Write(texto_2_1), run_time=5)
        self.wait(2)
        self.play(Write(ejemplo_2_2_1), run_time=3)
        self.play(Write(ecuacion_2_2_1), run_time=3)
        self.wait(2)
        self.play(FadeOut(titulo_1, texto_2_1, ejemplo_2_2_1, ecuacion_2_2_1))
        # Lamina 2 Parte 3: Texto con solución normal y saltos de línea
        texto_2_3 = Tex(
                        r"Solución. Por separar las variables de la ecuación se entiende \\",
                        r"que, por medio de operaciones algebraicas válidas, se coloquen \\",
                        r"todas las $x$ de un lado de la igualdad y todas las $y$ del otro \\",
                        r"lado. En este caso:"
                    ).scale(0.8).to_edge(UP, buff=0.5)

        ecuacion_2_3 = MathTex(
            r"\left(x^2 - x\right)\left(y^2 + 3\right) = 2xy \Rightarrow \frac{x^2 - x}{x} = \frac{2y}{y^2 + 3}"
        ).scale(0.8).next_to(texto_2_3, DOWN)

        texto_2_4 = Tex(
            r"Como explicamos, se han colocado las $x$ del lado izquierdo de\\"
            r"la ecuación y las $y$ del lado derecho.",
        ).scale(0.8).next_to(ecuacion_2_3, DOWN)

        # Mostrar Lamina 2 Parte 3
        self.play(Write(texto_2_3), run_time=5)
        self.play(Write(ecuacion_2_3), run_time=3)
        self.play(Write(texto_2_4), run_time=3)
        self.wait(2)
        self.play(FadeOut(texto_2_3, ecuacion_2_3, texto_2_4))