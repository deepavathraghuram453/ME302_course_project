import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('Compressor_operation_map.txt')

# Extract columns
mdot_ref = data[:, 0]  # kg/s (X-axis)
T0_ratio = data[:, 1]
P0_ratio = data[:, 2]  # (Y-axis)

# Calculate scale
scale = (mdot_ref / P0_ratio)**0.5 * (T0_ratio)**0.25 * 0.206

# Find max scale point
max_scale = np.max(scale)
max_index = np.argmax(scale)

print(f"Max scale: {max_scale:.6f} at index {max_index}")
print(f"mdot_ref: {mdot_ref[max_index]:.2f} kg/s, P0_ratio: {P0_ratio[max_index]:.2f}")

# Create plot
plt.figure(figsize=(10, 6))

# Plot mdot_ref (X) vs P0_ratio (Y)
plt.plot(mdot_ref, P0_ratio, 'b-', label='Compressor Data')
plt.scatter(mdot_ref[max_index], P0_ratio[max_index], 
            color='red', s=100, label=f'Max Scale = {max_scale:.2f}')

# Set axis labels & ticks
plt.xlabel('mdot_ref (kg/s)')  # X-axis
plt.ylabel('P0_ratio')         # Y-axis

# Customize Y-axis (P0_ratio: 1.21, 1.22, ..., 1.27)
plt.yticks(np.arange(1.21, 1.28, 0.01))  

# Customize X-axis (mdot_ref: 9.0, 9.5, 10.0, etc.)
plt.xticks(np.arange(9.0, 10.6, 0.5))  

plt.title('Compressor Map: mdot_ref vs P0_ratio')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()