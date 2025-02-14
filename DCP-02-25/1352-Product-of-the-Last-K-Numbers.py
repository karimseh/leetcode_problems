class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        last_product = self.prefix_product[-1]
        if num != 0:
            self.prefix_product.append(last_product * num)
        else:
            self.prefix_product = [1]

    def getProduct(self, k: int) -> int:
        if(k < len(self.prefix_product)):
            return int(self.prefix_product[-1] / self.prefix_product[-k - 1 : -k][0])
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
