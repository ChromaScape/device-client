GRID_SIZE_X = 5
GRID_SIZE_Y = 5
GRID_SIZE_Z = 1

TOTAL_LIGHT_COUNT = GRID_SIZE_X * GRID_SIZE_Y * GRID_SIZE_Z

light_pos = []

for x in range(1, GRID_SIZE_X + 1):
    for y in range(1, GRID_SIZE_Y + 1):
        for z in range(1, GRID_SIZE_Z + 1):
            x_pos = (x - 1) / GRID_SIZE_X
            y_pos = (y - 1) / GRID_SIZE_Y
            z_pos = (z - 1) / GRID_SIZE_Z

            light_pos.append([x_pos, y_pos, z_pos])

