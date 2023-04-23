#!/usr/bin/python3

import os
import sys
import signal
import socket
import optparse
from colorama import Fore

############----------############
#          By: LexaHck           #
#    https://github.com/LexaHck  #
#                                #
#     From the dark side...      #
#             -2023-             #
############----------############

# Colores
rojo = Fore.RED
azul = Fore.BLUE
amarillo = Fore.YELLOW
verde = Fore.GREEN
magenta = Fore.MAGENTA
blanco = Fore.WHITE
cyan = Fore.CYAN
reset = Fore.RESET

# CTRl_C
def ctrl_c(signum, frame):
    msg = f"\n\n{rojo}[!] Escaneo interrumpido...{reset}\n"
    print(msg, end='', flush=True)
    sys.stdout.flush()
    exit(1)

signal.signal(signal.SIGINT, ctrl_c)

all_ports = range(1, 65536)
open_ports = []

parser = optparse.OptionParser()

parser.add_option('-t', '--target', action="store", dest="target", help="Dirección IP (ex. 10.10.10.100).")

options, args = parser.parse_args()

target = options.target

if not target:
    print(f"{azul}USO: python3 PortScan.py -t {amarillo}<direccion-ip>{reset}")
    print(f"\n{rojo}[!] Error: Falta la dirección ip.{reset}")
    exit()

for port in all_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((target, port))
        
    if resultado == 0:
        print(f"{magenta}Puerto {port} (ABIERTO){reset}")
        open_ports.append(port)
        sock.close()
