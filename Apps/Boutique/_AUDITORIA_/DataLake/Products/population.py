import csv
import random
import math

FIELDS = ['id', 'sku', 'name', 'material', 'percentage', 'sex', 'color', 'category', 'price', 'discount']

PRODUCTS = []

PK = 1

SKUS = set ()

SKU = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


MATERIAL = [
	"Cotton",

	"Denim",

	"Wool",

	"Leather",

	"Flannel",

	"Other",
]

PERCENTAGE = [ 100 ]

COLOR = [
	"Red",
	"Dark Blue",
	"Blue",
	"Green",
	"White",
	"Black",
	"Brown",
	"Orange",
	"Violet",
	"Purple",
	"Dark Red",
	"Dark Green",
	"Camel",
	"Yellow",
	"Other",
]

DISCOUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 20, 15, 10]



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Blazers                                                          #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Blazers"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Blazers

NAME = [
	
	"The RL67 Plaid Tweed Jacket",

	"The Iconic Doeskin Blazer",

	"The RL67 Jacket",

	"Wool Herringbone Tweed Waistcoat",

	"The RL67 Herringbone Jacket",

	"Polo Tailored Cashmere Blazer",

	"Polo Tailored Wool Flannel Blazer",

	"Polo Soft Tailored Chino Blazer",

	"The RL67 Herringbone Jacket",

	"Polo Soft Tailored Stretch Chino Jacket",

	"Polo Camel-Hair Blazer",

	"Polo Soft Tailored Chambray Suit Jacket",

	"Polo Modern Performance Twill Jacket",

	"Polo Soft Tailored Linen Suit Jacket",

	"The RL67 Linen Twill Jacket",

	"Polo Soft Tailored Seersucker Blazer",

	"Polo Soft Tailored Hemp Twill Jacket",

	"Tailored Washed Twill Suit Jacket",

	"Polo Modern Gabardine Blazer",

	"Polo Tailored Velvet Jacket",

	"Polo Modern Stretch Chino Suit Jacket",

	"The Iconic Doeskin Two-Button Blazer",

	"Modern Herringbone Blazer",

	"Polo Tailored Plaid Harris Tweed Jacket",

	"The RL67 Corduroy Jacket",

	"Polo Wool Twill Blazer",

	"The Pearson Twill Jacket",

	"Polo Modern Plaid Twill Sport Coat",

]

PRICE_MIN = 299
PRICE_MAX = 4950

# Samples
TOTAL = 88

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Cardigans                                                        #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Cardigans"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Cardigans

NAME = [
	
	"Snowflake Wool-Blend Cardigan",

	"The Polo Tartan Wool Cardigan",

	"Wool-Blend Letterman Cardigan",

	"Slub Fleece Letterman Cardigan",

	"Varsity-Inspired Cotton Cardigan",

	"Anchor Aran-Knit Cotton Cardigan",

	"Slim Fit Washable Wool V-Neck Cardigan",

	"Cable-Knit Wool-Cashmere Shawl Cardigan",

	"Cable-Knit Cotton Cardigan",

	"Aran-Knit Cotton Shawl-Collar Cardigan",

	"Aran-Knit Marled Cotton Cardigan",

	"Cable-Knit Wool-Cashmere Cardigan",

	"Suede-Patch V-Neck Cardigan",

	"Logo Wool V-Neck Cardigan",

	"Polo Ralph Lauren Yankees Cardigan",

	"Textured Wool-Cashmere Shawl Cardigan",

	"Cotton Letterman Cardigan",

	"Cashmere V-Neck Cardigan",

	"PRL x Naiomi Glasses Wrap Cardigan",

	"Cable-Knit Cashmere Shawl Cardigan",

	"PRL x Naiomi Glasses Wool Jacket",

	"Textured Cotton-Linen V-Neck Cardigan",

	"PRL x Naiomi Glasses Wrap Cardigan",

	"Cashmere Blazer Cardigan",

	"Cable-Knit Wool-Cashmere Cardigan",

	"Ralph Lauren Yankees Cashmere Cardigan",

	"Suede-Panel Cashmere Cardigan",

	"Double-Breasted Blazer Cardigan",

]

PRICE_MIN = 199
PRICE_MAX = 3450

# Samples
TOTAL = 49

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1




#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Casual Shirts                                                    #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Casual Shirts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Casual%20Shirts&allRefinementsRemoved=true

NAME = [
	
	"Custom Fit Plaid Double-Faced Shirt",

	"Classic Fit Skier-Snowflake Workshirt",

	"Classic Fit Polo Bear Oxford Shirt",

	"Classic Fit Plaid Knit Flannel Workshirt",

	"Custom Fit Brushed Oxford Shirt",

	"Classic Fit Plaid Flannel Shirt",

	"Custom Fit Plaid Twill Shirt",

	"Plaid Patchwork Fleece Shirt Jacket",

	"Custom Fit Checked Double-Faced Shirt",

	"Classic Fit Plaid Oxford Fun Shirt",

	"Custom Fit Plaid Brushed Oxford Shirt",

	"Classic Fit Foulard Oxford Camp Shirt",

	"Classic Fit Skier-Print Satin Camp Shirt",

	"Classic Fit Plaid Brushed Oxford Shirt",

	"Classic Fit Corduroy Camp Shirt",

	"Knit Oxford Shirt",

	"Classic Fit Glen Plaid Poplin Shirt",

	"Custom Fit Stretch Poplin Shirt",

	"Custom Fit Striped Stretch Poplin Shirt",

	"Slim Fit Striped Stretch Poplin Shirt",

	"Slim Fit Checked Stretch Poplin Shirt",

	"Jersey Spread-Collar Shirt",

	"Custom Fit Striped Stretch Oxford Shirt",

	"Custom Fit Double-Faced Shirt",

	"Custom Fit Gingham Stretch Poplin Shirt",

	"Custom Fit Indigo Chambray Shirt",

	"Custom Fit Plaid Performance Twill Shirt",

	"The Plaid Big Shirt",

	"Sheepskin Western Shirt",

	"Glen Plaid Linen Shirt",

	"Equestrian-Print Cashmere-Silk Shirt",

	"Plaid Wool-Cashmere Shirt",

	"Cotton-Cashmere Corduroy Shirt",

	"Patchwork Jacquard Workshirt",

]

PRICE_MIN = 129
PRICE_MAX = 2000

