class Medicine:
    def __init__(self, code_number, price_per_unit, Batch_no, exp_date, vendor_id, available_quantity,  unit_selling,threshold_value=0, trade_name="", generic_name="", company_description="", medicine_description=""):
        self.code_number = code_number
        self.trade_name = trade_name
        self.generic_name = generic_name
        self.price_per_unit = price_per_unit
        self.Batch_no = Batch_no
        self.exp_date = exp_date
        self.vendor_id = vendor_id
        self.company_description = company_description
        self.medicine_description = medicine_description
        self.available_quantity = available_quantity
        self.threshold_value = threshold_value
        self.unit_selling = unit_selling

    def addNewMedicineToInventory(self):
        self.code_number = input("Enter code number of the medicine")
        self.trade_name = input("Enter trade name of the medicine")
        self.generic_name = input("Enter generic name of the medicine")
        self.price_per_unit = input("Enter price per unit of the medicine")
        self.Batch_no = input("Enter batch number of the medicine")
        self.exp_date = input("Enter expiry date of the medicine")
        self.vendor_id = input("Enter vendor id of the medicine")
        self.company_description = input("Enter the company name of the medicine")
        self.medicine_description = input("Enter the description of the medicine")
        self.available_quantity = input("Enter quantity of the medicine")
        self.unit_selling = input("Enter the unit selling of the medicine")
        #Add self to json

    def addExistMedicineToInventory(self):
        med_id = input("Enter the id of medicine to be added")
        #Find medicine from json with this med_id as code_number
        #Use it to get data not given from terminal
        B_no = input("Enter the batch number of the medicine")
        expiry = input("Enter the expiry date of the medicine")
        qnty = input("Enter the quantity of the medicine")
        #Add this to json


    def deleteMedicineFromInventory(self):
        med_id = input("Enter the id of medicine to be deleted")
        #Delete from json

    def editMedicinesInInventory(self):
        med_id = input("Enter the id of medicine to be edited")
        qnty = input("Enter the quantity to be added(use \"-\" to if certain quantity is to be removed)")
        #Edit from json

    def medicineInfo(self):
        s = input("Temp")

    def listExpiredMedicines(self):
        d = input("GAS")


