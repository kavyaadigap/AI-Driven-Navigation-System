
# AI-Driven Autonomous Spacecraft Navigation & Space Debris Avoidance 🚀

This project simulates an **AI-driven autonomous spacecraft navigation system** that avoids **space debris** while navigating through space. The spacecraft starts at a predefined position and navigates toward a target destination, using a reactive AI algorithm to avoid collisions with space debris.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [How It Works](#how-it-works)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Visualization](#visualization)


---

## Overview 🌌

The goal of this project is to demonstrate how AI-inspired algorithms can be used for **autonomous navigation** in space. The spacecraft must navigate through a field of space debris (defunct satellites, rocket bodies, and fragments) to reach its destination safely. The system combines:
- A **desired direction** (toward the destination).
- An **avoidance vector** (away from debris).

The simulation is visualized in **3D** using Plotly, and the entire application is built with **Streamlit** for an interactive user experience.

---

## Features ✨

- **Realistic Space Debris Data**: Uses real-world space debris data to simulate obstacles.
- **AI-Driven Navigation**: Combines desired direction and avoidance vectors for smooth navigation.
- **3D Visualization**: Interactive 3D plot to visualize the spacecraft's trajectory, debris, and destination.
- **Customizable Parameters**: Adjust simulation parameters like speed, safe margin, and weight for desired direction vs. avoidance.

---

## Technologies Used 💻

- **Python**: Core programming language.
- **NumPy**: For numerical computations and vector math.
- **Pandas**: For processing and analyzing the space debris dataset.
- **Streamlit**: For building the interactive web application.
- **Plotly**: For creating 3D visualizations of the simulation.
- **Git**: For version control.

---

## Dataset 📊

The project uses a dataset containing information about space debris, including:
- `OBJECT_NAME`: Name of the debris object.
- `MEAN_MOTION`: Mean motion of the object (revolutions per day).
- `INCLINATION`: Orbital inclination (degrees).
- `RA_OF_ASC_NODE`: Right ascension of the ascending node (degrees).
- `X`, `Y`, `Z`: Randomly generated positions for the debris in 3D space.
- `Radius`: Randomly generated size of the debris.

The dataset is stored in a CSV file (`space_debris.csv`), which is processed and used to simulate obstacles in the 3D environment.

---

## How It Works 🛠️

1. **Obstacle Avoidance**:
   - The spacecraft calculates an **avoidance vector** based on the positions and sizes of nearby debris.
   - The avoidance vector uses a **repulsion force** (`1 / dist^3`) to steer the spacecraft away from debris.

2. **Combined Direction**:
   - The spacecraft combines the **desired direction** (toward the destination) and the **avoidance vector** using a weighted sum.
   - A small random perturbation is added to prevent the spacecraft from getting stuck.

3. **Simulation Loop**:
   - The spacecraft moves step-by-step, updating its position based on the combined direction and speed.
   - The simulation stops when the spacecraft reaches the destination or exceeds the maximum number of steps.

4. **Visualization**:
   - The spacecraft's trajectory, debris, and destination are visualized in 3D using Plotly.

---

## Installation 🛠️

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/spacecraft-navigation.git
   cd spacecraft-navigation
   Run the Streamlit App
   ---------
## Usage 🚀
Open the Streamlit app in your browser.

Adjust simulation parameters (e.g., speed, safe margin, weight) using the sidebar.

Click Run Simulation to start the spacecraft's journey.

Explore the 3D visualization to see how the spacecraft navigates through space debris.
---------
## Visualization 📈
The simulation is visualized in 3D using Plotly:

Spacecraft Trajectory: Shown as a blue line.

Destination: Marked with a green point.

Space Debris: Represented as red spheres.
