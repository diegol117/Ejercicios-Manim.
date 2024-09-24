from manim import *

class IntervalAB(Scene):
    def construct(self):
        # Set up the number line
        number_line = NumberLine(
            x_range=[-1, 6, 1],  # x_range=[start, end, step]
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP
        )

        # Create open dots at a and b
        dot_a = Dot(point=number_line.number_to_point(1), color=WHITE)
        dot_b = Dot(point=number_line.number_to_point(5), color=WHITE)
        
        # Create the open interval line between (a, b)
        interval_line = Line(
            start=number_line.number_to_point(1),
            end=number_line.number_to_point(5),
            color=YELLOW
        )
        interval_line.set_stroke(width=6)  # Make the line thicker
        
        # Add the number line to the scene first
        self.add(number_line)
        
        # Add dot 'a' and 'b' with labels, but not the line yet
        label_a = Text("a", font_size=24).next_to(dot_a, DOWN)
        label_b = Text("b", font_size=24).next_to(dot_b, DOWN)
        
        # Add dot 'a' and label
        self.add(dot_a, label_a)
        
        # Animate the drawing of the line from 'a' to 'b'
        self.play(Create(interval_line), run_time=2)
        
        # After the line is drawn, add dot 'b' and label
        self.add(dot_b, label_b)
        
        # Optional: Wait for a moment to let the animation linger
        self.wait(1)
