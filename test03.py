# 对xml文件的增加object节点，如下：

body = """
    <object>
    <name>{0}</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>{1}</xmin>
        <ymin>{2}</ymin>
        <xmax>{3}</xmax>
        <ymax>{4}</ymax>
    </bndbox>
</object>
"""

import xml.etree.ElementTree as et

class_name,x1,y1,x2,y2 = "name","x1","y1","x2","y2"

def creat_body(pathXml,id = 6): # 参数：xml文件名，插入位置（索引）

    # 打开解析对象，拿出根节点root
    tree = et.parse(pathXml)
    root = tree.getroot()

    # 创建父节点object
    object = et.Element("object")
    root.insert(id, object)

    # 创建object子节点name、pose、truncated、difficult、bndbox
    name = et.SubElement(object,"name")
    pose = et.SubElement(object,"pose")
    truncated = et.SubElement(object,"truncated")
    difficult = et.SubElement(object,"difficult")
    bndbox = et.SubElement(object, "bndbox")
    # 赋值
    object.text = "\n    "
    name.text = class_name
    pose.text = "Unspecified"
    truncated.text = "0"
    difficult.text = "0"
    bndbox.text = "\n        "
    # 调整格式（对齐、缩进）
    object.tail = "\n    "
    name.tail = "\n    "
    pose.tail = "\n    "
    truncated.tail = "\n    "
    difficult.tail = "\n    "
    bndbox.tail = "\n"

    # 创建bndbox子节点xmin、ymin、ymin、ymin
    xmin = et.SubElement(bndbox,"xmin")
    ymin = et.SubElement(bndbox,"ymin")
    xmax = et.SubElement(bndbox,"xmax")
    ymax = et.SubElement(bndbox,"ymax")
    # 赋值
    xmin.text = x1
    ymin.text = y1
    xmax.text = x2
    ymax.text = y2
    # 调整格式（对齐、缩进）
    xmin.tail = "\n        "
    ymin.tail = "\n        "
    xmax.tail = "\n        "
    ymax.tail = "\n    "

    return tree.write('file.xml')

creat_body("14.xml")
