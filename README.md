# n-body-gravity-simulator

A real-time gravitational N-body simulator written in Python using Pygame. Physics are computed with a Barnes-Hut quadtree for O(n log n) performance, and integration uses a two-pass Leapfrog scheme for stability.

## Features

- Barnes-Hut quadtree for efficient force approximation
- Two built-in presets: Solar System and Black Hole system
- Inelastic body merging and black hole absorption
- Orbital trail rendering with configurable length
- Camera pan/zoom and body-follow mode
- On-screen HUD with simulation controls

## Requirements

```
pip install pygame numpy
```

## Running

```
python src/main.py
```

## Controls

| Key | Action |
|-----|--------|
| `Space` | Pause / Resume |
| `=` / `-` | Speed up / slow down simulation |
| `1` | Load Solar System preset |
| `2` | Load Black Hole preset |
| `R` | Reset current preset |
| `Tab` | Cycle selected body |
| `F` | Toggle follow selected body |
| Mouse drag | Pan camera |
| Scroll wheel | Zoom in / out |
