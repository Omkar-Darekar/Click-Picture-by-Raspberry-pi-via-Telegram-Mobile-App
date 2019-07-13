import pygame.camera


def captured():
		pygame.camera.init()
		cam=pygame.camera.Camera("/dev/video0",(640,480)) # note --> if primary camera connected then make changes to  video0 or if secondary camera connected then video1
		cam.start()
		img=cam.get_image()
		pygame.image.save(img,"./img/img.jpg")
		cam.stop()
captured()
