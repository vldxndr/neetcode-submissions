class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        
        for interval in intervals:
            # Cazul 1: Intervalul curent se termină înainte să înceapă cel nou
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            # Cazul 2: Intervalul curent începe după ce s-a terminat cel nou
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
            
            # Cazul 3: Există o suprapunere (overlap)
            # Nu adăugăm nimic în 'res' încă, doar actualizăm marginile noului interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # Dacă am ajuns la final și nu l-am adăugat (e cel mai mare), îl punem acum
        if not inserted:
            res.append(newInterval)
            
        return res