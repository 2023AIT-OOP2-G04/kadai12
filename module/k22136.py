from PIL import Image, ImageEnhance

def adjust_saturation_and_brightness(image_path, saturation_factor, brightness_factor, output_path):
    # 画像を開く
    img = Image.open(image_path)

    # 彩度を変更
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation_factor)

    # 明度を変更
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness_factor)

    # 画像を保存
    img.save(output_path)

if __name__ == "__main__":
    # ユーザーからの入力を受け取る  
    image_path = "img/edit/iro_input.jpg"
    output_path = "img/edit/iro_input.jpg"
    saturation_factor = float(input("彩度の変更倍率を入力してください (1.0 が変更なし): "))
    brightness_factor = float(input("明度の変更倍率を入力してください (1.0 が変更なし): "))

    # 関数を呼び出して画像の彩度と明度を変更
    adjust_saturation_and_brightness(image_path, saturation_factor, brightness_factor, output_path)

    print("画像の彩度と明度を変更しました。")