# Samples
TOTAL = 331

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Coats                                                            #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Coats"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Coats

NAME = [
	
	"Faux Fur-Trim Down Parka",

	"Polo Soft Tailored Wool-Blend Topcoat",

	"The Wainwright Down Coat",

	"Shearling-Collar Plaid Wool Ranch Coat",

	"Down Hooded Coat",

	"Packable Walking Coat",

	"Quilted Car Coat",

	"3-in-1 Twill Marsh Coat",

	"Polo Wool-Blend Melton Peacoat",

	"Wool Twill Toggle Coat",

	"Oilcloth Bike Coat",

	"The Pearson Car Coat & Liner Jacket",

	"PRL x Naiomi Glasses Great Ranch Coat",

	"Twill Car Coat",

	"The Polo Coat",

	"Wool Melton Polo Coat",

	"Lightweight Cotton-Blend Trench Coat",

	"Packable Walking Coat",

	"Performance Stretch Wool Car Coat",

	"Kent Handmade Wool-Cashmere Topcoat",

	"Shearling-Collar Leather-Yoke Jacket",

	"Leather-Yoke Sateen Parka",

	"Oilcloth Hooded Jacket",

	"Fringe Leather Jacket",

	"Moleskin Peacoat",

]

PRICE_MIN = 349
PRICE_MAX = 4950

# Samples
TOTAL = 37

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1




#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Formal Shirts                                                    #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Formal Shirts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Formal%20Shirts

NAME = [
	
	"Custom Fit French Cuff Tuxedo Shirt",

	"Slim Fit Poplin Shirt",

	"Custom Fit Poplin Shirt",

	"Custom Fit Striped Poplin Shirt",

	"Custom Fit Oxford Shirt",

	"Custom Fit Striped Dobby Shirt",

	"Custom Fit Monogram Oxford Shirt",

	"Regent Slim Fit Textured Shirt",

	"Custom Fit Plaid Poplin Shirt",

	"Regent Custom Fit Textured Shirt",

	"Custom Fit Checked Poplin Shirt",

	"Slim Fit Pinpoint Oxford Shirt",

	"Custom Fit French Cuff Tuxedo Shirt",

	"Classic Fit French Cuff Tuxedo Shirt",

	"Classic Fit Striped Shirt",

	"Regent Slim Fit Textured Shirt",

	"Custom Fit Indigo Chambray Shirt",

	"End-on-End Shirt",

	"Bengal-Stripe Shirt",

	"Stretch Jersey Shirt",

	"Herringbone Shirt",

	"Pique-Bib French Cuff Tuxedo Shirt",

	"Poplin French Cuff Shirt",

	"Slim Fit Striped Dobby Shirt",

]

PRICE_MIN = 139
PRICE_MAX = 950

# Samples
TOTAL = 70

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1


#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Hoodies                                                          #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Hoodies"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Hoodies

NAME = [
	
	"Polo Bear Fleece Hoodie",

	"P-Wing Fleece Hoodie",

	"Relaxed Fit Logo Fleece Hoodie",

	"The RL Fleece Plaid-Logo Hoodie",

	"The RL Fleece Hoodie",

	"The RL Fleece Logo Hoodie",

	"Double-Knit Hoodie",

	"Loopback Fleece Full-Zip Hoodie",

	"Pile Fleece Hybrid Hoodie",

	"Big Pony Loopback Fleece Hoodie",

	"Logo Fleece Hoodie",

	"Polo Sport Fleece Hoodie",

	"Vintage Fit Fleece Graphic Hoodie",

	"Polo Ball Hooded Jersey",

	"Vintage Fit Polo Ball Fleece Hoodie",

	"Double-Knit Hoodie",

	"Spa Terry Full-Zip Hoodie",

	"The RL Fleece Full-Zip Hoodie",

	"Double-Knit Full-Zip Hoodie",

	"Striped French Terry Full-Zip Hoodie",

]

PRICE_MIN = 149
PRICE_MAX = 1250

# Samples
TOTAL = 40

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1




#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Jackets                                                          #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Jackets"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Jackets

NAME = [
	
	"Pile Fleece Hybrid Jacket",

	"Faux-Fur-Trim Down Hooded Coat",

	"The Gorham Hybrid Down Jacket",

	"Wool-Blend Melton Topcoat",

	"Hybrid Fleece Jacket",

	"Plaid Wool Utility Jacket",

	"The Gorham Down Jacket",

	"The Gorham Down Gilet",

	"The Gorham Corduroy Down Jacket",

	"The Gorham Glossed Down Jacket",

	"The Colden Hybrid Jacket",

	"Leather-Trim Shearling Bomber Jacket",

	"Suede Jacket",

	"Suede Bomber Jacket",

	"Full-Zip Hooded Jacket",

	"Reversible Suede-Taffeta Hooded Jacket",

	"Reversible Suede-Taffeta Shirt Jacket",

	"P-Wing Sateen Coach's Jacket",

	"Twill Bi-Swing Jacket",

	"Pullover Hooded Jacket",

	"Suede Trucker Jacket",

	"Lightweight Field Jacket",

	"Garment-Dyed Oxford Overshirt",

	"Canvas Wading Jacket",

	"Deerskin Leather Gilet",

	"Ventile Jacket",
	
	"Bi-Swing Jacket",

	"Faille Hooded Jacket",
	
	"Double-Knit Bomber Jacket",

	"The Colden Packable Gilet",
	
	"Plaid Wool Waistcoat",

	"Water-Repellent Quilted Jacket",
	
	"The Beaton Quilted Utility Jacket",

	"The Colden Packable Jacket",
	
	"The Iconic Field Jacket",

	"The Colden Packable Gilet",
	
	"Quilted Down Hooded Gilet",

	"Shearling-Collar Down Bomber Jacket",
	
	"The Hartland Down Shirt Jacket",

	"The Iconic Field Jacket",

	"The Gorham Colour-Blocked Down Jacket",


]

PRICE_MIN = 179
PRICE_MAX = 5950

# Samples
TOTAL = 218

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Jeans                                                            #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Jeans"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Jeans

