class RetailItem:
	def GetInformation(self):
		print("RetailItem item # is " + self.ItemNum)
		print("RetailItem description is " + self.Desc)
		print("RetailItem units is " + self.Units)
		print("RetailItem price is " + self.Price)

RetailItem1 = RetailItem()
RetailItem1.ItemNum = "1"
RetailItem1.Desc = "Jacket"
RetailItem1.Units = "12"
RetailItem1.Price = "59.95"

RetailItem2 = RetailItem()
RetailItem2.ItemNum = "2"
RetailItem2.Desc = "Designer Jeans"
RetailItem2.Units = "40"
RetailItem2.Price = "34.95"

RetailItem3 = RetailItem()
RetailItem3.ItemNum = "3"
RetailItem3.Desc = "Shirt"
RetailItem3.Units = "20"
RetailItem3.Price = "24.95"



RetailItem1.GetInformation()

RetailItem2.GetInformation()

RetailItem3.GetInformation()