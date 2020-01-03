"""exprmap module provides functions to create expression map files"""
import xml.etree.ElementTree as ET


def createExpressionMap(articulations):
    """createExpressionMapXml(dict()) -> dict()
    builds an expression map dict based on passed in articulations"""
    # Create your dictionary class 
    mainEl = ET.Element('InstrumentMap')
    for instrument in articulations['articulations']:
        ET.SubElement(mainEl, 'string', attrib={'name': str(instrument), 'wide': 'true'})
        svMemberEl = ET.SubElement(mainEl, 'member', attrib={'name': "slotvisuals"})
        ET.SubElement(svMemberEl, 'int', attrib={'name': "ownership", 'value': '1'})
        svListEl = ET.SubElement(svMemberEl, 'list', attrib={'name': "obj", 'type': "obj"})
        sMemberEl = ET.SubElement(mainEl, 'member', attrib={'name': "slots"})
        ET.SubElement(sMemberEl, 'int', attrib={'name': "ownership", 'value': '1'})
        sListEl = ET.SubElement(sMemberEl, 'list', attrib={'name': "obj", 'type': "obj"})
        elControllerMember = ET.SubElement(mainEl, 'member', attrib={'name': "controller"})

        #slotvisuals
        for articulation in articulations['articulations'][instrument]:
            usvEl = ET.SubElement(svListEl, 'obj', attrib={'class': "USlotVisuals", 'ID':"106652629072304"})
            ET.SubElement(usvEl, 'int name="displaytype" value="1"')
            ET.SubElement(usvEl, 'int name="articulationtype" value="1"')
            ET.SubElement(usvEl, 'int name="symbol" value="178"')
            ET.SubElement(usvEl, "string name=""text"" value="+ str(articulation) + " wide=""true""")
            ET.SubElement(usvEl, "string name=""description"" value=" + str(articulation) + " wide=""true""")
            ET.SubElement(usvEl, 'int name="group" value="0"')

        #slots
        for articulation in articulations['articulations'][instrument]:
            elPSoundSlot = ET.SubElement(sMemberEl, 'obj', attrib={'class': "PSoundSlot", 'ID':"106652631041584"}) 
            elThruTrigger = ET.SubElement(elPSoundSlot, 'int', attrib={'class': "PSlotThruTrigger", 'name':"remote", 'id':"106652634220992"})
            ET.SubElement(elThruTrigger, 'int', attrib={'name': "status", 'value':"144"})
            ET.SubElement(elThruTrigger, 'int', attrib={'name': "status", 'value':"-1"})
            
            elMidiAction = ET.SubElement(elPSoundSlot, 'obj', attrib={'class':"PSlotMidiAction", 'name':"action", 'ID':"106652635014048"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"version", 'value':"600"})
            elMidiActionMember = ET.SubElement(elMidiAction, 'member', attrib={'name':"noteChanger"})
            ET.SubElement(elMidiActionMember, 'int', attrib={'name':"ownership", 'value':"1"})
            elMidiActionList = ET.SubElement(elMidiActionMember, 'list', attrib={'name': "obj", 'type': "obj"})
            elNoteChanger = ET.SubElement(elMidiActionList, 'obj', attrib={'class': "PSlotNoteChanger", 'ID':"106652835902816"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"channel", 'value':"-1"})
            ET.SubElement(elNoteChanger, 'float', attrib={'name':"velocityFact", 'value':"1"})
            ET.SubElement(elNoteChanger, 'float', attrib={'name':"lengthFact", 'value':"1"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"minVelocity", 'value':"0"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"maxVelocity", 'value':"127"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"transpose", 'value':"0"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"minPitch", 'value':"0"})
            ET.SubElement(elNoteChanger, 'int', attrib={'name':"maxPitch", 'value':"127"})

            elMidiMessagesMember = ET.SubElement(elMidiAction, 'member', attrib={'name':"midiMessages"})
            ET.SubElement(elMidiMessagesMember, 'int', attrib={'name':"ownership", 'value':"1"})
            elMidiMessageList = ET.SubElement(elMidiMessagesMember, 'list', attrib={'name': "obj", 'type': "obj"})
            elMidiMessages = ET.SubElement(elMidiMessageList, 'obj', attrib={'class': "POutputEvent", 'ID':"106652634228432"})
            ET.SubElement(elMidiMessages, 'int', attrib={'name':"status", 'value':"176"})
            ET.SubElement(elMidiMessages, 'int', attrib={'name':"data1", 'value':"32"})
            ET.SubElement(elMidiMessages, 'int', attrib={'name':"data2", 'value':"1"})
            
            ET.SubElement(elMidiAction, 'int', attrib={'name':"channel", 'value':"-1"})
            ET.SubElement(elMidiAction, 'float', attrib={'name':"velocityFact", 'value':"1"})
            ET.SubElement(elMidiAction, 'float', attrib={'name':"lengthFact", 'value':"1"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"minVelocity", 'value':"0"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"maxVelocity", 'value':"127"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"transpose", 'value':"0"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"maxPitch", 'value':"127"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"controller1num", 'value':"32"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"controller1value", 'value':"1"})
            ET.SubElement(elMidiAction, 'int', attrib={'name':"key", 'value':"1"})


        #  <obj class="PSoundSlot" ID="106652631041584">
        #     <member name="sv">
        #        <int name="ownership" value="2"/>
        #        <list name="obj" type="obj">
        #           <obj class="USlotVisuals" ID="106652631048784">
        #              <int name="displaytype" value="1"/>
        #              <int name="articulationtype" value="1"/>
        #              <int name="symbol" value="178"/>
        #              <string name="text" value="arco" wide="true"/>
        #              <string name="description" value="Arco" wide="true"/>
        #              <int name="group" value="0"/>
        #           </obj>
        #        </list>
        #     </member>
        #     <member name="name">
        #        <string name="s" value="Arco" wide="true"/>
        #     </member>
        #     <int name="color" value="1"/>
        #  </obj>


    ET.dump(mainEl)
    #print(instrmap)
    #xml = dicttoxml.dicttoxml(instrmap, custom_root='InstrumentMap', attr_type=False)
    #print(xml)
    return articulations
