# 各画像処理関数が書いてあるファイルのクラスをインポート
from sample import k20000 as Sample 

class PPManager():
    def __init__(self):
        # ここで各クラスをインスタンス化する
        self.sample = Sample()
        pass


# debug用
if __name__ == "__main__":
    # 使用例
    ppManager = PPManager()
    ppManager.sample.sampleFunc()
    ppManager.sample.exportImage("sample.png")