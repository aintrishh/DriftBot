# DriftBot v1.0 - Basic Aerodynamic Simulator
# Author: ainttrishh

rho = 1.225  # air density (kg/m³)

speed = float(input("Enter car speed (m/s): "))
area = float(input("Enter frontal area (m²): "))
Cd = float(input("Enter drag coefficient: "))
Cl = float(input("Enter lift coefficient (negative for downforce): "))


drag_force = 0.5 * rho * (speed**2) * Cd * area
lift_force = 0.5 * rho * (speed**2) * Cl * area

print(f"\n--- DriftBot Aerodynamic Analysis ---")
print(f"Speed: {speed} m/s")
print(f"Drag Force: {drag_force:.2f} N")
print(f"Lift/Downforce: {lift_force:.2f} N")
