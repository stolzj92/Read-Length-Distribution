import os 
import sys
import re
sam_file = open(sys.argv[1])
output_file = open("sam_histogram2.csv", "w")
#input the path of the sam file at the command line
histogram = {}
for line in sam_file:
	if line.startswith("D"):
		split = line.split("\t")
		length = split[8]	
		current_count = histogram.get(length, 0)
		new_count = current_count + 1
		histogram[length] = new_count
for length, count in histogram.items():
	output_file.write(length + " * " + str(count) + ",")
