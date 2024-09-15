from manim import *

class Ejemplo226(Scene):
    def construct(self):
        # Ejemplo 2.2.6 - Primera parte
        ejemplo_226_1 = Tex(
            r"Ejemplo. Resolver la ecuación diferencial $y^{\prime}=2 x \sqrt{y-1}$.\\",
        ).scale(0.8).to_edge(UP)

        # Mostrar primera parte
        self.play(Write(ejemplo_226_1))
        self.wait(2)
        self.play(FadeOut(VGroup(ejemplo_226_1)))

        ejemplo_226_2 = Tex(
            r"Solución. Separando las variables e integrando:"
            r"$$\frac{d y}{d x}=2 x(y-1)^{\frac{1}{2}} \Rightarrow(y-1)^{-\frac{1}{2}} d y=2 x d x$$"
            ).scale(0.8).to_edge(UP)



        self.play(Write(ejemplo_226_2))
        self.wait(2)



        ejemplo_226_3 = Tex(
            r"$$\Rightarrow \int(y-1)^{-\frac{1}{2}} d y=2 \int x d x \Rightarrow 2(y-1)^{\frac{1}{2}}+C_{1}=x^{2}+C_{2}$$"
            ).scale(0.8).next_to(ejemplo_226_2, DOWN)

        self.play(Write(ejemplo_226_3))
        self.wait(2)


        ejemplo_226_4 = Tex(
            r"$$\Rightarrow 2(y-1)^{\frac{1}{2}}=x^{2}+C$$", 
            ).scale(0.8).next_to(ejemplo_226_3, DOWN)


        self.play(Write(ejemplo_226_4))
        self.wait(2)


        ejemplo_226_5 = Tex(
            r"Elevando al cuadrado:",
            r"$$4(y-1)=\left(x^{2}+C\right)^{2}$$"
        ).scale(0.8).next_to(ejemplo_226_4, DOWN)

        self.play(Write(ejemplo_226_5))
        self.wait(2)

        ejemplo_226_6 = Tex(
            r"$$\Rightarrow y=1+\frac{1}{4}\left(x^{2}+C\right)^{2}$$"
        ).scale(0.8).next_to(ejemplo_226_5, DOWN)

        self.play(Write(ejemplo_226_6))
        self.wait(2)

        rectanguloA = SurroundingRectangle(ejemplo_226_6, color=YELLOW, buff=0.2)
        self.play(Create(rectanguloA), run_time=2)

        ejemplo_226_7 = Tex(
            r"Esta última expresión representa la solución general de la ED en forma explícita.",
        ).scale(0.8).next_to(ejemplo_226_6, DOWN)

        self.play(Write(ejemplo_226_7))
        self.wait(2)


        self.play(FadeOut(VGroup(ejemplo_226_2, ejemplo_226_3, ejemplo_226_4, ejemplo_226_5, ejemplo_226_6, ejemplo_226_7, rectanguloA)))


class Ejemplo227(Scene):
    def construct(self):
        # Ejemplo 2.2.7 - Primera parte
        ejemplo_227_1 = Tex(
            r"Ejemplo 2.2.7 Resolver el PVI $y^{\prime}=x y+x-2 y-2$, con la condición $y(0)=2$.\\"
            r"$Para separar las variables, comenzamos factorizando y después integramos:",
            r"$$\frac{d y}{d x}=x(y+1)-2(y+1)=(y+1)(x-2)$$"
            r"$$\Rightarrow \frac{d y}{y+1}=(x-2) d x$$"
            r"$$\Rightarrow \int \frac{d y}{y+1}=\int (x-2) d x \Rightarrow \ln (y+1)+C_{1}=\frac{1}{2}(x-2)^{2}+C_{2}$$",
        ).scale(0.8).shift(UP)

        # Mostrar primera parte
        self.play(Write(ejemplo_227_1))
        self.wait(2)

        # Ejemplo 2.2.7 - Segunda parte
        ejemplo_227_2 = Tex(
            r"Para determinar $C$, consideramos la condición inicial $y(0)=2$: ",
            r"$$\ln 3=\frac{1}{2}(-2)^{2}+C \Rightarrow C=\ln 3-2$$"
            r"$$\ln (y+1)=\frac{1}{2}(x-2)^{2}+\ln 3-2$$",
            r"De donde:",
            r"$$y=3 e^{\frac{1}{2}(x-2)^{2}-2}-1$$"
        ).scale(0.8).shift(DOWN)

        # Mostrar segunda parte
        self.play(Write(ejemplo_227_2))
        self.wait(2)
