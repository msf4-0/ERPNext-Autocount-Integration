# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from autocount.autocount.doctype.list_controller import ListController
from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "Cash Sale"
DOCTYPE_URL_NAME = "CashSale"
ERP_PRIMARY_KEY = "doc_no"
AUTOCOUNT_PRIMARY_KEY = "DocNo"
URL_GET_ALL = f"{autocount_settings.get_ip_address()}/{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{autocount_settings.get_ip_address()}/{DOCTYPE_URL_NAME}/getDetail"

def transform_payment_mode(api_json_value):
	maps = {
	1 : "1 - Cash",
	4 : "4 - Credit Sale"
	}
	return maps[api_json_value]


def transform_discount(api_json_discount):
	if not api_json_discount:
		return 0
	return float(api_json_discount)

def transform_to_str(api_json_discount):
	if api_json_discount is None:
		return None
	return str(api_json_discount)


def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"item_code": child["ItemCode"],
			"uom": child["UOM"],
			"quantity": child["Qty"],
			"unit_price": child["UnitPrice"],
			"discount": transform_discount(child["Discount"])
			}
			new_child_list.append(x)

	output_data = {
	"doc_no" : data.get("DocNo"),
	"debtor_code" : data.get("DebtorCode"),
	"date" : data.get("DocDate"),
	"ship_info" : data.get("ShipInfo"),
	"item_table" : new_child_list,
	"total" : transform_to_str(data.get("Total")),
	"payment_mode" : transform_payment_mode(data.get("PaymentMode")),
	"cash_payment" : data.get("CashPayment"),
	"change" : data.get("Change"),
	"outstanding" : transform_to_str(data.get("Outstanding"))
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)