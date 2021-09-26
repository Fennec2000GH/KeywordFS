import numpy as np, os 
from pyquery import PyQuery as pq
from pprint import pprint
from termcolor import colored, cprint
from xml.etree import ElementTree as ET

# global variables
line_color = 'green'
text_color = 'magenta'
xml_pq = None
xml_etree = None
xml_path = None

# functions
def load_xml(path: str):
    """
    Load xml file from given path to current global xml file.

    Parameters:
        path (str): Path to XML file.

    Returns:
        None.
    """
    if not os.path.exists(path=path):
        raise Exception(f'{path} is not a valid path.')

    global xml_pq, xml_etree, xml_path
    xml_pq = pq(open(file=path, mode='r').read())
    xml_etree = ET.parse(source=path)
    xml_path = path

    if __debug__:
        cprint(text='-' * 100, color=line_color)
        cprint(text=f'xml_pq: {xml_pq}', color=text_color)
        cprint(text='-' * 100, color=line_color)
        cprint(text=f'xml_etree: {xml_etree}', color=text_color)

def make_file_in_xml(path: str, exist_ok: bool = False):
    """
    Alter XML structure to accomodate new filepath.

    Parameters:
        path (str): Path to file.

    Returns:
        None
    """
    # edge case 
    if not (os.path.exists(path=path) and os.path.isfile(path=path)):
        raise ValueError(f'{path} is not a valid path to a file.')

    path_parts = path.split('/')
    extension = path_parts[-1].split('.')[-1]

    if __debug__:
        cprint(text='-' * 100, color=line_color)
        cprint(text='path_parts:', color=text_color)
        pprint(path_parts)
        cprint(text='-' * 100, color=line_color)
        cprint(text=f'extension: {extension}', color=text_color)

    # creating missing parts in XML to file path
    dir_pq = xml_pq('root')
    dir_etree = xml_etree.getroot()
    for dir in path_parts[1:-1]:
        if __debug__:
            cprint(text='-' * 100, color=line_color)
            pprint(dir_pq)
            pprint(dir_etree)

        if dir not in set(dir_pq.children()):
            dir_pq.append(value=f'<{dir}></{dir}>')
            sub_elem = ET.SubElement(dir_etree, dir)
            dir_etree.append(sub_elem)
            
        dir_pq = dir_pq(dir)
        dir_etree = dir_etree.find(path=dir)

    filename = path_parts[-1]
    if __debug__:
        cprint(text='-' * 100, color=line_color)
        cprint(text=f'filename: {filename}', color=text_color)
        

    if filename not in set(dir_pq.children()):
        dir_pq.after(value=f'<{filename} type="{extension}"></{filename}>')
        sub_elem = ET.SubElement(dir_etree, filename, dict({'type': extension}))
        dir_etree.append(sub_elem)

    with open(file=xml_path, mode='w') as file:
        xml_etree.write(file_or_filename=file, encoding='unicode')

if __name__ == '__main__':
    load_xml(path='linux.xml')
    pprint(list(xml_etree.getroot()))

    # pprint(xml)
    # pprint(xml.contents())
    # pprint(xml.children())
    # pprint(xml('boot').text())

    make_file_in_xml(path='/mnt/d/share/TopicFS/CUAD_v1/master_clauses.csv')