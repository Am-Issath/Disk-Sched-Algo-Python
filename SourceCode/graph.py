import matplotlib.pyplot as plt
from disk_scheduling import FCFS, SSTF, SCAN, CSCAN, CLOOK


def graphy(request_arr, start):
    plot_list = []
    algos = ["FCFS", "SSTF", "SCAN", "CSCAN", "CLOOK"]
    dummy = 0
    request = list(request_arr.split(" "))
    request = [int(i) for i in request]
    _, dummy = FCFS(request, start)
    plot_list.append(dummy)
    _, dummy = SSTF(request, start)
    plot_list.append(dummy)
    _, dummy = SCAN(request, start)
    plot_list.append(dummy)
    _, dummy = CSCAN(request, start)
    plot_list.append(dummy)
    _, dummy = CLOOK(request, start)
    plot_list.append(dummy)

    # Stylish Graph
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(algos, plot_list, color='#176B87')

    # Set plot title and labels
    ax.set_title('Total Head Movement Graph', fontsize=14)
    ax.set_xlabel('Algorithm', fontsize=12)
    ax.set_ylabel('Total Head Movement', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()