NAME = [
	
	"Parkside Active Taper Selvedge Jean",

	"Sullivan Slim Stretch Jean",

	"Heritage Straight Distressed Jean",

	"Heritage Straight Jean",

	"Varick Slim Straight Stretch Jean",

	"Sullivan Slim Polo Pony Stretch Jean",

	"Vintage Classic Distressed Jean",

	"PRL x Naiomi Glasses Indigo Jean",

	"PRL x Naiomi Glasses Jean",

	"Denim Overall",

	"Sullivan Slim Stretch Jean",

	"PRL x Naiomi Glasses Garment-Dyed Jean",

	"Eldridge Skinny Stretch Jeans",

	"PRL x Naiomi Glasses Embroidered Jean",

	"Prospect Straight Stretch Jean",

	"Slim Fit Stretch Moleskin Trouser",

	"Stretch Skinny Jean",

]

PRICE_MIN = 139
PRICE_MAX = 850

# Samples
TOTAL = 88

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Joggers                                                          #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Joggers"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Joggers

NAME = [
	
	"The RL Fleece Big Pony Jogging Bottoms",

	"Slub Fleece Graphic Tracksuit Bottoms",

	"Loopback Fleece Tracksuit Bottoms",

	"Double-Knit Jogging Bottom",

	"Loopback Fleece Drawstring Trouser",

	"Double-Knit Mesh Jogger",

	"The RL Fleece Tracksuit Bottoms",

	"Double-Knit Joggers",

	"Double-Knit Track Trouser",

	"Logo Fleece Jogging Bottoms",

	"Relaxed Fit Logo Fleece Tracksuit Bottom",

	"Double-Knit Mesh Jogging Bottom",

	"Polo Sport Fleece Joggers",

	"Waffle Washable Cashmere Jogging Bottoms",

	"Pink Pony Warm-Up Trouser",

	"Pink Pony Tracksuit Bottoms",

	"Polo Sport Fleece Joggers",

	"Water-Repellent Racing Trouser",

]

PRICE_MIN = 129
PRICE_MAX = 990

# Samples
TOTAL = 37

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Jumpers                                                          #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Jumpers"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Jumpers

NAME = [
	
	"Polo Bear Jumper",

	"Snowflake Wool Rollneck Jumper",

	"Dog-Intarsia Cashmere Jumper",

	"Soft Cotton Roll Neck",

	"Polo Bear Family Jumper",

	"Snowflake Cotton-Cashmere Jumper",

	"Plaid Patchwork Wool-Blend Jumper",

	"Colour-Blocked Cotton Shawl Jumper",

	"Cotton Crewneck Jumper",

	"Cable-Knit Wool-Cashmere Jumper",

	"Cable Wool-Cashmere Roll neck Jumper",

	"Wool-Alpaca Fisherman’s Jumper",

	"Hooded Jumper",

	"Striped Waffle-Knit Crewneck",

	"Reindeer-Patterned Wool Jumper",

	"Aran Wool-Alpaca Quarter-Zip Jumper",

	"Soft Cotton Roll Neck",

	"Washable Cashmere Hooded Jumper",

	"Textured Cotton Crewneck Jumper",

	"NYC Washable Wool-Blend Jumper",

	"Wool-Blend Roll Neck Jumper",

	"The Iconic Cricket Jumper",

	"Textured Cotton Full-Zip Jumper",

	"Waffle Wool-Cotton Quarter-Zip Jumper",

	"Mesh-Knit Cotton Crewneck Jumper",

	"Washable Wool Full-Zip Gilet",

	"NYC Cotton-Linen Jumper",

	"Fair Isle Indigo Cotton Sleeveless Jumper",

	"Cotton-Blend Fisherman's Jumper",

	"Mesh-Knit Cotton Quarter-Zip Jumper",

	"Cable-Knit Cotton Jumper",

	"Bullion-Patch Cashmere Jumper",

]

PRICE_MIN = 129
PRICE_MAX = 3450

# Samples
TOTAL = 178

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Polo Shirts                                                      #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Polo Shirts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Polo%20Shirts

NAME = [
	
	"Classic Fit Polo Bear Mesh Polo Shirt",

	"Classic Fit Skier-Print Mesh Polo Shirt",

	"Classic Fit Crest Mesh Polo Shirt",

	"Slim Fit Stretch Mesh Polo",

	"Custom Slim Fit Soft Cotton Polo Shirt",

	"Custom Slim Fit Stretch Mesh Polo Shirt",

	"Original Fit Mesh Polo Shirt",

	"Classic Fit Tennis-Crest Mesh Polo Shirt",

	"Classic Fit Stretch Mesh Polo Shirt",

	"Custom Slim Fit Printed Mesh Polo Shirt",

	"Standard Fit Striped Jersey Polo Shirt",

	"Custom Slim Fit Printed Mesh Polo Shirt",

	"Classic Fit Garment-Dyed Polo Shirt",

	"Slim Fit Mesh Polo Shirt",

	"The Iconic Mesh Polo Shirt",

	"Custom Slim Fit Mesh Polo Shirt",

	"Luxury Jersey Polo Shirt",

	"Slim Fit Mesh Long-Sleeve Polo",

	"Custom Slim Fit Soft Cotton Polo Shirt",

	"Classic Fit Knit Corduroy Polo Shirt",

	"Classic Fit Stretch Mesh Zip Polo Shirt",

	"Slim Fit Mesh Long-Sleeve Polo Shirt",

	"Classic Fit Mesh Polo Shirt",

	"Indigo-Dyed Mesh Polo Shirt",

	"Mesh-Knit Cotton Crewneck Jumper",

	"Lisle Long-Sleeve Polo Shirt",

	"The Polo Tartan Polo Shirt",

	"Classic Fit Polo Bear Mesh Polo Shirt",

	"Custom Slim Plaid-Trim Mesh Polo Shirt",

	"The Polo Big Shirt",

	"Custom Slim Duck-Print Mesh Polo Shirt",

	"Classic Fit Leather-Pony Mesh Polo Shirt",

	"Classic Fit Dog-Embroidered Polo Shirt",

]

PRICE_MIN = 109
PRICE_MAX = 450

# Samples
TOTAL = 143

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Shorts                                                           #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Shorts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Shorts

