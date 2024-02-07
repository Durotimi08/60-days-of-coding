given_numbers = [2, 7, 11, 13]

target = 9

discovered_numbers = {}

for current_index, current_number in enumerate(given_numbers):
    couterpart = target-current_number
    
    if couterpart in discovered_numbers: 
        print([discovered_numbers[couterpart], current_index])
        break
        
    discovered_numbers[current_number] = current_index
