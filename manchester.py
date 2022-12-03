
def decode(buf):
  out = bytearray(len(buf) / 2)
  return out


def e(b):
  ret = 0
  ret |= (0b01 if (b & 1) else 0b10) << 0
  ret |= (0b01 if (b & 2) else 0b10) << 2
  ret |= (0b01 if (b & 4) else 0b10) << 4
  ret |= (0b01 if (b & 8) else 0b10) << 6

  return ret

def encode(buf):
  out = bytearray(len(buf) * 2)
  in_len = len(buf)
  idx = 0
  while idx < in_len:
    out[idx*2] = e(buf[idx] >> 4)
    out[(idx*2) + 1] = e(buf[idx] & 0xF)
    idx += 1

  return out

def d(b):
  ret = 0
  def offset(o):
    nonlocal ret
    two_bits = (b >> (o*2)) & 0b11
    if two_bits == 1:
      ret |= 1 << o
    elif two_bits == 2:
      pass
    else:
      raise StopIteration

  offset(0)
  offset(1)
  offset(2)
  offset(3)

  return ret

def decode(buf):
  in_len = (len(buf) // 2) * 2 ## to iterate over
  out_len = len(buf) // 2
  if len(buf) % 2:
    out_len += 1

  out = bytearray(out_len)
  idx = 0
  while idx < in_len:
    try:
      out[idx//2] = (d(buf[idx]) << 4)
      idx += 1
    except StopIteration:
      break

    try:
      out[idx//2] |= d(buf[idx])
      idx += 1
    except StopIteration:
      idx += 1

  if idx == (len(buf) - 1):
    try:
      out[idx//2] = d(buf[idx]) << 4
      idx += 1
    except StopIteration:
      pass

  return out[:(idx//2)]