NAME = [
	
	"15.2 cm Polo Prepster Corduroy Short",

	"15 cm Polo Prepster P-Wing Short",

	"19 cm P-Wing Terry Short",

	"16.5 cm Relaxed Heavyweight Fleece Short",

	"12.7 cm Cormac Relaxed Fit Pleated Short",

	"20.3 cm Classic Fit Canvas Aviator Short",

	"16.5 cm Loopback Fleece Short",

	"15 cm Polo Prepster Corduroy Short",

	"20.3 cm Stretch Straight Fit Chino Short",

	"26.7 cm Classic Fit Twill Cargo Short",

	"15-cm Polo Prepster Stretch Chino Short",

	"15.2 cm Polo Prepster Corduroy Short",

	"24-cm Stretch Slim Fit Chino Short",

	"16.5 cm Relaxed Fit Logo Fleece Short",

	"15.2-cm Polo Prepster Chino Short",

	"14 cm Relaxed Fit Carpenter Short",

	"23 cm Double-Knit Short",

	"20.3 cm Stretch Straight Fit Chino Short",

	"20.3-cm Polo Sport Fleece Short",

	"12.5 cm Stretch Classic Fit Chino Short",

	"Stretch Classic Fit Short",

	"20.3 cm Stretch Straight Fit Chino Short",

	"US Open 14 cm Terry Short",

	"19-cm Terry Drawstring Short",

]

PRICE_MIN = 99
PRICE_MAX = 490

# Samples
TOTAL = 51

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Suits                                                            #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Suits"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Suits

NAME = [
	
	"Polo Tailored Velvet Suit",

	"Polo Tailored Wool Sharkskin Suit",

	"Polo Tailored Wool Twill Suit",

	"Polo Tailored Wool Barathea Peak Tuxedo",

	"Polo Tailored Wool Barathea Peak Tuxedo",

	"Polo Tailored Silk-Linen Hopsack Suit",

	"Polo Lightweight Wool 3-Piece Suit",

	"Polo Tailored Chalk-Stripe Flannel Suit",

	"Polo Tailored Linen Tuxedo",

	"Gregory Hand-Tailored Wool Serge Suit",

	"Gregory Hand-Tailored Wool Peak Tuxedo",

	"Gregory Barathea Peak Tuxedo",

	"Gregory Handmade Barathea Shawl Tuxedo",

	"Kent Hand-Tailored Wool Serge Suit",

	"Kent Hand-Tailored Pinstripe Wool Suit",

	"Kent Hand-Tailored Birdseye Suit",

	"Gregory Hand-Tailored Nailhead Wool Suit",

	"Gregory Hand-Tailored Sharkskin Suit",

	"Kent Hand-Tailored Plaid Cashmere Suit",

	"Kent Hand-Tailored Pin Dot Wool Suit",

]

PRICE_MIN = 999
PRICE_MAX = 5950

# Samples
TOTAL = 18

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Sweatshirts                                                      #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Sweatshirts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Sweatshirts

NAME = [
	
	"Polo Bear Fleece Hybrid Hoodie",

	"Polo Bear Fleece Sweatshirt",

	"Snowflake Brushed Fleece Pullover",

	"The RL Fleece Full-Zip Hoodie",

	"The RL Fleece Sweatshirt",

	"Plaid Patchwork-Print Fleece Hoodie",

	"Plaid Soft Cotton Roll Neck",

	"Plaid Pile Fleece Hybrid Jacket",

	"Skier-Print Brushed Fleece Pullover",

	"Colour-Blocked Brushed Fleece Pullover",

	"Double-Knit Mesh Quarter-Zip Pullover",

	"Graphic Fleece Quarter-Zip Sweatshirt",

	"Crest Fleece Collared Sweatshirt",

	"P-Wing Fleece Collared Sweatshirt",

	"The Bayport P-Wing Fleece Jacket",

	"Slub Fleece Graphic Sweatshirt",

	"Double-Knit Track Jacket",

	"Triple-Pony Fleece Baseball Jacket",

	"Vintage Fit Graphic Fleece Sweatshirt",

	"Loopback Fleece Hoodie",

	"Double-Knit Full-Zip Hoodie",

	"Estate-Rib Quarter-Zip Pullover",

	"Double-Knit Pullover",

	"Double-Knit Sweatshirt",

	"Logo Pile Fleece Hoodie",

	"Big Fit Heavyweight Fleece Hoodie",

	"Loopback Fleece Sweatshirt",

	"Polo Sport Fleece Full-Zip Hoodie",

	"Double-Knit Quarter-Zip Pullover",

	"Double-Knit Track Jacket",

	"Polo Bear Double-Knit Sweatshirt",

	"Relaxed Fit Logo Collared Sweatshirt",

	"Luxury Jersey Quarter-Zip Pullover",

	"The Ralph Hoodie",

	"Vintage Fit Fleece Graphic Sweatshirt",

	"Marled Double-Knit Sweatshirt",

	"Pink Pony Relaxed Fit Hoodie",
]

PRICE_MIN = 135
PRICE_MAX = 249

# Samples
TOTAL = 147

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1




#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - T-Shirts                                                         #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["T-Shirts"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=T-Shirts

NAME = [
	
	"Classic Fit Polo Bear Jersey T-Shirt",

	"Classic Fit Logo Jersey T-Shirt",

	"Moleskin Henley Shirt",

	"Custom Slim Fit Soft Cotton T-Shirt",

	"Classic Fit Jersey Graphic T-Shirt",

	"Classic Fit Jersey Pocket T-Shirt",

	"Classic Fit Crest Jersey T-Shirt",

	"Classic Fit Heavyweight Jersey T-Shirt",

	"Classic Fit Logo Slub Jersey T-Shirt",

	"Classic Fit Polo Bear Jersey T-Shirt",

	"Standard Fit Striped Jersey T-Shirt",

	"Classic Fit Plaid-Logo Jersey T-Shirt",

	"Classic Fit Striped Slub Jersey Shirt",

	"Classic Fit Jersey Crewneck T-Shirt",

	"Classic Fit Jersey Long-Sleeve T-Shirt",

	"Classic Fit Jersey Pocket T-Shirt",

	"Custom Slim Fit Soft Cotton T-Shirt",

	"Classic Fit Polo Sport Pocket T-Shirt",

	"Classic Fit Jersey Long-Sleeve T-Shirt",

	"Classic Fit Stretch Mesh T-Shirt",

	"Classic Fit Jersey V-Neck T-Shirt",

	"Big Fit Heavyweight Jersey T-Shirt",

	"Custom Slim Fit Jersey Crewneck T-Shirt",

	"Classic Fit Logo Jersey T-Shirt",

	"Men's Cotton Jersey Tee",
]

PRICE_MIN = 65
PRICE_MAX = 129

# Samples
TOTAL = 138

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Man - Trousers                                                         #
#																															#
#############################################################################################################################


SEX = ["Man"]

