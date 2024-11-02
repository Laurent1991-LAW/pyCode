import os
from PIL import Image
import shutil
import pyheif


def heic_to_pil(heic_path):
    """ 将 HEIC 文件转换为 PIL.Image 对象 """
    heif_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    return image


def process_images():
    # 当前文件夹路径
    current_dir = os.getcwd()
    origin_dir = os.path.join(current_dir, 'origin')

    # 创建origin目录
    if not os.path.exists(origin_dir):
        os.makedirs(origin_dir)

    # 获取当前目录下所有图片文件
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.heic']
    image_files = [f for f in os.listdir(current_dir) if os.path.isfile(
        f) and os.path.splitext(f)[1].lower() in image_extensions]

    # 移动图片到origin目录
    for image_file in image_files:
        shutil.move(image_file, origin_dir)

    # 处理图片
    for image_file in image_files:
        try:
            image_path = os.path.join(origin_dir, image_file)
            if image_file.lower().endswith('.heic'):
                img = heic_to_pil(image_path)
            else:
                img = Image.open(image_path)

            print(f'Processing: {image_file}')
            # 计算新的尺寸
            width, height = img.size
            new_width = width // 3
            new_height = int((new_width / width) * height)

            # 调整图片尺寸
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 转换格式
            if img.mode != 'RGB':
                img = img.convert('RGB')

            new_image_file = os.path.splitext(image_file)[0] + '.jpg'
            img.save(os.path.join(current_dir, new_image_file), 'JPEG')

        except Exception as e:
            print(f"{image_file} processing encountered an error: {str(e)}")


if __name__ == "__main__":
    process_images()
