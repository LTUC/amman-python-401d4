
## How to access data
You have:
- data
- key for the data

hashtable(key) => data

## Insert data
- You have the data
- Generate a key from that data
- Insert data to hatable(data)

## Notes:
- key is a string
- data can be any type

## Hashing
- Used to generate a memory location (aka array index) from the key
- Hash keys should be:
    - Deterministic: Output is determined by input
    - Not Random: Same key always generate same hash
e.g. 
```python
ages = {'ahmad':25, 'abdullah':23, 'Amarah':22, 'Qusai':24}
print(ages['Qusai']) #always get 24 (no randomness)
```

## Save data in Hashtable
- We save data in memeory
- e.g. Arrays with indeces 0,1,2,...,n-1
    - Sequence of data (next to each other)
    - At each index there is a piece of data
    - Index represents memory address (if we start at 8000, index 3 will be at address 8003)
### How about hashtables?
    - We save key and data (aka value) on the same memory address
### Process of saving data:
    - You have data and it's key
    - Use Hash function (algorithm) to generate memory address from the key of data
    - Save data on that memory address
### Process og getting data
    - You have a key
    - Use the Hash function to convert the key into memory address
    - Get the data from the memory address


### Exmaple of saving data in memory
```python
key = 'ahmad'
data = 25 # value

# First step is to convert the key to a memory location
# Memory will be represented by an array
# You should set the size of array 
# Size of array will be 1024 (1K)

sum_of_asccii = 97 + 104 + 109 + 97 + 100 = 507
temp_value = sum_of_asccii * 19 # 9633
index = temp_value % 1024 # modulus size of array => 417
# Save data (25) at index 417
```

### Example of getting data from memory using a key
```python
key = 'ahmad'
sum_of_asccii = 97 + 104 + 109 + 97 + 100 = 507
temp_value = sum_of_asccii * 19 #9633
index = temp_value % 1024 # modulus size of array => 417
# Get data at index 417
```

### Challenge: Two keys are hashed to the same index (collision)
Examples: 
- `cloud` and `could` hashed to the same index
- `silent` and `listen` hashed to the same index

#### Solution: Use buckets
- Use another data structure to save all pairs of keys and values in the same memory location
