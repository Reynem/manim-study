from manim import *
from subanimations.text_animation import textAnimation


class MainScene(Scene):
    def construct(self):
        welcomeTextObj = Text("Monkeys of our School")
        self.play(textAnimation(welcomeTextObj))

        A = LEFT * 3 + DOWN * 2
        B = LEFT + DOWN * 2
        C = LEFT + UP
        D = LEFT * 3 + UP
        
        triangleObject = Polygon(
            A, B, C, D,
            color=WHITE,
            stroke_width=4,
            fill_color=BLUE,
            fill_opacity=0.3
        )
        self.play(Create(triangleObject))

        self.wait(1)

        descriptionTextObj = Text("Here you can see\nexample of a monkey ", font_size=DEFAULT_FONT_SIZE / 1.5).next_to(triangleObject, RIGHT, buff=1.5)
        arrow = Arrow(start=descriptionTextObj.get_left(), end=triangleObject.get_right(), color=BLUE_E, buff=0.25)

        self.play(Create(descriptionTextObj), Create(arrow))

        self.wait(2)