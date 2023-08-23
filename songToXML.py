from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import re
import os

def songToXML(text):
    # Splitting the text into verses
    verses = re.split(r'\d+\.\s+', text)[1:]

    # Create XML structure
    root = Element("song", xmlns="http://openlyrics.info/namespace/2009/song", version="0.8", createdIn="OpenLP 2.1.6", modifiedIn="OpenLP 2.1.6", modifiedDate="2017-03-01T20:47:44")

    properties = SubElement(root, "properties")
    titles = SubElement(properties, "titles")
    title = SubElement(titles, "title")
    title.text = "001 Ó, prekrásna Hviezda ranná"

    authors = SubElement(properties, "authors")
    author1 = SubElement(authors, "author")
    author1.text = "Advent"
    author2 = SubElement(authors, "author")
    author2.text = "JKS"

    lyrics = SubElement(root, "lyrics")

    # Adding verses to XML
    for i, verse in enumerate(verses, start=1):
        verse_element = SubElement(lyrics, "verse", name=f"v{i}")
        lines_element = SubElement(verse_element, "lines")
        lines = re.split(r'\s+-\s+', verse.strip())
        lines_text = "<br/>".join(lines)
        lines_element.text = f"{i}.<br/>{lines_text}"

    # Convert the XML structure to a string
    xml_string = tostring(root, encoding="UTF-8").decode()

    # Pretty-print the XML using minidom
    xml_dom = minidom.parseString(xml_string)
    pretty_xml_string = xml_dom.toprettyxml(indent="  ", encoding="UTF-8").decode().replace("&lt;","<").replace("&gt;",">")
    # Save the XML to a file
    xml_filename = title.text
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = os.path.join(script_dir, xml_filename)

    with open(xml_path, "w", encoding="utf-8") as xml_file:  # Use binary write mode for UTF-8 encoded file
        xml_file.write(pretty_xml_string)

    print(f"XML file saved as '{xml_filename}' in the script's directory.")

if __name__ == "__main__":
    # Original text
    text = """
    1.
    1. Ó, prekrásna Hviezda ranná, - ktorá si nám z neba daná, - vrúcne, Panna, bud' vítaná! -
    2. Božieho tys' výkvet diela, - k tebe poslal Gabriela - sám Boh, svojho archanjela. -
    3. Počneš Syna premilého, - Bohom Otcom nám daného, - Spasiteľa čakaného. -
    4. Ako dcéra Stvoriteľa - Matkou budeš Spasiteľa - a Nevestou Tešiteľa. -
    5. Trojici bud' svätej sláva, - Márii česť nech sa vzdáva, - že sa Božou Matkou stáva.
    """
    songToXML(text)