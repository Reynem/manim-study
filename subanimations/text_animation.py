from manim import *

def textAnimation(textObject: Text):
    return Succession(
        Write(textObject),
        Wait(1),
        textObject.animate.shift(UP * 2).scale(0.7),
        Wait(0.5),
    )