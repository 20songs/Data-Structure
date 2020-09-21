blocks = [7, 4, 2, 0, 0, 6, 0, 7, 0]

max_block = blocks[0]
max_index = 0
for i in range(len(blocks)):
    if blocks[i] > max_block:
        max_blocks = blocks[i]
        max_index = i

for j in range(max_index+1, len(blocks)):
    if blocks[max_index] == blocks[j]:
        result = j-max_index
        break
    else:
        result = len(blocks) - max_index -1

print(result)
