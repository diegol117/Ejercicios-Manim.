
from manim import *
from numpy import cos, sqrt, sin

class Capitulo2Ej5(Scene):
    def construct(self):
        # Definir las funciones f(x), g(x), y h(x) (identidad)
        def f(x):
            return np.sin(x)
        
        def g(x):
            return 2*np.cos(x)
        
        def h(x):
            return x  # Función identidad

        # Crear los ejes
        axes = Axes(
            x_range=[-5.0, 5.0],
            y_range=[-3.0, 3.0],
            axis_config={"include_tip": True}
        )
        axes.set_color(BLUE)
       
        
        self.play(Create(axes))

        Nombrefunc = Tex(r"$f(x)=sin(x)$").to_edge(UL).set_color(TEAL_A) 
        self.play(Write(Nombrefunc))
        # Graficar f(x)
        graph_f = axes.plot(f, color=TEAL_A)
        self.play(Create(graph_f))

        Nombrefunc1 = Tex(r"$g(x)=2cos(x)$").to_edge(UL).set_color(LIGHT_PINK).next_to(Nombrefunc, DOWN, aligned_edge=LEFT) 
        self.play(Write(Nombrefunc1))



        # Graficar g(x)
        graph_g = axes.plot(g, color=LIGHT_PINK)
        self.play(Create(graph_g))

        # Graficar h(x) = x (identidad)
        graph_h = axes.plot(h, color=WHITE)
        self.play(Create(graph_h))

        # Valor específico para graficar f(g(-0.5))
        x_value = -0.5
        g_value = g(x_value)  # g(x_value)
        h_value = h(g_value)  # h(g(x_value)) = g(x_value), porque h(x) es identidad
        f_of_g_value = f(h_value)  # f(g(x_value))


        t_label = Tex(f"${x_value}$")
        t_label.scale(0.5)
        t_label.next_to(axes.coords_to_point(x_value, 0), UP)
        self.play(Create(t_label), run_time=1)
        # Punto en g(x_value)
        dot_g = Dot(axes.coords_to_point(x_value, g_value), color=YELLOW)
        label_g = Tex(f"$g({x_value}) = {round(g_value, 2)}$").scale(0.6)
        label_g.next_to(dot_g, DR)

        # Línea vertical en g(x)
        line_g = DashedLine(
            start=axes.coords_to_point(x_value, 0),
            end=axes.coords_to_point(x_value, g_value),
            color=YELLOW
        )
        self.play(Create(line_g))
        self.play(Create(dot_g), Write(label_g))

        # Punto en la función identidad h(g(-0.5)) = g(-0.5)
        dot_h = Dot(axes.coords_to_point(g_value, h_value), color=YELLOW)
        label_h = Tex(f"$g({x_value}) = {round(h_value, 2)}$").scale(0.6)
        label_h.next_to(dot_h, DR)

        # Línea punteada en h(x) desde g(-0.5) hasta f(g(-0.5))
        horizontal_line = DashedLine(
            start=dot_g.get_center(),
            end=axes.coords_to_point(g_value, h_value),
            color=YELLOW
        )
        self.play(Create(horizontal_line))
        self.play(Create(dot_h), Write(label_h))

        # Punto en f(g(-0.5))
        dot_f_of_g = Dot(axes.coords_to_point(h_value, f_of_g_value), color=YELLOW)
        label_f_of_g = Tex(f"$f(g({x_value})) = {round(f_of_g_value, 2)}$").scale(0.6)
        label_f_of_g.next_to(dot_f_of_g, DR)

        # Línea vertical en f(g(-0.5))
        line_f_of_g = DashedLine(
            start=axes.coords_to_point(g_value, h_value),
            end=axes.coords_to_point(g_value, f_of_g_value),
            color=YELLOW
        )
        self.play(Create(line_f_of_g))
        self.play(Create(dot_f_of_g), Write(label_f_of_g))
        self.wait()

        # Línea vertical en f(g(-0.5))
        line_final = DashedLine(
            start=axes.coords_to_point(g_value, f_of_g_value),
            end=axes.coords_to_point(x_value, f_of_g_value),
            color=YELLOW
        )
        dot_final = Dot(axes.coords_to_point(x_value, f_of_g_value), color=YELLOW)
        self.play(Create(line_final))
        self.play(Create(dot_final))

        label_fin = Tex((x_value, {round(f_of_g_value, 2)})).scale(0.6)
        label_fin.next_to(dot_final, DR)
        self.play(Write(label_fin))
        self.wait()
        
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
if __name__ == "__main__":
    scene = GraficaCompuesta()
    scene.render()
