# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json

from autocount.autocount.doctype.form_controller import FormController
from autocount.autocount.doctype.utils import convert_date_string

# from autocount.autocount.doctype.autocount_settings import autocount_settings
from autocount.autocount.doctype import url_config

DOCTYPE = "Cancel SO"
DOCTYPE_URL_NAME = "CancelSO"

controller = FormController(DOCTYPE_URL_NAME)

class CancelSO(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def get_items_by_debtor_autocount(debtor_code):
	# BASE_URL = autocount_settings.get_ip_address()
	# BASE_URL = "http://host.docker.internal:8888"
	SOCKET_ADDRESS = url_config.get_socket_address()
	
	results_list = []
	for sales_order in frappe.get_all("Autocount Sales Order", filters={"debtor_code":debtor_code}):
		results = json.loads(requests.get(f"{SOCKET_ADDRESS}/SalesOrder/getDetail/{sales_order.name}", timeout = 10).text)
		if results:
			for result in results:
				result["SalesOrderNo"] = sales_order.name
		results_list += results
	return results_list


@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	new_date = convert_date_string(data.get("date"))
	detail_list = []

	if data.get("chosen_table") is not None:			### chosen_table
		for item in data.get("chosen_table"):	
			detail = {
			"salesOrderNo" : item.get("sales_order_no"),
			"itemCode" : item.get("item_code"),
			"uom" : item.get("uom"),
			"quantity" : str(item.get("quantity"))
			}
			detail_list.append(detail)

	submitted_data = {
	"docNo" : data.get("doc_no"), 
	"debtorCode" : data.get("debtor_code"), 
	"date" : new_date,
	"detailList" : detail_list
	}
	return submitted_data

@frappe.whitelist()
def add(doc):
	submitted_data = parse_doc(doc)
	return controller.add_to_autocount(submitted_data)

@frappe.whitelist()
def edit(doc):
	submitted_data = parse_doc(doc)
	return controller.edit_on_autocount(submitted_data)