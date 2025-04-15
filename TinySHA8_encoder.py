
class TinySHA_8:
    def __init__(self):
        self.prev_message = [1,1,1,0,1,1,1,0]
        self.master_message: list = [0,1,0,0,1,0,0,0]
        assert len(self.master_message) == 8, "Invalid letter!"
        
        self.H: list = [1,0,1,0,1,0,1,0]
    
    def algorithm(self):
        self.message = [1,0,1,0,0,1,1,0]
        for i in range(8):
                if self.prev_message[i] ^ self.master_message[i]:
                    self.message[i] = 1
                    print
                else:
                    self.message[i] = 0
        


        self.message.extend([1,0,0,0,0,0,0,0])
        for section in range(4):

            self.W = self.message[section*4:(section+1)*4] * 2

            for i in range(8):
                if self.W[i] ^ self.H[i]:
                    self.H[i] = 1
                else:
                    self.H[i] = 0

            self.H = self.H[1:] + [self.H[0]]
            self.final_output = self.H



if __name__ == "__main__":
    tiny = TinySHA_8()
    TinySHA_8.algorithm(tiny)
    print(tiny.final_output)