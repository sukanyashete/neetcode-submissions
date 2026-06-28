class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars = sorted(cars, reverse=True)
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if stk and stk[-1] >= time:
                # Car joined the fleet
                continue
            else:
                # Car formed a new fleet
                stk.append(time)

        return len(stk)