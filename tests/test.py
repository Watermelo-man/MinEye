import cv2

def resize_image(input_image_path, target_width=1024):
    # Загрузка изображения
    image = cv2.imread(input_image_path)
    
    # Получение исходных размеров изображения
    height, width, _ = image.shape

    # Вычисление новой высоты с сохранением соотношения сторон
    new_height = int(height * (target_width / width))

    # Изменение размера изображения
    resized_image = cv2.resize(image, (target_width, new_height))

    # Сохранение измененного изображения
   # cv2.imwrite(output_image_path, resized_image)
    cv2.imshow('orig',image)
    cv2.imshow("res",resized_image)
    cv2.waitKey(0)
if __name__ == "__main__":
    input_image_path = 'C:\\Projects\\orereco\\source\\0010.jpg'  # Укажите путь к вашему изображению
    #output_image_path = 'измененное_изображение.jpg'   # Укажите путь для сохранения измененного изображения

    resize_image(input_image_path)