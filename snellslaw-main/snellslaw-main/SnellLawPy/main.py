import numpy as np
import matplotlib.pyplot as plt
import math

divs = 40
n = list(np.flip(np.arange(1.8, 2.5, 1 / divs)))
initial_angle = math.radians(45)


def f(x):
    return math.tan(math.pi / 2 + initial_angle) * x + n[0]


initial_p1 = [(-1 / divs) / (math.tan(math.pi / 2 + initial_angle)),
              f((-1 / divs) / (math.tan(math.pi / 2 + initial_angle)))]


def angle_2(n_1, n_2, angle_1):
    if (n_1 * math.sin(angle_1)) / n_2 < 1:
        return (
            math.asin(
                (n_1 * math.sin(angle_1)) / n_2
            )
        )
    else:
        return 0


def snell_point_angle(n_1, n_2, angle_1, p1):
    ng2 = angle_2(n_1, n_2, angle_1)

    m = math.tan(ng2 + math.pi / 2)
    b = p1[1] - m * p1[0]

    return [ng2, [((n_2 + 1 / divs) - b) / m, n_2 + 1 / divs]]


pts = [initial_p1]
angles = [initial_angle]

for index, value in enumerate(n):
    if index + 1 < len(n) - 1:
        if snell_point_angle(value, n[index + 1], angles[index], pts[index])[0] == 0:
            break
        if index < len(n) - 1:
            plt.axhline(y=pts[index][1], color='r', linestyle='-')
            pts.append(snell_point_angle(value, n[index + 1], angles[index], pts[index])[1])
            angles.append(snell_point_angle(value, n[index + 1], angles[index], pts[index])[0])
            print(pts[index])

fig, ax = plt.subplots()

ax.grid(axis='y')

plt.scatter(*zip(*pts))

plt.plot(*zip(*pts))

fig.suptitle('Snell"s Law', fontsize=30)
plt.gcf().set_size_inches(13, 9)
plt.savefig("main.png", dpi=200)
