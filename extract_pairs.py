# Input: 
# "41426aa1425d"=hex:b3,da,91,6d,0b,4a,7f,10,01,cf,5f,49,3f,ea,25,f2
# Output:
# 41:42:6A:A1:42:5D B3DA916D0B4A7F1001CF5F493FEA25F2
def parseRegfile(file_path:str):
  try:
    with open(file_path, "rb") as file:
      # read as text
      file_contents = file.read().decode(("utf-16"))
      for line in file_contents.splitlines():
        splits = line.split("=hex:")
        if len(splits) != 2:
            continue
        deviceId, linkKey = splits
        deviceId = deviceId.strip('"').upper()
        # every 2 characters, add a ':' in deviceId
        deviceId = ":".join([deviceId[i:i+2] for i in range(0, len(deviceId), 2)])
        linkKey = linkKey.replace(",", "").upper()
        print(deviceId, linkKey)
  except FileNotFoundError:
    print("File not found:", file_path)

def parse_args():
  import argparse
  parser = argparse.ArgumentParser(
      description="Bluetooth link key parser. Returns <mac address> <link key> pairs."
  )
  parser.add_argument("file", type=str, help="Path to the registry file")
  return parser.parse_args()

def main():
  """Run if main module"""
  args = parse_args()
  parseRegfile(args.file)

if __name__ == "__main__":
  main()
