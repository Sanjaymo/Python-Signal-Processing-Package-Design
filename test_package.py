# File: test_package.py
"""
Comprehensive testing script for signal_ICT_abhinaychoudhari_92400133174 package

This script tests all functionality and generates a test report.
Author: Abhinay Choudhari
Contact: 92400133174
"""

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt

def test_imports():
    """Test if all modules can be imported successfully"""
    print("Testing imports...")
    try:
        from signal_ICT_abhinaychoudhari_92400133174 import (
            unit_step, unit_impulse, ramp_signal,
            sine_wave, cosine_wave, exponential_signal,
            time_shift, time_scale, signal_addition, signal_multiplication
        )
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_unitary_signals():
    """Test unitary signals functionality"""
    print("\nTesting unitary signals...")
    try:
        from signal_ICT_abhinaychoudhari_92400133174 import unit_step, unit_impulse, ramp_signal
        
        n = np.arange(-5, 6)
        
        # Test unit step
        step = unit_step(n)
        expected_step = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
        assert np.array_equal(step, expected_step), "Unit step test failed"
        
        # Test unit impulse
        impulse = unit_impulse(n)
        expected_impulse = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
        assert np.array_equal(impulse, expected_impulse), "Unit impulse test failed"
        
        # Test ramp signal
        ramp = ramp_signal(n)
        expected_ramp = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5])
        assert np.array_equal(ramp, expected_ramp), "Ramp signal test failed"
        
        print("✓ Unitary signals tests passed")
        return True
    except Exception as e:
        print(f"✗ Unitary signals test failed: {e}")
        return False

def test_trigonometric_signals():
    """Test trigonometric signals functionality"""
    print("\nTesting trigonometric signals...")
    try:
        from signal_ICT_abhinaychoudhari_92400133174 import sine_wave, cosine_wave, exponential_signal
        
        t = np.linspace(0, 1, 100)
        
        # Test sine wave
        sine = sine_wave(A=1, f=1, phi=0, t=t)
        expected_sine_start = np.sin(2 * np.pi * 1 * t[0] + 0)
        assert np.isclose(sine[0], expected_sine_start), "Sine wave test failed"
        
        # Test cosine wave
        cosine = cosine_wave(A=1, f=1, phi=0, t=t)
        expected_cosine_start = np.cos(2 * np.pi * 1 * t[0] + 0)
        assert np.isclose(cosine[0], expected_cosine_start), "Cosine wave test failed"
        
        # Test exponential signal
        exp_sig = exponential_signal(A=1, a=1, t=t[:10])  # Limit to avoid overflow
        expected_exp_start = 1 * np.exp(1 * t[0])
        assert np.isclose(exp_sig[0], expected_exp_start), "Exponential signal test failed"
        
        print("✓ Trigonometric signals tests passed")
        return True
    except Exception as e:
        print(f"✗ Trigonometric signals test failed: {e}")
        return False

def test_operations():
    """Test signal operations functionality"""
    print("\nTesting signal operations...")
    try:
        from signal_ICT_abhinaychoudhari_92400133174 import (
            time_shift, time_scale, signal_addition, signal_multiplication
        )
        
        # Test signals
        signal1 = np.array([1, 2, 3, 4, 5])
        signal2 = np.array([5, 4, 3, 2, 1])
        
        # Test time shift
        shifted = time_shift(signal1, 2)
        expected_shifted = np.array([0, 0, 1, 2, 3, 4, 5])
        assert np.array_equal(shifted, expected_shifted), "Time shift test failed"
        
        # Test signal addition
        added = signal_addition(signal1, signal2)
        expected_added = np.array([6, 6, 6, 6, 6])
        assert np.array_equal(added, expected_added), "Signal addition test failed"
        
        # Test signal multiplication
        multiplied = signal_multiplication(signal1, signal2)
        expected_multiplied = np.array([5, 8, 9, 8, 5])
        assert np.array_equal(multiplied, expected_multiplied), "Signal multiplication test failed"
        
        # Test time scaling
        scaled = time_scale(signal1, 2)
        assert len(scaled) == len(signal1) // 2, "Time scaling test failed"
        
        print("✓ Operations tests passed")
        return True
    except Exception as e:
        print(f"✗ Operations test failed: {e}")
        return False

