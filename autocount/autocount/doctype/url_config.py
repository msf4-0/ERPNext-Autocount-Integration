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
	try:
		doc = frappe.get_single("Autocount Settings")
		ip_address = doc.ip_address
		port = doc.port
		if not ip_address:
			doc.set("ip_address", DEFAULT_IP_ADDRESS)
			doc.save()
		if not port:
			doc.set("port", DEFAULT_URL)
			doc.save()
		return f"http://{ip_address}:{port}"
	except:
		return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"
