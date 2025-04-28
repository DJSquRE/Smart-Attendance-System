import cv2
import os

path = 'known_faces'
student_names = []
images = []

mylist = os.listdir(path)

for cl in mylist:
    # Try loading the image
    curimg = cv2.imread(f'{path}/{cl}')
    
    # Check if image was loaded successfully
    if curimg is None:
        print(f"Warning: {cl} is not a valid image or is corrupted.")
        continue  # Skip this image
    
    # Optional: Check if image has valid shape (e.g., width > 0 and height > 0)
    if curimg.shape[0] == 0 or curimg.shape[1] == 0:
        print(f"Warning: {cl} is an empty image.")
        continue  # Skip this image

    images.append(curimg)
    student_names.append(os.path.splitext(cl)[0])

print("Valid images loaded:", len(images))
