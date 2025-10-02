from PIL import Image
import os

def voltear_imagen(imagen_ruta, imagen_salida):
    """
    Voltea una imagen horizontalmente para cambiar su dirección (izquierda <-> derecha).
    """
    try:
        imagen = Image.open(imagen_ruta)
        imagen_volteada = imagen.transpose(Image.FLIP_LEFT_RIGHT)
        imagen_volteada.save(imagen_salida)
        print(f"Imagen guardada en: {imagen_salida}")
    except Exception as e:
        print(f"Error al procesar la imagen '{imagen_ruta}': {e}")

def voltear_imagenes_en_lote(carpeta_entrada, carpeta_salida):
    """
    Voltea horizontalmente todas las imágenes en una carpeta.
    """
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    for archivo in os.listdir(carpeta_entrada):
        if archivo.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            ruta_original = os.path.join(carpeta_entrada, archivo)
            ruta_volteada = os.path.join(carpeta_salida, f"left_{archivo}")
            voltear_imagen(ruta_original, ruta_volteada)

if __name__ == "__main__":
    carpeta_entrada = r"C:\Users\elpaj\Documents\my_game\assets\img\players\npc\king\mis sprites\derecha"     # Carpeta con imágenes originales
    carpeta_salida = r"C:\Users\elpaj\Documents\my_game\assets\img\players\npc\king\mis sprites"    # Carpeta para guardar las imágenes volteadas
    voltear_imagenes_en_lote(carpeta_entrada, carpeta_salida)
