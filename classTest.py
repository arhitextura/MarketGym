class Comment():
    def __init__(self):
        self._productRecommender = None

    @property
    def productRecommender(self):
        print("getter called")
        return self._productRecommender if self._productRecommender is not None else 'Onbekend'

c = Comment()
foo = c.productRecommender