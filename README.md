# Manimaciones
 
Animaciones matemáticas creadas con [Manim](https://www.manim.community/), utilizadas para mis propios videos en [mi canal](https://www.instagram.com/).
 
## Requisitos
 
- Python 3.9 o superior
- [Manim Community](https://docs.manim.community/en/stable/installation.html)
- Una distribución de LaTeX (por ejemplo [MiKTeX](https://miktex.org/) en Windows), necesaria para renderizar fórmulas
- Paciencia

## Instalación
 
```bash
git clone https://github.com/Cyor-byte/Manimaciones.git
cd Manimaciones
pip install manim
```
 
## Uso
 
Para renderizar una escena:
 
```bash
manim -pql archivo.py NombreDeLaEscena
```
 
La opción `-p` abre el video al terminar y `-ql` renderiza en baja calidad, muy útil para ir probando. Para la versión final usá `-qh` (alta calidad, 1080p) o `-qk` (4K).
 
Los videos se generan en la carpeta `media/`, que no se incluye en el repositorio.
 
## Contribuciones
 
Las sugerencias y mejoras son bienvenidas. Podés abrir un *issue* o enviar un *pull request*.
