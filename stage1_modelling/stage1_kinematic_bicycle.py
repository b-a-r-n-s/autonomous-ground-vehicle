"""
Stage 1A: Kinematic Bicycle Model - Open Loop Simulation
Project: Autonomous Ground Vehicle Modeling and Control
Author: [Your Name]
Date: January 2026

Purpose: Simulate the kinematic bicycle model with constant inputs
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1. DEFINE VEHICLE PARAMETER
# ============================================================================

L = 2.5  # Wheelbase [meters] - distance between front and rear axle

# ============================================================================
# 2. DEFINE SIMULATION PARAMETERS
# ============================================================================

dt = 0.01          # Time step [seconds]
t_final = 10.0     # Total simulation time [seconds]
time = np.arange(0, t_final, dt)  # Time array from 0 to t_final
N = len(time)      # Number of time steps

print(f"Simulation time: {t_final} seconds")
print(f"Time step: {dt} seconds")
print(f"Number of steps: {N}")

# ============================================================================
# 3. INITIALIZE STATE VECTOR
# ============================================================================

# State vector: x = [x, y, theta, v]
# x: horizontal position [m]
# y: vertical position [m]
# theta: heading angle [rad]
# v: forward velocity [m/s]

# Create array to store states over time
# Shape: (4 rows, N columns) = (4 states, N time steps)
x = np.zeros((4, N))

# Set initial conditions
x[0, 0] = 0.0    # Initial x position = 0 meters
x[1, 0] = 0.0    # Initial y position = 0 meters
x[2, 0] = 0.0    # Initial heading = 0 radians (pointing east)
x[3, 0] = 5.0    # Initial velocity = 5 m/s

print(f"\nInitial state:")
print(f"  Position: ({x[0,0]}, {x[1,0]}) meters")
print(f"  Heading: {np.degrees(x[2,0])} degrees")
print(f"  Velocity: {x[3,0]} m/s")

# ============================================================================
# 4. DEFINE CONTROL INPUTS (OPEN LOOP - CONSTANT)
# ============================================================================

# Input vector: u = [a, delta]
# a: longitudinal acceleration [m/s^2]
# delta: steering angle [rad]

a = 0.0           # Acceleration [m/s^2] - constant speed (cruising)
delta = 0.1       # Steering angle [rad] - constant turn

print(f"\nControl inputs:")
print(f"  Acceleration: {a} m/s^2")
print(f"  Steering angle: {delta} rad ({np.degrees(delta):.2f} degrees)")

# ============================================================================
# 5. SIMULATE VEHICLE MOTION
# ============================================================================

# Kinematic bicycle model equations:
# x_dot = v * cos(theta)
# y_dot = v * sin(theta)
# theta_dot = (v / L) * tan(delta)
# v_dot = a

print(f"\nRunning simulation...")

# Main simulation loop
for k in range(N - 1):
    # Extract current state at time step k
    x_k = x[0, k]        # Current x position
    y_k = x[1, k]        # Current y position
    theta_k = x[2, k]    # Current heading
    v_k = x[3, k]        # Current velocity
    
    # Compute state derivatives (rates of change)
    x_dot = v_k * np.cos(theta_k)
    y_dot = v_k * np.sin(theta_k)
    theta_dot = (v_k / L) * np.tan(delta)
    v_dot = a
    
    # Update state using Euler integration
    # New state = Current state + (rate of change × time step)
    x[0, k+1] = x_k + x_dot * dt
    x[1, k+1] = y_k + y_dot * dt
    x[2, k+1] = theta_k + theta_dot * dt
    x[3, k+1] = v_k + v_dot * dt

print(f"Simulation complete!")
print(f"\nFinal state:")
print(f"  Position: ({x[0,-1]:.2f}, {x[1,-1]:.2f}) meters")
print(f"  Heading: {np.degrees(x[2,-1]):.2f} degrees")
print(f"  Velocity: {x[3,-1]:.2f} m/s")

# ============================================================================
# 6. PLOT RESULTS
# ============================================================================

# Create figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Vehicle path (X vs Y)
axes[0, 0].plot(x[0, :], x[1, :], 'b-', linewidth=2, label='Trajectory')
axes[0, 0].plot(x[0, 0], x[1, 0], 'go', markersize=10, label='Start')
axes[0, 0].plot(x[0, -1], x[1, -1], 'ro', markersize=10, label='End')
axes[0, 0].set_xlabel('X Position [m]', fontsize=12)
axes[0, 0].set_ylabel('Y Position [m]', fontsize=12)
axes[0, 0].set_title('Vehicle Path (Top View)', fontsize=14, fontweight='bold')
axes[0, 0].grid(True)
axes[0, 0].axis('equal')
axes[0, 0].legend()

# Plot 2: X position vs time
axes[0, 1].plot(time, x[0, :], 'b-', linewidth=2)
axes[0, 1].set_xlabel('Time [s]', fontsize=12)
axes[0, 1].set_ylabel('X Position [m]', fontsize=12)
axes[0, 1].set_title('X Position Over Time', fontsize=14, fontweight='bold')
axes[0, 1].grid(True)

# Plot 3: Heading angle vs time
axes[1, 0].plot(time, np.degrees(x[2, :]), 'r-', linewidth=2)
axes[1, 0].set_xlabel('Time [s]', fontsize=12)
axes[1, 0].set_ylabel('Heading θ [degrees]', fontsize=12)
axes[1, 0].set_title('Heading Angle Over Time', fontsize=14, fontweight='bold')
axes[1, 0].grid(True)

# Plot 4: Velocity vs time
axes[1, 1].plot(time, x[3, :], 'g-', linewidth=2)
axes[1, 1].set_xlabel('Time [s]', fontsize=12)
axes[1, 1].set_ylabel('Velocity [m/s]', fontsize=12)
axes[1, 1].set_title('Velocity Over Time', fontsize=14, fontweight='bold')
axes[1, 1].grid(True)

# Adjust layout and show
plt.tight_layout()
plt.savefig('stage1_kinematic_bicycle_results.png', dpi=300, bbox_inches='tight')
print(f"\nPlot saved as 'stage1_kinematic_bicycle_results.png'")
plt.show()
