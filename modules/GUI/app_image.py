import customtkinter as ctk
import PIL.Image
class ImageLabel(ctk.CTkLabel):
    
    def __init__(self, ch_master: ctk.CTkFrame = None, path_image: str = None, **kwargs):
        self.WIDTH = ch_master._current_width
        self.HEIGHT = ch_master._current_height
        
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
                light_image= PIL.Image.open(fp = image),
                size= (image.width, image.height) if image.width < self.WIDTH and image.height < self.HEIGHT else (self.WIDTH, self.HEIGHT)
                # if image.width < self.WIDTH and image.height < self.HEIGHT:
                #     return (image.width, image.height)
                # else:
                #     return (self.WIDTH, self.HEIGHT) 
            )
        except Exception as error:
            print(f"Error while loading image: {str(error)}")
            return None

def show_image(parent: ctk.CTkFrame, path_image: str | None):
    image_label = ImageLabel(ch_master= parent, path_image= path_image)
    image_label.pack()


# image = ImageLabel(path_image= "/Users/worlditacademy/Downloads/worldIT_LOGO.ico").load_image()