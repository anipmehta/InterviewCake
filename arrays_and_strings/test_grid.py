'''
    Linearly interpolate down a path of points by
    a ratio of the path's length.
'''

import math


def interp(points, ratio):
    # do stuff here
    previous_x = points[0][0]
    previous_y = points[0][1]
    total_distance = 0
    distances = []
    for i in range(1, len(points)):
        current_x = points[i][0]
        current_y = points[i][1]
        current = pow(abs(current_x - previous_x), 2) + pow(abs(current_y - previous_y), 2)
        current = pow(current, 0.5)
        total_distance += current
        previous_x = current_x
        previous_y = current_y
        distances.append(current)
    target = total_distance * ratio
    previous_sum = 0
    point_a_index = None
    point_b_index = None
    for i in range(len(distances)):
        if previous_sum+distances[i] > target:
            point_a_index = i
            point_b_index = i - 1
            break
        previous_sum += distances[i]
    import pdb;pdb.set_trace()
    current = points[point_a_index]
    previous = points[point_b_index]
    line_segment = pow(abs(previous[1] - current[1]), 2) + pow(abs(previous[0] - current[0]), 2)
    ratio = line_segment / (target - previous_sum)
    ratio = 1 /ratio
    x = previous[0] + (current[0] - previous[0]) * ratio
    y = previous[1] + (current[1] - previous[1]) * ratio
    delta_x = x - previous[0]
    delta_y = y - previous[1]
    angle = math.atan2(delta_y, delta_x)
    return x, y, angle


# radians
# 0 : right
# pi/2 : up
# pi : left


# ==========  TESTING  ==========

# TEST HELPER
def print_test(points, ratio):
    x, y, angle = interp(points, ratio)
    print("Ratio: {:2.1f}    choord:  {:4.2f}, {:4.2f}    angle: {:4.2f}".format(ratio, x, y, angle))


# TEST DATA
test_points_a = [
    (2, 3),  # origin
    (3, 4),  # 1
    (4, 8),  # 3
    (0, 0),  # 4
    (-5, -2),  # 5  (total: 13)
]
ratio = 0.3
print interp(test_points_a, ratio)
test_points_b = [
    (0, 0),
    (1, 2),
    (2, 24)
]
# 0.5*2.24 = 1.12
# x, y

# 1/1 - pi/4
# 4 - itan(4)


# add up all distances
# multiply by ratio to get target distance
# using target distance you can solve for which points the desired XY is between
# interpolate between those two points by remaining ratio to get final X,Y

# we need ratio between two target points
# ratio = current_line_seg_len / (target_dist - previous_sum)

# final_point = first + (second - first) * ratio
# heading = atan2(delta_y, delta_x)


#      (1,1)
#     /       \
#    /            \
# (0,0)            (4,0)


# (0)------(4)

# inter
# 0.0 : 0
# 1.0 : 4
# 0.5 : 2
# 0.25 : 1


# TEST CASES
print_test(test_points_a, 0.3)  # 3.81, 7.62    angle: -2.03
print_test(test_points_b, 0.5)  # 0.5, 1
