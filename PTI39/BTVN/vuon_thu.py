import json

class Animal:

    def __init__(self, name, species, sound, weight):
        self.name = name
        self.species = species
        self.sound = sound
        self.weight = weight

    def make_sound(self):
        print(f"{self.name} kêu '{self.sound}'")


# Danh sách động vật trong vườn bách thú
zoo = [
    Animal("ran", "bo_sat", "Phì phì", 5),
    Animal("su_tu", "co_vu", "Gầm gừ", 190),
    Animal("khi", "co_vu", "Chí chóe", 40),
    Animal("vet", "chim", "Líu lo", 1)
]

# Sắp xếp theo cân nặng tăng dần
zoo.sort(key=lambda animal: animal.weight)

# Hiển thị thông tin sau khi sắp xếp
for animal in zoo:
    print("ten:", animal.name)
    print("loai:", animal.species)
    print("can nang:", animal.weight, "kg")
    animal.make_sound()
    print()

# Chỉ lưu tên và cân nặng vào file JSON
data = []

for animal in zoo:
    data.append({
        "ten": animal.name,
        "can_nang": animal.weight
    })

with open("animals.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Đã lưu dữ liệu vào file animals.json")