"""
Linear Regression
Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit in the
play area. As such, he is working on researching the bounciness of different balls so as to optimize the pit.
He is running an experiment to bounce different sizes of bouncy balls, and then fitting lines to the data points
he records. He has heard of linear regression, but needs your help to implement a
version of linear regression in Python.
Linear Regression is when you have a group of points on a graph, and you find a line that approximately resembles
that group of points. A good Linear Regression algorithm minimizes the error, or the distance from each point to
the line. A line with the least error is the line that fits the data the best. We call this a line of best fit.
We will use loops, lists, and arithmetic to create a function that will find a line of
best fit when given a set of data.
"""

#Function that takes in m, b, and x. (y = m*x + b)
#It should return what the y value would be for that x on that line
def get_y(m, b, x):
    y = m * x + b
    return y

#Testing get_y
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


#calculate_error function which will take in m, b, and an [x, y] point and return the distance between the line and the point.
def calculate_error(m, b, point):
    x_point, y_point = point
    getY = get_y(m, b, x_point)
    distance = getY - y_point
    return abs(distance)

#TESTING the calculate_error function

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))

#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))

#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))

#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


#Reggie's datasets will be sets of points.
#The first datapoint, (1, 2), means that his 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]


#function calculate_all_error, which takes m and b that describe a line, and points, a set of data like the example above.
#calculate_all_error should iterate through each point in points and calculate the error from that point to the line(using calculate_error).
#It should keep a running total of the error, and then return that total after the loop.
def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        calcualteError = calculate_error(m, b, point)
        total += calcualteError
    return total


#TESTING the calculate_all_error function

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


"""
The way Reggie wants to find a line of best fit is by trial and error. He wants to try a bunch of different
slopes (m values) and a bunch of different intercepts (b values) and see which one produces the smallest error
value for his dataset.
"""

#List of possible m values to try
possible_ms = [m*0.1 for m in range(-100, 101)]

#List of possible b values to check
possible_bs = [b*0.1 for b in range(-200, 201)]

#Find the smallest error. Seeing which y = m*x + b line produces the smallest total error with the set of data stored in datapoint.
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

#Iterate through each element m in possible_ms. For every m value, take every b value in possible_bs, If the value
#returned from calculate_all_error on this m value, this b value, and datapoints is less than our current smallest_error,
#set best_m and best_b to be these values, and set smallest_error to this error.
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
            
print(best_m, best_b, smallest_error)



"""
What does our model predict?
Now we have seen that for this set of observations on the bouncy balls, the line that fits the data best has an
m of 0.3 and a b of 1.7:

y = 0.3x + 1.7
This line produced a total error of 5.

Using this m and this b, what does your line predict the bounce height of a ball with a width of 6 to be?
"""

#TESTING y = 0.3x + 1.7 with get_y function
get_y(0.3, 1.7, 6)


"""
Our model predicts that the 6cm ball will bounce 3.5m.

Now, Reggie can use this model to predict the bounce of all kinds of sizes of balls he may choose to include
in the ball pit!
"""
