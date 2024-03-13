from flask import jsonify, request
from . import api
from app import neomodels


@api.route('/frameworks', methods=['POST'])
def create_framework():
	payload = request.get_json()
	framework = neomodels.Framework(name=payload["name"],
		description=payload["description"])
	framework.save()

	return jsonify({"message": "ok"})