<p align="center">
  <img src="https://i.ibb.co/gSmwN76/image-removebg-preview.png" width="250px">
</p>
Herramienta para escanear todos los puertos de una red, mediante el uso de la
libreria **socket**, no es necesario especificar, ya que escaneará los 65535 puertos.

#### Ejemplo:
<img src="https://i.ibb.co/0qXPpXJ/ejemplo.png" width="400px">

#### Pasos de instalación:

```
git clone https://github.com/LexaHck/PortScan
cd PortScan
```

```
chmod +x PortScan.py
pip3 install -r requeriments.txt
```

#### Uso:
```bash
python3 PortScan.py -t <ip-target>
```

##### Nota:
Debería funcionar todo bien, lo probé con distintos objetivos y me arroja buenos resultados y sin errores, en caso de fallos avisarme para arreglarlos. :D