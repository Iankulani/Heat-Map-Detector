import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re  # To validate IP address format

# Function to generate and display a curve graph
def generate_curve():
    try:
        # Get data from input fields (assuming comma-separated values)
        data_str = data_entry.get()
        data = list(map(float, data_str.split(',')))

        # Validate data
        if len(data) == 0:
            messagebox.showerror("Input Error", "Please enter valid numerical data.")
            return
        
        # Plot the curve graph
        plt.figure(figsize=(6, 4))
        plt.plot(data, marker='o', linestyle='-', color='b')
        plt.title('Curve Graph')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure the data is a comma-separated list of numbers.")

# Function to generate and display a heatmap
def generate_heatmap():
    try:
        # Get data from input fields (assuming space-separated values for matrix)
        data_str = data_entry.get()
        rows = data_str.split(';')
        data = [list(map(float, row.split(','))) for row in rows]

        # Validate data
        if len(data) == 0 or any(len(row) != len(data[0]) for row in data):
            messagebox.showerror("Input Error", "Please enter valid matrix data (rows separated by semicolons, columns by commas).")
            return

        # Plot the heatmap
        plt.figure(figsize=(6, 6))
        sns.heatmap(data, annot=True, cmap='YlGnBu', cbar=True)
        plt.title('Heatmap')
        plt.show()
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure the data is a valid matrix with numbers.")

# Function to validate IP address format
def validate_ip(ip):
    # Regular expression for a valid IP address (IPv4)
    regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    if re.match(regex, ip):
        return True
    else:
        return False

# Function to handle button click and graph selection
def handle_generate():
    ip_address = ip_entry.get()  # Get the IP address entered by the user

    # Validate IP address
    if not validate_ip(ip_address):
        messagebox.showerror("IP Error", "Please enter a valid IP address.")
        return

    print(f"IP Address entered: {ip_address}")  # Optional: You can print or use the IP address for further tasks.

    if graph_choice.get() == "Curve":
        generate_curve()
    elif graph_choice.get() == "Heatmap":
        generate_heatmap()
    else:
        messagebox.showerror("Input Error", "Please select a valid graph type.")

# Set up the main window
root = tk.Tk()
root.title("Cybersecurity Graph and Heatmap Tool")
root.geometry("400x400")  # Increase window size to accommodate IP input field
root.config(bg="skyblue")

# Create the UI elements
tk.Label(root, text="Enter data for graph (comma-separated):", bg="skyblue").pack(pady=5)
data_entry = tk.Entry(root, width=40)
data_entry.pack(pady=5)

tk.Label(root, text="Enter IP Address:", bg="skyblue").pack(pady=5)
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=5)

tk.Label(root, text="Select the graph type:", bg="skyblue").pack(pady=5)
graph_choice = tk.StringVar()
graph_choice.set("Curve")  # Default choice
curve_radio = tk.Radiobutton(root, text="Curve", variable=graph_choice, value="Curve", bg="skyblue")
curve_radio.pack(pady=2)
heatmap_radio = tk.Radiobutton(root, text="Heatmap", variable=graph_choice, value="Heatmap", bg="skyblue")
heatmap_radio.pack(pady=2)

generate_button = tk.Button(root, text="Generate Graph", command=handle_generate, bg="lightgreen")
generate_button.pack(pady=20)

# Run the application
root.mainloop()
