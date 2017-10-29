import clr
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import xml.etree.ElementTree as ET

elementlist = []

root = ET.fromstring(IN[0])
node_ver = root.get("Version")
node_name = root.get("Name")
node_id = root.get("ID")
node_desc = root.get("Description")
node_cat = root.get("Category")
node_inputs = []
node_input_types = []
node_input_defaults = []
node_outputs = []
node_scripts = []
node_customnodes = []
node_customnodes_count = []
node_ootbnodes = []
node_ootbnodes_count = []

for child in root:
	if child.tag == "Elements":
		for element in child:
			if element.tag == "Dynamo.Nodes.Symbol" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Symbol":
				for symbol in element:
					inputdef = symbol.get("value")
					inputdef2 = inputdef.split(":")
					node_inputs.append(inputdef2[0].strip())
					if len(inputdef2) > 1:
						inputdef3 = inputdef2[1].split("=")
						node_input_types.append(inputdef3[0].strip())
						if len(inputdef3) > 1:
							node_input_defaults.append(inputdef3[1].strip())
						else:
							node_input_defaults.append("")
					else:
						node_input_types.append("")
						node_input_defaults.append("")
			elif element.tag == "Dynamo.Nodes.Output" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Output":
				for symbol in element:
					#node_outputs.append(symbol.get("value").strip())
					if symbol.get("value") != None:
						node_outputs.append(symbol.get("value").strip())
			elif element.tag == "DSIronPythonNode.PythonNode" or element.tag == "PythonNodeModels.PythonNode":
				for script in element:
					if script.text != None:
						node_scripts.append(script.text)
			elif element.tag == "Dynamo.Nodes.Function" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Function":
				if element.get("nickname") in node_customnodes:
					node_customnodes_count[node_customnodes.index(element.get("nickname"))] += 1
				else:
					node_customnodes.append(element.get("nickname"))
					node_customnodes_count.append(1)
			else:
				if element.get("nickname") in node_ootbnodes:
					node_ootbnodes_count[node_ootbnodes.index(element.get("nickname"))] += 1
				else:
					node_ootbnodes.append(element.get("nickname"))
					node_ootbnodes_count.append(1)
OUT = (node_ver,node_name,node_id,node_desc,node_cat,node_inputs,node_input_types,node_input_defaults,node_outputs,node_scripts,node_customnodes,node_customnodes_count,node_ootbnodes,node_ootbnodes_count)