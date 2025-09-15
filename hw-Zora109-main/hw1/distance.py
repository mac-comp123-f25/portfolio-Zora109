import math

x1, y1 = 10, 20
x2, y2 = -5, -10
distance_1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
midpoint_1 = ((x1 + x2) / 2, (y1 + y2) / 2)
print('distance:', round(distance_1, 1), 'midpoint:', midpoint_1)

x3, y3 = 0.5, -1.9
x4, y4 = -3.7, 2.4
distance_2 = math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
midpoint_2 = ((x3 + x4) / 2, (y3 + y4) / 2)
print('distance:', round(distance_2, 1), 'midpoint:', midpoint_2)