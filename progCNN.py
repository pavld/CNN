import plotter
import water
import sonar

water = water.Water()
(time, signalLeft, signalRight) = water.get_signals(800,30)

plotter = plotter.Plotter(400,400)
plotter.plot(time, signalLeft, "black")
plotter.plot(time, signalRight, "red")
distance = sonar.Sonar().get_coordinates(signalLeft, signalRight)