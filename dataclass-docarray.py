import pickle
from glob import glob

from docarray import Document, DocumentArray, dataclass
from docarray.typing import Image, Text


def get_id(filename):
    bare_name = filename.split('/')[-1]
    id = bare_name[:-4]  # cut off the file extension

    return id


filename = 'ikea/text_data/products_dict.p'
with open(filename, mode='rb') as file:
    text_data = pickle.load(file)


@dataclass
class IkeaDoc:
    image: Image
    item_type: Text
    id: Text
    name: Text
    color: Text


docs = DocumentArray()

for filename in glob('./ikea/images/**/*.jpg'):
    id = get_id(filename)
    try:
        item_type = text_data[id]['type']
        name = text_data[id]['name']
        color = text_data[id]['color']
    except:
        item_type = 'misc'
        name = 'unknown'
        color = 'unknown'

    ikea_doc = IkeaDoc(
        image=filename,
        id=get_id(filename),
        item_type=item_type,
        color=color,
        name=name,
    )
    doc = Document(ikea_doc)
    docs.append(doc)

print(docs[0].chunks.summary())

for doc in docs[0].chunks:
    print(doc.text)

docs.push(name='IvonaTau_ikea')
