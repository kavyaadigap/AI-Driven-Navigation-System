import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title("AI-Driven Autonomous Spacecraft Navigation & Space Debris Avoidance")
st.write("""
This simulator demonstrates an AI-driven system where a spacecraft navigates through space,
heading toward a target destination while avoiding space debris.
The AI calculates a steering direction by combining the desired path with an avoidance vector.
""")

# --- Read Satellite Data Directly ---
file_path = r"space_debris.csv"  # 🔥 Change this to your actual CSV file path
df = pd.read_csv(file_path)

# Check if required columns exist
required_cols = {'OBJECT_NAME', 'MEAN_MOTION', 'INCLINATION', 'RA_OF_ASC_NODE'}
missing_cols = required_cols - set(df.columns)

if missing_cols:
    raise ValueError(f"Missing columns in the dataset: {missing_cols}")

# Convert columns to numeric
df['MEAN_MOTION'] = pd.to_numeric(df['MEAN_MOTION'], errors='coerce')
df['INCLINATION'] = pd.to_numeric(df['INCLINATION'], errors='coerce')
df['RA_OF_ASC_NODE'] = pd.to_numeric(df['RA_OF_ASC_NODE'], errors='coerce')

# Convert mean motion to an approximate velocity (simplified formula)
df['Velocity'] = (df['MEAN_MOTION'] / 16) * 7.91  

# Generate random positions for satellites
np.random.seed(42)  
df['X'] = np.random.uniform(20, 80, size=len(df))  
df['Y'] = np.random.uniform(20, 80, size=len(df))
df['Z'] = np.random.uniform(20, 80, size=len(df))
df['Radius'] = np.random.uniform(5, 15, size=len(df))  

# --- Simulation Parameters ---
num_steps = 300     
dt = 0.1            
speed = 2.0         

# Spacecraft start and destination
start_pos = np.array([0.0, 0.0, 0.0])
destination = np.array([100.0, 100.0, 100.0])
ship_pos = start_pos.copy()

# Convert obstacles (satellites) into usable format
obstacles = list(zip(df[['X', 'Y', 'Z']].values, df['Radius'].values))

# --- Obstacle Avoidance Function ---
# --- Obstacle Avoidance Function ---
# --- Obstacle Avoidance Function ---
def avoid_obstacles(pos, obstacles, safe_margin=20):
    avoid_vector = np.array([0.0, 0.0, 0.0])
    epsilon = 1e-5  # Prevent divide-by-zero
    for center, radius in obstacles:
        vec = pos - center
        dist = np.linalg.norm(vec) + epsilon  
        if dist < (radius + safe_margin):
            avoid_vector += vec / (dist**3)  # Stronger repulsion
    return avoid_vector

# --- Simulation Parameters ---
num_steps = 1000  # Increase number of steps
dt = 0.1            
speed = 5.0  # Increase speed
destination_threshold = 5.0  # Distance threshold to consider destination reached

# --- Simulation Loop ---
trajectory = [ship_pos.copy()]
for step in range(num_steps):
    # Check if spacecraft is close to destination
    if np.linalg.norm(ship_pos - destination) < destination_threshold:
        st.write("Destination reached!")
        break

    desired_direction = destination - ship_pos
    desired_direction = desired_direction / np.linalg.norm(desired_direction)

    # Compute avoidance direction
    avoidance = avoid_obstacles(ship_pos, obstacles)
    if np.linalg.norm(avoidance) > 0:
        avoidance = avoidance / np.linalg.norm(avoidance)

    # Combine movement
    weight = 0.4  # Prioritize avoidance more
    combined_direction = weight * desired_direction + (1 - weight) * avoidance
    combined_direction = combined_direction / np.linalg.norm(combined_direction)

    # Add small random perturbation to avoid getting stuck
    perturbation_strength = 0.8
    random_perturbation = np.random.uniform(-perturbation_strength, perturbation_strength, size=3)
    combined_direction += random_perturbation
    combined_direction = combined_direction / np.linalg.norm(combined_direction)

    # Update spacecraft position
    velocity = combined_direction * speed
    ship_pos = ship_pos + velocity * dt
    trajectory.append(ship_pos.copy())

trajectory = np.array(trajectory)

# --- Create 3D Visualization Using Plotly ---
fig = go.Figure()

# Plot spacecraft trajectory
fig.add_trace(go.Scatter3d(
    x=trajectory[:, 0],
    y=trajectory[:, 1],
    z=trajectory[:, 2],
    mode='lines+markers',
    marker=dict(size=3, color='blue'),
    line=dict(width=4, color='blue'),
    name='Spacecraft Trajectory'
))

# Plot destination point
fig.add_trace(go.Scatter3d(
    x=[destination[0]],
    y=[destination[1]],
    z=[destination[2]],
    mode='markers',
    marker=dict(size=6, color='green'),
    name='Destination'
))

# Plot obstacles (satellites) as scatter points
fig.add_trace(go.Scatter3d(
    x=df['X'],
    y=df['Y'],
    z=df['Z'],
    mode='markers',
    marker=dict(size=df['Radius'], opacity=0.5, color='red'),
    name="Satellites"
))

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title='X (units)',
        yaxis_title='Y (units)',
        zaxis_title='Z (units)'
    ),
    title="Autonomous Spacecraft Navigation & Obstacle Avoidance",
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig, use_container_width=True)

st.write("**Simulation Complete!** ")
