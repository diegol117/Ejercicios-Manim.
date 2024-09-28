from manim import *
import numpy as np


class ejemplo(Scene):
    def construct(self):

        # Definir las pendientes y los interceptos
        m1, b1 = 1, 1  # Pendiente e intercepto de la primera recta
        m2, b2 = -1, 3  # Pendiente e intercepto de la segunda recta

        # Crear las ecuaciones de las rectas en función de x
        def recta1(x):
            return np.exp(x-5)

        def recta2(x):
            return 0.5*x

        # Crear los ejes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE,
                         "include_ticks": False}
        )

        # Etiquetas de los ejes
        labels = axes.get_axis_labels(x_label="Time", y_label="Results").set_color(BLUE)

        # Calcular el punto de intersección


        # Convertir el punto de intersección a las coordenadas de los ejes
        punto_interseccion = axes.coords_to_point(3.059, 6.11+1)
        punto_interseccion1 = axes.coords_to_point(7.5, 2.5)
        punto_interseccion2 = axes.coords_to_point(3, 3.5)
        punto_interseccion3 = axes.coords_to_point(9, 5)

        # Crear las rectas
        recta_1 = axes.plot(lambda x: recta1(x), color=TEAL_A, x_range=[0, 7.3])
        recta_2 = axes.plot(lambda x: recta2(x), color=LIGHT_PINK, x_range=[0, 7.3])
        
        # Crear el punto de intersección

        label_punto = Tex(r"Exponential growth ",
                          r"\\(Reality)", color=TEAL_A).next_to(punto_interseccion, UP)
        
        
        label_punto1 = Tex(r"Linear growth ", 
                           r"\\(Expectation)", color=LIGHT_PINK).next_to(punto_interseccion1, DOWN)
        label_punto2 = Tex(f"Impatience for results", color=GOLD).next_to(punto_interseccion2, UP)
        label_punto3 = Tex(f"Real benefits", color=GREY).next_to(punto_interseccion3, UP)

        area = axes.get_area(recta_2, [0, 6.11], bounded_graph=recta_1, color=GOLD, opacity=0.5)
        area1 = axes.get_area(recta_1, [6.12, 7.3], bounded_graph=recta_2, color=GREY, opacity=0.5)
        # Añadir los ejes, las rectas y el punto de intersección a la escena
        self.play(Create(axes), FadeIn(labels))

        self.play(Create(recta_1))
        self.play(FadeIn(label_punto))
    
        self.play(Create(recta_2))
        self.play(FadeIn(label_punto1))

        self.play(FadeIn(area))
        self.play(FadeIn(label_punto2))
        # Animación final: resaltar el punto de intersección
        self.play(FadeIn(area1))
        self.play(FadeIn(label_punto3))

        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )