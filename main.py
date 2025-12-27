from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square() 
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    ob_size_factor = 0.5
    sc_size_factor = 0.1

    plane = NumberPlane(
        x_range=[-50,50,1],
        y_range=[-30,30,1],
        background_line_style={
            "stroke_color": BLUE_E,
            "stroke_width": 1,
            "stroke_opacity": 0.6,
        }
    ).scale(sc_size_factor)

    def construct(self):
        self.add(self.plane)

        circle = Circle(radius=4).scale(self.sc_size_factor)
        circle.set_fill(PINK, opacity=0.5)

        square = Square().scale(self.ob_size_factor)
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)

        self.play(Create(circle), Create(square))

        self.play(Transform(circle, square))
        self.remove(circle)
        
        number_of_spins = 3
        path_line = Line(square.get_center(), square.get_center() + LEFT * number_of_spins)
        self.play(Rotate(square, PI * number_of_spins / 2), MoveAlongPath(square, path_line))

        self.pause(duration=1) # время в секундах


"""
Theta - поворот по оси Oy
Phi - высота камеры (0 - смотрим сверху, 360 - смотрим снизу)
Gamma - поворот вверх или вниз
"""
class MyPrism(ThreeDScene):
    plane = ThreeDAxes(
        x_range=[-10, 10, 1],
        y_range=[-10, 10, 1],
        z_range=[-10, 10, 1],
        axis_config={
            "stroke_color": BLUE_E,
            "stroke_width": 1,
            "stroke_opacity": 0.6,
        }
    )

    def construct(self):
        self.add(self.plane)
        self.set_camera_orientation(theta=135*DEGREES, phi=60*DEGREES, gamma=0*DEGREES, zoom=0.5)

        prismBig = Prism(dimensions=[2, 2, 2])
        prismBig.set_fill(BLUE_E, opacity=0.5)
        self.add(prismBig)

        prismSmall = Prism(dimensions=[1,1,1])
        prismSmall.set_fill(RED, opacity=0.5)

        self.wait(2)

        self.play(Rotate(prismBig, 2 * PI), Transform(prismBig, prismSmall))

        self.wait(1)

class RectangularVolume(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(zoom=0.3)

        self.wait(1)
        
        rectangle = Rectangle(color=RED_E, width=8, height=5)

        header = Text(text="Welcome to my video!")

        self.play(Create(rectangle), Create(header))

        self.wait(1)

        cube = Cube(side_length=1)
        self.play(FadeIn(cube), FadeOut(rectangle), header.animate.shift(UP))
        self.remove(rectangle)

        new_text = (Text("I fucked ur mom btw"))

        self.play(
            ReplacementTransform(header, new_text),
            cube.animate.rotate(40 * DEGREES, axis=Y_AXIS).shift(DOWN)
            )
        header = new_text

        self.wait(1)

class AbsoluteFreaky(Scene):
    def construct(self):
        imageObject = ImageMobject("assets\img\proxy-image.jpg")
        
        self.add(imageObject)

        self.wait(1)
        
        self.play(
            imageObject.animate.shift(DOWN).stretch_to_fit_width(4)
        )

        self.wait(0.5)

        self.play(
            imageObject.animate.rotate(120 * DEGREES).shift(UP * 2 + RIGHT)
        )

        self.wait(0.5)