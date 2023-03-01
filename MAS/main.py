from tkinter import *
# import tkinter as ttk
# from tkinter import scrolledtext
from tkinter import messagebox
# from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
# import random
import datetime
from datetime import date
import json

# from MAS.Data import LogInCredentials


class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Page")
        self.window.geometry('1350x750+0+0')
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)
        self.frame = Frame(self.window, width=1350, height=750)
        self.frame.pack()
        self.frame.grid_propagate(False)
        bg = ImageTk.PhotoImage(Image.open("./Data/OnlinePharmacy.jpg"))
        img_label = Label(self.frame, image=bg)
        img_label.place(x=0, y=0)

        self.labelTitle = Label(self.frame, text="Medicine Automation Software", font=('arial', 30, 'bold'),
                                fg="#222730", bg="#b6b2ad", bd=20)
        self.labelTitle.grid(row=0, column=0, pady=(0, 40), padx=(0, 50))
        self.labelTitle.place(in_=self.frame, anchor="c", relx=.5, rely=.123)

        # ****   FRAMES     *************

        self.frame1 = Frame(self.frame, width=542, height=180, bd=2, relief='solid', padx=12, bg="#7D8CA3")
        self.frame1.place(in_=self.frame, anchor="c", relx=.5, rely=.44)
        # self.frame2.grid(row=2, column=0)
        self.frame1.grid_propagate(False)

        self.frame2 = Frame(self.frame, width=542, height=70, bd=2, relief='solid', padx=12, bg="#7D8CA3")
        self.frame2.place(in_=self.frame, anchor="c", relx=.5, rely=.61)
        # self.frame3.grid(row=3, column=0)
        self.frame2.grid_propagate(False)

        # self.frame3 = Frame(self.frame, width=542, height=80, bd=2, relief='solid', padx=12, bg="#7D8CA3")
        # self.frame3.place(in_=self.frame, anchor="c", relx=.5, rely=.75)
        # # self.frame2.grid(row=2, column=0)
        # self.frame3.grid_propagate(False)

        # ===========             USERNAME AND PASSWORD (FRAME 2)            ===================================================================================

        self.labelUser = Label(self.frame1, text="USERNAME / USER ID   ", font=('arial', 12, 'bold'), bg="#7D8CA3",
                               bd=20)
        self.labelUser.grid(row=0, column=0, columnspan=2, pady=10)
        self.username = StringVar()
        self.eUsername = Entry(self.frame1, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1, textvariable=self.username)
        self.eUsername.grid(row=0, column=2, columnspan=2, pady=10)

        self.labelPass = Label(self.frame1, text="PASSWORD   ", font=('arial', 12, 'bold'), bg="#7D8CA3", bd=20)
        self.labelPass.grid(row=1, column=0, columnspan=2, pady=10)
        self.password = StringVar()
        self.ePass = Entry(self.frame1, show="*", width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1, textvariable=self.password)
        self.ePass.grid(row=1, column=2, columnspan=2, pady=10)

        # ===========            LOGIN RESET EXIT (FRAME 3)            ===================================================================================

        self.btnLogin = Button(self.frame2, text="Login", command=lambda: self.userLogin(), font=('arial', 12, 'bold'),
                               width=13)
        self.btnLogin.grid(row=0, column=0, padx=11, pady=11)
        self.btnReset = Button(self.frame2, text="Reset", command=lambda: self.reset(), font=('arial', 12, 'bold'),
                               width=15)
        self.btnReset.grid(row=0, column=1, padx=11, pady=11)
        self.btnExit = Button(self.frame2, text="Exit", command=lambda: self.exitProgram(), font=('arial', 12, 'bold'),
                              width=13)
        self.btnExit.grid(row=0, column=2, padx=11, pady=11)

        self.window.mainloop()

    def userLogin(self):
        if (
                self.eUsername.get() != shopowner[0] and self.eUsername.get() != shopowner[1]) or self.ePass.get() != shopowner[2]:
            messagebox.showwarning("Invalid Entries!", "The Username or Password entered is incorrect")
        else:
            self.operation_selection_window()

    def reset(self):
        self.window.destroy()
        MainWindow(Tk())

    def exitProgram(self):
        choice = messagebox.askquestion("Exit", "Are you sure?")
        if choice == 'yes':
            exit()

    def operation_selection_window(self):
        self.username.set("")
        self.password.set("")
        self.newWindow = Toplevel(self.window)
        self.app = OperationSelectionWindow(self.newWindow)


class OperationSelectionWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Operation Selection Page")
        self.window.geometry('1350x750+0+0')
        self.frame = Frame(self.window)
        self.frame.pack()

        # ====================             FRAMES             ===================================================================================

        self.frame1 = Frame(self.frame, width=1000, height=100, bd=7, relief='ridge', bg="SkyBlue2")
        self.frame1.grid(row=0, column=0, sticky="news")

        self.frame2 = Frame(self.frame, width=900, height=630, bd=7, relief='ridge', padx=12)
        self.frame2.grid(row=0, column=1)

        # ====================             BUTTONS IN FRAME1             ===================================================================================

        self.btnNewMedicine = Button(self.frame1, text="Add New Medicine",
                                     command=lambda: self.addNewMedicineToInventory(), font=('arial', 12, 'bold'),
                                     width=20)
        self.btnNewMedicine.grid(row=0, column=0, padx=40, pady=10)

        self.btnExistMedicine = Button(self.frame1, text="Add New Batch of \nExisting Medicine",
                                       command=lambda: self.addExistMedicine(), font=('arial', 12, 'bold'), width=20)
        self.btnExistMedicine.grid(row=1, column=0, padx=40, pady=10)

        # self.btnAddPublication = Button(self.frame1, text="Restock a Medicine", command=lambda: self.restock(),
        #                                 font=('arial', 12, 'bold'), width=20)
        # self.btnAddPublication.grid(row=2, column=0, padx=40, pady=10)

        self.btnEditPublications = Button(self.frame1, text="Query about a Medicine", command=lambda: self.Query(),
                                          font=('arial', 12, 'bold'), width=20)
        self.btnEditPublications.grid(row=3, column=0, padx=40, pady=10)

        self.btnCustomerBills = Button(self.frame1, text="Print the list of \nexpired Medicines",
                                       command=lambda: self.printexpiredlist(), font=('arial', 12, 'bold'), width=20)
        self.btnCustomerBills.grid(row=4, column=0, padx=40, pady=10)

        self.btnCustomerBills = Button(self.frame1, text="Process \ncustomer order",
                                       command=lambda: self.processOrder(), font=('arial', 12, 'bold'), width=20)
        self.btnCustomerBills.grid(row=5, column=0, padx=40, pady=10)

        self.btnSummary = Button(self.frame1, text="Print and Store \nrequirement for the \nnext day",
                                 command=lambda: self.printandstorerequirement(), font=('arial', 12, 'bold'), width=20)
        self.btnSummary.grid(row=6, column=0, padx=40, pady=10)

        self.btnAddDeliverer = Button(self.frame1, text="Add Vendor",
                                      command=lambda: self.operationsonvendors(), font=('arial', 12, 'bold'), width=20)
        self.btnAddDeliverer.grid(row=7, column=0, padx=40, pady=10)

        self.btnDeliveryDetails = Button(self.frame1, text="Place an order \nfor the requirement",
                                         command=lambda: self.placeOrder(), font=('arial', 12, 'bold'), width=20)
        self.btnDeliveryDetails.grid(row=8, column=0, padx=40, pady=10)

        self.btnDeliveryDetails = Button(self.frame1, text="Generate Revenue \nand Profit",
                                         command=lambda: self.Generate(), font=('arial', 12, 'bold'), width=20)
        self.btnDeliveryDetails.grid(row=9, column=0, padx=40, pady=10)

        self.window.mainloop()

    def addNewMedicineToInventory(self):
        self.reset()
        # ====================            ADD NEW MEDICINE HEADING             ===================================================================================

        self.labelNewMedicine = Label(self.frame2, text="Add New Medicine", font=('arial', 17, 'bold'),
                                      bd=20)
        self.labelNewMedicine.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelcnumber = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelcnumber.grid(row=0, column=0, rowspan=2)
        self.cNum = IntVar()
        self.ecNum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.cNum)
        self.ecNum.grid(row=2, column=0, padx=10)

        self.labeltradename = Label(self.frameDetails, text="Trade Name ", font=('arial', 12, 'bold'), bd=10,
                                    bg="SkyBlue2", justify=LEFT)
        self.labeltradename.grid(row=0, column=1, rowspan=2)
        self.trname = StringVar()
        self.eTrame = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.trname)
        self.eTrame.grid(row=2, column=1, padx=10)

        self.labelgenname = Label(self.frameDetails, text="Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelgenname.grid(row=0, column=2, rowspan=2)
        self.gname = StringVar()
        self.eGname = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.gname)
        self.eGname.grid(row=2, column=2, padx=10)

        self.labelppu = Label(self.frameDetails, text="Price per Unit ", font=('arial', 12, 'bold'), bd=10,
                              bg="SkyBlue2", justify=LEFT)
        self.labelppu.grid(row=4, column=0, rowspan=2)
        self.pricepU = IntVar()
        self.ePPU = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.pricepU)
        self.ePPU.grid(row=6, column=0, padx=10)

        self.labelBNo = Label(self.frameDetails, text="Batch Number ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelBNo.grid(row=4, column=1, rowspan=2)
        self.bnum = StringVar()
        self.eBnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.bnum)
        self.eBnum.grid(row=6, column=1, padx=10)

        self.labelexpD = Label(self.frameDetails, text="Expiry Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelexpD.grid(row=4, column=2, rowspan=2)
        self.expdate = StringVar()
        self.eExpdate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                              borderwidth=1,
                              textvariable=self.expdate)
        self.eExpdate.grid(row=6, column=2, padx=10)

        self.labelvid = Label(self.frameDetails, text="Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=8, column=0, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=10, column=0, padx=10)

        self.labelcompD = Label(self.frameDetails, text="Company Description ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelcompD.grid(row=8, column=1, rowspan=2)
        self.compd = StringVar()
        self.eCompd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.compd)
        self.eCompd.grid(row=10, column=1, padx=10)

        self.labelmedD = Label(self.frameDetails, text="Medicine Description ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelmedD.grid(row=8, column=2, rowspan=2)
        self.medd = StringVar()
        self.eMedd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.medd)
        self.eMedd.grid(row=10, column=2, padx=10)

        self.labelavailQ = Label(self.frameDetails, text="Available Quantity ", font=('arial', 12, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelavailQ.grid(row=12, column=0, rowspan=2)
        self.availq = IntVar()
        self.eAvailq = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                             borderwidth=1,
                             textvariable=self.availq)
        self.eAvailq.grid(row=14, column=0, padx=10)

        self.labelthresval = Label(self.frameDetails, text="Threshold Value ", font=('arial', 12, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelthresval.grid(row=12, column=1, rowspan=2)
        self.thresVal = IntVar()
        self.eThresVal = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.thresVal)
        self.eThresVal.grid(row=14, column=1, padx=10)

        self.labelusell = Label(self.frameDetails, text="Unit Selling ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelusell.grid(row=12, column=2, rowspan=2)
        self.uSell = IntVar()
        self.eUSell = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.uSell)
        self.eUSell.grid(row=14, column=2, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Add", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addnewMed())
        self.btnAddTop.grid(row=19, column=1, padx=20)

    def addnewMed(self):
        var = {
            "code_number": self.cNum.get(),
            "trade_name": self.trname.get(),
            "generic_name": self.gname.get(),
            "price_per_unit": self.pricepU.get(),
            "Batch_no": self.bnum.get(),
            "exp_date": self.expdate.get(),
            "vendor_id": self.vId.get(),
            "company_description": self.compd.get(),
            "medicine_description": self.medd.get(),
            "available_quantity": self.availq.get(),
            "threshold_value": self.thresVal.get(),
            "unit_selling": self.uSell.get()
        }

        medicineInventory.append(var)

        with open("./Data/MedicineInventory.json", "w") as p:
            json.dump(medicineInventory, p, indent=4)
            messagebox.showinfo("Success", "Medicine added succesfully", parent=self.window)

    def addExistMedicine(self):
        self.reset()
        # ====================            ADD NEW BATCH OF EXISTING MEDICINE HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Add New Batch of \nExisting Medicine", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelcnumber = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelcnumber.grid(row=0, column=0, rowspan=2)
        self.cNum = IntVar()
        self.ecNum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.cNum)
        self.ecNum.grid(row=2, column=0, padx=10)

        self.labelBNo = Label(self.frameDetails, text="Batch Number ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelBNo.grid(row=0, column=1, rowspan=2)
        self.bnum = StringVar()
        self.eBnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.bnum)
        self.eBnum.grid(row=2, column=1, padx=10)

        self.labelexpD = Label(self.frameDetails, text="Expiry Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelexpD.grid(row=0, column=2, rowspan=2)
        self.expdate = StringVar()
        self.eExpdate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                              borderwidth=1,
                              textvariable=self.expdate)
        self.eExpdate.grid(row=2, column=2, padx=10)

        self.labelppu = Label(self.frameDetails, text="Price per Unit ", font=('arial', 12, 'bold'), bd=10,
                              bg="SkyBlue2", justify=LEFT)
        self.labelppu.grid(row=4, column=0, rowspan=2)
        self.pricepU = IntVar()
        self.ePPU = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.pricepU)
        self.ePPU.grid(row=6, column=0, padx=10)

        self.labelvid = Label(self.frameDetails, text="Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=4, column=1, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=6, column=1, padx=10)

        self.labelavailQ = Label(self.frameDetails, text="Available Quantity ", font=('arial', 12, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelavailQ.grid(row=4, column=2, rowspan=2)
        self.availq = IntVar()
        self.eAvailq = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                             borderwidth=1,
                             textvariable=self.availq)
        self.eAvailq.grid(row=6, column=2, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addExisting())
        self.btnAddTop.grid(row=8, column=1, padx=20)

    def addExisting(self):
        flag = False
        for i in (medicineInventory):
            if i["code_number"] == self.cNum.get():
                if str(i["Batch_no"]) == str(self.bnum.get()):
                    i["available_quantity"] += self.availq.get()
                    messagebox.showinfo("Success",
                        "Quantity of the medicines increased for batch_no: " + i["Batch_no"] + " by " + str(self.availq.get()), parent=self.window)
                else:
                    obj = {"code_number": self.cNum.get(),
                           "trade_name": i["trade_name"],
                           "generic_name": i["generic_name"],
                           "price_per_unit": self.pricepU.get(),
                           "Batch_no": self.bnum.get(),
                           "exp_date": self.expdate.get(),
                           "vendor_id": self.vId.get(),
                           "company_description": i["company_description"],
                           "medicine_description": i["medicine_description"],
                           "available_quantity": self.availq.get(),
                           "threshold_value": i["threshold_value"],
                           "unit_selling": i["unit_selling"]}
                    medicineInventory.append(obj)
                    messagebox.showinfo("Success","New batch has been added.",parent=self.window)
                flag = True
                break

        with open("./Data/MedicineInventory.json", "w") as p:
            json.dump(medicineInventory, p, indent=4)
        if flag == False:
            messagebox.showinfo("Success","No medicine with the given code number is found.",parent=self.window)

    def Query(self):
        self.reset()
        # ====================            QUERY HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Query about a medicine", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelqname = Label(self.frameDetails, text="Trade Name/Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelqname.grid(row=0, column=0, rowspan=2)
        self.qName = StringVar()
        self.eQName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.qName)
        self.eQName.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.printmedicine())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def printmedicine(self):
        flag = False
        if self.qName.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.window)
            flag = True

        for i in medicineInventory:
            if (i["trade_name"] == self.qName.get() or i["generic_name"] == self.qName.get()):
                flag = True
                self.reset()
                self.labelMed = Label(self.frame2, text="Medicine Info", font=('arial', 17, 'bold'),
                                               bd=20)
                self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
                self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                          bg="SkyBlue2")
                self.frameDetails.grid(row=1, column=0)
                self.labelName = Label(self.frameDetails, text="Medicine Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=0, column=0)
                self.labelName = Label(self.frameDetails, text=i["generic_name"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=0, column=1)
                self.labelName = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=1, column=0)
                self.labelName = Label(self.frameDetails, text=i["code_number"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=1, column=1)
                self.labelID = Label(self.frameDetails, text="Available Qunatity", font=('arial', 12, 'bold'), bd=10,
                                     bg="SkyBlue2", justify=LEFT)
                self.labelID.grid(row=2, column=0)
                self.labelID = Label(self.frameDetails, text=i["available_quantity"], font=('arial', 12, 'bold'), bd=10,
                                     bg="SkyBlue2", justify=LEFT)
                self.labelID.grid(row=2, column=1)
                break
        if flag == False:
            messagebox.showwarning("Invalid Entries!", "Medicine Not Found", parent=self.window)

    def printexpiredlist(self):
        self.reset()
        # ====================            PRINT LIST HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="List of Expired Medicines", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Print", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.expirylist())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def expirylist(self):
        self.reset()
        self.labelMed = Label(self.frame2, text="List of Expired Medicines", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)
        t = self.tDate.get().split('-')
        t = [int(k) for k in t]
        d1 = date(t[2], t[1], t[0])
        self.labelName = Label(self.frameDetails, text="Medicine Generic Name", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)
        self.labelName = Label(self.frameDetails, text="Vendor Id", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)

        l=1
        for i in medicineInventory:
            temp = i["exp_date"]
            f = temp.split('-')
            f = [int(k) for k in f]
            d2 = date(f[2], f[1], f[0])
            if d1 < d2:
                self.labelName = Label(self.frameDetails, text=i["generic_name"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=l, column=0)
                self.labelName = Label(self.frameDetails, text=i["vendor_id"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=l, column=1)
                l=l+1


    def processOrder(self):
        self.reset()
        self.reset()
        self.medicineQuantityPair = []
        self.CustomerOrder = []

        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Generate bill for\n customer order", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Medicine Code Number", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tmed = IntVar()
        self.eTmed = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tmed)
        self.eTmed.grid(row=2, column=0, padx=10)

        self.labeltdate = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                                justify=LEFT)
        self.labeltdate.grid(row=0, column=1, rowspan=2)
        self.tQ = IntVar()
        self.eTQ = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tQ)
        self.eTQ.grid(row=2, column=1, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Add to list", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.medicineQuantityPairFunction())
        self.btnAddTop.grid(row=2, column=2, padx=20)

        self.btnAddTop = Button(self.frameDetails, text="Print Bill", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.printcustomerorder())
        self.btnAddTop.grid(row=4, column=1, padx=20)

    def medicineQuantityPairFunction(self):
        self.medicineQuantityPair = [self.tmed.get(),self.tQ.get()]
        self.CustomerOrder.append(self.medicineQuantityPair)

    def printcustomerorder(self):
        self.reset()
        self.labelMed = Label(self.frame2, text="Customer Bill", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=1, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=0, column=1)

        self.labelName = Label(self.frameDetails, text="Medicine Generic Name", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=1, column=0)

        self.labelName = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=1, column=1)

        self.labelName = Label(self.frameDetails, text="Price Per Unit", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=1, column=2)
        cost = 0
        for i in self.CustomerOrder:
            self.labelName = Label(self.frameDetails, text=i["generic_name"], font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=1, column=0)

            self.labelName = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=1, column=1)

            self.labelName = Label(self.frameDetails, text="Price Per Unit", font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=1, column=2)


    def printandstorerequirement(self):
        self.reset()
        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Requirement for the next day", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Print", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.makechange())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def operationsonvendors(self):
        self.reset()
        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Add Vendor", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelvid = Label(self.frameDetails, text="Enter Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=0, column=0, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=2, column=0, padx=10)

        self.labelvname = Label(self.frameDetails, text="Enter Vendor Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvname.grid(row=0, column=1, rowspan=2)
        self.vName = StringVar()
        self.eVName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vName)
        self.eVName.grid(row=2, column=1, padx=10)

        self.labelvadd = Label(self.frameDetails, text="Enter Vendor Address ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvadd.grid(row=0, column=2, rowspan=2)
        self.vAdd = StringVar()
        self.eVAdd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vAdd)
        self.eVAdd.grid(row=2, column=2, padx=10)

        self.labelvcnum = Label(self.frameDetails, text="Enter Code Numbers of Medicines ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvcnum.grid(row=3, column=0, rowspan=2)
        self.vCnum = StringVar()
        self.eVCnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vCnum)
        self.eVCnum.grid(row=5, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addVendor())
        self.btnAddTop.grid(row=5, column=2, padx=20)

    def addVendor(self):
        var2 = {
            "vendor_id": self.vId.get(),
            "code_numers": self.vCnum.get(),
            "vendor_name": self.vName.get(),
            "vendor_address": self.vAdd.get()
        }

        vendorlist.append(var2)

        with open("./Data/vendorDetails.json", "w") as p:
            json.dump(vendorlist, p, indent=4)
            messagebox.showinfo("Success", "Vendor added succesfully", parent=self.window)

    def placeOrder(self):
        self.reset()
        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Place order to a vendor", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Place Order", font=('arial', 12, 'bold'), width=10,
                                command=lambda: self.makechange())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def Generate(self):
        self.reset()
        # ====================            GENERATE REVENUE AND PROFIT HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Generate Revenue and Profit", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Generate", font=('arial', 12, 'bold'), width=10,
                                command=lambda: self.makechange())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def reset(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()


def main():
    root = Tk()
    run = MainWindow(root)
    return


shopowner_ = json.load(open("./Data/LogInCredentials.json"))
shopowner = (shopowner_["name"], shopowner_["ID"], shopowner_["password"])
medicineInventory = json.load(open("./Data/MedicineInventory.json"))
vendorlist = json.load(open("./Data/vendorDetails.json"))

if __name__ == '__main__':
    main()

