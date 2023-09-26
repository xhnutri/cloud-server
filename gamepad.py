import uinput
import socketio
import uvicorn

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


def get_input_valueX(joyValue):
    if joyValue == 0:
        return 126
    elif joyValue > 0:
        return int(255 * joyValue)
    else:
        return int((126 * joyValue) + 126)


def get_input_valueY(joyValue):
    if joyValue == 0:
        return 126
    elif joyValue < 0:
        return int(255 * joyValue * -1)
    else:
        return int((126 * joyValue * -1) + 126)

# Create a virtual mouse device
deviceMouse = uinput.Device([
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    uinput.REL_X,
    uinput.REL_Y,
])

@sio.on("mouseMoveClick")
async def mouseMoveClick(sid, data):
    print("MouseClick")
    print(data)
    # Move the mouse pointer to (100, 100) and click the left button
    deviceMouse.emit(uinput.REL_X, data['posX'])
    deviceMouse.emit(uinput.REL_Y, data['posY'])
    deviceMouse.emit(uinput.BTN_LEFT, 1)
    deviceMouse.emit(uinput.BTN_LEFT, 0)

@sio.on("RightJoystick")
async def RightJoystick(sid, data):
    print("RightJoystick")
    controls[data["gamepad"]].emit(
        uinput.ABS_X, get_input_valueX(data["joystickX"]))
    controls[data["gamepad"]].emit(
        uinput.ABS_Y, get_input_valueY(data["joystickY"]))


@sio.on("LeftJoystick")
async def LeftJoystick(sid, data):
    print("LeftJoystick")
    controls[data["gamepad"]].emit(
        uinput.ABS_RX, get_input_valueX(data["joystickX"]))
    controls[data["gamepad"]].emit(
        uinput.ABS_RY, get_input_valueY(data["joystickY"]))


@sio.on("DPAD_UP")
async def A(sid, data):
    print(data)
    print("DPAD_UP")
    if data["DPAD_UP"]:
        controls[data["gamepad"]].emit(uinput.BTN_DPAD_UP, 1)
    else:
        controls[data["gamepad"]].emit(uinput.BTN_DPAD_UP, 0)


class ButtonsGamepad:
    def __init__(self, name, btn_type):
        self.name = name
        self.btn_type = btn_type

    def OnBtn(self, data):
        print(data)
        print(self.name)
        if data[self.name]:
            controls[data["gamepad"]].emit(self.btn_type, 1)
        else:
            controls[data["gamepad"]].emit(self.btn_type, 0)


@sio.on("A")
async def A(sid, data):
    print(data)
    print("A")
    ButtonsGamepad("A", uinput.BTN_A).OnBtn(data)


@sio.on("B")
async def B(sid, data):
    print(data)
    print("B")
    ButtonsGamepad("B", uinput.BTN_B).OnBtn(data)


@sio.on("C")
async def C(sid, data):
    print(data)
    print("C")
    ButtonsGamepad("C", uinput.BTN_C).OnBtn(data)


@sio.on("X")
async def X(sid, data):
    print(data)
    print("X")
    ButtonsGamepad("X", uinput.BTN_X).OnBtn(data)


@sio.on("Y")
async def Y(sid, data):
    print(data)
    print("Y")
    ButtonsGamepad("Y", uinput.BTN_Y).OnBtn(data)


@sio.on("Z")
async def Z(sid, data):
    print(data)
    print("Z")
    ButtonsGamepad("Z", uinput.BTN_Z).OnBtn(data)


@sio.on("TL")
async def TL(sid, data):
    print(data)
    print("TL")
    ButtonsGamepad("TL", uinput.BTN_TL).OnBtn(data)


@sio.on("TR")
async def TR(sid, data):
    print(data)
    print("TR")
    ButtonsGamepad("TR", uinput.BTN_TR).OnBtn(data)


@sio.on("TL2")
async def TL2(sid, data):
    print(data)
    print("TL2")
    ButtonsGamepad("TL2", uinput.BTN_TL2).OnBtn(data)


@sio.on("TR2")
async def TR2(sid, data):
    print(data)
    print("TR2")
    ButtonsGamepad("TR2", uinput.BTN_TR2).OnBtn(data)


@sio.on("THUMBL")
async def THUMBL(sid, data):
    print(data)
    print("THUMBL")
    ButtonsGamepad("THUMBL", uinput.BTN_THUMBL).OnBtn(data)


@sio.on("THUMBR")
async def THUMBR(sid, data):
    print(data)
    print("THUMBR")
    ButtonsGamepad("THUMBR", uinput.BTN_THUMBR).OnBtn(data)


@sio.on("DPAD_UP")
async def DPAD_UP(sid, data):
    print(data)
    print("DPAD_UP")
    ButtonsGamepad("DPAD_UP", uinput.BTN_DPAD_UP).OnBtn(data)


@sio.on("DPAD_DOWN")
async def DPAD_DOWN(sid, data):
    print(data)
    print("DPAD_DOWN")
    ButtonsGamepad("DPAD_DOWN", uinput.BTN_DPAD_DOWN).OnBtn(data)


