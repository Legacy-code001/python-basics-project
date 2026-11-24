# ### Task 4: Monitor and Filter Temperature Readings

# **Scenario:** At **AtliQ**, your next ad-hoc task involves monitoring equipment sensor data to promptly identify any readings that suggest potential overheating. The sensor data file ```sensor_data.txt``` is so HUGE that you can't read it all at once (For this exercise we have given a small file but just assume that in real life such a file will be pretty HUGE).

# **Objective:** Develop a Python program with a generator function `read_and_filter_temperatures` that efficiently processes this large dataset by:

# 1. Taking two parameters: ```filename``` (the name of the sensor data file) and ```threshold``` (the temperature limit that indicates overheating).
# 2. Yielding temperatures that exceed the specified threshold.
# 3. Printing each critical temperature reading as it's identified to allow immediate action.

def read_and_filter_temperature(filename, threshold):
    with open(filename, 'r') as f:
        for line in f:
            result = line.strip().split(",")
            temp = float(result[1])
            if temp > threshold:
                yield temp
greater_temp = read_and_filter_temperature("sensor_data.txt", 20)
print(iter(greater_temp))
print(next(greater_temp))
print(next(greater_temp))

