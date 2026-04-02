# The item's discount and stock status have been defined
discounted = False
lowStock = True
# Evaluate whether an item is discounted or low in stock
movingProduct = discounted or lowStock
promotion = not discounted and not lowStock
print("Is the item eligible for promotion?", promotion)
