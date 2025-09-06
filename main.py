# File: main.py (to be placed OUTSIDE the package directory)
"""
Main demonstration script for signal_ICT_abhinaychoudhari_92400133174 package

This script runs from outside the package directory and imports the modules correctly.

Author: Abhinay Choudhari
Contact: 92400133174
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add the package directory to Python path
package_path = os.path.join(os.path.dirname(__file__), 'signal_ICT_abhinaychoudhari_92400133174_')
sys.path.insert(0, package_path)

# Now import the modules
try:
    import unitary_signals
    import trigonometric_signals  
    import operations
    print("✓ All modules imported successfully!")
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Make sure the package directory 'signal_ICT_abhinaychoudhari_92400133174' exists in the same folder as main.py")
    sys.exit(1)

def main():
    """
    Main function to demonstrate all signal processing capabilities.
    """
    print("=" * 80)
    print("SIGNAL PROCESSING PACKAGE DEMONSTRATION")
    print("Package: signal_ICT_abhinaychoudhari_92400133174")
    print("Author: Abhinay Choudhari")
    print("Contact: 92400133174")
    print("=" * 80)
    
    # Task 1: Generate and plot unit step signal and unit impulse signal of length 20
    print("\n1. GENERATING UNITARY SIGNALS (Length: 20)")
    print("-" * 50)
    
    n = np.arange(-10, 10)  # 20 samples from -10 to 9
    
    print("Generating Unit Step Signal u[n]...")
    step_signal = unitary_signals.unit_step(n)
    
    print("Generating Unit Impulse Signal δ[n]...")
    impulse_signal = unitary_signals.unit_impulse(n)
    
    print("Generating Ramp Signal r[n]...")
    ramp_sig = unitary_signals.ramp_signal(n)
    
    # Task 2: Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec
    print("\n2. GENERATING SINE WAVE")
    print("-" * 50)
    print("Parameters: Amplitude = 2, Frequency = 5 Hz, Phase = 0, Time = 0 to 1 sec")
    
    t = np.linspace(0, 1, 1000)  # 1000 samples from 0 to 1 second
    sine_sig = trigonometric_signals.sine_wave(A=2, f=5, phi=0, t=t)
    
    # Task 3: Perform time shifting on the sine wave by +5 units and plot both signals
    print("\n3. TIME SHIFTING OPERATION")
    print("-" * 50)
    print("Shifting sine wave by +5 units (right shift/delay)")
    
    # For demonstration, work with a discrete version of the sine wave
    n_discrete = np.arange(0, 100)
    t_discrete = n_discrete / 100  # Normalize to 0-1 second range
    sine_discrete = trigonometric_signals.sine_wave(A=2, f=5, phi=0, t=t_discrete)
    
    # Apply time shift
    shifted_sine = operations.time_shift(sine_discrete, k=5)
    
    # Plot comparison
    print("Plotting original and time-shifted signals...")
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(n_discrete, sine_discrete, 'b-', linewidth=2, label='Original Sine Wave')
    plt.title('Original Sine Wave')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    n_shifted = np.arange(len(shifted_sine))
    plt.plot(n_shifted, shifted_sine, 'r-', linewidth=2, label='Time Shifted (+5 units)')
    plt.title('Time Shifted Sine Wave (+5 units)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Task 4: Perform addition of unit step and ramp signal and plot the result
    print("\n4. SIGNAL ADDITION OPERATION")
    print("-" * 50)
    print("Adding Unit Step Signal and Ramp Signal")
    
    added_signal = operations.signal_addition(step_signal, ramp_sig)
    
    # Plot the operation
    print("Plotting signal addition result...")
    plt.figure(figsize=(14, 10))
    
    plt.subplot(3, 1, 1)
    plt.stem(n[:len(step_signal)], step_signal, basefmt='b-', label='Unit Step')
    plt.title('Unit Step Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.stem(n[:len(ramp_sig)], ramp_sig, basefmt='g-', label='Ramp Signal')
    plt.title('Ramp Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 3)
    n_added = np.arange(len(added_signal))
    plt.stem(n_added, added_signal, basefmt='r-', label='Step + Ramp')
    plt.title('Signal Addition Result (Step + Ramp)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Task 5: Multiply sine and cosine wave of same frequency and plot the result
    print("\n5. SIGNAL MULTIPLICATION OPERATION")
    print("-" * 50)
    print("Multiplying Sine and Cosine waves of same frequency (5 Hz)")
    
    # Generate cosine wave with same parameters as sine wave
    cosine_sig = trigonometric_signals.cosine_wave(A=2, f=5, phi=0, t=t_discrete)
    
    # Perform multiplication
    multiplied_signal = operations.signal_multiplication(sine_discrete, cosine_sig)
    
    # Plot the operation
    print("Plotting signal multiplication result...")
    plt.figure(figsize=(14, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(t_discrete, sine_discrete, 'b-', linewidth=2, label='Sine Wave (5 Hz)')
    plt.title('Sine Wave: 2sin(2π×5×t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(t_discrete, cosine_sig, 'g-', linewidth=2, label='Cosine Wave (5 Hz)')
    plt.title('Cosine Wave: 2cos(2π×5×t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 3)
    plt.plot(t_discrete, multiplied_signal, 'm-', linewidth=2, label='Sine × Cosine')
    plt.title('Signal Multiplication Result (Sine × Cosine)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Additional Demonstrations
    print("\n6. ADDITIONAL DEMONSTRATIONS")
    print("-" * 50)
    
    # Demonstrate exponential signal
    print("Generating Exponential Signals...")
    t_exp = np.linspace(0, 2, 500)
    
    # Decaying exponential
    exp_decay = trigonometric_signals.exponential_signal(A=5, a=-2, t=t_exp)
    
    # Growing exponential (shorter time to avoid overflow)
    exp_growth = trigonometric_signals.exponential_signal(A=1, a=1, t=t_exp[:250])
    
    # Demonstrate time scaling
    print("Demonstrating Time Scaling...")
    # Compress the sine wave (speed up)
    compressed_sine = operations.time_scale(sine_discrete, k=2)
    
    # Expand the sine wave (slow down)  
    expanded_sine = operations.time_scale(sine_discrete, k=0.5)
    
    # Plot scaling results
    plt.figure(figsize=(14, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(n_discrete, sine_discrete, 'b-', linewidth=2, label='Original Sine')
    plt.title('Original Sine Wave')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(np.arange(len(compressed_sine)), compressed_sine, 'r-', linewidth=2, label='Compressed (k=2)')
    plt.title('Time Scaled - Compressed (k=2)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(3, 1, 3)
    plt.plot(np.arange(len(expanded_sine)), expanded_sine, 'g-', linewidth=2, label='Expanded (k=0.5)')
    plt.title('Time Scaled - Expanded (k=0.5)')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Summary statistics
    print("\n7. SIGNAL STATISTICS SUMMARY")
    print("-" * 50)
    
    signals_info = {
        "Unit Step": {"signal": step_signal, "samples": len(step_signal)},
        "Unit Impulse": {"signal": impulse_signal, "samples": len(impulse_signal)},
        "Ramp": {"signal": ramp_sig, "samples": len(ramp_sig)},
        "Sine Wave": {"signal": sine_discrete, "samples": len(sine_discrete)},
        "Added Signal": {"signal": added_signal, "samples": len(added_signal)},
        "Multiplied Signal": {"signal": multiplied_signal, "samples": len(multiplied_signal)}
    }
    
    for name, info in signals_info.items():
        signal_data = info["signal"]
        print(f"{name:16}: Samples={info['samples']:3d}, "
              f"Max={np.max(signal_data):7.3f}, "
              f"Min={np.min(signal_data):7.3f}, "
              f"Mean={np.mean(signal_data):7.3f}, "
              f"RMS={np.sqrt(np.mean(signal_data**2)):7.3f}")
    
    # Create a comprehensive comparison plot
    print("\n8. COMPREHENSIVE SIGNAL COMPARISON")
    print("-" * 50)
    
    plt.figure(figsize=(16, 12))
    
    # Plot 1: Unit Step Signal
    plt.subplot(3, 2, 1)
    plt.stem(n[:len(step_signal)], step_signal, basefmt='b-', label='Unit Step')
    plt.title('Unit Step Signal u[n]')
    plt.xlabel('n (sample index)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot 2: Unit Impulse Signal
    plt.subplot(3, 2, 2)
    plt.stem(n[:len(impulse_signal)], impulse_signal, basefmt='r-', label='Unit Impulse')
    plt.title('Unit Impulse Signal δ[n]')
    plt.xlabel('n (sample index)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot 3: Trigonometric Signals
    plt.subplot(3, 2, 3)
    plt.plot(t_discrete, sine_discrete, 'b-', label='Sine Wave (5 Hz)', linewidth=2)
    plt.plot(t_discrete, cosine_sig, 'r--', label='Cosine Wave (5 Hz)', linewidth=2)
    plt.title('Trigonometric Signals')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot 4: Signal Addition
    plt.subplot(3, 2, 4)
    n_extended = np.arange(len(added_signal))
    plt.stem(n_extended, added_signal, basefmt='g-', label='Step + Ramp')
    plt.title('Signal Addition Result')
    plt.xlabel('n (sample index)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot 5: Signal Multiplication
    plt.subplot(3, 2, 5)
    plt.plot(t_discrete, multiplied_signal, 'm-', label='Sine × Cosine', linewidth=2)
    plt.title('Signal Multiplication Result')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot 6: Time Shifting
    plt.subplot(3, 2, 6)
    plt.plot(n_discrete, sine_discrete, 'b-', label='Original Sine', alpha=0.7, linewidth=2)
    n_shift = np.arange(len(shifted_sine))
    plt.plot(n_shift, shifted_sine, 'r-', label='Shifted Sine (+5)', alpha=0.7, linewidth=2)
    plt.title('Time Shifting Result')
    plt.xlabel('n (sample index)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETED SUCCESSFULLY!")
    print("All required tasks have been completed:")
    print("✓ Task 1: Unit step and impulse signals (length 20)")
    print("✓ Task 2: Sine wave (A=2, f=5Hz, φ=0, t=0-1s)")
    print("✓ Task 3: Time shifting by +5 units")
    print("✓ Task 4: Addition of step and ramp signals")
    print("✓ Task 5: Multiplication of sine and cosine waves")
    print("Package: signal_ICT_abhinaychoudhari_92400133174")
    print("=" * 80)


if __name__ == "__main__":
    try:
        # Check if required packages are installed
        import numpy
        import matplotlib
        print("✓ Required packages (numpy, matplotlib) are installed")
        
        # Run the main demonstration
        main()
        
        # Keep plots open
        input("\nPress Enter to exit and close all plots...")
        plt.close('all')
        
    except ImportError as e:
        print(f"✗ Import Error: {e}")
        print("\nPlease install required packages:")
        print("pip install numpy matplotlib")
        
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure the 'signal_ICT_abhinaychoudhari_92400133174' folder exists")
        print("2. Ensure all .py files are in the package folder")
        print("3. Check file permissions")