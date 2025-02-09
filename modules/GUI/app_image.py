import customtkinter as ctk
import PIL.Image

class ImageLabel(ctk.CTkLabel):
    
    def __init__(self, ch_master: ctk.CTkFrame = None, path_image: str = None, **kwargs):
        self.WIDTH = int(ch_master._current_width * 0.9)
        self.HEIGHT = int(ch_master._current_height * 0.9)
        
        self.PATH_IMAGE = path_image
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
        
    def load_image(self):
        try:
            image = PIL.Image.open(fp = self.PATH_IMAGE)
            return ctk.CTkImage(
                light_image= image,
                size = self.image_size(image = image)
                # size= (image.width, image.height) if image.width < self.WIDTH and image.height < self.HEIGHT else (self.WIDTH, self.HEIGHT)
                # if image.width < self.WIDTH and image.height < self.HEIGHT:
                #     return (image.width, image.height)
                # else:
                #     return (self.WIDTH, self.HEIGHT) 
            )
        except Exception as error:
            print(f"Error while loading image: {str(error)}")
            return None
    def image_size(self, image: PIL.Image):
        if image.width == image.height:
            if image.width >= self.WIDTH and image.height >= self.HEIGHT:
                return (self.HEIGHT, self.HEIGHT)
            else:
                return(image.width, image.height)
        elif image.width >= self.WIDTH and image.height >= self.HEIGHT:
            return (self.WIDTH, self.HEIGHT)
        else:
            return (image.width, image.height)
        


