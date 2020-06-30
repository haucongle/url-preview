from chalice import Chalice
import validators
import re
import gzip
import urllib.request
import urllib.parse
import ImageFile
from bs4 import BeautifulSoup
from urllib.request import (
    Request,
    urlopen,
)

USER_AGENT = "Workspace Preview Bot"
IMAGE_LINK_MAX_WIDTH = 768
url = "https://docbao.vn/video/video-lao-xe-qua-cong-sat-roi-dam-vao-nha-dan-nu-tai-xe-khien-nguoi-than-gao-thet-tintuc688635"
# url='https://www.now.vn/ho-chi-minh/2-chi-em-com-ga-nha-trang'
parsed_uri = urllib.parse.urlsplit(url)
q = Request(url)
q.add_header('User-Agent', USER_AGENT)
html = urlopen(q, timeout=10)

encoding = html.getheader("Content-Encoding")

content = html.read()

if encoding == "gzip":
    content = gzip.decompress(content)

soup = BeautifulSoup(
    content.decode("utf-8", "ignore"),
    "html.parser"
)

title = str(soup.title.string)

# titles = re.compile("[-–|:•]+").split(title)

# title = titles[0].strip()

# Get the desc from whatever we can find
desc_elems = [soup.findAll(
    attrs={attr: re.compile(r"Desc", re.I)}
) for attr in ["name", "property"]]

for i in range(1):
    if len(desc_elems[i]) > 0:
        desc = desc_elems[i][0]["content"]
        break
    else:
        desc = ""

if len(desc.split()) > 30:
    desc = " ".join(desc.split()[0:29]).strip()

    desc = desc.strip("…")
    desc = desc.strip(".")
    desc += "..."

icon_link = soup.find("link", rel=re.compile(r"shortcut icon"))

if icon_link is None:
    icon_link = soup.find("link", rel=re.compile(r"icon"))

if icon_link is not None:
    # Check if icon link is global or relative
    icon_href = icon_link["href"]

    if icon_href.find("http") != -1:
        icon = icon_href
    elif icon_href.find("//") != -1:
        icon = 'http:' + icon_href
    else:
        icon = parsed_uri.hostname + icon_href

# Fetch Open Graph Image
image = soup.find("meta", property="og:image")

if image is None:
    # Use favicon if no image is specified
    image = icon

if image is not None:
    # Check if image link is global or relative
    image_link = image["content"]

    if image_link.find("http") != -1:
        image = image_link
    elif image_link.find("//") != -1:
        image = 'http:' + image_link
    else:
        image = parsed_uri.hostname + image_link

print('title:', title)  
print('description:', desc)  
print('image:', image)  
print('icon:', icon)   
print("=========================")

# from linkpreview import link_preview
# preview = link_preview(url)
# print("title:", preview.title)
# print("description:", preview.description)
# print("image:", preview.image)
# print("=========================")

# from link_preview import link_preview
# dict_elem = link_preview.generate_dict(url)
# print("title:", dict_elem['title'])
# print("description:", dict_elem['description'])
# print("image:", dict_elem['image'])   
# print("=========================")
