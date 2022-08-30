# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

DEFAULT_URL = "http://host.docker.internal:8888"

@frappe.whitelist()
def get_ip_address():
	try:
		doc = frappe.get_single("Autocount Settings")
		ip_address = doc.ip_address
		port = doc.port
		return f"http://{ip_address}:{port}"
	except:
		return DEFAULT_URL