import tkinter as tk
from tkinter import ttk
import random
import time

button_width = 100  # Ancho fijo para los botones
button_height = 50  # Alto fijo para los botones

# Bubble Sort Algorithm
def bubble_sort(arr, draw_data, time_tick):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw_data(arr, ['red' if x == j or x == j + 1 else 'blue' for x in range(n)])
                time.sleep(time_tick)
        if not swapped:
            break
    draw_data(arr, ['green' for _ in range(n)])

# Selection Sort Algorithm
def selection_sort(arr, draw_data, time_tick):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_data(arr, ['red' if x == i or x == min_idx else 'blue' for x in range(n)])
        time.sleep(time_tick)
    draw_data(arr, ['green' for _ in range(n)])

# Function to draw the array data
def draw_data(arr, color_array):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 900
    bar_width = canvas_width / (len(arr) * 2)
    offset = 30
    spacing = 10
    normalized_data = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_data):
        x0 = i * bar_width + offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(arr[i]))
    window.update_idletasks()

# Generate a random list of numbers
def generate():
    global data
    data = [random.randint(1, 100) for _ in range(13)]
    draw_data(data, ['blue' for _ in range(len(data))])

# Start the sorting algorithm
def start_algorithm():
    global data
    if not data:
        return
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, speed_scale.get())
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, draw_data, speed_scale.get())

# Reset the data
def reset():
    global data
    data = []
    canvas.delete("all")

# Main window
window = tk.Tk()
window.title("Sorting Algorithms Visualization")
window.geometry("700x500")

# Load background image
background_image = tk.PhotoImage(file="C:\\Users\\Usuario\\Downloads\\dg873kd-7f9e093e-6da0-4164-974d-96546cf286a0.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=430, y=0, relwidth=1, relheight=1)

# Frame for buttons and options
frame = tk.Frame(window, width=600, height=380, bg='grey')
frame.grid(row=0, column=0, padx=5, pady=1)

# Canvas for drawing the array
canvas = tk.Canvas(window, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# Label for algorithm selection
algo_label = tk.Label(frame, text="Algoritmo: ", bg='grey', font=("Arial", 12))
algo_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Dropdown menu for algorithm selection
algo_menu = ttk.Combobox(frame, textvariable=tk.StringVar(), values=['Bubble Sort', 'Selection Sort'], font=("Arial", 12))
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# Button to generate random data
gen_button = tk.Button(frame, text="Generar Tabla", command=generate, bg='orange', font=("Arial", 12), height=4, width=12)
gen_button.grid(row=0, column=2, padx=5, pady=5)

# Button to start sorting
start_button = tk.Button(frame, text="Iniciar", command=start_algorithm, bg='green', font=("Arial", 12), height=4, width=12)
start_button.grid(row=0, column=3, padx=5, pady=5)

# Button to reset
reset_button = tk.Button(frame, text="Reinciar", command=reset, bg='red', font=("Arial", 12), height=4, width=12)
reset_button.grid(row=0, column=4, padx=5, pady=5)

# Speed scale
speed_scale = tk.Scale(frame, from_=0.1, to=2.0, length=130, digits=3, resolution=0.2, orient=tk.VERTICAL, label="Select Speed [s]", font=("Arial", 12))
speed_scale.grid(row=0, column=5, padx=5, pady=5)

# Initialize data
data = []

window.mainloop()