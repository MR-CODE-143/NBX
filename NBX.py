import os,platform
bit = platform.architecture()[0]
if bit=='64bit':
    os.system('chmod +x file')
    os system('./file')
else:
    exit('[•] ONLY FOR 64bit')
