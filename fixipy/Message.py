import re

'''
    fixipy Message provides methods for parsing, composing, modifying and analyzing FIX messages
'''

class Message():
    def __init__(self):
        self.raw_message = ''
        self.message = []
        self.valid_checksum = None
        self.checksum_calculation = True
        
    
    def __checksum__(self, raw_message):
        try:
            raw_msg = re.sub(r'10=[0-9]{3}$', '', raw_message)
            chksum = 0
            for byte in bytearray(raw_msg, 'utf-8'):
                chksum += byte
            checksum = chksum % 256
            return '%03d' % checksum
        except:
            raise
        
    def compose(self, calculate_checksum = True):
        try:
            raw_message = ''
            for item in self.message:
                if calculate_checksum == True and item[0] == 10:
                    pass
                else:
                    raw_item = '{}={}'.format(item[0],item[1])
                    raw_message += raw_item
            if calculate_checksum == True:
                checksum = self.__checksum__(raw_message)
                raw_item = '10={}'.format(checksum)
                raw_message += raw_item
            self.raw_message = raw_message
            return self.raw_message
        except:
            print('[Error]', 'while composing raw message')
            raise
        pass
    def checksum(self):
        try:
            ''' if raw_message is empty we still have checksum in raw_message, but want to return None '''
            if self.raw_message == '10=000':
                return None
            return self.__checksum__(self.raw_message)
        except:
            raise
    def parse(self, message, keep_checksum = True):
        try:
            self.message = []
            if type(message) is str:
                self.raw_message = message
                for raw_item in self.raw_message.split(''):
                    if raw_item != '':
                        item = raw_item.split('=')
                        tag, value = int(item[0]), str(item[1])
                        if keep_checksum == False and tag == 10:
                            pass
                        else:
                            if tag == 10:
                                self.valid_checksum = self.__checksum__(message) == value
                                print (self.__checksum__(message), value)
                            self.message += [[tag, value]]
                if keep_checksum == False:
                    self.compose()
                    self.message += [[10, self.checksum()]]
                return self.message
            else:
                raise ValueError('expected str or list')
        except:
            print('[Error]', 'while parsing message')
            raise
    
    def add_item(self, item, index=None):
        pass
    def remove_item(self, index):
        try:
            del self.message[index]
        except:
            raise
    def exchange_item(self, index_a, index_b):
        try:
            a, b = self.message[index_a], self.message[index_b]
            self.message[index_a], self.message[index_b] = b, a
        except:
            raise
    def search(self):
        pass
    def get_item(self, tag):
        pass
    def get_item_by_index(self, index):
        pass
