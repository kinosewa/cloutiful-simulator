# jajajajajajjaajjajajsjajsajsajjajsjaj

import time
import random
import logging
from pynput import keyboard

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

key_pressed = False
dks_key = "n" # acá pones la tecla donde singletapeas, idealmente es el mismo valor de k1
k1 = "n" # este es k1
k2 = "m" # acá pones la otra tecla que usas
stop_key = "o" # con esta detienes el Cloutiful Simulator™

def press_key(controller, key):
    logging.debug(f"Presionando: {key}")
    controller.press(key)
    time.sleep(random.uniform(0.01, 0.07))
    controller.release(key)
    logging.debug(f"Liberada: {key}")

def on_press(key):
    global key_pressed
    try:
        if key.char == dks_key and not key_pressed:
            logging.debug(f"{dks_key} presionada")
            press_key(controller, k1)
            key_pressed = True
    except AttributeError:
        pass

def on_release(key):
    global key_pressed
    try:
        if key.char == dks_key and key_pressed:
            logging.debug(f"{dks_key} liberada")
            press_key(controller, k2)
            key_pressed = False
        if key.char == stop_key:
            logging.debug(f"La tecla para detener el programa ({stop_key}) ha sido presionada, deteniendo el Cloutiful Simulator™, ¡Vuelva pronto!")
            return False
    except AttributeError:
        pass


controller = keyboard.Controller()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    logging.debug(f"Bienvenido a Cloutiful Simulator™, presiona tu tecla de singletap ({dks_key}) para comenzar!")
    listener.join()
