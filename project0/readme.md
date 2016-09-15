# Project 0 
There are two primary objectives of this project: get a basic understanding of Python and familiarize yourself with the grading environment of the class.

### Problem 1

Add a buyLotsOfFruit(orderList) function to buyLotsOfFruit.py that takes a list of (fruit, pound) tuples and returns the cost of your list. If there is some fruit in the list that doesn't appear in fruitPrices, it should print an error message and return None. Please do not change the fruitPrices variable.

Test Case: We will check your code by testing that the script correctly outputs

```python
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
```
###Problem 2

Fill in the function shopSmart(orders, shops) in shopSmart.py, which takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder()) and a list of FruitShop and returns the FruitShop where your order costs the least amount in total. Don't change the file name or variable names, please. Note that we will provide the shop.py implementation as a "support" file, so you don't need to submit yours.

Test Case: We will check that, with the following variable definitions:

```python
orders1 = [('apples',1.0), ('oranges',3.0)]
orders2 = [('apples',3.0)]
dir1 = {'apples': 2.0, 'oranges':1.0}
shop1 =  shop.FruitShop('shop1',dir1)
dir2 = {'apples': 1.0, 'oranges': 5.0}
shop2 = shop.FruitShop('shop2',dir2)
shops = [shop1, shop2]
```	      
The following are true:

```python
shopSmart.shopSmart(orders1, shops).getName() == 'shop1'

shopSmart.shopSmart(orders2, shops).getName() == 'shop2'
'''
