
import numpy as np


execution_data = np.random.randint(5, 51, size=(5, 50))


average_per_cycle = np.mean(execution_data, axis=1)
max_execution_time = np.max(execution_data)
std_deviation_per_cycle = np.std(execution_data, axis=1)


first_10_cycle1 = execution_data[0, :10]
last_5_cycle5 = execution_data[4, -5:]
alternate_cycle3 = execution_data[2, ::2]


add_cycle1_cycle2 = execution_data[0] + execution_data[1]
sub_cycle1_cycle2 = execution_data[0] - execution_data[1]
mul_cycle4_cycle5 = execution_data[3] * execution_data[4]
div_cycle4_cycle5 = execution_data[3] / execution_data[4]


squared_data = np.power(execution_data, 2)
cubed_data = np.power(execution_data, 3)
sqrt_data = np.sqrt(execution_data)
log_data = np.log(execution_data + 1)


shallow_copy = execution_data.view()
shallow_copy[0, 0] = 100  
deep_copy = execution_data.copy()
deep_copy[0, 1] = 200  


cycle2_above_30 = execution_data[1][execution_data[1] > 30]
consistently_above_25 = execution_data[:, execution_data.min(axis=0) > 25]
thresholded_data = execution_data.copy()
thresholded_data[thresholded_data < 10] = 10


print("Average Execution Time per Cycle:", average_per_cycle)
print("Maximum Execution Time in Dataset:", max_execution_time)
print("Standard Deviation per Cycle:", std_deviation_per_cycle)

print("\nFirst 10 Test Times from Cycle 1:", first_10_cycle1)
print("Last 5 Test Times from Cycle 5:", last_5_cycle5)
print("Alternate Tests from Cycle 3:", alternate_cycle3)

print("\nAddition of Cycle 1 and Cycle 2:", add_cycle1_cycle2)
print("Subtraction of Cycle 1 and Cycle 2:", sub_cycle1_cycle2)
print("Multiplication of Cycle 4 and Cycle 5:", mul_cycle4_cycle5)
print("Division of Cycle 4 and Cycle 5:", div_cycle4_cycle5)

print("\nSquared Execution Times:\n", squared_data)
print("Cubed Execution Times:\n", cubed_data)
print("Square Root of Execution Times:\n", sqrt_data)
print("Logarithmic Transformation:\n", log_data)

print("\nShallow Copy Modified (affects original):", execution_data[0, 0])
print("Deep Copy Modified (original unaffected):", execution_data[0, 1])

print("\nCycle 2 Tests > 30 seconds:", cycle2_above_30)
print("Tests consistently > 25 seconds across all cycles:\n", consistently_above_25)
print("Thresholded Data (values < 10 replaced with 10):\n", thresholded_data)
