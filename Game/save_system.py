import xml.etree.ElementTree as et
import definition as df


class SaveSystem:
    def __init__(self):
        self.root = df.ROOT_PATH
        self.coins = 0

    def create_save(self):
        root = et.Element("root")
        stats = et.SubElement(root, "stats")
        tree = et.ElementTree(root)
        with open(f"{self.root}/save.xml", "wb") as file:
            tree.write(file)

    def load_options(self) -> int:
        try:
            tree = et.parse(f"{self.root}/options.xml")
            root = tree.getroot()
            return float(root[0].text)
        except FileNotFoundError:
            root = et.Element("root")
            volume = et.SubElement(root, "volume")
            volume.text = "1"
            tree = et.ElementTree(root)
            with open(f"{self.root}/options.xml", "wb") as file:
                tree.write(file)
            return 1

    def save_options(self, v=0.1):
        root = et.Element("root")
        volume = et.SubElement(root, "volume")
        volume.text = str(v)
        tree = et.ElementTree(root)
        with open(f"{self.root}/options.xml", "wb") as file:
            tree.write(file)

    def save_data(self, data: dict):
        root = et.Element("root")
        stats = et.SubElement(root, "stats")
        for key in data["stats"]:
            e = et.SubElement(stats, key)
            e.text = data["stats"][key]

        tree = et.ElementTree(root)
        with open(f"{self.root}/save.xml", "wb") as file:
            tree.write(file)

    def load_save_data(self):
        try:
            tree = et.parse(f"{self.root}/save.xml")
            root = tree.getroot()
            data_to_return = {
                "stats": {
                    "coins": root[0][0].text,
                    "map": root[0][1].text
                }
            }
            return data_to_return
        except FileNotFoundError:
            return None
