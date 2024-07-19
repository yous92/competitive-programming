class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        
        start = 0
        tank = 0
        total_gas = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            
            if tank < 0 : 
                start = i + 1 
                print(start)
                tank = 0
        return start if total_gas >= 0 else -1