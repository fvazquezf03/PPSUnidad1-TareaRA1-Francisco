### 1. Instalar Firejail y Firetools
```bash 
# En Debian/Ubuntu
sudo apt update
sudo apt install -y firejail firetools
```
- **Captura de instalación**:
![alt text](image.png)

- **Para saber que versión tiene** :
```bash
# Verificar instalación
firejail --version
```
![alt text](image-1.png)

### 2. Primero preparar el firejail:
- Si quieres que tu aplicación acceda solo en una carpeta especifica:
```bash
firejail --private=/home/ppsfran/Proyecto-Lavadero/

```

![alt text](image-2.png)


### 3.Segundo prepara el entorno para poder ejecutar las pruebas:
1. Creamos entorno virtual de Python

```bash
python3 -m venv sanbox
```

![alt text](image-3.png)

2. Activamos el entorno virtual:

```bash
source sanbox/bin/activate
```

![alt text](image-4.png)

3. Ejecutar el programa dentro de sanbox dentro de la carpeta aislada:

```bash
PYTHONPATH=src python3 main_app
```

![alt text](image-5.png)