import numpy

raw_data_1 = [86, 87, 88, 86, 87, 85, 86]
raw_data_2 = [32, 111, 138, 28, 59, 77, 97]

std_deviation_raw_data_1 = numpy.std(raw_data_1)
std_deviation_raw_data_2 = numpy.std(raw_data_2)

print(f'{std_deviation_raw_data_1:.2f}')
print(f'{std_deviation_raw_data_2:.2f}')
