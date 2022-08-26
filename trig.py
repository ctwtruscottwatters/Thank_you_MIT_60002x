import os
import datetime
import numpy as np
import pandas
import sklearn
import math
from matplotlib import pyplot as plot

def main():
	x = []
	y = []
	x_1 = []
	y_1 = []
	x_2 = []
	y_2 = []
	for q in range(-360, 360 + 5, 5):
		x.append((q * (math.pi / 180)))
	for r in range(-360, 360 + 5, 5):
		x_1.append((r * (math.pi / 180)))
		x_2.append((r * (math.pi / 180)))
		y.append(math.sin(r * (math.pi / 180)))
		y_1.append(math.cos(r * (math.pi / 180)))
		y_2.append(math.tan(r * (math.pi / 180)))
	plot.figure(1)
	plot.title("Charles Truscott Watters")
	plot.ylabel("sine x")
	plot.xlabel("x = -360 to 360 degrees in intervals of five degrees")
	plot.plot(x, y)
	plot.show()
	plot.savefig('./sineCharlesTruscott.jpg')
	plot.figure(2)
	plot.title("Charles Truscott Watters")
	plot.ylabel("cosine x")
	plot.xlabel("x = -360 to 360 degrees in intervals of five degrees")
	plot.plot(x_1, y_1)
	plot.show()
	plot.savefig('./cosineCharlesTruscott.jpg')
	plot.figure(3)
	plot.title("Charles Truscott Watters")
	plot.ylabel("tangent x")
	plot.xlabel("x = -360 to 360 degrees in intervals of five degrees")
	plot.plot(x_2, y_2)
	plot.show()
	plot.savefig('./tangentCharlesTruscott.jpg')

if __name__ == "__main__": main()