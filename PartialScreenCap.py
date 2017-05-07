import pyscreenshot as ImageGrab
import argparse
import cv2

# We save the (x,y) couples of the partial screenshot in corners and if we are doing cropping operations
corners = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	
	# global variables references
	global corners, cropping;

	if event == cv2.EVENT_LBUTTONDOWN:
		corners = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:

		corners.append((x, y))
		cropping = False

		cv2.rectangle(image, corners[0], corners[1], (0,0,0), 2)
		cv2.imshow("image", image)

	


if __name__ == "__main__":

	im = ImageGrab.grab_to_file('im.png')
	im = ImageGrab.grab()
	
	image = cv2.imread('im.png')
	clone = image.copy()
	cv2.namedWindow("image")
	cv2.moveWindow("image", 0, 0)
	cv2.setMouseCallback("image", click_and_crop)

	while True:
		cv2.imshow('image', image)
		key = cv2.waitKey(1) & 0xFF

		if key == ord(' ') or key == ord('p'):
			break

	xleft    = min(corners[0][0],corners[1][0])
	xright   = max(corners[0][0],corners[1][0])
	ytop     = min(corners[0][1],corners[1][1])
	ybottom  = max(corners[0][1],corners[1][1])


	im2 = ImageGrab.grab(bbox=(xleft+8, ytop+30, xright+3, ybottom+25))
	cv2.destroyAllWindows()
	im2.save("im.png")
	im2.show()
