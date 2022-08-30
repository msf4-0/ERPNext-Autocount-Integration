# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

DEFAULT_IP_ADDRESS = "host.docker.internal"
DEFAULT_PORT = "8888"

@frappe.whitelist()
def get_socket_address():
	# try:
	# 	doc = frappe.get_single("Autocount Settings")
	# 	ip_address = doc.ip_address
	# 	port = doc.port
	# 	if not ip_address:
	# 		doc.set("ip_address", DEFAULT_IP_ADDRESS)
	# 		doc.save()
	# 	if not port:
	# 		doc.set("port", DEFAULT_URL)
	# 		doc.save()
	# 	return f"http://{ip_address}:{port}"
	# except:
	# 	return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"

	# return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"

	data = frappe.db.get("Autocount Settings")

	if not data:
		return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"

	ip_address = data.get("ip_address")
	port = data.get("port")
	if not ip_address:
		ip_address = DEFAULT_IP_ADDRESS
		frappe.db.set("Autocount Settings", "Autocount Settings", "ip_address", DEFAULT_IP_ADDRESS)
		frappe.db.commit()
	if not port:
		port = DEFAULT_PORT
		frappe.db.set("Autocount Settings", "Autocount Settings", "port", DEFAULT_PORT)
		frappe.db.commit()
	return f"http://{ip_address}:{port}"


	
