# import os
# import shutil
# import random
# from tqdm import tqdm

# # Base paths
# base_path = r"C:\imagevision projects\tata\23sept_augumented\DATASET"
# train_images = os.path.join(base_path, "train", "images")
# train_labels = os.path.join(base_path, "train", "labels")

# valid_images = os.path.join(base_path, "valid", "images")
# valid_labels = os.path.join(base_path, "valid", "labels")

# # Create valid output folders
# os.makedirs(valid_images, exist_ok=True)

# os.makedirs(valid_labels, exist_ok=True)

# # List all image files
# image_files = [f for f in os.listdir(valid_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
# random.shuffle(image_files)

# # 20% split
# num_valid = int(len(image_files) * 0.5)
# print(num_valid)
# valid_files = image_files[:num_valid]

# # Move 20% to valid folder
# for img_file in tqdm(valid_files, desc="Moving to valid set"):
#     label_file = os.path.splitext(img_file)[0] + ".txt"

#     # Move image
#     src_img = os.path.join(train_images, img_file)
#     dst_img = os.path.join(valid_images, img_file)
#     shutil.move(src_img, dst_img)

#     # Move label
#     src_lbl = os.path.join(train_labels, label_file)
#     dst_lbl = os.path.join(valid_labels, label_file)
#     if os.path.exists(src_lbl):
#         shutil.move(src_lbl, dst_lbl)
#     else:
#         print(f"⚠️ Label missing for {img_file}")

# ----------------------------------------------------------------------------------------
# VALID DATA
# import os
# import shutil
# import random
# from tqdm import tqdm

# # Base paths
# base_path = r"c:\imagevision projects\tata\bottomcut_8oct"
# train_images = os.path.join(base_path, "train", "images")
# train_labels = os.path.join(base_path, "train", "labels")

# valid_images = os.path.join(base_path, "valid", "images")
# valid_labels = os.path.join(base_path, "valid", "labels")

# # Create valid output folders
# os.makedirs(valid_images, exist_ok=True)
# os.makedirs(valid_labels, exist_ok=True)

# # List all image files from TRAIN (not valid)
# image_files = [f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
# random.shuffle(image_files)

# # 20% split
# num_valid = int(len(image_files) * 0.2)
# print(f"Moving {num_valid} images to validation set...")
# valid_files = image_files[:num_valid]

# # Move 20% to valid folder
# for img_file in tqdm(valid_files, desc="Moving to valid set"):
#     label_file = os.path.splitext(img_file)[0] + ".txt"

#     # Move image
#     src_img = os.path.join(train_images, img_file)
#     dst_img = os.path.join(valid_images, img_file)
#     if not os.path.exists(dst_img):
#         shutil.move(src_img, dst_img)

#     # Move label
#     src_lbl = os.path.join(train_labels, label_file)
#     dst_lbl = os.path.join(valid_labels, label_file)
#     if os.path.exists(src_lbl):
#         shutil.move(src_lbl, dst_lbl)
#     else:
#         print(f"⚠️ Label missing for {img_file}")

# -------------------------------------------------------------------------------------
#test
import os
import shutil
import random
from tqdm import tqdm

# Base paths
base_path = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\TATA_V3_HIMALAYA\image_data_\day_1_(05_12_25)\tata_meach_side_view_images\bp_images\data_set_final"
train_images = os.path.join(base_path, "train", "images")
train_labels = os.path.join(base_path, "train", "labels")

test_images = os.path.join(base_path, "valid", "images")
test_labels = os.path.join(base_path, "valid", "labels")

# Create output folders
os.makedirs(test_images, exist_ok=True)
os.makedirs(test_labels, exist_ok=True)

# ✅ List all image files from TRAIN (not TEST!)
image_files = [f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

# % split for test
test_split = 0.16    # 25% of data will go to test
num_test = int(len(image_files) * test_split)

print(f"Moving {num_test} images to test set...")

test_files = image_files[:num_test]

# ✅ Move test images/labels
for img_file in tqdm(test_files, desc="Moving to test set"):
    label_file = os.path.splitext(img_file)[0] + ".txt"

    # Image
    src_img = os.path.join(train_images, img_file)
    dst_img = os.path.join(test_images, img_file)
    if not os.path.exists(dst_img):
        shutil.move(src_img, dst_img)

    # Label
    src_lbl = os.path.join(train_labels, label_file)
    dst_lbl = os.path.join(test_labels, label_file)
    if os.path.exists(src_lbl):
        shutil.move(src_lbl, dst_lbl)
    else:
        print(f"⚠️ Label missing for {img_file}")
