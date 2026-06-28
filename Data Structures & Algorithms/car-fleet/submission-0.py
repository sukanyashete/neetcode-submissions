class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars = sorted(cars, reverse=True)
        
        #cars[0] = (position[0], speed[0])
        for pos, spd in cars:
            time = (target - pos) / spd
            if stk and stk[-1] >= time:
                #stk.append(time)
                print("Ignore")
            else:
                stk.append(time)

        return len(stk)