def test_assignment_requirements():
    """Test specific assignment requirements"""
    print("\nTesting assignment requirements...")
    try:
        from signal_ICT_abhinaychoudhari_92400133174 import (
            unit_step, unit_impulse, ramp_signal,
            sine_wave, cosine_wave,
            time_shift, signal_addition, signal_multiplication
        )
        
        # Task 1: Generate unit step and impulse signals (length 20)
        n = np.arange(-10, 10)  # 20 samples
        step_signal = unit_step(n)
        impulse_signal = unit_impulse(n)
        assert len(step_signal) == 20, "Unit step length should be 20"
        assert len(impulse_signal) == 20, "Unit impulse length should be 20"
        
        # Task 2: Generate sine wave (A=2, f=5Hz, phi=0, t=0-1s)
        t = np.linspace(0, 1, 1000)
        sine_sig = sine_wave(A=2, f=5, phi=0, t=t)
        assert np.max(sine_sig) <= 2.1, "Sine wave amplitude should be ~2"
        assert np.min(sine_sig) >= -2.1, "Sine wave amplitude should be ~2"
        
        # Task 3: Time shifting by +5 units
        n_discrete = np.arange(0, 100)
        t_discrete = n_discrete / 100
        sine_discrete = sine_wave(A=2, f=5, phi=0, t=t_discrete)
        shifted_sine = time_shift(sine_discrete, k=5)
        assert len(shifted_sine) == len(sine_discrete) + 5, "Time shift should increase length"
        
        # Task 4: Addition of step and ramp signals
        ramp_sig = ramp_signal(n)
        added_signal = signal_addition(step_signal, ramp_sig)
        assert len(added_signal) == 20, "Added signal should have same length"
        
        # Task 5: Multiplication of sine and cosine waves (same frequency)
        cosine_sig = cosine_wave(A=2, f=5, phi=0, t=t_discrete)
        multiplied_signal = signal_multiplication(sine_discrete, cosine_sig)
        assert len(multiplied_signal) == len(sine_discrete), "Multiplied signal should have same length"
        
        print("✓ All assignment requirements satisfied")
        return True
    except Exception as e:
        print(f"✗ Assignment requirements test failed: {e}")
        return False

def test_console_script():
    """Test if console script is available"""
    print("\nTesting console script availability...")
    try:
        import subprocess
        result = subprocess.run(['signal-demo', '--help'], 
                              capture_output=True, text=True, timeout=10)
        # If the command exists, it should not return "command not found"
        if "not found" not in result.stderr.lower() and "not recognized" not in result.stderr.lower():
            print("✓ Console script 'signal-demo' is available")
            return True
        else:
            print("⚠ Console script might not be properly installed")
            return False
    except Exception as e:
        print(f"⚠ Console script test inconclusive: {e}")
        return False

def generate_test_report():
    """Generate a comprehensive test report"""
    print("\n" + "="*60)
    print("COMPREHENSIVE PACKAGE TEST REPORT")
    print("Package: signal_ICT_abhinaychoudhari_92400133174")
    print("Author: Abhinay Choudhari")
    print("Contact: 92400133174")
    print("="*60)
    
    tests = [
        ("Import Test", test_imports),
        ("Unitary Signals Test", test_unitary_signals),
        ("Trigonometric Signals Test", test_trigonometric_signals),
        ("Operations Test", test_operations),
        ("Assignment Requirements Test", test_assignment_requirements),
        ("Console Script Test", test_console_script),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ {test_name} encountered an error: {e}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name:<35} {status}")
        if result:
            passed += 1
    
    print("-"*60)
    print(f"TOTAL: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Package is ready for submission.")
    else:
        print(f"\n⚠️  {total-passed} test(s) failed. Please review and fix issues.")
    
    print("="*60)
    
    return passed == total

def main():
    """Main test function"""
    try:
        # Suppress matplotlib plots during testing
        plt.ioff()
        
        # Run comprehensive tests
        success = generate_test_report()
        
        if success:
            print("\nPackage validation complete! ✅")
            sys.exit(0)
        else:
            print("\nPackage validation failed! ❌")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error during testing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()