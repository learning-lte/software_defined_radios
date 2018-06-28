
from  bitstring import BitArray
import binascii

def is_cmt_tag(data, target="b84c020"):
  return target in data
class DataMap:
  def __init__(self):
    self.conv_map = []
  def __save__(self):
    print "saving the data!.........."
    file_name = "data/data_"+self.__getTime__()+'.pickle'
    with open(file_name, 'wb') as f:
      pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
  def __getTime__(self):
    return str(int(time.time()))
  def add(self,data):
    
    self.conv_map.append(data)


class ByteMap:
  def __init__(self, num_items):
    self.arr = [0]*num_items
  def push(self,item):
    self.arr.append(item)
    self.arr.pop(0)
def attach(byte_map):
  mac_address = binascii.hexlify(bytearray(byte_map))



def search_bites(byte1,byte2,gr_buffer,num_bites):
  old_bytes = ByteMap(num_bites);
  for position, byte, in enumerate(gr_buffer):
    
    if byte1==byte and byte2 in old_bytes.arr:
      print "old_bytes:", old_bytes.arr
      print str(byte)+"="+str(byte1)
      print BLE_PREAMBLE
    old_bytes.push(byte)

class Convolution:
  def __init__(self,target, gr_buffer):
    self.target_vect = self.hex_to_binary(target);
    self.search_vect = self.gr_buffer_to_binary_array(gr_buffer)
    #print "target vector:",self.target_vect
    #print "search vector:", self.search_vect

    self.index = len(self.target_vect)
    self.n = len(self.target_vect)
    self.conv_map = {};
  def convolve(self):

    while True:
      try:
        xor_result = self.compute_hamming_distance()
        if xor_result==None:
          return self.conv_map
        if xor_result>self.n/2:
          if xor_result in self.conv_map:
            self.conv_map[xor_result].append(self.index);
          else:
            self.conv_map[xor_result]=[self.index];

        self.index+=1;
      except IndexError:
        return self.conv_map
  def compute_hamming_distance(self):
    xor_segment = self.search_vect[self.index:self.index+self.n];
    ###########
    if len(xor_segment)!=len(self.target_vect):
      #print "segment length: ", len(xor_segment), "binary_array len:", len(self.target_vect)
      #print xor_segment,type(xor_segment)
      return None
    target = self.binary_to_integer(self.target_vect)
    new_segment  = self.binary_to_integer(xor_segment)
    ########
    return self.n-"{0:b}".format(target^new_segment).count('1');
  def hex_to_binary(self,_hex):
    '''
    Examples 
    >>> hex_to_binary('0xfe')
    '11111110'
    '''
    bin_obj = BitArray(hex = _hex);
    return bin_obj.bin;
  def gr_buffer_to_binary_array(self, gr_buff):
    '''
    Examples
    >>> 
    '''
    binary_array = ''
    for position, byte, in enumerate(gr_buff):
      binary_array+=self.get_binary(byte)
    return binary_array
  def get_binary(self,byte_hex, prefix = '0x'):
    '''
    examples 
    >>> get_binary('\xAA')
    '10101010'
    '''
    digits = binascii.hexlify(byte_hex);
    byte_arr =BitArray(hex=prefix+digits);
    return  byte_arr.bin[2:]
  def attach_prefix(self, arr,prefix = '0b'):
    '''
    examples
    >>> attach_prex('01010101')
    '0b01010101'
    >>> >>> attach_prex('01010101',prefix='0x')
    '0x01010101'
    '''
    return prefix+arr;
  def binary_to_integer(self,binary_string):
    '''
    examples
    >>> binary_to_integer('11111111')
    255
    >>> binary_to_integer('0b11111111')
    255
    '''
    #print "n:",self.n
    #print "binary_string: ", binary_string
    try:
      return int(binary_string,2)
    except:
      print "binary_string xun: ", binary_string
  def info(self):
    
    search_len = len(self.target_vect)
    max_match = 0
    if conv.conv_map:
      max_match = max(conv.conv_map.keys())
    if max_match>search_len-3:
      matching_index = min(self.conv_map[max_match])
      strt = max(0,matching_index-8)
      print "target vector: ", self.target_vect
      print "search space:",self.search_vect[max(matching_index-8,0):]
      print "matching part:",self.search_vect[matching_index:matching_index+search_len]
      print "map:", self.conv_map[max_match], len(self.search_vect)

def hamming2(s1, s2):
  """Calculate the Hamming distance between two bit strings"""
  assert len(s1) == len(s2)
  return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def hex_to_binary(_hex):
  '''
  Examples 
  >>> hex_to_binary('0xfe')
  '11111110'
  '''
  bin_obj = BitArray(hex = _hex);
  return bin_obj.bin;