# Signal Processing Package - ICT Project

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Package Status](https://img.shields.io/badge/status-stable-green.svg)](https://github.com/abhinaychoudhari/signal_ICT_abhinaychoudhari_92400133174)

**Author**: Sanjay Choudhari  
**Contact**: 9963785768 

## 📋 Overview

`signal_ICT_abhinaychoudhari_92400133174` is a comprehensive Python package designed for signal generation and processing operations. This package demonstrates fundamental concepts of **Signals and Systems** through a modular architecture with three main components for generating unitary signals, trigonometric signals, and performing various signal operations.

## 🚀 Features

### 📊 Unitary Signals
- **Unit Step Signal** - `u[n]`: Discrete step function
- **Unit Impulse Signal** - `δ[n]`: Discrete delta function  
- **Ramp Signal** - `r[n]`: Linear ramp function

### 🌊 Trigonometric Signals
- **Sine Wave**: Configurable amplitude, frequency, and phase
- **Cosine Wave**: Configurable amplitude, frequency, and phase
- **Exponential Signal**: Growing/decaying exponential functions

### ⚙️ Signal Operations
- **Time Shifting**: Delay or advance signals in time domain
- **Time Scaling**: Compress or expand signals in time
- **Signal Addition**: Point-wise addition of two signals
- **Signal Multiplication**: Point-wise multiplication of signals

### 📈 Visualization
- Automatic plotting for all generated signals
- Comprehensive comparison plots
- Signal statistics and analysis
- Professional matplotlib-based visualizations

## 📦 Installation

### Install from PyPI (Recommended)
```bash
pip install signal-ICT-abhinaychoudhari-92400133174
```

### Install from TestPyPI
```bash
pip install -i https://test.pypi.org/simple/ signal-ICT-abhinaychoudhari-92400133174
```

### Install from Wheel (Local)
```bash
# Download the wheel file from releases
pip install signal_ICT_abhinaychoudhari_92400133174-1.0.0-py3-none-any.whl
```

### Install from Source
```bash
git clone https://github.com/abhinaychoudhari/signal_ICT_abhinaychoudhari_92400133174.git
cd signal_ICT_abhinaychoudhari_92400133174
pip install -e .
```

## 📚 Package Structure

```
signal_ICT_abhinaychoudhari_92400133174/
├── __init__.py                 # Package initialization
├── unitary_signals.py         # Unit step, impulse, ramp signals
├── trigonometric_signals.py   # Sine, cosine, exponential signals
├── operations.py               # Signal operations and utilities
└── main.py                     # Demonstration script
```

## 🔧 Dependencies

- **Python** >= 3.7
- **NumPy** >= 1.19.0 (Numerical computations)
- **Matplotlib** >= 3.3.0 (Plotting and visualization)

## 💡 Quick Start

### Basic Usage

```python
import numpy as np
from signal_ICT_abhinaychoudhari_92400133174 import (
    unit_step, unit_impulse, ramp_signal,
    sine_wave, cosine_wave, exponential_signal,
    time_shift, signal_addition
)

# Generate time indices
n = np.arange(-10, 11)
t = np.linspace(0, 1, 1000)

# Create unitary signals
step = unit_step(n)           # Unit step signal
impulse = unit_impulse(n)     # Unit impulse signal
ramp = ramp_signal(n)         # Ramp signal

# Create trigonometric signals
sine = sine_wave(A=2, f=5, phi=0, t=t)      # 2sin(2π×5×t)
cosine = cosine_wave(A=1, f=3, phi=np.pi/4, t=t)  # cos(2π×3×t + π/4)
exp_decay = exponential_signal(A=1, a=-2, t=t)    # e^(-2t)

# Perform operations
shifted = time_shift(sine, k=5)              # Shift by 5 units
combined = signal_addition(step, ramp)       # Add signals
```

### Run Complete Demo

```python
# Run the comprehensive demonstration
from signal_ICT_abhinaychoudhari_92400133174.main import main
main()
```

Or from command line after installation:
```bash
signal-demo
```

## 📖 Module Documentation

### 1. `unitary_signals.py`

#### `unit_step(n)`
Generates a unit step signal u[n].

**Parameters:**
- `n` (array-like): Time indices or sample points

**Returns:**
- `numpy.ndarray`: Unit step signal values (1 for n≥0, 0 for n<0)

**Example:**
```python
n = np.arange(-5, 6)
step = unit_step(n)  # [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
```

#### `unit_impulse(n)`
Generates a unit impulse signal δ[n].

**Parameters:**
- `n` (array-like): Time indices or sample points

**Returns:**
- `numpy.ndarray`: Unit impulse signal values (1 for n=0, 0 elsewhere)

#### `ramp_signal(n)`
Generates a ramp signal r[n].

**Parameters:**
- `n` (array-like): Time indices or sample points

**Returns:**
- `numpy.ndarray`: Ramp signal values (n for n≥0, 0 for n<0)

### 2. `trigonometric_signals.py`

#### `sine_wave(A, f, phi, t)`
Generates a sine wave signal.

**Parameters:**
- `A` (float): Amplitude
- `f` (float): Frequency in Hz
- `phi` (float): Phase shift in radians
- `t` (array-like): Time vector

**Returns:**
- `numpy.ndarray`: Sine wave: A×sin(2πft + φ)

#### `cosine_wave(A, f, phi, t)`
Generates a cosine wave signal.

**Parameters:**
- `A` (float): Amplitude
- `f` (float): Frequency in Hz  
- `phi` (float): Phase shift in radians
- `t` (array-like): Time vector

**Returns:**
- `numpy.ndarray`: Cosine wave: A×cos(2πft + φ)

#### `exponential_signal(A, a, t)`
Generates an exponential signal.

**Parameters:**
- `A` (float): Amplitude scaling factor
- `a` (float): Exponential parameter (positive=growth, negative=decay)
- `t` (array-like): Time vector

**Returns:**
- `numpy.ndarray`: Exponential signal: A×e^(at)

### 3. `operations.py`

#### `time_shift(signal, k)`
Shifts signal by k units in time domain.

**Parameters:**
- `signal` (array-like): Input signal
- `k` (int): Shift amount (positive=right shift/delay, negative=left shift/advance)

**Returns:**
- `numpy.ndarray`: Time-shifted signal

#### `time_scale(signal, k)`
Scales the time axis by factor k.

**Parameters:**
- `signal` (array-like): Input signal
- `k` (float): Scaling factor (k>1=compress, 0<k<1=expand)

**Returns:**
- `numpy.ndarray`: Time-scaled signal

#### `signal_addition(signal1, signal2)`
Performs point-wise addition of two signals.

**Parameters:**
- `signal1, signal2` (array-like): Input signals

**Returns:**
- `numpy.ndarray`: Sum of input signals

#### `signal_multiplication(signal1, signal2)`
Performs point-wise multiplication of two signals.

**Parameters:**
- `signal1, signal2` (array-like): Input signals

**Returns:**
- `numpy.ndarray`: Product of input signals

## 🎯 Assignment Implementation

This package successfully implements all required assignment tasks:

### ✅ Task 1: Unitary Signals (Length 20)
```python
n = np.arange(-10, 10)  # 20 samples
step_signal = unit_step(n)
impulse_signal = unit_impulse(n)
```

### ✅ Task 2: Sine Wave Generation
```python
t = np.linspace(0, 1, 1000)
sine_wave(A=2, f=5, phi=0, t=t)  # Amplitude=2, Frequency=5Hz, Phase=0
```

### ✅ Task 3: Time Shifting
```python
shifted_sine = time_shift(sine_signal, k=5)  # +5 units shift
```

### ✅ Task 4: Signal Addition
```python
added_signal = signal_addition(step_signal, ramp_signal)
```

### ✅ Task 5: Signal Multiplication
```python
sine = sine_wave(A=2, f=5, phi=0, t=t)
cosine = cosine_wave(A=2, f=5, phi=0, t=t)  # Same frequency
result = signal_multiplication(sine, cosine)
```

## 📊 Expected Outputs

### Console Output
- Progress messages for each operation
- Signal statistics (samples, max, min, mean, RMS)
- Confirmation of successful task completion

### Graphical Outputs
- Individual signal plots with proper labeling
- Comparison plots for operations
- Comprehensive multi-subplot visualizations
- Professional matplotlib styling with grids and legends

### Signal Statistics Example
```
Unit Step       : Samples= 20, Max=  1.000, Min=  0.000, Mean=  0.500, RMS=  0.707
Unit Impulse    : Samples= 20, Max=  1.000, Min=  0.000, Mean=  0.050, RMS=  0.224
Sine Wave       : Samples=100, Max=  2.000, Min= -2.000, Mean= -0.000, RMS=  1.414
```

## 🐛 Troubleshooting

### Common Issues

**Import Error**: `No module named 'signal_ICT_abhinaychoudhari_92400133174'`
```bash
# Solution: Install the package properly
pip install signal-ICT-abhinaychoudhari-92400133174
```

**Matplotlib Backend Issues**:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

**Missing Dependencies**:
```bash
pip install numpy matplotlib
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support & Contact

- **Author**: Sanjay Choudhari
- **Phone**: 9963785768
- **Course**: Data Science
- **Institution**: PARUL UNIVERSITY

For issues, questions, or contributions, please open an issue on the GitHub repository.

## 🎓 Academic Context

This package was developed as part of an ICT course assignment focusing on:
- Digital Signal Processing fundamentals
- Python package development
- Software engineering best practices
- Documentation and testing
- PyPI distribution workflow

## 📈 Version History

- **v1.0.0** (2024): Initial release with full signal processing capabilities
  - Unitary signals implementation
  - Trigonometric signals with visualization
  - Comprehensive signal operations
  - Professional documentation and testing
