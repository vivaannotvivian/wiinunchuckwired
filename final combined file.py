import vgamepad as vg
import time 
import serial
arduino_port = "COM5"
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout= 1)
time.sleep(2)

print("Reading from Arduino...")
def value_overflow(number):
    if number > 1:
        number = 1
    elif number < -1:
        number = -1
    if number < 0.2 and number > 0:
        number = 0
    if number < 0 and number > -0.2:
        number = 0
    return number

    

print("Listening for button presses... (Press Ctrl+C to exit)")
gamepad = vg.VX360Gamepad()
while True:
    data = ser.readline().decode('utf-8').strip()
    if data:
        print(data)
        #print(f" Arduino says: {data}")
        processed_data = data.split()
        Stick_X = int(processed_data[1])       
        Stick_Y = int(processed_data[3])
        Acc_X = int(processed_data[6])
        Acc_Y = int(processed_data[9])
        Acc_Z = int(processed_data[12])
        C_btn = int(processed_data[15])
        Z_btn = int(processed_data[18])
    controller_x = ((Acc_X-520)/400)*2
    controller_y = ((Acc_Y-520)/400)*2
    controllerstick_x = ((Stick_X-120)/100)
    controllerstick_y = ((Stick_Y-120)/100)
    finalCX = value_overflow(controller_x)
    finalCY = value_overflow(controller_y)
    finalCX2 = value_overflow(controllerstick_x)
    finalCY2 = value_overflow(controllerstick_y)
    
    
    #print(x_stick)
    print(finalCX, finalCY, finalCX2, finalCY2)
    gamepad.left_joystick_float(x_value_float=0, y_value_float=finalCY)
    gamepad.right_joystick_float(x_value_float=finalCX, y_value_float=0)
    gamepad.update()
    #Joysticks
    if C_btn == 1:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        time.sleep(0.15)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
    if Z_btn == 1:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        time.sleep(0.15)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
# A and B Buttons
    if finalCX2 > 0.5:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.update()
    elif finalCX2 < -0.5:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        gamepad.update()
# X and Y Buttons
    if finalCY2 > 0.5:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.update()
    elif finalCY2 < -0.5:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.1)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
    if KeyboardInterrupt == True:
        print("Exiting")
        break
        

