import xml.etree.ElementTree as ET
from config import filename

tree = ET.parse(filename)
root = tree.getroot()

print(root[0][0].text, root[0][1].text)