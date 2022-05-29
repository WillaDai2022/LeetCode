class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        
        res = []

        for i in range(1, len(currentState)):
            x = list(currentState)
            if currentState[i] == "+" and currentState[i-1] == "+":
                x[i] = "-"
                x[i-1] = "-"
                x = "".join(x)
                res.append(x)
            
        return res