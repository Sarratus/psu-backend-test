import numpy as np
import math

np.seterr(all='raise')


def inputCheck(testType, *matchValue):
	while True:
		try:
			answer = testType(input())
			if matchValue and answer not in matchValue:
				raise ValueError

			return answer
		except ValueError:
			print("Неверная форма входных данных. Попробуйте ещё раз:")


print("Введите число точек n:")
numpoints = inputCheck(int)

# Создание массива случайных точек
randomGenerator = np.random.default_rng()
points = randomGenerator.integers(-100, 100, (numpoints, 2), endpoint=True)

# Исключение из массива нулевых векторов
nonZeroPoints = points[[True if point.any() else False for point in points]]
isThereZeroVector = True if len(nonZeroPoints) != len(points) else False

# Нахождение длины каждого вектора
lengthOfVectors = [
	np.sqrt(
		np.sum(
			np.power(point, 2)
		)
	)
	for point in nonZeroPoints
]

# Создание массива нормализованных исходных векторов
normalizedVectors = [
	np.divide(nonZeroPoints[i], lengthOfVectors[i])
	for i in range(len(nonZeroPoints))
]

answer = []
i = 0
# Вычисления угла, учитывая, что x = cos(x), y = sin(x) (т.к. окружность единичная)
for vector in normalizedVectors:
	xAngle = math.degrees(np.arccos(vector[0]))
	angle = xAngle if vector[1] >= 0 else 360 - xAngle
	# Пермещение начала отсчёта
	angle += -90 if angle >= 90 else 270
	answer.append({'index': i, 'pointCords': nonZeroPoints[i], 'angle': angle})

	i += 1

# Сортировка по углу
answer.sort(key=lambda Dict: Dict['angle'])
# Вставка первого элемента из первой четверти
answer = answer[-1:] + answer[:-1]
pointsOrder = [item['index'] for item in answer]
# Применение порядка индексов из сортированного массива
nonZeroPoints = nonZeroPoints[pointsOrder]


print(nonZeroPoints)
print(
	f"Расстояния точек от центра координат:\n"
    f"\t> минимальное: {0 if isThereZeroVector else np.min(lengthOfVectors)}\n"
    f"\t> среднее: {np.average(lengthOfVectors)}\n"
    f"\t> максимальное: {np.max(lengthOfVectors)}\n"
)

# Раскомментировать, если нужно сгенерировать анимацию (требуется matplotlib и imagemagick)

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig = plt.figure()
# ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
# dots, = ax.plot([], [], '.', lw=3)
#
#
# def init():
# 	dots.set_data([], [])
# 	return dots,
#
#
# def animate(i):
# 	dots.set_data(nonZeroPoints[:i, 0], nonZeroPoints[:i, 1])
# 	return dots,
#
#
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=numpoints, interval=16.67, blit=True)
# anim.save('animation.gif', writer='imagemagick')


# ^-^
