from PIL import Image


def load_image(path):
    return Image.open(path)


def save_image(image, path):
    image.save(path)


def convert_to_grayscale(image):
    return image.convert('L')


def binarize_image(image, threshold=128):
    binary_image = image.point(lambda p: 255 if p >= threshold else 0)
    return binary_image


# Caminho para a imagem de entrada
input_image_path = "/home/fcc/workspace/machine_learning_specialist_dio/desafio3/lena.png"

# Carregar a imagem
image = load_image(input_image_path)

# Converter para níveis de cinza
grayscale_image = convert_to_grayscale(image)
grayscale_image_path = '/home/fcc/workspace/machine_learning_specialist_dio/desafio3/lena_grayscale.png'
save_image(grayscale_image, grayscale_image_path)

# Binarizar a imagem
binary_image = binarize_image(grayscale_image)
binary_image_path = '/home/fcc/workspace/machine_learning_specialist_dio/desafio3/lena_binary.png'
save_image(binary_image, binary_image_path)

print("Imagens em níveis de cinza e binarizadas salvas.")