CATEGORY = ["Trousers"]

# https://www.ralphlauren.pt/en/men/clothing/1020?prefn1=CategoryCode&prefv1=Trousers

NAME = [
	
	"The Big Corduroy Trouser",

	"Relaxed Fit Corduroy Cargo Trouser",

	"Velvet Trouser",

	"Plaid Wool Suit Trouser",

	"Sullivan Slim Knitlike Chino Trouser",

	"Pleated Wool Flannel Trouser",

	"Stretch Straight Fit Chino Trouser",

	"Stretch Slim Fit Chino Trouser",

	"Jarrett Stretch Slim Fit Sateen Trouser",

	"Slim Fit Wool Twill Trouser",

	"Garment-Dyed Stretch Chino Suit Trouser",

	"Chambray Suit Trouser",

	"Stretch Chino Suit Trouser",

	"Stretch Slim Fit Knitlike Cargo Trouser",

	"Performance Stretch Twill Suit Trouser",

	"Pleated Linen Trouser",

	"Stretch Slim Fit Chino Trouser",

	"Pleated Knit Mesh Trouser",

	"Pleated Linen Trouser",

	"Pleated Double-Knit Suit Trouser",

	"Whitman Relaxed Fit Pleated Trouser",

	"Polo Prepster Classic Fit Oxford Trouser",

	"The Big Chino",

	"Linen Trouser",

	"Double-Knit Cargo Jogger",
]

PRICE_MIN = 139
PRICE_MAX = 550

# Samples
TOTAL = 143

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Blazers                                                         #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Blazers"]


# https://www.ralphlauren.pt/en/Women/clothing/2020?prefn1=CategoryCode&prefv1=Blazers

NAME = [

	"Plaid Wool Twill Blazer",

	"Sequinned Stand-Collar Blazer",

	"Silk-Blend Velvet Blazer",

	"Long Velvet Waistcoat",

	"Buttoned Wool Jacket",

	"Double-Knit Jacquard Blazer",

	"Double-Breasted Wool-Blend Blazer",

	"Silk-Lapel Double-Breasted Wool Blazer",

	"Silk-Lapel Velvet Cropped Blazer",

	"Double-Breasted Wool-Blend Blazer",

	"Double-Breasted Crest Blazer",

	"Double-Breasted Stretch-Wool Blazer",

	"Double-Breasted Blazer",

	"Linen-Blend Herringbone Hacking Blazer",

	"Patchwork Herringbone Tweed Blazer",

	"Glen Plaid Tweed Blazer",

	"Lambskin Hacking Blazer",

	"Herringbone Wool Blazer",

	"Plaid Double-Breasted Satin-Trim Blazer",
	
    "Double-Breasted Wool Crepe Blazer",

	"Double-Breasted Satin-Trim Crepe Blazer",

	"Wool-Blend Herringbone Tweed Blazer",

	"Glen Check Double-Breasted Wool Blazer",

	"Glen Plaid Belted Wool-Blend Blazer",

	"Bullion Jacquard Blazer",

	"Metallic-Trim Twill Jacket",

	"Double-Breasted Canvas Cropped Blazer",

	"Camden Cashmere Jacket",

	"Camden Linen Jacket",

	"Wilmington Double-Faced Wool Jacket",
	
    "Madelena Lambskin Jacket",

]

PRICE_MIN = 294
PRICE_MAX = 3100

# Samples
TOTAL = 91

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                    Woman's - Coats                                                        #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Coats"]


# https://pt.sacoorbrothers.com/en/collections/jacket-man
# https://www.ralphlauren.pt/en/men/clothing/jackets-coats/10205

NAME = [
	
	"Quilted Jacket",
	
	"Quilted Coat"

	"Reversible Quilted Barn Coat",

	"Quilted Leather Bomber Jacket",

	"Velvet Quilted Down Jacket",

	"Cable-Knit Hooded Down Coat",

	"Belted Plaid Wool Herringbone Coat",

	"Wool Melton Long Coat",

	"Leather-Sleeve Bomber Jacket",

	"Cotton Canvas Utility Jacket",

	"Plaid Quilted Down Jacket",

	"Houndstooth Quilted Down Jacket",

	"Embroidered Patch Insulated Jacket",

	"Water-Resistant Packable Hooded Jacket",

	"Water-Repellent Quilted Down Jacket",

	"Water-Repellent Packable Gilet",

	"Packable Water-Repellant Quilted Gilet",

	"Packable Quilted Jacket",

	"Single-Breasted Wool Coat",

	"Double-Faced Wool Wrap Coat",

	"Plaid Wool Twill Trench Coat",
	
    "Camel-Hair Twill Long Polo Coat",
	
    "Sheepskin Leather Moto Jacket",
	
    "Corduroy Windbreaker Jacket",
	
    "Cotton Canvas Jacket",
	
    "Cotton Twill Field Jacket",
	
    "Embroidered Patch Denim Trucker Jacket",
	
    "Logo Satin Bomber Jacket",
	
    "Embroidered Bomber Jacket",
	
    "Camel-Hair Twill Long Polo Coat",
	
    "PRL x Naiomi Glasses Wool Coat",
	
    "Logo Fleece Baseball Jacket",
]

PRICE_MIN = 119
PRICE_MAX = 4119

# Samples
TOTAL = 158

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Dresses                                                         #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Dresses"]


NAME = [

	"Sequinned Long-Sleeve Polo Dress",

	"Velvet Scoopback Dress",

	"Inset-Lace Georgette Dress",

	"Sequinned Scoopneck Dress",

	"Plaid Crinkled Slip Dress",

	"Keyhole Jersey Halter Dress",

	"Belted Plaid Cotton-Blend Dress",

	"Shirred-Yoke Oxford Shirtdress",

	"Poplin Tuxedo Shirtdress",

	"Georgette Tie-Neck Dress",

	"Plaid A-Line Shirtdress",

	"Double-Faced Zip-Front Flight Suit",

	"Striped Waffle-Knit Dress",

	"Cashmere Crewneck Jumper Dress",

	"Fair Isle Wool-Blend Jumper Dress",

	"Wool-Blend Roll Neck Dress",

	"Polo Jumper-Bodice Midi Dress",

	"Pleated Sleeveless Mockneck Dress",

	"Lace-Trim Cotton Voile Dress",
	
    "Floral Ruffle-Trim Georgette Dress",

	"Satin Midi Slip Dress",

	"Floral Georgette Tie-Neck Dress",

	"Floral Silk Crepe Dress",

	"Belted Striped Cotton Shirtdress",

	"Tiered Cotton Shirtdress",

	"Cable-Knit Short-Sleeve Jumper Dress",

	"Wool-Blend Roll Neck Dress",

	"Jumper-Bodice Long-Sleeve Dress",

	"Panelled Cotton Shirtdress",

	"PRL x Naiomi Glasses Wool-Blend Dress",
	
    "Metallic Knit Twist-Front Gown",
	
    "Metallic Off-the-Shoulder Cocktail Dress",
	
    "Belted Faille & Jersey Cocktail Dress",
	
    "Ruffle-Trim Sequined Cocktail Dress",
	
    "Jersey Off-the-Shoulder Gown",
	
    "Stretch Jersey Sleeveless Gown",
	
    "Jersey One-Shoulder Gown",
	
]

