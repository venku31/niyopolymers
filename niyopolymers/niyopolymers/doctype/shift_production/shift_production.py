# -*- coding: utf-8 -*-
# Copyright (c) 2021, Atriina and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ShiftProduction(Document):
	pass

# @frappe.whitelist()
def create_stock_entry(doc, handler=""):
    for se_item in doc.items:
        if se_item.basic_rate > 0:    
                se = frappe.new_doc("Stock Entry")
                se.update({ "purpose": "Repack" , "stock_entry_type": "Repack"})
#       for se_item in doc.items:
                se.append("items", { "item_code":se_item.preform, "qty": se_item.blowing,"s_warehouse": se_item.rm_warehouse,"transfer_qty" : se_item.blowing,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":0})
#       for se_item in doc.items:
                se.append("items", { "item_code":se_item.product_code, "qty": se_item.blowing_perform,"set_basic_rate_manually":1,"t_warehouse":se_item.fg_warehouse,"transfer_qty" : se_item.blowing_perform,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":0,"basic_rate": se_item.basic_rate})
#        for se_item in doc.items:
                if se_item.rejection > 0:
                        se.append("items", { "item_code":se_item.rejection_item, "qty": se_item.rejection,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":0,"basic_rate": se_item.basic_rate})
#        for se_item in doc.items:
                if se_item.white > 0:
                        se.append("items", { "item_code":se_item.rejection_white, "qty": se_item.white,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection_white,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":0,"basic_rate": se_item.basic_rate})
#       for se_item in doc.items:
                if se_item.hot > 0:
                        se.append("items", { "item_code":se_item.rejection_hot, "qty": se_item.hot,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection_hot,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":0,"basic_rate": se_item.basic_rate})
#    frappe.msgprint('Stock Entry is created please submit the stock entry')
        else:
                se = frappe.new_doc("Stock Entry")
                se.update({ "purpose": "Repack" , "stock_entry_type": "Repack"})
#       for se_item in doc.items:
                se.append("items", { "item_code":se_item.preform, "qty": se_item.blowing,"s_warehouse": se_item.rm_warehouse,"transfer_qty" : se_item.blowing,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":1})
#       for se_item in doc.items:
                se.append("items", { "item_code":se_item.product_code, "qty": se_item.blowing_perform,"set_basic_rate_manually":1,"t_warehouse":se_item.fg_warehouse,"transfer_qty" : se_item.blowing_perform,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":1,"basic_rate": se_item.basic_rate})
#        for se_item in doc.items:
                if se_item.rejection > 0:
                        se.append("items", { "item_code":se_item.rejection_item, "qty": se_item.rejection,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":1,"basic_rate": se_item.basic_rate})
#        for se_item in doc.items:
                if se_item.white > 0:
                        se.append("items", { "item_code":se_item.rejection_white, "qty": se_item.white,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection_white,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":1,"basic_rate": se_item.basic_rate})
#       for se_item in doc.items:
                if se_item.hot > 0:
                        se.append("items", { "item_code":se_item.rejection_hot, "qty": se_item.hot,"set_basic_rate_manually":1,"t_warehouse": se_item.rejection_warehouse,"transfer_qty" : se_item.rejection_hot,"conversion_factor": 1,"uom" : se_item.uom,"allow_zero_valuation_rate":1,"basic_rate": se_item.basic_rate})
#    frappe.msgprint('Stock Entry is created please submit the stock entry')
#        se.save()
        se.docstatus=1
        se.insert()
