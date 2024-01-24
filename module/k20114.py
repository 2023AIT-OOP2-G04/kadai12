import cv2
import os
from postProcessing import PostProcessing

class ImageProcessor(PostProcessing):

    def __init__(self, input_dir):
        super().__init__()
        self.input_dir = input_dir

    def process_images(self, vertical_crop_size=None, horizontal_crop_size=None):
         # 指定されたフォルダ内のファイルを取得
        files = os.listdir(self.input_dir)

         # フォルダ内の各画像ファイルに対して処理を行う
        for file_name in files:
            # 画像ファイルであるかを確認
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                # 画像ファイルのパスを構築
                input_path = os.path.join(self.input_dir, file_name)

                # 画像の読み込み
                img = cv2.imread(input_path)
                height, width, _ = img.shape

                # トリミングサイズが指定されていればトリミングを行う
                if vertical_crop_size is not None and horizontal_crop_size is not None:
                    top = max(0, (height - vertical_crop_size) // 2)
                    bottom = min(height, top + vertical_crop_size)
                    left = max(0, (width - horizontal_crop_size) // 2)
                    right = min(width, left + horizontal_crop_size)
                else:
                    # サイズ指定がない場合は元のサイズを維持
                    top, bottom, left, right = 0, height, 0, width

                # トリミングされた画像を元のファイルに上書き保存
                cropped_img = img[top:bottom, left:right]
                cv2.imwrite(input_path, cropped_img)

class K20114(ImageProcessor):

    def __init__(self, input_dir):
        super().__init__(input_dir)

    def processImage(self, vertical_crop_size=None, horizontal_crop_size=None) -> None:
        # 画像のトリミング処理を実行
        self.process_images(vertical_crop_size, horizontal_crop_size)
        img = self.getEditImage()  # PostProcessing内の関数を適切に使用

if __name__ == "__main__":
    # ユーザーからの入力を受け取る
    input_dir = input("画像フォルダの相対パスを入力してください: ")
    vertical_crop_size = int(input("縦のトリミングサイズを入力してください（単位: ピクセル）: "))
    horizontal_crop_size = int(input("横のトリミングサイズを入力してください（単位: ピクセル）: "))

    # K20114クラスのインスタンスを生成
    k20114_instance = K20114(input_dir=input_dir)

    # 画像のトリミング処理を実行
    k20114_instance.processImage(vertical_crop_size, horizontal_crop_size)