PRICE_MIN = 380
PRICE_MAX = 5960

# Samples
TOTAL = 338

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Hoodies & Sweatshirts                                           #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Hoodies & Sweatshirts"]


NAME = [

	"Logo Fleece Mockneck",

	"Logo Fleece High-Crewneck",

	"Fleece Crewneck Sweatshirt",

	"Polo Bear Fleece Hoodie",

	"Polo Bear Fleece Crewneck",

	"Fleece Pullover Hoodie",

	"Polo-Collar Fleece Pullover",

	"Logo Crest Lightweight Fleece Mockneck",

	"High-Pile Fleece Graphic Zip Jacket",

	"Nautical Logo Fleece Crewneck",

	"Logo & Wave Graphic Fleece Hoodie",

	"Shrunken Fit Fleece Hoodie",

	"Fleece Full-Zip Hoodie",

	"Logo Flag Oversize Fleece Hoodie",

	"Bullion-Crest Fleece Pullover",

	"Double-Knit Jacquard Half-Zip Hoodie",
	
	"US Open Chevron French Terry Hoodie",
	
    "US Open Lightweight Fleece V-Neck",
	
    "Polo Bear Fleece Crewneck",
	
    "High-Pile Fleece Quarter-Zip",
	
    "Stretch Velvet Off-the-Shoulder Blouse",

]


PRICE_MIN = 99
PRICE_MAX = 420

# Samples
TOTAL = 60

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1







#############################################################################################################################
#																													        #
# 																													        #
#                                                    Woman's - Jackets & Coats                                              #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Jackets & Coats"]


NAME = [
	
	"Quilted Jacket",
	
	"Quilted Coat"

	"Reversible Quilted Barn Coat",

	"Quilted Leather Bomber Jacket",

	"Velvet Quilted Down Jacket",

	"Cable-Knit Hooded Down Coat",

	"Belted Plaid Wool Herringbone Coat",

	"Wool Melton Long Coat",

	"Leather-Sleeve Bomber Jacket",

	"Cotton Canvas Utility Jacket",

	"Plaid Quilted Down Jacket",

	"Houndstooth Quilted Down Jacket",

	"Embroidered Patch Insulated Jacket",

	"Water-Resistant Packable Hooded Jacket",

	"Water-Repellent Quilted Down Jacket",

	"Water-Repellent Packable Gilet",

	"Packable Water-Repellant Quilted Gilet",

	"Packable Quilted Jacket",

	"Single-Breasted Wool Coat",

	"Double-Faced Wool Wrap Coat",

	"Plaid Wool Twill Trench Coat",
	
    "Camel-Hair Twill Long Polo Coat",
	
    "Sheepskin Leather Moto Jacket",
	
    "Corduroy Windbreaker Jacket",
	
    "Cotton Canvas Jacket",
	
    "Cotton Twill Field Jacket",
	
    "Embroidered Patch Denim Trucker Jacket",
	
    "Logo Satin Bomber Jacket",
	
    "Embroidered Bomber Jacket",
	
    "Camel-Hair Twill Long Polo Coat",
	
    "PRL x Naiomi Glasses Wool Coat",
	
    "Logo Fleece Baseball Jacket",
]

PRICE_MIN = 320
PRICE_MAX = 5900

# Samples
TOTAL = 221

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1


#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Jumpsuits                                                       #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Jumpsuits"]


NAME = [

	"Double-Faced Zip-Front Flight Suit",

	"Cape Georgette One-Shoulder Jumpsuit",

	"Chain-Trim Stretch Jersey Jumpsuit",

	"Satin-Trim Crepe Sleeveless Jumpsuit",

	"Belted Cape Georgette Jumpsuit",

	"Cape Georgette One-Shoulder Jumpsuit",

	"Satin-Trim Crepe Sleeveless Jumpsuit",

	"Twist-Front Jersey One-Shoulder Jumpsuit",

	"Belted Jersey Twist-Front Jumpsuit",

	"Belted Cape Georgette Jumpsuit",

	"Eve Crepe-Back-Satin Jumpsuit",

	"Mélange Wool Jersey Roll Neck Jumpsuit",

	"Woven Cape One-Shoulder Jumper Jumpsuit",

	"Embroidered Crepe Wide-Leg Jumpsuit",

	"Robynne Denim Overall",

	"Linen-Cotton Dobby Coverallr",

	"Indigo Floral-Print Jersey Jumpsuit",
]


PRICE_MIN = 99
PRICE_MAX = 420

# Samples
TOTAL = 25

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1


#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Knitwear                                                        #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Knitwear"]

