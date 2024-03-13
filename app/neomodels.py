from neomodel import StructuredNode, StringProperty, RelationshipTo
from app import neo_db

class Control(StructuredNode):
	name = StringProperty(unique_index=True, required=True)

class Framework(StructuredNode):
	name = StringProperty(unique_index=True, required=True)
	description = StringProperty(unique_index=True, required=True)

	control = RelationshipTo(Control, "HAS_A")
