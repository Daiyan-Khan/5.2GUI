
import tkinter as tk
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for LEDs
LED_pins = [17, 18, 22]
for pin in LED_pins:
    GPIO.setup(pin, GPIO.OUT)

# Create PWM objects for LEDs
PWM_LEDs = [GPIO.PWM(pin, 100) for pin in LED_pins]
for pwm in PWM_LEDs:
    pwm.start(0)  # Start with duty cycle of 0 (LEDs off)

def update_pwm(led_index, duty_cycle):
    # Update PWM duty cycle for the selected LED
    PWM_LEDs[led_index].ChangeDutyCycle(duty_cycle)

def exit_gui():
    # Cleanup GPIO
    
    for pwm in PWM_LEDs:
        pwm.stop()
    GPIO.cleanup()
    root.destroy()

def slider_changed(led_index):
    duty_cycle = slider_vars[led_index].get()
    update_pwm(led_index, duty_cycle)

# Create the GUI
root = tk.Tk()
root.title("LED Intensity Controller")

slider_vars = [tk.DoubleVar() for _ in range(len(LED_pins))]

for i in range(len(LED_pins)):
    tk.Label(root, text="LED {}: ".format(i+1)).grid(row=i, column=0)
    tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=slider_vars[i], command=lambda val, i=i: slider_changed(i)).grid(row=i, column=1)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=exit_gui)
exit_button.grid(row=len(LED_pins), columnspan=2)

root.mainloop()
