start:
	conda activate manim_env
	manim -pqm main.py

prism:
	manim -pqm main.py MyPrism

fast:
	manim -pql main.py