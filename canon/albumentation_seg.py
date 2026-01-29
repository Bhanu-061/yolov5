import os
import cv2
import random
import albumentations as A

IMAGE_DIR = "dataset/images"
LABEL_DIR = "dataset/labels_yolo_seg"

AUG_IMAGE_DIR = "dataset/aug_images"
AUG_LABEL_DIR = "dataset/aug_labels"

os.makedirs(AUG_IMAGE_DIR, exist_ok=True)
os.makedirs(AUG_LABEL_DIR, exist_ok=True)

# -------------------------
# Helpers
# -------------------------
def load_yolo_seg(txt):
    polys, labels = [], []
    with open(txt) as f:
        for line in f:
            p = line.strip().split()
            labels.append(int(p[0]))
            coords = list(map(float, p[1:]))
            polys.append([(coords[i], coords[i+1]) for i in range(0, len(coords), 2)])
    return polys, labels


def save_yolo_seg(path, polys, labels):
    with open(path, "w") as f:
        for poly, cls in zip(polys, labels):
            flat = []
            for x, y in poly:
                flat.extend([min(max(x, 0), 1), min(max(y, 0), 1)])
            f.write(f"{cls} " + " ".join(f"{v:.6f}" for v in flat) + "\n")

# -------------------------
# Augmentations
# -------------------------
transforms = [
    A.HorizontalFlip(p=1),
    A.Affine(rotate=20, fit_output=True, cval=(0,0,0)),
    A.Affine(scale=(1.2,1.5), fit_output=True, cval=(0,0,0)),
    A.Affine(scale=(0.7,0.9), fit_output=True, cval=(0,0,0)),
    A.RandomBrightnessContrast(p=1)
]

N_AUGS = 4

for img_name in os.listdir(IMAGE_DIR):
    if not img_name.lower().endswith((".jpg", ".png")):
        continue

    base = os.path.splitext(img_name)[0]
    img_path = os.path.join(IMAGE_DIR, img_name)
    lbl_path = os.path.join(LABEL_DIR, base + ".txt")

    if not os.path.exists(lbl_path):
        continue

    image = cv2.imread(img_path)
    polygons, labels = load_yolo_seg(lbl_path)

    chosen = random.sample(transforms, N_AUGS)

    for i, t in enumerate(chosen, 1):
        aug = A.Compose(
            [t],
            polygon_params=A.PolygonParams(
                label_fields=["labels"],
                min_visibility=0.2
            )
        )

        out = aug(image=image, polygons=polygons, labels=labels)

        cv2.imwrite(
            os.path.join(AUG_IMAGE_DIR, f"{base}_aug{i}.jpg"),
            out["image"]
        )

        save_yolo_seg(
            os.path.join(AUG_LABEL_DIR, f"{base}_aug{i}.txt"),
            out["polygons"],
            out["labels"]
        )

    print(f"✅ Augmented {img_name}")
