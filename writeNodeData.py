import sys
import nuke

nuke.scriptOpen(sys.argv[1])
writeNodes = nuke.allNodes("Write")
for node in writeNodes:
    if nuke.NUKE_VERSION_MAJOR > 12:
        print(str(node.name()), ":", str(node.frameRange()))
    else:
        a_set = str(node.name()), ":", str(node.frameRange())
        list_of_strings = [str(s) for s in a_set]
        joined_string = " ".join(list_of_strings)
        print(str(joined_string))
