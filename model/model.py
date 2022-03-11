import json
import os


class Model:
    def __init__(self):
        self.root = os.getcwd()
        self.config = self.read()

    def new(self) -> None:
        """
        ayarları sıfırlar
        :rtype: None
        """
        self.config = {
            'fg': '#000000',
            'bg': '#ffffff',
            'font-family': 'Arial',
            'font-size': 14,
            'font-style': 'normal',
            'screen_width': 700,
            'screen_height': 700
        }

        self._write()

    def _write(self) -> None:
        """
        Sınıf içerisinde dosyaya yazmak için kullanılmalıdır.
        :rtype: None
        """
        dumping = json.dumps(self.config, indent=4, sort_keys=True)

        with open(os.path.join(self.root, "model", "config.json"), "w") as f:
            f.write(dumping)

    def update(self, key: str, value: any) -> None:
        """
        Belli bir ayarı değiştirmek ve kaydetmek için kullanılır
        :rtype: None
        """
        self.config = self.read()
        self.config[key] = value
        self._write()

    def read(self) -> dict:
        """
        Ayarları okutur ve geri döndürür
        :rtype: dict
        """
        with open(os.path.join(self.root, "model", "config.json")) as f:
            data = f.read()
            return json.loads(data)

    def get(self, key: str) -> str:
        """
        Belli bir ayarı okutur ve geri döndürür
        :param key: str
        :return: str
        """
        self.config = self.read()
        return self.config.get(key)
