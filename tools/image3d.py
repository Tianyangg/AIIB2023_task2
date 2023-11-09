import SimpleITK as sitk

class Image3d:
    def __init__(self, itk_image):
        self.image = itk_image
        self._construct_image3d()
    
    def _construct_image3d(self):
        self._size = self.image.GetSize()
        self._dimension = self.image.GetDimension()
        self._spacing = self.image.GetSpacing()
        self._data = sitk.GetArrayFromImage(self.image)
    
    def to_numpy(self):
        return self._data
    
    def size(self):
        return self._size
    
    def spacing(self):
        return self._spacing
    
    # TODO calculate world coordinate and voxel coordinate


def read_image(image_path):
    # TODO assert medical suffix
    reader = sitk.ImageFileReader()
    reader.SetImageIO("NiftiImageIO")
    reader.SetFileName(image_path)
    image = reader.Execute()

    image3d = Image3d(image)
    return image3d


if __name__ == "__main__":
    image_path = "/home/tianyang/Code/SynthSR/data/images/brain1.nii.gz"
    im = read_image(image_path)
    from IPython import embed
    embed()

