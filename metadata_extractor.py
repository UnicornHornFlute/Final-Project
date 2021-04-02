from __future__ import print_function
from argparse import ArgumentParser
from datetime import datetime as dt
from xml.etree import ElementTree as etree
import zipfile
parser = argparse.ArgumentParser('Office Document Metadata’)
parser.add_argument("Office_File", help="Path to office file to read")
args = parser.parse_args()

zipfile.is_zipfile(args.Office_File)
zfile = zipfile.ZipFile(args.Office_File)
core_xml = etree.fromstring(zfile.read('docProps/core.xml'))
app_xml = etree.fromstring(zfile.read('docProps/app.xml'))

core_mapping = {
 'title': 'Title',
 'subject': 'Subject',
 'creator': 'Author(s)',
 'keywords': 'Keywords',
 'description': 'Description',
 'lastModifiedBy': 'Last Modified By',
 'modified': 'Modified Date',
 'created': 'Created Date',
 'category': 'Category',
 'contentStatus': 'Status',
 'revision': 'Revision'
}

for element in core_xml.getchildren():
 for key, title in core_mapping.items():
	if key in element.tag:
		if 'date' in title.lower():
			text = dt.strptime(element.text, "%Y-%m-%dT%H:%M:%SZ")
		else:
			text = element.text
		print("{}: {}".format(title, text))
 
 app_mapping = {
	'TotalTime': 'Edit Time (minutes)',
	'Pages': 'Page Count',
	'Words': 'Word Count',
	'Characters': 'Character Count',
	'Lines': 'Line Count',
	'Paragraphs': 'Paragraph Count',
	'Company': 'Company',
	'HyperlinkBase': 'Hyperlink Base',
	'Slides': 'Slide count',
	'Notes': 'Note Count',
	'HiddenSlides': 'Hidden Slide Count',
}
for element in app_xml.getchildren():
 for key, title in app_mapping.items():
	if key in element.tag:
		if 'date' in title.lower():
			text = dt.strptime(element.text, "%Y-%m-%dT%H:%M:%SZ")
		else:
			text = element.text
		print("{}: {}".format(title, text)) 