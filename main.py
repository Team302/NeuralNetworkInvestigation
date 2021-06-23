import tensorflow as tf
import json

with open('Images Tagged as Valid/Filming Day 1 Video/ann/frame_00015.png.json') as f:
    data = json.load(f)

# for i in data["objects"]:
#     for j in data["points"]:
#         for k in data["exterior"]:
#             print(k)

# corners[0] is top left corner, corners[1] is bottom right corner of rectangle.
corners = data["objects"][1]["points"]["exterior"]
print(corners)
