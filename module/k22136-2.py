from PIL import Image

def resize_image(input_path, output_path, target_aspect_ratio):
    # 画像を開く
    original_image = Image.open(input_path)

    # 元の画像の縦横比を計算
    original_width, original_height = original_image.size
    original_aspect_ratio = original_width / original_height

    # ターゲットの縦横比に合わせて新しいサイズを計算
    if original_aspect_ratio > target_aspect_ratio:
        new_width = int(original_height * target_aspect_ratio)
        new_height = original_height
    else:
        new_width = original_width
        new_height = int(original_width / target_aspect_ratio)

    # 画像をリサイズ
    resized_image = original_image.resize((new_width, new_height))

    # リサイズされた画像を保存
    resized_image.save(output_path)


# debug用
if __name__ == "__main__":
    # ユーザーによって指定された縦横比を取得
    user_aspect_ratio = float(input("縦横比を入力してください（例: 1.77）: "))

    # 例: 入力画像のパスと出力画像のパス
    image_path = "img/edit/tateyoko_input.jpg"
    output_path = "img/edit/tateyoko_input.jpg"

    # 画像を指定された縦横比にリサイズ
    resize_image(image_path, output_path, user_aspect_ratio)