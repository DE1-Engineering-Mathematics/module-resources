# complex_numbers.py
# Cosmin Vonsovici Dyson School of Design Engineering

from manim import *
import cmath

"""
(1) FOR MOD ARG PLOTTER, ENTER THE NUMBER BELOW:
"""
number = 0.5 + 1j
"""
Then, render with: manim -pqh complex_numbers.py ComplexPlot

(2) FOR MULTIPLICATION VISUAL, ENTER THE NUMBER TO MULTIPLY THE NUMBER IN (1) BY BELOW:
"""
multiplier = 2 + 1j
""" 
Then, render with: manim -pqh complex_numbers.py ComplexMultiply
"""

class ComplexPlot(Scene):
    def construct(self):

        plane = ComplexPlane()
        plane.set_opacity(0.5)

        vect = Vector(plane.n2p(number), color = GREEN)
        angle = Angle(Vector([1, 0]), vect)
        arg = Text("" + str(np.round(vect.get_angle(), 2)) + ".. rad", color = YELLOW).next_to(
                                                angle.get_end(), buff = 0.5).scale(0.5)
        mod = Text("" + str(np.round(vect.get_length(), 2)) + "..", color = RED).next_to(
                                                            vect.get_center(), buff = 0.5)

        self.play(Create(plane),
                  GrowArrow(vect),
                  Write(Text("Modulus", color = RED).to_corner(UP + LEFT)),
                  Write(Text("Argument", color = YELLOW).to_corner(UP + RIGHT)))
        self.wait()
        self.play(Create(angle),
                  Write(arg),
                  Write(mod))

class ComplexMultiply(Scene):
    def construct(self):

        plane = ComplexPlane()
        plane.set_opacity(0.5)
        
        vect1 = Vector(plane.n2p(number), color = GREEN)
        vect2 = Vector(plane.n2p(multiplier), color = YELLOW)
        vect3 = Vector(plane.n2p(number * multiplier), color = PURPLE)

        reference = DashedLine([0, 0, 0], [1, 0, 0])
        angle1 = Angle(reference, vect1, radius = 0.3, color = GREEN)
        angle2 = Angle(reference, vect2, radius = 0.5, color = YELLOW)
        vg = VGroup(reference, vect2, angle2)

        self.play(Create(plane))
        self.play(GrowArrow(vect1))
        self.play(Create(reference))
        self.play(Create(angle1))
        self.play(GrowArrow(vect2))
        self.play(Create(angle2))
        self.play(Rotate(vg, vect1.get_angle(), about_point = [0, 0, 0]))
        self.wait(2)
        self.play(Transform(vect2, vect3))
        self.wait(2)

class SineCurveUnitCircle(Scene):
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)