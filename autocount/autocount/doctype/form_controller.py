# -*- coding: utf-8 -*-
# Copyright (c) 2022, Timothy Wong and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

import requests
import time

from autocount.autocount.doctype.autocount_settings import autocount_settings

class FormController:
	BASE_URL = autocount_settings.get_ip_address()

	def __init__(self, doctype_url_name):
		self.doctype_url_name = doctype_url_name
		self.url_add = f"{self.BASE_URL}/{self.doctype_url_name}/add"
		self.url_edit = f"{self.BASE_URL}/{self.doctype_url_name}/edit"
		self.url_delete = f"{self.BASE_URL}/{self.doctype_url_name}/delete"

	def add_to_autocount(self, data):
		start_time = time.time()
		res = requests.post(self.url_add, json = data)
		end_time = time.time()
		if res.status_code == 200:
			return f"{res.text}\n(Done in {end_time - start_time} seconds)\n"
		frappe.throw(res.text, title = "Server Exception")


	def edit_on_autocount(self, data):
		start_time = time.time()
		res = requests.put(self.url_edit, json = data)
		end_time = time.time()
		if res.status_code == 200:
			return f"{res.text}\n(Done in {end_time - start_time} seconds)\n"
		frappe.throw(res.text, title = "Server Exception")

	def delete_on_autocount(self, key):
		res = requests.delete(f"{self.url_delete}/{key}")
		if res.status_code == 200:
			frappe.msgprint(res.text)
			return res.text
		# Comment: Will delete ERPNext even if HTTP Error
		# frappe.throw(res.text, title = "Server Exception")	
