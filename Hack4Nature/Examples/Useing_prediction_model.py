from deepforest import main
from deepforest import get_data
import matplotlib.pyplot as plt
model = main.deepforest()
model.use_release()
model.config

im_bgr = model.predict_image(path="Hach4Nature/data/limit_marseille.png", return_plot=True)
#predict_image returns plot in BlueGreenRed (opencv style), but matplotlib likes RedGreenBlue, switch the channel order.
im_rgb = im_bgr[:, :, [2, 1, 0]]


plt.figure(figsize = (20,20))
plt.imshow(im_rgb)