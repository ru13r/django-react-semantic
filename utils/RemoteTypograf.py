# -*- encoding: windows-1251 -*-
import sys

PY3 = sys.version.startswith('3.')

"""
    remotetypograf.py
    python-implementation of ArtLebedevStudio.RemoteTypograf class (web-service client)
    
    Copyright (c) Art. Lebedev Studio | http://www.artlebedev.ru/

    Typograf homepage: http://typograf.artlebedev.ru/
    Web-service address: http://typograf.artlebedev.ru/webservices/typograf.asmx
    WSDL-description: http://typograf.artlebedev.ru/webservices/typograf.asmx?WSDL
    
    Default charset: UTF-8

    Python version 
    Author: Sergey Lavrinenko (s.lavrinenko@gmail.com)
    Version: 1.0 (2007-05-18) based on script by Andrew Shitov (ash@design.ru)

    Example:
        from RemoteTypograf import RemoteTypograf
            rt = RemoteTypograf()
        # rt = RemoteTypograf('windows-1251')
        print rt.processText ('"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"');
"""

import socket


class RemoteTypograf:
    _entityType = 4
    _useBr = 0
    _useP = 0
    _maxNobr = 3
    _encoding = 'UTF-8'

    def __init__(self, encoding='UTF-8'):
        self._encoding = encoding

    def htmlEntities(self):
        self._entityType = 1

    def xmlEntities(self):
        self._entityType = 2

    def mixedEntities(self):
        self._entityType = 4

    def noEntities(self):
        self._entityType = 3

    def br(self, value):
        if value:
            self._useBr = 1
        else:
            self._useBr = 0

    def p(self, value):
        if value:
            self._useP = 1
        else:
            self._useP = 0

    def nobr(self, value):
        if value:
            self._maxNobr = value
        else:
            self._maxNobr = 0

    def processText(self, text):

        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')

        SOAPBody = '<?xml version="1.0" encoding="%s"?>\n' % self._encoding
        SOAPBody += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
        SOAPBody += '<soap:Body>\n'
        SOAPBody += ' <ProcessText xmlns="http://typograf.artlebedev.ru/webservices/">\n'
        SOAPBody += '  <text>%s</text>\n' % text
        SOAPBody += '     <entityType>%s</entityType>\n' % self._entityType
        SOAPBody += '     <useBr>%s</useBr>\n' % self._useBr
        SOAPBody += '     <useP>%s</useP>\n' % self._useP
        SOAPBody += '     <maxNobr>%s</maxNobr>\n' % self._maxNobr
        SOAPBody += '	</ProcessText>\n'
        SOAPBody += ' </soap:Body>\n'
        SOAPBody += '</soap:Envelope>\n'

        host = 'typograf.artlebedev.ru'
        SOAPRequest = 'POST /webservices/typograf.asmx HTTP/1.1\n'
        SOAPRequest += 'Host: typograf.artlebedev.ru\n'
        SOAPRequest += 'Content-Type: text/xml\n'
        SOAPRequest += 'Content-Length: %d\n' % len(SOAPBody.encode('utf-8'))
        SOAPRequest += 'SOAPAction: "http://typograf.artlebedev.ru/webservices/ProcessText"\n\n'

        SOAPRequest += SOAPBody

        remoteTypograf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remoteTypograf.connect((host, 80))
        remoteTypograf.sendall(SOAPRequest.encode())

        typografResponse = ''
        while 1:
            buf = remoteTypograf.recv(8192)
            if len(buf) == 0: break
            typografResponse += buf.decode()

        remoteTypograf.close()

        startsAt = typografResponse.find('<ProcessTextResult>') + 19
        endsAt = typografResponse.find('</ProcessTextResult>')
        typografResponse = typografResponse[startsAt:endsAt]

        typografResponse = typografResponse.replace('&amp;', '&')
        typografResponse = typografResponse.replace('&lt;', '<')
        typografResponse = typografResponse.replace('&gt;', '>')

        return typografResponse


if __name__ == '__main__':
    data = """
Карта занимает промежуточное положение между Пятеркой (нищета) и Десяткой (полнота). На карте изображены отношения "давать и получать", "власть и подчинение". В раскладе карта означает, что человеку необходимо задуматься над тем, что для него значит "иметь" в материальном и нематериальном плане. Мир существует в равновесии. Представьте себе успешного бизнесмена, который стал банкротом, учителя, который учится у учеников...

Следует сохранять равновесие между тем, что мы отдаем и что получаем (на карте также присутствуют весы - символ справедливости и равновесия).

Следует быть благодарным за то, что мы имеем и делиться с другими. Чем больше мы отдаем, тем больше иногда получаем.

Следует также соблюдать меру и правильно использовать нашу энергию и ресурсы.

Если речь об отношениях - необходимо исследовать, кто что дает и получает. Есть ли равновесие?    
    """
    rt = RemoteTypograf()  # UTF-8
    rt.htmlEntities()
    rt.p(0)
    rt.br(1)
    rt.nobr(1)
    data = rt.processText(data)
    data = data.replace('<br />\n<br />', '\n')
    print(data)