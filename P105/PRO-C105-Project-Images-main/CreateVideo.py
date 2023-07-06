import os
import cv2

path = "/Users/gurje/Desktop/P105/PRO-C105-Project-Images-main/Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in['.gif', '.png', '.jpg', '.jpeg']:
        filename = path + "/" + file
        print(filename)
        Images.append(filename)
print(len(Images))
count = len(Images)
frame =  cv2.imread(Images[0])
height, width, layers = frame.shape
size = (width, height)
out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    print(Images[i])
    frame = cv2.imread(Images[i])
    out.write(frame)
    cv2.imshow("movie", frame)
    if cv2.waitKey(25) == 32:
        break

out.release()
print("done")