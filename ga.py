import uinput
import socketio
import uvicorn
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
# wrap with ASGI application
app = socketio.ASGIApp(sio)
sio.always_connect = False
controls = {}
events = (
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_C,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_Z,
    uinput.BTN_TL,
    uinput.BTN_TR,
    uinput.BTN_TL2,
    uinput.BTN_TR2,
    uinput.BTN_THUMBL,
    uinput.BTN_THUMBR,
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT,
    uinput.BTN_START,
    uinput.BTN_SELECT,
    uinput.BTN_MODE,
    uinput.BTN_JOYSTICK,
    uinput.BTN_0,
    uinput.BTN_1,
    uinput.BTN_2,
    uinput.BTN_3,
    uinput.BTN_4,
    uinput.BTN_5,
    uinput.BTN_6,
    uinput.BTN_7,
    uinput.BTN_8,
    uinput.BTN_9,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),
    uinput.ABS_RX + (0, 255, 0, 0),
    uinput.ABS_RY + (0, 255, 0, 0),
)

control1 = uinput.Device(
    events,
    vendor=0x045E,
    product=0x028E,
    version=0x110,
    name="Microsoft X-Box 360 gamepad1",
)

print("Printed A.")
control1.emit(uinput.BTN_A, 1)
time.sleep(2.4)

print("Printed A End.")
control1.emit(uinput.BTN_A, 0)
