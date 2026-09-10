"""
Animación: "goles (+ asistencias)" - Haaland vs Messi
Formato vertical (9:16) pensado para TikTok / Instagram / YouTube Shorts.

Para renderizar:
    Vista previa rápida (baja calidad):
        manim -pql goles_asistencias.py GolesAsistencias
    Render final (alta calidad):
        manim -pqh goles_asistencias.py GolesAsistencias
"""

from manim import *

# --- Configuración de formato vertical (9:16) para redes sociales ---
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# --- Colores ---
CELESTE = "#5BC8F5"   # celeste para Haaland
DORADO = "#FFD700"    # dorado para Messi


def crear_punto_brillante(punto, color, radio=0.16):
    """
    Simula un punto 'dorado brillante' apilando círculos concéntricos
    de opacidad decreciente detrás del punto principal (efecto halo/glow).
    """
    halo_externo = Dot(punto, radius=radio * 3.2, color=color, fill_opacity=0.12)
    halo_medio = Dot(punto, radius=radio * 2.1, color=color, fill_opacity=0.30)
    nucleo = Dot(punto, radius=radio, color=color, fill_opacity=1)
    return VGroup(halo_externo, halo_medio, nucleo)


class GolesAsistencias(Scene):
    def construct(self):
        # Posición horizontal "arbitraria" para los puntos: el eje x no tiene
        # escala/significado, así que se elige un valor fijo, corrido hacia la
        # izquierda para dejar espacio a la derecha para los nombres.
        X_POS = 2.5

        # ------------------------------------------------------------------
        # PASO 1 y 2 (simultáneos):
        # Título arriba centrado + creación de los ejes (x sin escala,
        # y de 0 a 600 de 100 en 100)
        # ------------------------------------------------------------------
        titulo = Text("Goles (+ asistencias)", font_size=40).to_edge(UP, buff=2 )

        ejes1 = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 600, 100],
            x_length=6,
            y_length=10,
            tips=False,
            axis_config={"color": WHITE},
            x_axis_config={
                "include_numbers": False,
                "include_ticks": False,
            },
            y_axis_config={
                "include_numbers": True,
                "font_size": 24,
            },
        ).next_to(titulo, DOWN, buff=0.8)

        self.play(Write(titulo), Create(ejes1), run_time=1.5)
        self.wait(2)

        # ------------------------------------------------------------------
        # PASO 3:
        # Punto celeste en (x, 366) + nombre "Haaland" a la derecha +
        # valor "366" arriba, todo en color celeste
        # ------------------------------------------------------------------
        punto_haaland = Dot(
            ejes1.coords_to_point(X_POS, 366), radius=0.14, color=CELESTE
        )
        nombre_haaland = Text("Haaland", font_size=30, color=CELESTE).next_to(
            punto_haaland, RIGHT, buff=0.5
        )
        valor_haaland = Text("366", font_size=30, color=CELESTE).next_to(
            punto_haaland, UP, buff=0.5
        )

        self.play(
            FadeIn(punto_haaland, scale=0.5),
            Write(nombre_haaland),
            Write(valor_haaland),
        )
        self.wait(2)

        # ------------------------------------------------------------------
        # PASO 4:
        # El punto se mueve a (x, 373) manteniendo la misma x.
        # Los textos lo acompañan y el valor cambia de "366" a "373"
        # ------------------------------------------------------------------
        nueva_pos_haaland = ejes1.coords_to_point(X_POS, 373)

        nuevo_valor_haaland = Text("373", font_size=30, color=CELESTE).next_to(
            nueva_pos_haaland, UP, buff=0.6
        )

        self.play(
            punto_haaland.animate.move_to(nueva_pos_haaland),
            nombre_haaland.animate.next_to(nueva_pos_haaland, RIGHT, buff=0.6),
            Transform(valor_haaland, nuevo_valor_haaland),
        )
        self.wait(2)

        # ------------------------------------------------------------------
        # PASO 5:
        # Se "achica" la escala del eje y (ahora llega hasta 1300) para que
        # sea visible el tramo 1100-1200. El punto y los textos de Haaland
        # se reposicionan para seguir representando el mismo valor (373)
        # en la nueva escala.
        # ------------------------------------------------------------------
        ejes2 = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 1300, 100],
            x_length=6,
            y_length=10,
            tips=False,
            axis_config={"color": WHITE},
            x_axis_config={
                "include_numbers": False,
                "include_ticks": False,
            },
            y_axis_config={
                "include_numbers": True,
                "font_size": 24,
            },
        ).next_to(titulo, DOWN, buff=0.8)

        pos_haaland_reescalada = ejes2.coords_to_point(X_POS, 373)

        self.play(
            Transform(ejes1, ejes2),
            FadeOut(valor_haaland), FadeOut(nombre_haaland),
            punto_haaland.animate.move_to(pos_haaland_reescalada),
            run_time=2,
        )
        self.wait(2)

        # ------------------------------------------------------------------
        # PASO 6:
        # Punto dorado brillante en (x, 1198) + nombre "Messi" a la derecha +
        # valor "1198" arriba, todo en color dorado
        # ------------------------------------------------------------------
        pos_messi = ejes2.coords_to_point(X_POS, 1198)
        punto_messi = crear_punto_brillante(pos_messi, DORADO)

        nombre_messi = Text("Messi", font_size=30, color=DORADO).next_to(
            pos_messi, RIGHT, buff=0.6
        )
        valor_messi = Text("1198", font_size=30, color=DORADO).next_to(
            pos_messi, UP, buff=0.8
        )

        self.play(
            FadeIn(punto_messi, scale=0.5),
            Write(nombre_messi),
            Write(valor_messi),
        )
        self.wait(2)
