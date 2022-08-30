# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json

class AutocountSettings(Document):
	pass

DEFAULT_IP_ADDRESS = "http://host.docker.internal:8888"

@frappe.whitelist()
def get_ip_address():
	try:
		doc = frappe.get_doc("Autocount Settings")
		ip_address = doc.ip_address
		port = doc.port
		return f"http://{ip_address}:{port}"
	except:
		return DEFAULT_IP_ADDRESS

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	ip_address = data.get("ip_address")
	port = data.get("port")
	return f"http://{ip_address}:{port}"

@frappe.whitelist()
def test_connection(doc):
	ip_address = parse_doc(doc)
	url = f"{ip_address}/StockItem/getAll"
	print(url)
	try:
		res = requests.get(url)
		if res.status_code == 200:
			return "Connection success"
		return f"HTTP Error: {res.status_code}"
	except Exception as ex:
		return str(ex)
