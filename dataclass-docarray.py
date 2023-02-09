from glob import glob

from docarray import Document, DocumentArray, dataclass
from docarray.typing import Image


@dataclass
class ImageDoc:
    image: Image


docs = DocumentArray()

for filename in glob('./ikea/images/**/*.jpg'):
    image_doc = ImageDoc(image=filename)
    doc = Document(image_doc)
    docs.append(doc)

docs.push(name='IvonaTau_ikea')
