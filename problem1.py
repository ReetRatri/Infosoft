from typing import Dict
import time
class DataStream:
    def __init__(self):
        self.last_seen: Dict[str, int] = {}

    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        
        if data_str not in self.last_seen or timestamp - self.last_seen[data_str] >= 5:
           
            self.last_seen[data_str] = timestamp
            
            return True
        return False

data_stream = DataStream()

# Test with the provided sequence
test_input = [
    (0, "helmlo"),
    (1, "world"),
    (6, "hello"),
    (7, "hello"),
    (8, "world")
]

output = [data_stream.should_output_data_str(timestamp, data_string) for timestamp, data_string in test_input]
print(output)  
