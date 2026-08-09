# Stage 1: Vehicle Modelling

## 1. Overview

Stage 1 establishes a foundational mathematical model for the autonomous ground vehicle using the kinematic bicycle model. The model represents the vehicle with four states and two control inputs and is simulated in Python under constant inputs.

The model is intended as a simplified representation of vehicle motion. It assumes flat ground and pure rolling without tire slip, and does not include forces, mass, engine dynamics, or other vehicle dynamics at this stage.

## 2. Model Selection

The **kinematic bicycle model** is used as the vehicle model. It approximates a four-wheeled vehicle as a two-wheeled bicycle model and provides a standard foundational model for studying vehicle motion and control.

The model assumes no tire slip and therefore represents pure rolling motion.

## 3. State Vector

The vehicle state is defined as:

```text
x = [x, y, θ, v]ᵀ
```

where:

- `x`: horizontal position [m]
- `y`: vertical position [m]
- `θ`: heading angle [rad]
- `v`: forward velocity [m/s]

## 4. Control Input Vector

The control input is defined as:

```text
u = [a, δ]ᵀ
```

where:

- `a`: longitudinal acceleration [m/s²]
- `δ`: steering angle [rad]

The wheelbase is represented by the constant parameter:

```text
L = 2.5 m
```

## 5. Governing Nonlinear Equations

The kinematic bicycle model is described by the following equations:

```text
ẋ = v cos(θ)
ẏ = v sin(θ)
θ̇ = (v / L) tan(δ)
v̇ = a
```

The equations are nonlinear because they contain products of state variables and nonlinear trigonometric functions such as `cos`, `sin`, and `tan`.

## 6. Model Assumptions

The Stage 1 model uses the following assumptions:

- Flat ground
- No tire slip
- Pure rolling motion
- No forces or mass dynamics are modelled
- No engine dynamics are modelled
- Wheelbase `L` is constant

## 7. Simulation Setup

The model is implemented in Python using NumPy and Matplotlib.

Simulation parameters:

| Parameter | Value |
|---|---:|
| Wheelbase, `L` | 2.5 m |
| Time step, `dt` | 0.01 s |
| Simulation time | 10 s |
| Initial position | (0, 0) m |
| Initial heading | 0 rad |
| Initial velocity | 5 m/s |
| Acceleration, `a` | 0 m/s² |
| Steering angle, `δ` | 0.1 rad (5.73°) |
| Integration method | Euler integration |

The simulation is open-loop with constant acceleration and steering inputs. Since `a = 0`, the vehicle maintains its initial velocity of 5 m/s.

## 8. Implementation

The complete implementation is contained in:

`stage1_kinematic_bicycle.py`

The script:

1. Defines the vehicle wheelbase.
2. Defines simulation parameters.
3. Initializes the four-state vector.
4. Sets constant control inputs.
5. Computes the state derivatives from the nonlinear model.
6. Updates the states using Euler integration.
7. Displays the final state.
8. Generates four plots of the simulated vehicle motion.

## 9. Conceptual Questions

### 9.1 Why is the model nonlinear?

The governing equations contain products of state variables and nonlinear functions (`cos`, `sin`, and `tan`). They therefore cannot be expressed simply as linear combinations of the states and inputs.

### 9.2 What does the wheel slip assumption mean?

The model assumes pure rolling motion. The wheels roll without sliding, meaning the contact point between the wheel and ground has zero relative velocity and the vehicle does not skid.

### 9.3 What happens as `δ → π/2` (90°)?

As the steering angle approaches 90°, `tan(δ)` approaches infinity. Therefore, according to the model, `θ̇` also approaches infinity. This is physically impossible and exposes a limitation of the kinematic model at extreme steering angles. Real vehicles have physical steering limits, typically on the order of approximately ±30–45°.

### 9.4 What is the physical meaning of `v/L`?

`v/L` represents the vehicle's turning-rate capability or angular velocity potential for a given steering angle, with units of rad/s when combined with the dimensionless `tan(δ)` term. A larger velocity produces a faster heading change for a given steering angle, while a larger wheelbase produces a slower heading change and therefore a less agile turning response.

## 10. Simulation Output

The script generates four plots:

1. Vehicle path (`x` position versus `y` position)
2. X position versus time
3. Heading angle versus time
4. Velocity versus time

The script saves the generated figure as:

`stage1_kinematic_bicycle_results.png`

Expected final state from the provided simulation:

```text
Position: (46.87, 11.73) meters
Heading: 114.59 degrees
Velocity: 5.0 m/s
```

## 11. Stage Status

**Complete**

Stage 1 provides the baseline vehicle model and open-loop simulation on which the subsequent feedback-control work will be developed.
