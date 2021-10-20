import sys
import nuke

nuke.scriptOpen(sys.argv[1])
writeNodes = nuke.allNodes("Write")
for node in writeNodes:
    print(node.name(), ":", node.frameRange())
