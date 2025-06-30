
import random
import threading
import time

def generate_numbers():
    # Generates 100 random integers between 0 and 10000
    numbers = [random.randint(0, 10000) for _ in range(100)]
    return numbers

def run_with_threads():
    thread_list = []
    start_ns = time.time_ns()

    for _ in range(3):
        thread = threading.Thread(target=generate_numbers)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    return time.time_ns() - start_ns

def run_without_threads():
    start_ns = time.time_ns()

    for _ in range(3):
        generate_numbers()

    return time.time_ns() - start_ns

# Conduct 10 rounds of performance testing
timing_mt = []
timing_nmt = []

for _ in range(10):
    timing_mt.append(run_with_threads())
    timing_nmt.append(run_without_threads())

# Calculate differences and averages
timing_diff = [mt - nmt for mt, nmt in zip(timing_mt, timing_nmt)]

total_mt = sum(timing_mt)
total_nmt = sum(timing_nmt)
average_mt = total_mt / len(timing_mt)
average_nmt = total_nmt / len(timing_nmt)
average_diff = average_mt - average_nmt

# Output table
print("\nComparison of Execution Times Per Round:")
print("+--------+----------------------------+-------------------------------+---------------------------+")
print("| Round  | With Threads (ns)         | Without Threads (ns)         | Time Difference (ns)      |")
print("+--------+----------------------------+-------------------------------+---------------------------+")
for idx, (mt, nmt, diff) in enumerate(zip(timing_mt, timing_nmt, timing_diff), start=1):
    print(f"| {idx:<6} | {mt:<26} | {nmt:<29} | {diff:<25} |")
print("+--------+----------------------------+-------------------------------+---------------------------+")

# Summary
print("\nOverall Summary:")
print("+-------------------+----------------------------+-------------------------------+---------------------------+")
print("| Metric            | With Threads (ns)         | Without Threads (ns)         | Time Difference (ns)      |")
print("+-------------------+----------------------------+-------------------------------+---------------------------+")
print(f"| Total Time        | {total_mt:<26} | {total_nmt:<29} | {total_mt - total_nmt:<25} |")
print(f"| Average Time      | {average_mt:<26.1f} | {average_nmt:<29.1f} | {average_diff:<25.1f} |")
print("+-------------------+----------------------------+-------------------------------+---------------------------+")
