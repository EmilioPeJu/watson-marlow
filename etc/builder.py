from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

class Pump323Du(AutoSubstitution, AutoProtocol):
    '''Controls a Watson Marlow 323Du Pump'''

    ## Parse this template file for macros
    TemplateFile = '323Du.template'

    ## This is the streamDevice protocol file to use
    ProtocolFiles = ['323Du.proto']

