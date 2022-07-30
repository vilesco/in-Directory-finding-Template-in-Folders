import xml.etree.ElementTree as ET
class XmlExporter:
    def exportToXml(self, rootFolder,templateFolder,fileInfos):
        print('Found files ', len(fileInfos))
        xmlRoot = ET.Element('Root')
        xmlRoot.set('root', rootFolder)
        xmlRoot.set('template', templateFolder)
        foundFilesXmlELement = ET.SubElement(xmlRoot, 'FoundFiles')
        foundFilesXmlELement.set('count', str(len(fileInfos)))

        for fileInfo in fileInfos:
            fileXml = ET.SubElement(foundFilesXmlELement,'File')
            fileXml.set('nr', fileInfo.number)
            nameElement = ET.SubElement(fileXml,'Name')
            pathElement = ET.SubElement(fileXml,'Path')
            lastModifyDateElement = ET.SubElement(fileXml,'LastModifyDate')
            nameElement.text = fileInfo.name
            pathElement.text = fileInfo.path
            lastModifyDateElement.text = fileInfo.lastUpdate
    
    
        xml = ET.tostring(xmlRoot)
        with open("fileReport.xml", "wb") as f:
            f.write(xml)
