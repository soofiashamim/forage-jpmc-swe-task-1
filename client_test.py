import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_price_b_as_zero(self):
    prices = [
      {'price_a': 119.2, 'price_b': 0},
      {'price_a': 121.67, 'price_b': 0}
    ]
    for p in prices:
      self.assertEqual(getRatio(p['price_a'],p['price_b']), None)

  def test_getRatio_price_a_as_zero(self):
    prices = [
      {'price_a': 0, 'price_b': 119.2},
      {'price_a': 0, 'price_b': 121.67}
    ]
    for p in prices:
      self.assertNotEqual(getRatio(p['price_a'],p['price_b']), None)




if __name__ == '__main__':
    unittest.main()
