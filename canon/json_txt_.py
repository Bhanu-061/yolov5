import json
import os
from PIL import Image

# ---------- paths ----------
json_dir = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\Canon\engineering\image_json\labels"
image_dir = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\Canon\engineering\image_json\images"
output_dir = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\Canon\engineering\image_json"

os.makedirs(output_dir, exist_ok=True)

# ---------- class mapping ----------
class_map = {
    "ceti_box": 0
}

# ---------- process all json files ----------
for json_file in os.listdir(json_dir):
    if not json_file.endswith(".json"):
        continue

    json_path = os.path.join(json_dir, json_file)

    # image name must match json name
    base_name = os.path.splitext(json_file)[0]
    image_path = os.path.join(image_dir, base_name + ".jpg")

    if not os.path.exists(image_path):
        print(f"⚠ Image not found for {json_file}, skipping")
        continue

    # load image
    img = Image.open(image_path)
    img_w, img_h = img.size

    # load json
    with open(json_path, "r") as f:
        data = json.load(f)

    yolo_lines = []

    for shape in data.get("shapes", []):
        label = shape.get("label")
        if label not in class_map:
            continue

        if shape.get("shape_type") != "polygon":
            continue

        class_id = class_map[label]
        points = shape["points"]

        # normalize polygon points
        norm_points = []
        for x, y in points:
            x /= img_w
            y /= img_h
            norm_points.append(f"{x:.6f} {y:.6f}")

        line = f"{class_id} " + " ".join(norm_points)
        yolo_lines.append(line)

    # write txt
    txt_path = os.path.join(output_dir, base_name + ".txt")
    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

    print(f"✅ Converted: {json_file} → {base_name}.txt")

print("\n🎯 All LabelMe JSON files converted successfully!")
