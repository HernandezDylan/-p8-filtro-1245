import cv2

# Cargar la imagen
imagen = cv2.imread("../imagenes/Ballena 1245.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original Ballena 1245", imagen)
cv2.imshow("Imagen con filtro de mediana", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/Ballena 1245.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/Ballena 1245.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()