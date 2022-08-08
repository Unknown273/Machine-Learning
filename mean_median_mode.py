import statistics

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
speed.sort()


def calculate_mean():
	mean_speed = statistics.mean(speed)

	print(f"{mean_speed:.2f}")


def calculate_median():
	median_speed = statistics.median(speed)

	print(median_speed)


def calculate_mode():
	mode_speed = statistics.mode(speed)

	print(mode_speed)


def calculate_range():
	speed_range = speed[len(speed) - 1] - speed[0]

	print(speed_range)


if __name__ == '__main__':
	print(f"Data set: {speed}\n")
	calculate_mean()
	calculate_median()
	calculate_mode()
	calculate_range()
