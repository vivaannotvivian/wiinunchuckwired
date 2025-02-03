import vgamepad as vg
import XInput
import time

print("Listening for button presses... (Press Ctrl+C to exit)")
gamepad = vg.VX360Gamepad()

try:
    while True:
        state = XInput.get_state(0)  # Get controller state
        controller_state = XInput.get_button_values(state)

        if True in controller_state.values():
            print("Button Pressed:", [btn for btn, pressed in controller_state.items() if pressed])

            # Get thumbstick values and normalize them
            left_thumb = XInput.get_thumb_values(state)[0]
            x = left_thumb[0]  
            y = left_thumb[1] 
    
            gamepad.left_joystick_float(x_value_float=x, y_value_float=y)
            gamepad.update()  # Corrected update method
            print(f"Joystick input detected(left joystick): X={x}, Y={y}")
        else:
            print("Button Pressed:", [btn for btn, pressed in controller_state.items() if pressed])

            # Get thumbstick values and normalize them
            right_thumb = XInput.get_thumb_values(state)[0]
            x = right_thumb[0]  
            y = right_thumb[1] 
    
            gamepad.right_joystick_float(x_value_float=x, y_value_float=y)
            gamepad.update()  # Corrected update method
            print(f"Joystick input detected(right joystick): X={x}, Y={y}")

        time.sleep(0.1)  # Polling delay
except KeyboardInterrupt:
    print("\nExiting...")

