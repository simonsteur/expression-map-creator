"""exprmap module provides functions to create expression map files"""
import xml.etree.ElementTree as ET
from files import readArticulationsFromFile

def createExpressionMaps(files):
    """createExpressionMaps(list()) -> loops thru list of files to create expression maps using the createExpressionMap() function"""
    for f in files:
        f = readArticulationsFromFile(f)
        createExpressionMap(f)

def createExpressionMap(articulations):
    """createExpressionMapXml(dict()) -> dict()
    builds an expression map based on passed in articulations, then writes that expressionmap to file to be imported into cubase"""
    for instrument in articulations['map']:
        try:
            mainEl = ET.Element('InstrumentMap')
            ET.SubElement(mainEl, 'string', attrib={'name':"name", 'value':str(instrument), 'wide':'true'})
            svMemberEl = ET.SubElement(mainEl, 'member', attrib={'name':"slotvisuals"})
            ET.SubElement(svMemberEl, 'int', attrib={'name':"ownership", 'value':'1'})
            svListEl = ET.SubElement(svMemberEl, 'list', attrib={'name':"obj", 'type':"obj"})
            sMemberEl = ET.SubElement(mainEl, 'member', attrib={'name':"slots"})
            ET.SubElement(sMemberEl, 'int', attrib={'name':"ownership", 'value':'1'})
            sListEl = ET.SubElement(sMemberEl, 'list', attrib={'name':"obj", 'type':"obj"})
            elControllerMember = ET.SubElement(mainEl, 'member', attrib={'name':"controller"})
            ET.SubElement(elControllerMember, 'int', attrib={'name':"ownership", 'value':'1'})
            #slotvisuals

            for articulation in articulations['map'][instrument]:
                usvEl = ET.SubElement(svListEl, 'obj', attrib={'class':"USlotVisuals", 'ID':"1"})
                ET.SubElement(usvEl, 'int', attrib={'name':"displaytype", 'value':"1"})
                ET.SubElement(usvEl, 'int', attrib={'name':"articulationtype", 'value':"1"})
                ET.SubElement(usvEl, 'int', attrib={'name':"symbol", 'value':"73"})
                ET.SubElement(usvEl, 'string', attrib={'name':"text", 'value':str(articulation), 'wide':"true"})
                ET.SubElement(usvEl, 'string', attrib={'name':"description", 'value':str(articulation), 'wide':"true"})
                ET.SubElement(usvEl, 'int', attrib={'name':"group", 'value':"0"})

            #slots
            for i, articulation in enumerate(articulations['map'][instrument], start=1):

                #set defaults if no specifics in articulations
                art = articulations['map'][instrument][articulation]
                try:
                    keyswitch = art['ks']
                except KeyError:
                    keyswitch = "0"
                try:
                    channel = (art['chan'] - 1)
                except KeyError:
                    channel = "-1"
                try:
                    velocity = art['vel']
                except KeyError:
                    velocity = "1"
                try:
                    length = art['length']
                except KeyError:
                    length = "1"
                try:
                    minVelocity = art['min-vel']
                except KeyError:
                    minVelocity = "0"
                try:
                    maxVelocity = art['max-vel']
                except KeyError:
                    maxVelocity = "127"
                try:
                    minPitch = art['min-pitch']
                except KeyError:
                    minPitch = "0"
                try:
                    maxPitch = art['max-pitch']
                except KeyError:
                    maxPitch = "127"
                try:
                    transpose = art['transpose']
                except KeyError:
                    transpose = "0"
                try:
                    remote = art['remote']
                except KeyError:
                    remote = (i - 1)

                elPSoundSlot = ET.SubElement(sListEl, 'obj', attrib={'class':"PSoundSlot", 'ID':"1"})
                elThruTrigger = ET.SubElement(elPSoundSlot, 'obj', attrib={'class':"PSlotThruTrigger", 'name':"remote", 'ID':"1"})
                ET.SubElement(elThruTrigger, 'int', attrib={'name':"status", 'value':"144"})
                ET.SubElement(elThruTrigger, 'int', attrib={'name':"data1", 'value':str(remote)})

                elMidiAction = ET.SubElement(elPSoundSlot, 'obj', attrib={'class':"PSlotMidiAction", 'name':"action", 'ID':"1"})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"version", 'value':"600"})
                elMidiActionMember = ET.SubElement(elMidiAction, 'member', attrib={'name':"noteChanger"})
                ET.SubElement(elMidiActionMember, 'int', attrib={'name':"ownership", 'value':"1"})
                elMidiActionList = ET.SubElement(elMidiActionMember, 'list', attrib={'name':"obj", 'type':"obj"})
                elNoteChanger = ET.SubElement(elMidiActionList, 'obj', attrib={'class':"PSlotNoteChanger", 'ID':"1"})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"channel", 'value':str(channel)})
                ET.SubElement(elNoteChanger, 'float', attrib={'name':"velocityFact", 'value':str(velocity)})
                ET.SubElement(elNoteChanger, 'float', attrib={'name':"lengthFact", 'value':str(length)})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"minVelocity", 'value':str(minVelocity)})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"maxVelocity", 'value':str(maxVelocity)})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"transpose", 'value':str(transpose)})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"minPitch", 'value':str(minPitch)})
                ET.SubElement(elNoteChanger, 'int', attrib={'name':"maxPitch", 'value':str(maxPitch)})

                elMidiMessagesMember = ET.SubElement(elMidiAction, 'member', attrib={'name':"midiMessages"})
                ET.SubElement(elMidiMessagesMember, 'int', attrib={'name':"ownership", 'value':"1"})
                elMidiMessageList = ET.SubElement(elMidiMessagesMember, 'list', attrib={'name':"obj", 'type':"obj"})
                elMidiMessages = ET.SubElement(elMidiMessageList, 'obj', attrib={'class':"POutputEvent", 'ID':"1"})
                ET.SubElement(elMidiMessages, 'int', attrib={'name':"status", 'value':"144"})
                ET.SubElement(elMidiMessages, 'int', attrib={'name':"data1", 'value':str(keyswitch)})
                ET.SubElement(elMidiMessages, 'int', attrib={'name':"data2", 'value':"127"})

                ET.SubElement(elMidiAction, 'int', attrib={'name':"channel", 'value':str(channel)})
                ET.SubElement(elMidiAction, 'float', attrib={'name':"velocityFact", 'value':str(velocity)})
                ET.SubElement(elMidiAction, 'float', attrib={'name':"lengthFact", 'value':str(length)})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"minVelocity", 'value':str(minVelocity)})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"maxVelocity", 'value':str(maxVelocity)})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"transpose", 'value':str(transpose)})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"maxPitch", 'value':str(maxPitch)})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"controller1num", 'value':"32"})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"controller1value", 'value':"1"})
                ET.SubElement(elMidiAction, 'int', attrib={'name':"key", 'value':"1"})

                elsvMember = ET.SubElement(elPSoundSlot, 'member', attrib={'name':"sv"})
                ET.SubElement(elsvMember, 'int', attrib={'name':"ownership", 'value':"2"})
                elsvList = ET.SubElement(elsvMember, 'list', attrib={'name':"obj", 'type':"obj"})
                elsv = ET.SubElement(elsvList, 'obj', attrib={'class':"USlotVisuals", 'ID':"1"})

                ET.SubElement(elsv, 'int', attrib={'name':"displaytype", 'value':"1"})
                ET.SubElement(elsv, 'int', attrib={'name':"articulationtype", 'value':"1"})
                ET.SubElement(elsv, 'int', attrib={'name':"symbol", 'value':"73"})
                ET.SubElement(elsv, 'string', attrib={'name':"text", 'value':str(articulation), 'wide':"true"})
                ET.SubElement(elsv, 'string', attrib={'name':"description", 'value':str(articulation), 'wide':"true"})
                ET.SubElement(elsv, 'int', attrib={'name':"group", 'value':"0"})

                elMemberName = ET.SubElement(elPSoundSlot, 'member', attrib={'name':"name"})
                ET.SubElement(elMemberName, 'string', attrib={'name':"s", 'value':str(articulation), 'wide':"true"})
                ET.SubElement(elPSoundSlot, 'int', attrib={'name':"color", 'value':str(i)})

            data = ET.tostring(mainEl, encoding='unicode', method='xml')
            fileName = str(instrument) + ".expressionmap"
            expmap = open(fileName, "w")
            expmap.write(data)

        except Exception as e:
            print("something went wrong.")
            print(e)
