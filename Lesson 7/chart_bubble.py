import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

arr = random.sample(range(1000), 10)

def bubble_sort(arr):
    steps = []
    print(f"Unsorted array: {arr}")
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
                swapped = True
        if not swapped:
            break
    return steps

def visualize_bubble_sort(arr):
    steps = bubble_sort(arr)
    
    fig, ax = plt.subplots()
    
    ax.set_title("Step by step bubble sort")
    bar_rects = ax.bar(range(len(arr)), arr, align='edge', color='green')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 5)
    text = ax.text(0.02, 0.95, "", transform = ax.transAxes)
    
    def update_bars(frame):
        for rect, val in zip(bar_rects, steps[frame]):
            rect.set_height(val)
        text.set_text(f"Step {(frame+1):02}/{len(steps)}")
        return bar_rects
    
    ani = animation.FuncAnimation(fig, update_bars, frames=len(steps), interval = 1000, repeat = False)
    
    plt.show()
    
visualize_bubble_sort(arr)