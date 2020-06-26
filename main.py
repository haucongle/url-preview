from linkpreview import link_preview

url = "https://docbao.vn/video/video-lao-xe-qua-cong-sat-roi-dam-vao-nha-dan-nu-tai-xe-khien-nguoi-than-gao-thet-tintuc688635"
preview = link_preview(url)
print("title:", preview.title)
print("description:", preview.description)
print("image:", preview.image)
print("force_title:", preview.force_title)
print("absolute_image:", preview.absolute_image)

from link_preview import link_preview
dict_elem = link_preview.generate_dict(url)
print(dict_elem)
# Access values
# title = dict_elem['title']
# description = dict_elem['description']
# image = dict_elem['image']
# website = dict_elem['website']