@sio.on("DPAD_LEFT")
async def DPAD_LEFT(sid, data):
    print(data)
    print("DPAD_LEFT")
    ButtonsGamepad("DPAD_LEFT", uinput.BTN_DPAD_LEFT).OnBtn(data)


@sio.on("DPAD_RIGHT")
async def DPAD_RIGHT(sid, data):
    print(data)
    print("DPAD_RIGHT")
    ButtonsGamepad("DPAD_RIGHT", uinput.BTN_DPAD_RIGHT).OnBtn(data)


@sio.on("START")
async def START(sid, data):
    print(data)
    print("START")
    ButtonsGamepad("START", uinput.BTN_START).OnBtn(data)


@sio.on("SELECT")
async def SELECT(sid, data):
    print(data)
    print("SELECT")
    ButtonsGamepad("SELECT", uinput.BTN_SELECT).OnBtn(data)


@sio.on("MODE")
async def MODE(sid, data):
    print(data)
    print("MODE")
    ButtonsGamepad("MODE", uinput.BTN_MODE).OnBtn(data)


@sio.on("JOYSTICK")
async def JOYSTICK(sid, data):
    print(data)
    print("JOYSTICK")
    ButtonsGamepad("JOYSTICK", uinput.BTN_JOYSTICK).OnBtn(data)


@sio.on("0")
async def sioOn(sid, data):
    print(data)
    print("0")
    ButtonsGamepad("0", uinput.BTN_0).OnBtn(data)


@sio.on("1")
async def sioOn(sid, data):
    print(data)
    print("1")
    ButtonsGamepad("1", uinput.BTN_1).OnBtn(data)


@sio.on("2")
async def sioOn(sid, data):
    print(data)
    print("2")
    ButtonsGamepad("2", uinput.BTN_2).OnBtn(data)


@sio.on("3")
async def sioOn(sid, data):
    print(data)
    print("3")
    ButtonsGamepad("3", uinput.BTN_3).OnBtn(data)


@sio.on("4")
async def sioOn(sid, data):
    print(data)
    print("4")
    ButtonsGamepad("4", uinput.BTN_4).OnBtn(data)


@sio.on("5")
async def sioOn(sid, data):
    print(data)
    print("5")
    ButtonsGamepad("5", uinput.BTN_5).OnBtn(data)


@sio.on("6")
async def sioOn(sid, data):
    print(data)
    print("6")
    ButtonsGamepad("6", uinput.BTN_6).OnBtn(data)


@sio.on("7")
async def sioOn(sid, data):
    print(data)
    print("7")
    ButtonsGamepad("7", uinput.BTN_7).OnBtn(data)


@sio.on("8")
async def sioOn(sid, data):
    print(data)
    print("8")
    ButtonsGamepad("8", uinput.BTN_8).OnBtn(data)


@sio.on("9")
async def sioOn(sid, data):
    print(data)
    print("9")
    ButtonsGamepad("9", uinput.BTN_9).OnBtn(data)


def isExits(my_object, name):
    try:
        my_object[name]
        return False
    except:
        return True

BUS_VIRTUAL = 0x00
name = "Microsoft X-Box 360 gamepad1"
vendor=0x045E,
product=0x028E,
version=0x110,
@sio.on("gamepad1")
async def gamepad1(sid, data):
    if isExits(controls, "gamepad1"):
        controls["gamepad1"] = uinput.Device(events, name, vendor, product, version)
        # controls["gamepad1"] = uinput.Device(
        #     events,
        #     vendor=0x045E,
        #     product=0x028E,
        #     version=0x110,
        #     name="Microsoft X-Box 360 gamepad1",
        #     BUS_VIRTUAL
        # )
        print("conect gamepad 1")


@sio.on("reconnectgamepad1")
async def gamepad1(sid, data):
    print("recoconect gamepad 1")
    controls["gamepad1"].destroy()
    controls["gamepad1"] = uinput.Device(events, name, BUS_VIRTUAL)
    # controls["gamepad1"] = uinput.Device(
    #     events,
    #     vendor=0x045E,
    #     product=0x028E,
    #     version=0x110,
    #     name="Microsoft X-Box 360 gamepad1",
    # )


# @sio.on("gamepad2")
# async def gamepad2(sid, data):
#     if isExits(controls, "gamepad2"):
#         controls["gamepad2"] = vg.VX360Gamepad()
#         print("conect gamepad 2")


# @sio.on("gamepad3")
# async def gamepad3(sid, data):
#     if isExits(controls, "gamepad3"):
#         controls["gamepad3"] = vg.VX360Gamepad()
#         print("conect gamepad 3")


@sio.event
async def connect(sid, data):
    print("connect ", sid)


@sio.event
async def disconnect(sid):
    print("disconnect ", sid)


if __name__ == "__main__":
    print("Init Server")
    uvicorn.run(app, host="0.0.0.0", port=8090)