NAME = [

	"Snowflake-Motif Wool Crewneck Jumper",

	"Plaid Alpaca-Blend Crewneck Jumper",

	"Classic Fit Cable Wool-Cashmere Jumper",

	"Plaid Alpaca-Blend Short-Sleeve Jumper",

	"Fair Isle Alpaca-Blend Cardigan",

	"Striped Cable Wool-Cashmere Cardigan",

	"Aran-Knit Wool-Alpaca Roll Neck",

	"Anchor Logo Cable Cashmere Cardigan",

	"Wool Hooded Jumper",

	"Snowflake-Motif Shawl-Collar Cardigan",

	"Polo Bear Cotton Crewneck Jumper",

	"Sequinned Wool-Cashmere Cricket Jumper",

	"Classic Fit Cable Wool-Cashmere Jumper",

	"Cable-Knit Wool-Cashmere V-Neck Jumper",

	"Cropped Cable Wool-Cashmere Jumper",

	"Slim Fit Cashmere Rollneck",

	"Cable-Knit Cotton Crewneck Jumper",

	"Polo Bear Wool-Cashmere Jumper",

	"Cable-Knit Cashmere Jumper",
	
    "Cable-Knit Wool-Cashmere Cardigan",

	"Cable-Knit Wool-Cashmere Cricket Jumper",

	"Cable-Knit Wool-Cashmere V-Neck Jumper",

	"Fair Isle Wool Half-Zip Jumper",

	"Wool Shawl-Collar Cardigan",

	"Fair Isle Wool-Blend Jumper",

	"Logo Crest Wool Crewneck Jumper",

	"Cable-Knit Wool-Blend Crewneck Jumper",

	"Polo Bear Cotton Crewneck Jumper",

	"Aran-Knit Crewneck Jumper",

	"Flag Cotton Crewneck Jumper",
	
    "Cashmere Short-Sleeve Crewneck Jumper",
	
    "Aran-Knit Wool-Blend Crewneck Jumper",
	
    "Pointelle Linen Cardigan",
	
    "Striped Short-Sleeve Jumper",
	
    "Cable Wool-Cashmere Sleeveless V-Neck",
	
    "Cotton Crewneck Jumper",
	
    "Polo Bear French Terry Cardigan",
	
    "Intarsia-Knit Jacquard Cardigan",
	
    "Palm-Tree-Motif Cable Cotton Jumper",
	
    "Short-Sleeve Cotton Cricket Jumper",
	
    "The Ralph & Ricky Bear Jumper",
	
    "Polo Bear Cotton Crewneck Jumper",
	
    "Wimbledon Cable-Knit Cotton Jumper",
	
    "Polo Bear Wool-Cashmere Knit Hoodie",
	
    "Cable-Knit Cotton Cricket Jumper",
	
    "Wool-Blend Shawl Cardigan",
	
    "Geo-Motif Wool-Blend Jumper",
	
    "Cashmere Roll Neck Jumper",
	
    "Polo Bear Cotton Roll-Neck Jumper",
	
    "PRL x Naiomi Glasses Wool-Blend Jumper",
]

PRICE_MIN = 120
PRICE_MAX = 480

# Samples
TOTAL = 261

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1

#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Polo Shirts                                                     #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Polo Shirts"]

NAME = [

	"Cable Wool-Cashmere Polo Shirt",

	"Lace-Up Long-Sleeve Polo Shirt",

	"Buttoned-Placket Polo Shirt",

	"Slim Fit Cashmere Polo Shirt",

	"Slim Fit Stretch Polo Shirt",

	"Cable-Knit Cropped Polo Shirt",

	"US Open Tailored Fit Polo Shirt",

	"PRL x Naiomi Glasses Mesh Polo Shirt",

	"Piqué Polo Shirt",

	"Print Stretch Piqué Polo Shirt",

	"Belting-Print Stretch Piqué Polo Shirt",

	"Beaded-Crest Stretch Velvet Polo Shirt",

	"Slim Fit Rib-Knit Long-Sleeve Polo Shirt",

	"Classic Fit Tour Polo Shirt",

	"Tailored Fit Polo Bear Polo Shirt",

	"Tailored Fit Stretch Jersey Polo Shirt",
	
	"Patchwork piquÃ© Polo Shirt",

]

PRICE_MIN = 120
PRICE_MAX = 710

# Samples
TOTAL = 34

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1

#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Shirts & Blouses                                                #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Shirts & Blouses"]


NAME = [

	"Cotton Jacquard Overshirt",

	"Plaid Cotton Twill Workshirt",

	"Ruffled-Collar Blouse",

	"Slim Fit Oxford Shirt",

	"Slim Fit Knit Cotton Oxford Shirt",

	"Striped Knit Oxford Shirt",

	"Slim Fit Silk Shirt",

	"Oversize Fit Cotton Shirt",

	"Stretch Slim Fit Cotton Shirt",

	"Relaxed Fit Striped Cotton Shirt",

	"Patchwork Overshirt",

	"Classic Fit Corduroy Shirt",

	"Cropped Boxy Denim Shirt",

	"Linen Popover Shirt",

	"Linen Blouse",

	"Oversize Fit Striped Silk Shirt",

	"Floral Drawstring Cotton Top",

	"Lace Blouse",

	"Extended-Cuff Cotton Shirt",
	
    "Wimbledon Classic Fit Twill Shirt",

	"PRL x Naiomi Glasses Silk Western Shirt",

	"PRL x Naiomi Glasses Floral Shirt",

	"Slim Fit Cotton Oxford Shirt",

	"Satin Charmeuse Off-the-Shoulder Blouse",

	"Stretch Velvet Off-the-Shoulder Blouse",

	"Plaid Chain-Trim Charmeuse Halter Blouse",

	"Cutout Satin Charmeuse Blouse",

	"Bib-Front Cotton Broadcloth Shirt",

	"Ruffle-Trim Georgette Blouse",

	"Floral Satin Charmeuse Tie-Neck Blouse",
	
    "Satin Charmeuse Surplice Blouse",
	
    "Pleated Georgette Blouse",
	
    "Classic Fit Print Cotton Voile Shirt",
	
    "Slim Fit Belting-Print Jersey Shirt",
	
    "Classic Fit Print Crepe Shirt",
	
    "Ruffle-Trim Short-Sleeve Shirt",
	
    "Belting-Print Georgette Tie-Neck Blouse",

]


PRICE_MIN = 99
PRICE_MAX = 420

# Samples
TOTAL = 182

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1



#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Skirts                                                          #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Skirts"]



