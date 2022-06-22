class cars:
    def __init__(self , wight, model , price , is_hybrid):
        self.wight = wight
        self.model = model
        self.price = price
        self.is_hybrid = is_hybrid


    def is_hybridcar(self):
        if self.is_hybrid:
            return True

        else:
            return False


