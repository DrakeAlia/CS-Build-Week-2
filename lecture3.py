# pascal.py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            # First row
            if i == 0:
                rows.append([1])
            
            # Second row
            elif i == 1:
                rows.append([1,1])
                
            # General case rows
            else:
                # Start with 1
                new_row = [1]
                
                # Fill in the middle numbers
                middle_number_count = i - 1
                
                for j in range(middle_number_count):
                    col_index = j + 1
                    prev_row = rows[-1]
                    value = prev_row[col_index] + prev_row[col_index - 1]
                    
                    new_row.append(value)
                    
                # Add a one on the end
                new_row.append(1)
                
                rows.append(new_row)
            
        return rows

# pascal_recursive.py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        
        cache = {}
        
        def get_row(n):
            
            if n <= 1:
                return [1] * (n+1)
            
            if n not in cache:
                prev_row = get_row(n-1)
​
                # Start with 1
                new_row = [1]
​
                # Fill in the middle numbers
                middle_number_count = n - 1
​
                for j in range(middle_number_count):
                    col_index = j + 1
                    value = prev_row[col_index] + prev_row[col_index - 1]
​
                    new_row.append(value)
​
                new_row.append(1)
                
                cache[n] = new_row
            
            return cache[n]
            
        for r in range(numRows):
            rows.append(get_row(r))
            
        return rows


res = "_"
    d = {}
    for i,c in enumerate(s):
        if c in d.keys():
            d[c] = -1
        else:
            d[c] = i
    min_key = len(s)+1
    for k in d.keys():
        if d[k]>=0:
            min_key = min(min_key,d[k])
            res = s[min_key]
    return re



