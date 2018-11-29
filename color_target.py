import Image
import glob
import os

class color_target:

	def __init__(self):

		self.threshold = 200
		self.d_rgb = (0, 200, 200) # delta rgb

		self.in_dir = "./uncolored/*.JPG"
		self.out_dir = "./output_img/"

		if not os.path.exists(self.out_dir):
			os.makedirs(self.out_dir)

		self.import_images()

	def import_images(self):
		i = 0
		for filename in glob.glob(self.in_dir):
			i = i + 1
			img = Image.open(filename)
			print "image imported",filename
			img = self.change_color(img)
			print "color changed",filename
			self.save_img(img, i)
			print "image saved as ", self.out_dir + str(i) + '.JPG'


	def change_color(self, img):
		width, height = img.size
		for x in range(width):
			for y in range(height):
				rgb = img.getpixel((x,y))
				inrange = True
				for c in rgb:
					if c < self.threshold:
						inrange = False
				if inrange == True:
					r, g, b = rgb
					dr, dg, db = self.d_rgb # deltaRGB
					r = min(255, max(0, r-dr)) # bounded ( R - deltaR )
					g = min(255, max(0, g-dg)) # bounded ( G - deltaG )
					b = min(255, max(0, b-db)) # bounded ( B - deltaB )
					img.putpixel((x,y), (r,g,b))
		return img

	def save_img(self, img, i):
		img.save(self.out_dir + str(i) + '.JPG')


if __name__ == "__main__":
    color_target()
