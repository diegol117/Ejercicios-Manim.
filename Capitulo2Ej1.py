
from manim import *

class Capitulo2Ej1(Scene):
    def construct(self):
        # Definimos la función que queremos graficar
        def f(x):
            return x+1

        # Creamos los ejes
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"include_tip": True}
        )
        axes.set_color(BLUE)

        self.play(Create(axes))

        # Graficamos la función
        graph = axes.plot(f)
        graph.set_color(GREEN)
        self.play(Create(graph))

        # Iteramos sobre los valores de x
        for x_value in [0.5, 4.0, 7.0]:
            y_value = f(x_value)

            # Creamos un punto en la curva
            dot = Dot(axes.coords_to_point(x_value, y_value))

            # Creamos una línea vertical desde el punto hasta el eje x
            line = DashedLine(
                start=dot.get_center(),
                end=axes.coords_to_point(0, y_value),
                color=YELLOW
            )

            line1 = DashedLine(
                start=axes.coords_to_point(x_value, 0),
                end=dot.get_center(),
                color=YELLOW
            )

            text = Tex(f"${x_value}$")
            text.scale(0.7)
            text.next_to(axes.coords_to_point(x_value, 0), DOWN)

            text1 = Tex(f"$f({x_value})$")
            text1.scale(0.7)
            text1.next_to(axes.coords_to_point(0, y_value), LEFT)

            text2 = Tex(f"$({x_value}, f({x_value}))$")
            text2.scale(0.7)
            text2.next_to(axes.coords_to_point(x_value, y_value), RIGHT)

            # Animamos la creación de las líneas, puntos y textos
            self.play(Create(text), run_time=1)
            rectanguloA = SurroundingRectangle(text, color=YELLOW, buff=0.2)
            self.play(Create(rectanguloA), run_time=1)
            self.play(Create(line1))
            self.play(Create(dot))
            self.play(Create(text2), run_time=1)
            self.play(Create(line))
            self.play(Create(text1), run_time=1)
            rectanguloB = SurroundingRectangle(text1, color=YELLOW, buff=0.2)
            self.play(Create(rectanguloB), run_time=1)

        self.wait()

if __name__ == "__main__":
    scene = GraficaConLinea()
    scene.render()
