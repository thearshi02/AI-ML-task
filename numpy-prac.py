import numpy as np
#Using numpy, compute the mean, median, highest, lowest, and standard deviation, then print how many students scored above the mean
marks=np.array([72, 85, 90, 66, 78, 88, 95, 60, 74, 81])
mean=np.mean(marks)
median=np.median(marks)
highest=np.max(marks)
lowest=np.min(marks)
std_dev=np.std(marks)
student=np.sum(marks>mean)
print(mean)
print(median)
print(highest)
print(lowest)
print(std_dev)
print(student)

