import statistics

example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]

x=statistics.mean(example_list)
print(x)


y=statistics.median(example_list)
print(y)


z=statistics.stdev(example_list)
print(z)

p=statistics.variance(example_list)
print(p)