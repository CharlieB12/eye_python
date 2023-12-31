'''
Homework 3:

This program generates an eyeball using points extruding from the circumference of a circle to portray the iris and outer line.

Output: A graph displaying an eyeball with a color entered by the user

Name: Charlie Britt
Date: 12/6/2023

Feature tasks: 1, 2, 3

'''

import sys
sys.path.append('C:\\Users\\cbrit\\gisalgs')
from geom.point import *

import math
import random
import matplotlib.pyplot as plt


# Function to generate points on the circumference of a circle
def generate_points_on_circumference(radius, num_points):
    points = []
    for _ in range(num_points):
        # Generate random angle in radians
        theta = random.uniform(0, 2 * math.pi)
        # Convert polar coordinates to Cartesian coordinates
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        points.append(Point(x, y))
    return points

#Generates 250 points in a radius of 4 to symbolize the iris
iris = generate_points_on_circumference(4, 250)
#Generates 1000 points to make up the outer ring of the eyeball
outer = generate_points_on_circumference(16, 1000)


source = Point(0, 0) #where the points will extrude from
speed0 = 5 # distance moved per round, at source
fraction = 0.01 # speed decreases with distance, at a scale of 0.01

#Defines what the lines extruding from iris will look like
def speed(distance, speed0, fraction):
    speed = speed0 * fraction * distance
    return speed

fig, ax = plt.subplots(1, 1)

#Loops till a valid color is entered
boolean = True
while boolean:
    color = input("Enter an eye color: ")
    try:
        for i in range(15):
            #Alpha value to decrement with every loop
            alpha = 15;
            for p in iris:
                # The distance between the source and p value
                d = source.distance(p)
                #The angle in radians between the x-axis and the line connecting the source and p points
                angle = math.atan2(p.y - source.y, p.x - source.x)
                s = speed(d, speed0, fraction)
                delta = s
                dx = delta * math.cos(angle)
                dy = delta * math.sin(angle)
                # Moves the point outward
                p.x += dx
                p.y += dy
            #Plots the next point based off the change in x and y for every point in iris list.
            ax.scatter([p.x for p in iris], [p.y for p in iris], edgecolors='none', facecolors=color , marker='o', alpha=0.1*alpha/15)
            #Decrease alpha to make each point lighter
            alpha-=1
        boolean = False
    except:
        print("Not a valid color. Try again")

#Plots the outer black circle of eyeball.
ax.scatter([p.x for p in outer], [p.y for p in outer], edgecolors='none', facecolors='black', marker='.', alpha=0.2)

#Plots the pupil and glare in the center of eye.
pupil = plt.Circle((0, 0), 4, color = "black")
glare = plt.Circle((1, 1), 1, color = "white")

#Sets up final plot.
ax.add_artist(pupil)
ax.add_artist(glare)
ax.axis('equal')                        # x and y one the same scale
ax.axes.get_xaxis().set_visible(False)  # don't show axis
ax.axes.get_yaxis().set_visible(False)  # don't show axis
ax.set_frame_on(False)                  # no frame either
plt.show()