NAME = [

	"Wool Crepe Wrap Skirt",

	"Metallic Velvet Bias-Cut Skirt",

	"Sequinned Stretch Mesh Skirt",

	"Plaid Alpaca-Blend Flared Skirt",

	"Plaid Wool-Blend Wrap Skirt",

	"Wool Crepe Buttoned Skirt",

	"Plaid Pleated Wool Short",

	"Double-Faced Satin Skirt",

	"Silk Charmeuse Skirt",

	"Pleated Georgette Skirt",

	"Fringe-Trim Plaid Wrap Skirt",

	"Cashmere-Blend Flared Skirt",

	"Deconstructed Patchwork Denim Skirt",

	"Cable-Knit A-Line Skirt",

	"Logo Flag Fleece Drawstring Short",

	"Wimbledon Performance Pleated Skort",

	"PRL x Naiomi Glasses Cotton Maxiskirt",

	"Plaid Pleated Wrap Skirt",

	"Pleated Cotton Chambray Short",
	
    "PRL x Naiomi Glasses Wool-Blend Skirt",

	"PRL x Naiomi Glasses Silk Maxiskirt",

	"Satin Charmeuse Midi Skirt",

	"Pleated Satin Charmeuse Skirt",

	"Velvet A-Line Skirt",

	"Floral Crinkle Georgette Tiered Skirt",

	"Paisley Satin Charmeuse Miniskirt",

	"Glen Plaid Wool-Blend Pencil Miniskirt",

	"Denim Skirt",

	"Floral Knit Cotton Wrap Skirt",
	
    "38.1 cm Plaid Pleated Performance Skort",

]


PRICE_MIN = 119
PRICE_MAX = 960

# Samples
TOTAL = 84

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1

#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - T-Shirts & Tops                                                 #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["T-Shirts & Tops"]


NAME = [

	"Cotton Jersey Crewneck T-Shirt",

	"Cotton Jersey V-Neck T-Shirt",

	"Sequinned Mesh Roll Neck",

	"Logo Sequined Jersey",

	"Anchor Logo Cotton Jersey T-Shirt",

	"Rib-knit Cotton Long-Sleeve T-Shirt",

	"Striped Boatneck Mariner Tee",

	"Rib-Knit Cotton Tank",

	"Silk Camisole",

	"Striped Rib-Knit Cotton Crewneck T-Shirt",

	"Polo Bear Cotton Jersey T-Shirt",

	"Sueded Jersey Cropped Tank",

	"PRL x Naiomi Glasses Velvet Boatneck Top",

	"Beaded Mesh Sleeveless Top",

	"Beaded Cotton Jersey T-Shirt",

	"Stretch Velvet Off-the-Shoulder Blouse",

	"Embellished Jersey One-Shoulder Top",

	"Cotton-Blend Off-the-Shoulder Top",

	"Striped Boatneck Top",
	
    "Jersey Roll Neck",

	"Stretch Cotton Balloon-Sleeve Tee",

	"Paisley Sequinned Mesh Sleeveless Top",

	"Floral Stretch Jersey Tie-Neck Top",

	"Floral Stretch Cotton Boatneck T-shirt",

	"Eyelet Slub Jersey Boatneck Tee",

	"Cotton-Blend Tank Top",

	"Print Stretch Cotton Boatneck T-Shirt",

	"Striped Stretch Cotton Crewneck Tee",

	"Fringe-Trim Sheer & Opaque Knit Top",

	"Metallic Jersey Long-Sleeve Top",
	
    "Metallic Jersey Twist-Shoulder Tank Top",

]


PRICE_MIN = 99
PRICE_MAX = 420

# Samples
TOTAL = 114

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1


#############################################################################################################################
#																													        #
# 																													        #
#                                                   Woman - Trousers                                                        #
#																															#
#############################################################################################################################


SEX = ["Woman"]

CATEGORY = ["Trousers"]


NAME = [

	"Metallic Velvet Wide-Leg Trouser",

	"The Lambskin Side-Zip Trouser",

	"Silk-Blend Velvet Blazer",

	"Lambskin Relaxed Straight Trouser",

	"Plaid Wool Relaxed Straight Trouser",

	"Wool Wide-Leg Tuxedo Trouser",

	"Satin Wide-Leg Trouser",

	"Fleece Tracksuit bottoms",

	"Nautical Logo Fleece Tracksuit Bottoms",

	"Hemp Wide-Leg Trouser",

	"Wool Crepe Wide-Leg Trouser",

	"Wool-Blend Wide-Leg Trouser",

	"Stretch-Cotton Velvet Wide-Leg Trouser",

	"Wide-Leg Pinstripe Twill Trouser",

	"Suede-Wool Wide-Leg Trouser",

	"Wool-Blend Tweed Tapered Trouser",

	"High-Rise Relaxed Straight Trouser",

	"Pleated Straight-Leg Trouser",

	"The Ricky Trouser",
	
    "Cotton Sateen Utility Trouser",

	"Cotton Sateen Utility Trouser",

	"Cropped Slim Fit Twill Chino Trouser",

	"Chambray Cargo Trouser",

	"Fleece Athletic Trousers",

	"Sueded Jersey Legging",

	"Lambskin 5-Pocket Super-Slim Trouser",

	"Wool-Blend Tweed Curved Tapered Trouser",

	"PRL x Naiomi Glasses Wool Trouser",

	"High-Rise Stretch Velvet Boot Trouser",

	"Cotton Sateen Cargo Trouser",
	
    "Chain-Trim Pleated Wide-Leg Trouser",
	
	"Glen Check Pleated Stretch Wool Trouser",

]

PRICE_MIN = 99
PRICE_MAX = 420

# Samples
TOTAL = 146

random.seed (150)

def random_limit (limit):
	r = math.floor(random.random() * limit)
	return r

N = PK + TOTAL
while PK < N:

	product = {}

	# ID
	product["id"] = PK

	# SKU
	sku = False
	while sku == False:
		
		product["sku"] = ""

		for _ in range ( 12 ):

			i = random_limit ( len(SKU) )

			product["sku"] += str ( SKU[i] )

		if product["sku"] not in SKUS:
			sku = True
			SKUS.add ( product["sku"] )


	# Name
	i = random_limit ( len(NAME) )
	product["name"] = NAME[i]


	# Material
	i = random_limit ( len(MATERIAL) )
	product["material"] = MATERIAL[i]

	i = random_limit ( len(PERCENTAGE) )
	product["percentage"] = PERCENTAGE[i]


	# Color
	i = random_limit ( len(COLOR) )
	product["color"] = COLOR[i]


	# Sex
	product["sex"] = SEX[0]


	# Category
	product["category"] = CATEGORY[0]


	# Price
	price = random_limit ( PRICE_MAX )
	product["price"] = price + PRICE_MIN

	i = random_limit ( len(DISCOUNT) )
	product["discount"] = DISCOUNT[i]


	# Entry

	PRODUCTS.append ( product )

	PK += 1




# CSV EXPORTATION
with open('products.csv', 'w') as csvfile:

	writer = csv.DictWriter (csvfile, fieldnames = FIELDS)
	
	writer.writeheader()

	writer.writerows(PRODUCTS)