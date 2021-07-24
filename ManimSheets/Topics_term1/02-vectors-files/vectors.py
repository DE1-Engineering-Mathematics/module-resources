# vectors.py
# Cosmin Vonsovici Dyson School of Design Engineering

from manim import *

"""
(1) FOR DOT PRODUCT, ENTER THE VECTORS BELOW:
"""
v1_dot = np.array([-2.5, -3.5])
v2_dot = np.array([2, 1])
"""
Then, render with: manim -pqh vectors.py DotProduct

(2) FOR CROSS PRODUCT, ENTER THE VECTORS BELOW:
"""
v1_cross = np.array([-0.5, 0.7, 0.2])
v2_cross = np.array([-0.4, -1, -1.2])
"""
Then, render with: manim -pqh vectors.py CrossProduct
"""

class DotProduct(VectorScene):        
    def projection(self, vector1, vector2):
        projection = np.dot(vector1, vector2) / np.linalg.norm(vector2)
        unit_vector = vector2 / np.linalg.norm(vector2)
        return projection * unit_vector

    def brace(self, vector):
        return BraceBetweenPoints([0, 0, 0], vector.get_end(), color = BLUE, buff = 1.4)

    def construct(self):
        plane = NumberPlane(x_range = [-5, 5, 1],
                            y_range = [-5, 5, 1], 
                            x_length = 10, 
                            y_length = 10)  
        plane.set_opacity(0.2)

        v1 = Vector(direction = v1_dot, color = GREEN)
        v2 = Vector(direction = v2_dot, color = RED)

        t1 = v1.copy()
        t2 = v2.copy()

        proj1 = Vector(direction = self.projection(v1_dot, v2_dot), color = PURPLE)
        proj2 = Vector(direction = self.projection(v2_dot, v1_dot), color = PURPLE)

        line1 = DashedLine(v1.get_end(), proj1.get_end())
        line2 = DashedLine(v2.get_end(), proj2.get_end())

        b1 = self.brace(proj1)
        b2 = self.brace(proj2)
        b3 = self.brace(v2)
        b4 = self.brace(v1)

        b1text = b1.get_text("" + str(np.round(proj1.get_length(), 2)) + "...")
        b1text.set_color(BLUE)
        b2text = b2.get_text("" + str(np.round(proj2.get_length(), 2)) + "...")
        b2text.set_color(BLUE)
        b3text = b3.get_text("" + str(np.round(v2.get_length(), 2)) + "...")
        b3text.set_color(BLUE)
        b4text = b4.get_text("" + str(np.round(v1.get_length(), 2)) + "...")
        b4text.set_color(BLUE)

        self.play(Create(plane), runtime = 2)
        self.wait()
        self.play(GrowArrow(v1),
                  GrowArrow(v2))
        self.play(Create(line1))
        self.play(ReplacementTransform(t1, proj1))
        self.play(FadeIn(b1)) 
        self.play(FadeIn(b3))
        self.play(Write(b1text))
        self.play(Write(b3text))  
        self.wait(5)
        self.play(Uncreate(line1),
                  Uncreate(proj1),
                  FadeOut(b1),
                  FadeOut(b3),
                  Unwrite(b1text),
                  Unwrite(b3text))
        self.play(Create(line2))
        self.play(ReplacementTransform(t2, proj2))
        self.play(FadeIn(b2)) 
        self.play(FadeIn(b4))
        self.play(Write(b2text))
        self.play(Write(b4text))
        self.wait(3)

class CrossProduct(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())

        vector3 = np.cross(v1_cross, v2_cross)

        # Can use "Arrow3D" instead of "Line", but takes hours to render
        v1 = Line(start = [0, 0, 0], end = v1_cross, color = GREEN)
        v2 = Line(start = [0, 0, 0], end = v2_cross, color = RED)
        v3 = Line(start = [0, 0, 0], end = vector3, color = BLUE)

        parallelogram = Polygon([0, 0, 0],
                                v1_cross,
                                v1_cross + v2_cross,
                                v2_cross,
                                color = ORANGE,
                                fill_opacity = 0.5)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(axes),
                  Create(v1),
                  Create(v2))
        self.wait()
        self.play(Create(v3),
                  Create(parallelogram))
        self.wait(20)