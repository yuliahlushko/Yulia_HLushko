from xml.etree import ElementTree as ET
import xmltodict
import json


class Movie:
    def __init__(self, title, format, year, rating, description, category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category


    @classmethod
    def from_xml(cls, path):
        tree = ET.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies


def xml_file_to_json(path):
    with open(path, 'r') as xml_file:
        xml_dict = xmltodict.parse(xml_file.read())
        result_in_json = json.dumps(xml_dict, indent = 4)
        return result_in_json


def xml_file_to_string(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        xml_as_string = ET.tostring(root, encoding='utf-8').decode('utf-8')
        return xml_as_string
    except ET.ParseError as e:
        return f"Error: {str(e)}"


def xml_string_to_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
        str_as_xml = ET.ElementTree(root)
        return str_as_xml
    except ET.ParseError as e:
        return f"Error: {str(e)}"


xml_json = xml_file_to_json("films.xml")
print(xml_json)

xml_str= xml_file_to_string("films.xml")
print(xml_str)
print(isinstance(xml_str,str))

str_xml = xml_string_to_xml(xml_str)
print(str_xml)
print(isinstance(str_xml,str))