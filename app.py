# from selenium import webdriver
from fastapi import FastAPI, Header, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import Response, StreamingResponse
# from fastapi.responses import StreamingResponse
import uvicorn
# Importar el módulo Image de PIL
from PIL import Image
from os import getcwd, path
import cv2  # para procesar la imagen y guardarla como mp4
import numpy as np  # para trabajar con matrices
import pyscreenshot as ImageGrab
# import io
import asyncio

# import mss
print("Version 1.0")
# Create an mss object
# sct = mss.mss()

app = FastAPI()

PORTION_SIZE = 1024 * 1024

current_directory = getcwd() + "/"

# Mostrar la imagen en una ventana
# screenshot.show()

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
            await new()
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
    
    # # Create a webdriver object for Chrome
    # driver = webdriver.Chrome()
    # # Go to a website
    # driver.get('https://www.bing.com')

# @app.get("/videocap")
# def get_video():
#     print("getting video")
#     video = cv2.VideoCapture(0)
#     # Definir una función generadora que envía los chunks

#     def iterfile():
#         while True:
#             print("dffd")
#             # Leer un frame del vídeo
#             ret, frame = video.read()
#             if not ret:
#                 print("Breaksdklsk")
#                 break
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             frame = cv2.resize(frame, (960, 480),
#                                interpolation=cv2.INTER_AREA)
#             # Codificar el frame como un array de bytes
#             _, buffer = cv2.imencode(".jpg", frame)
#             bytes = buffer.tobytes()
#             yield bytes

#             # Obtener chunks de 1024 bytes del array de bytes
#             # chunks = [bytes[i:i+1024] for i in range(0, len(bytes), 1024)]

#             # Enviar los chunks
#             # for chunk in chunks:
#             #     yield chunk

#     # Devolver una respuesta de streaming con el media_type adecuado
#     return StreamingResponse(iterfile(), media_type="video/mp4")
#     # Definir una función generadora que envía los bytes
#     # while(True):
#     #     def iterfile():
#     #         print("iterfile video")
#     #         # Capturar la imagen con OpenCV
#     #         cap = cv2.VideoCapture(0)
#     #         ret, frame = cap.read()
#     #         cap.release()

#     #         # Convertir la imagen a bytes
#     #         _, buffer = cv2.imencode(".jpg", frame)
#     #         image_bytes = buffer.tobytes()

#     #         # Get chunks of 1024 bytes from the byte array
#     #         # chunks = [image_bytes[i:i+1024] for i in range(0, len(image_bytes), 1024)]
#     #         yield image_bytes
#     #     # url = "127.0.0.1:8000/videocap"
#     #     # session = requests.Session()
#     #     # r = session.get(url, stream=True)
#     #     # r.raise_for_status()

#     #     # for chunk in r.iter_content(1024*1024):
#     #     #     yield chunk

#     #     # Devolver una respuesta de streaming con el media_type adecuado
#     #     return StreamingResponse(iterfile(), media_type="video/mp4")


# @app.get("/video/{name_video}")
# def get_video(name_video: str, range: str = Header(None)):
#     # ///gETV DSKDOK
#     print("Get_Video")
#     # bytes=0-
#     start, end = range.replace("bytes=", "").split("-")
#     start = int(start)
#     end = int(start + PORTION_SIZE)

#     # LEEMOS LA POSICION EXACTA DEL ARCHIVO

#     # Tomar la captura de pantalla y convertirla a una matriz numpy
#     screenshot = pyautogui.screenshot()
#     image = np.array(screenshot)
#     video = cv2.VideoWriter("videocap.mp4", cv2.VideoWriter_fourcc(
#         *"mp4v"), 30, (image.shape[1], image.shape[0]))

#     # Escribir la imagen en el vídeo
#     video.write(image)

#     # Liberar el objeto VideoWriter
#     video.release()

#     with open(current_directory + name_video, "rb") as myfile:

#         myfile.seek(start)
#         data = myfile.read(end - start)
#         size_video = str(path.getsize(current_directory + name_video))

#         headers = {
#             'Content-Range': f'bytes {str(start)}-{str(end)}/{size_video}',
#             'Accept-Ranges': 'bytes'
#         }
#         return Response(content=data, status_code=206, headers=headers, media_type="video/mp4")
