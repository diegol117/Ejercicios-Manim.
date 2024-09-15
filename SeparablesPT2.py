from manim import *

class EDOSeparables(Scene):
    def construct(self):
        # Lamina 1 - Parte 1: Ejemplo 2.2.2
        parte_1 = Tex(
            r"Ejemplo. Separar las variables de la siguiente ED:",
            r"\\",
            r"$\frac{d y}{d x}=\frac{2 x y}{\left(x^2-x\right)\left(y^2+3\right)}$",
            color=GOLD
        ).scale(0.8).to_edge(UP)
        
        # Mostrar la primera parte
        self.play(Write(parte_1), run_time=3)
        self.wait(2)

        # Lamina 1 - Parte 2: Explicación de separación de variables
        parte_2 = Tex(
            r"Para una ED como ésta, separar variables significa que, por medio de operaciones algebraicas válidas, \\",
            r"se escriba la ED en la forma:",
            r"\\",
            r"$g(y) \, d y = h(x) \, d x$"
        ).scale(0.8).next_to(parte_1, DOWN)

        self.play(Write(parte_2), run_time=3)
        self.wait(3)
        self.play(FadeOut(parte_1, parte_2))
        # Lamina 1 - Parte 3: Reorganización de la ecuación
        parte_3 = Tex(
            r"Entonces tenemos:",
            r"\\",
            r"$\frac{d y}{d x} = \frac{2 x y}{(x^2 - x)(y^2 + 3)} \Rightarrow \frac{y^2 + 3}{y} \, d y = \frac{2x}{x^2 - x} \, d x$"
        ).scale(0.8).next_to(parte_2, UP)

        self.play(Write(parte_3), run_time=3)
        self.wait(3)

        # Lamina 1 - Parte 4: Definición de g(y) y h(x)
        parte_4 = Tex(
            r"Y ahora:",
            r"\\",
            r"$g(y) = \frac{y^2 + 3}{y} \quad \& \quad h(x) = \frac{2 x}{x^2 - x},$",
            r"\\",
            r"con $y \neq 0$ y $x^2 - x \neq 0$"
        ).scale(0.8).next_to(parte_3, DOWN)

        self.play(Write(parte_4), run_time=3)
        self.wait(3)

        # Lamina final: Conclusión
        conclusion = Tex(
            r"Del resultado anterior, se concluye que la ecuación diferencial \\",
            r"$\frac{d y}{d x}=\frac{2 x y}{(x^2 - x)(y^2 + 3)}$ es una ED de variables separables."
        ).scale(0.8).next_to(parte_4, DOWN)

        self.play(Write(conclusion), run_time=3)
        self.wait(3)

        # Desvanecer todos los textos
        self.play(FadeOut(parte_3, parte_4, conclusion))
