import random
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def counting_sort(arr, arr_len, k):
    count = np.zeros(k + 1, dtype=np.uint32)
    output = np.zeros(arr_len, dtype=np.uint32)

    for i in range(arr_len):
        count[arr[i]] += 1

    for i in range(1, k + 1):
        count[i] = count[i] + count[i - 1]

    for i in range(arr_len - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output.tolist()


def run_experiment(max_value, total_values):
    arr = random.choices(range(max_value), k=total_values)

    start_time = time.time_ns()
    counting_sort(arr, total_values, max_value)
    elapsed_time = (time.time_ns() - start_time) / 1_000_000

    return elapsed_time


def run_experiments(total_experiments):
    total_k = []
    total_n = []
    res_times = []

    for i in range(total_experiments):
        print(f"\rRunning experiment {i + 1} out of {total_experiments}...", end="")

        k = random.randrange(1_000, 1_000_000)
        n = random.randrange(10_000, 100_000)
        res_time = run_experiment(k, n)

        total_k.append(k)
        total_n.append(n)
        res_times.append(res_time)

    sns.set_theme(style="whitegrid")
    df = pd.DataFrame({
        "n": np.array(total_n),
        "k": np.array(total_k),
        "time": np.array(res_times),
    })

    sns.relplot(data=df, x="n", y="time", hue="k")
    plt.show()

    print(f"\rFinished running all {total_experiments} experiments...")


if __name__ == "__main__":
    run_experiments(100)
