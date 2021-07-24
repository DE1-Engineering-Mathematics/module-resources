# linear_transform.py
# Cosmin Vonsovici Dyson School of Design Engineering

from manim import *

"""
(1) FOR R, ENTER THE TRANSFORMATION SCALAR BELOW:
"""
scalar = -2
"""
Then, render with: manim -pqh linear_transform.py R

(2) FOR R2, ENTER THE TRANSFORMATION MATRIX BELOW:
"""
M2 = np.array([
                [1, 2],
                [-1, 2]
              ])
"""
Then, render with: manim -pqh linear_transform.py R2
To see this applied to just a vector render with: manim -pqh linear_transform.py R2V
The vector input is:
"""
vect = np.array([2, 1])
"""
(3) FOR R3, ENTER THE TRANSFORMATION MATRIX BELOW:
"""
M3 = np.array([
                [2, 1, 0],
                [1, 3, 1],
                [0, 0, 4]
            ])
"""
Then, render with: manim -pqh linear_transform.py R3
"""

class R(LinearTransformationScene):
    def __init__(self):
            LinearTransformationScene.__init__(
                self,
                include_background_plane=False,
                include_foreground_plane=False,
                show_coordinates=False,
                leave_ghost_vectors=False,
                show_basis_vectors=False)

    def construct(self):
        line = NumberLine(x_range=[-5, 5, 1],
                          length=10,
                          color=BLUE,
                          include_numbers=True,
                          numbers_with_elongated_ticks=[0])
        
        vect = Line(start = line.n2p(0), end = line.n2p(1), stroke_color = GREEN).add_tip(tip_length=0.25)
        vect.set_opacity(0.5)

        function = MathTex(str(scalar) + 'x', color = RED).scale(1)
        function.to_edge(UP)
        
        self.play(Create(line),
                  Write(function))
        self.add_vector([1, 0], color = GREEN)
        self.apply_function(lambda x: scalar * x, added_anims= [FadeIn(vect)])
        self.wait()

class R2(LinearTransformationScene):
    def __init__(self):
            LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                leave_ghost_vectors=True,
                show_basis_vectors=True)

    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)
        m.scale(0.75)
        m.to_corner(UP + LEFT)
        m.set_column_colors(GREEN, RED)
        return m

    def construct(self):
        matrix = self.create_matrix(M2)

        rect = Rectangle(height = 2,
                         width = 2, 
                         stroke_color = ORANGE, 
                         fill_color = ORANGE, 
                         fill_opacity = 0.6)

        self.add_transformable_mobject(rect)
        self.add(matrix)
        self.apply_matrix(M2)
        self.wait()

class R2V(LinearTransformationScene):
    def __init__(self):
            LinearTransformationScene.__init__(
                self,
                show_coordinates=True,
                leave_ghost_vectors=False,
                show_basis_vectors=True)

    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)
        m.scale(0.75)
        m.to_corner(UP + LEFT)
        m.set_column_colors(GREEN, RED)
        return m

    def construct(self):
        matrix = self.create_matrix(M2)
        self.add_vector(vect, color = PURPLE)
        self.apply_matrix(M2)
        self.play(Write(matrix))
        self.wait()

class R3(ThreeDScene):

    def create_matrix(self, np_matrix):
        m = Matrix(np_matrix)
        m.scale(0.5)
        m.to_corner(UP + LEFT)
        m.set_column_colors(GREEN, RED, BLUE)
        return m

    def construct(self):
        matrix = self.create_matrix(M3)
        self.add_fixed_in_frame_mobjects(matrix)

        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
    
        cube = Cube(side_length=1 , fill_color=ORANGE, stroke_width=2, fill_opacity=0.5)
        cube.set_stroke(ORANGE)

        # Can use "Arrow3D" instead of "Line", but takes hours to render
        i0 = Line(start = [0, 0, 0], end=[1, 0, 0], color = GREEN)     
        j0 = Line(start = [0, 0, 0], end=[0, 1, 0], color = RED)     
        k0 = Line(start = [0, 0, 0], end=[0, 0, 1], color = BLUE)     

        i1 = Line(start = [0, 0, 0], end = M3[:, 0], color = GREEN)
        j1 = Line(start = [0, 0, 0], end = M3[:, 1], color = RED)
        k1 = Line(start = [0, 0, 0], end = M3[:, 2], color = BLUE)

        anim = ApplyMatrix(M3, cube)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(axes),
                  Create(cube),
                  Create(i0),
                  Create(j0),
                  Create(k0))
        self.wait(2)
        self.play(
            anim,
            Transform(i0, i1, rate_func=anim.get_rate_func(),
                   run_time=anim.get_run_time()),
            Transform(j0, j1, rate_func=anim.get_rate_func(),
                   run_time=anim.get_run_time()),
            Transform(k0, k1, rate_func=anim.get_rate_func(),
                   run_time=anim.get_run_time()))
        self.wait(20)

class NonLinearTransform(Scene):
    def construct(self):
        grid = NumberPlane()

        self.play(Create(grid), run_time=3)
        grid.prepare_for_nonlinear_transform()
        self.play(grid.animate.apply_function(
            lambda p: p + np.array(
                [
                    np.cos(p[1]),
                    np.cos(p[0]),
                    0,
                ]
            )), run_time = 3,
        )