from xml.etree import ElementTree as ET
from string import punctuation
import glob

class RmhExtractor:
    def __init__(self, folder=None):
        self.folder = folder
        self.xml_files = glob.glob(f'/path/to/risamalheild/CC_BY/{folder}/**/*.xml',
                                   recursive=True)
    def extract(self, forms=False, lemmas=False, pos=False):
        i = 1
        counter = 0
        if forms:
            counter += 1
        if lemmas:
            counter += 1
        if pos:
            counter += 1
        with open(f'{self.folder}.txt', 'w', encoding='utf-8') as out:
            for file in self.xml_files:
                with open(file, 'r', encoding='utf-8') as content:
                    tree = ET.parse(content)
                    for element in tree.iter():
                        try:
                            if element.attrib.get('lemma') is not None:
                                if forms:
                                    out.write(element.text + '\t')
                                if lemmas:
                                    out.write(element.attrib.get('lemma') + '\t')
                                if pos:
                                    out.write(element.attrib.get('type') + '\t')
                            elif element.text in punctuation:
                                for _ in range(counter):
                                    out.write(element.text + '\t')
                        except TypeError:
                            pass
                        out.write('\n')
                print(f'Files processed: {i} of {len(self.xml_files)}')
                i += 1

    def extract_sentences(self, category):
        i = 0
        with open(f'{self.folder}_sentences.txt', 'w', encoding='utf-8') as out:
            for file in self.xml_files:
                with open(file, 'r', encoding='utf-8') as content:
                    tree = ET.parse(content)
                    for element in tree.iter():
                        try:
                            if element.attrib.get('lemma') is not None:
                                if category == 'word_form':
                                    out.write(element.text + ' ')
                                elif category == 'lemmas':
                                    out.write(element.attrib.get('lemma') + ' ')
                                elif category == 'pos':
                                    out.write(element.attrib.get('type') + ' ')
                            elif element.text in punctuation:
                                if element.text == '.':
                                    out.write(element.text + '\n')
                                else:
                                    out.write(element.text + ' ')
                        except TypeError:
                            pass
                print(f'Files processed: {i} of {len(self.xml_files)}')
                i += 1
if __name__ == '__main__':
    pass
    #RMH = RmhExtractor(folder='ruv')
    #RMH.extract(forms=True, lemmas=True, pos=True)
    #RMH.extract_sentences(category='word_form')
