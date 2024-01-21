import cv2
import os
from postProcessing import PostProcessing

class ImageProcessor(PostProcessing):

    def __init__(self, input_dir, output_dir, crop_size=None):
        super().__init__()
        self.input_dir = input_dir #入力ディレクトリのパス
        self.output_dir = output_dir #出力ディレクトリのパス
        self.crop_size = crop_size #画像のトリミングサイズ

    def process_images(self):
        os.makedirs(self.output_dir, exist_ok=True) # 出力ディレクトリを作成（存在しない場合）


        files = os.listdir(self.input_dir) # 入力ディレクトリ内のファイル一覧を取得する


        for file_name in files:
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(self.input_dir, file_name)
                output_path = os.path.join(self.output_dir, file_name)

                img = cv2.imread(input_path)  # 画像を読み込み

                height, width, _ = img.shape # 画像の高さ、幅、チャンネル数を取得


                if self.crop_size:
                     # トリミングサイズが指定されている場合
                    top = max(0, (height - self.crop_size) // 2)
                    bottom = min(height, top + self.crop_size)
                    left = max(0, (width - self.crop_size) // 2)
                    right = min(width, left + self.crop_size)
                else:
                     # トリミングサイズが指定されていない場合、短い辺のサイズに合わせてトリミング
                    crop_size = min(height, width)
                    top = (height - crop_size) // 2
                    bottom = top + crop_size
                    left = (width - crop_size) // 2
                    right = left + crop_size

                cropped_img = img[top:bottom, left:right]

                # 保存先をinput_dirに変更して上書き保存
                cv2.imwrite(input_path, cropped_img)
               #cv2.imwrite(output_path, cropped_img)

class K20114(ImageProcessor):

    def __init__(self):
        super().__init__(
            input_dir="/Users/k20114kk/Documents/GitHub/kadai12/img/edit",
            output_dir="/Users/k20114kk/Documents/GitHub/kadai12/img/saved",
            crop_size=200 # 画像のトリミングサイズを指定
        )

    def processImage(self, outputFileName: str) -> None:
        self.process_images() # 画像のトリミングを実行
        img = self.getEditImage()  # 編集された画像を取得
        if img is not None:
            self.exportImage(outputFileName, img) # 編集された画像を指定されたファイル名で保存

if __name__ == "__main__":
    # K20114クラスのインスタンスを作成
    k20114_instance = K20114()
    # 画像のトリミングと保存を実行
    k20114_instance.processImage("output_image.jpg")
