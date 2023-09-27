import subprocess
import io
# # Load the image into Python using PIL
# from PIL import Image
# image = Image.open("screenshot.png")

from fastapi import FastAPI, Header, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import Response, StreamingResponse
import uvicorn
# Importar el módulo Image de PIL
from PIL import Image
from os import getcwd, path
import cv2  # para procesar la imagen y guardarla como mp4
import numpy as np  # para trabajar con matrices
import pyscreenshot as ImageGrab
import asyncio

print("Version 1.0")
app = FastAPI()
PORTION_SIZE = 1024 * 1024
current_directory = getcwd() + "/"

@app.websocket("/ws")
async def get_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        # Define the screen region to capture
        monitor = {"top": 100, "left": 100, "width": 200, "height": 200}
        while True:
            async def imageggg():
                # Capturar una parte de la pantalla
                im = ImageGrab.grab()

                # Convertir la imagen de PIL a un array de NumPy
                im_np = np.array(im)

                # Convertir la imagen a escala de grises
                # frame = cv2.cvtColor(im_np, cv2.COLOR_RGB2GRAY)
                buffer = cv2.imencode('.jpg', im_np)[1]
                # Obtener los bytes de la imagen
                image_bytes = buffer.tobytes()
                # Abrir un archivo de imagen desde una ruta local

                await websocket.send_bytes(image_bytes)

            async def new():
                # subprocess.run([current_directory +"runImage.sh"], stdout=subprocess.PIPE)

                # Crear un subprocesso que ejecute el comando sleep 5
                # proceso = await asyncio.create_subprocess_exec("-window", "root", "yo.jpg")
                try:
                    # subprocess.run([current_directory +"runImage.sh"], stdout=subprocess.PIPE)
                    # # Esperar a que termine el subprocesso
                    # await proceso.wait()
                    # print("Iniciando Subproxeso")
                    # Crear un subprocesso que ejecute el comando sleep 5
                    # proceso = await asyncio.create_subprocess_exec("sleep", "")
                    proceso = await asyncio.create_subprocess_exec("import", "-window", "root", "yo.jpg")
                    await proceso.wait()
                    proceso = await asyncio.create_subprocess_exec("sleep", "0.3")
                    await proceso.wait()
                    # # Esperar a que termine el subprocesso
                    # await proceso.wait()
                    # print("End Subproceso")
                    screenshot = Image.open(current_directory + "yo.jpg")
                    frame = np.array(screenshot)
                    buffer = cv2.imencode('.jpg', frame)[1]
                    # buffer = io.BytesIO(frame)
                    # screenshot.save(buffer, output='png')
                    image_bytes = buffer.tobytes()
                    # success, frame = camera.read()
                    # if not success:
                    #     break
                    # else:
                    # buffer = cv2.imencode('.jpg', frame)[1]
                    await websocket.send_bytes(image_bytes)
                except Exception as e:
                    print(e)
                    Exception("Error sending")
            # await new()
            async def newapp():
                # Capture the screen using xwd
                xwd_output = subprocess.check_output(["xwd", "-root", "-silent"])
                
                # Convert the output to a PNG image using convert
                convert_output = subprocess.check_output(["convert", "xwd:-", "screenshot.png"], input=xwd_output)
                
                # Captura la pantalla utilizando xwd
                # xwd_output = subprocess.check_output(["xwd", "-root", "-silent"])
                
                # # Convierte la salida a una imagen PIL
                # image = Image.open(io.BytesIO(xwd_output))
                # image.save(current_directory + "screenshot.jpg", "JPEG")
                # screenshot = Image.open(current_directory + "screenshot.jpg")
                # frame = np.array(screenshot)
                # buffer = cv2.imencode('.jpg', frame)[1]
                # image_bytes = buffer.tobytes()
                # Open the PNG image
                image = Image.open("image.png")
                
                # Get the bytes of the image
                image_bytes = image.tobytes()
                await websocket.send_bytes(image_bytes)
            await newapp()

            async def funciona():
                screenshot = Image.open(current_directory + "yo.jpg")

                # Capture the whole screen
                # screenshot = sct.grab(monitor)
                # roi_img = screenshot.crop()
                # Create a bytes buffer
                # buffer = io.BytesIO()
                # Save the image to the buffer in PNG format
                # screenshot.save(buffer, output='jpg')
                # Get the bytes from the buffer
                # image_bytes = screenshot.tobytes()
                # Capture the whole screen
                # im = ImageGrab.grab()
                # screenshot = pyautogui.screenshot()
                frame = np.array(screenshot)
                buffer = cv2.imencode('.jpg', frame)[1]
                # buffer = io.BytesIO(frame)
                # screenshot.save(buffer, output='png')
                image_bytes = buffer.tobytes()
                # success, frame = camera.read()
                # if not success:
                #     break
                # else:
                # buffer = cv2.imencode('.jpg', frame)[1]
                await websocket.send_bytes(image_bytes)
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
