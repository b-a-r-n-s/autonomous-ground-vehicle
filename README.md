# Simulation and Control of an Autonomous Ground Vehicle Using State Space Modelling and Feedback Control

## Project Overview

This undergraduate Electrical/Electronics Engineering project focuses on modelling and control of an autonomous ground vehicle using state-space concepts, simulation, and feedback control.

The project is being developed incrementally, beginning with a nonlinear kinematic bicycle model and progressing toward feedback control, simulation-based validation, and potentially hardware implementation.

The project is intended as a technical engineering project for learning, documentation, and future implementation.

## Motivation

Autonomous ground vehicles combine mathematical modelling, control systems, simulation, and practical engineering. This project provides a structured way to study those areas by moving from a vehicle model to feedback control and, where appropriate, validation and hardware implementation.

## Technical Stack

- Python
- NumPy
- Matplotlib
- State-space modelling concepts
- Kinematic vehicle modelling
- Feedback control
- PID control
- Linear Quadratic Regulator (LQR) control

## Project Progress

### Stage 1 — Vehicle Modelling

- [x] Define the kinematic bicycle model
- [x] Define vehicle states and control inputs
- [x] Implement open-loop simulation in Python
- [x] Generate vehicle trajectory and state plots
- [x] Document modelling assumptions and conceptual questions

**Status:** Complete

The Stage 1 model uses the state vector

`x = [x, y, θ, v]ᵀ`

and control input vector

`u = [a, δ]ᵀ`.

The nonlinear model is:

```text
ẋ = v cos(θ)
ẏ = v sin(θ)
θ̇ = (v / L) tan(δ)
v̇ = a
```

The simulation uses a wheelbase of 2.5 m, constant acceleration `a = 0`, constant steering `δ = 0.1 rad`, Euler integration, `dt = 0.01 s`, and a 10 s simulation period.

See [`stage1_modelling/stage1_kinematic_bicycle.py`](stage1_modelling/stage1_kinematic_bicycle.py) and [`stage1_modelling/stage1_report.md`](stage1_modelling/stage1_report.md).

### Stage 2 — Feedback Control Design

- [ ] Finalize controller design
- [ ] Implement PID controller
- [ ] Implement LQR controller
- [ ] Compare controller performance
- [ ] Document results

**Status:** In progress

The current project direction is to investigate both PID and LQR control for trajectory/path tracking. Specific design decisions remain subject to finalization before implementation.

### Stage 3 — Simulation-Based Validation

- [ ] Introduce measurement noise
- [ ] Introduce parameter uncertainty
- [ ] Evaluate controller robustness
- [ ] Document validation results

**Status:** Planned

### Stage 4 — Python Performance Analysis

- [ ] Analyze controller performance quantitatively
- [ ] Compare relevant performance measures
- [ ] Document analysis

**Status:** Planned

This stage may be incorporated into the ongoing Python-based implementation rather than being a completely separate reimplementation.

### Stage 5 — Hardware Tie-In (Optional)

- [ ] Explore Arduino implementation
- [ ] Connect simulation concepts to hardware control

**Status:** Optional / planned

## How to Run Stage 1

The Stage 1 simulation requires Python with NumPy and Matplotlib installed.

Run:

```bash
python stage1_modelling/stage1_kinematic_bicycle.py
```

The script prints the simulation configuration and final state, then generates four plots covering:

1. Vehicle path
2. X position over time
3. Heading angle over time
4. Velocity over time

It also saves the generated figure as:

`stage1_kinematic_bicycle_results.png`

## Repository Structure

```text
autonomous-ground-vehicle/
├── README.md
├── stage1_modelling/
│   ├── stage1_kinematic_bicycle.py
│   ├── stage1_report.md
│   └── results/
│       └── stage1_kinematic_bicycle_results.png
├── stage2_control/
│   ├── stage2_pid_control.py
│   ├── stage2_lqr_control.py
│   └── stage2_report.md
├── stage3_validation/
│   └── (uncertainty/noise validation, later)
├── stage4_python_analysis/
│   └── (performance analysis, later)
└── stage5_hardware/
    └── (Arduino tie-in, optional)
```

Only completed and committed work should be treated as implemented. Future stages are intentionally marked as planned or in progress until their code and results are available.

## Author

**Barnabas**  
GitHub: [@b-a-r-n-s](https://github.com/b-a-r-n-s)
