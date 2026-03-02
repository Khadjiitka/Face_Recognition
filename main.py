import cv2

# Подключаем камеру
cap = cv2.VideoCapture(0)

# Загружаем классификатор лиц (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    ret, frame = cap.read()   # читаем кадр
    # ret — успешно ли считан кадр (True/False)
    # frame — сам кадр (изображение
    if not ret:
        break

    # Переводим кадр в черно-белый
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ищем лица
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=2,
        minNeighbors=3
    )

    # Рисуем прямоугольники
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Показываем результат
    cv2.imshow("Face Detection", frame)

    # Выход по нажатию q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем камеру
cap.release()
cv2.destroyAllWindows()