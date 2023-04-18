#!/usr/bin/env python3

# Created by: Kent G
# Date: Apr 17, 2023
# This program is simulating a building with N panels per floor and M floors.

# Set values for N (number of panels) and M (number of floors)
N = 3
M = 6

# Define the initial state of the bottom floor as a list of strings representing each panel.
new_floor = ["W", "W", "G"]

# Define a function to sort the panels into pairs, wrapping around to the first panel.
def sorting(total_floor_panels, list_of_windows):
    new_list = []
    for panel in range(total_floor_panels):
        # Checking if it is the last panel by adding 1 since range() counts from 0 to n-1.
        # If it is the last panel, we join the panel letter with the first the first's.
        if panel+1 == total_floor_panels:
            new_list.append(list_of_windows[panel]+list_of_windows[0])
        # Since it is not the last panel, it is safe to assume we have another panel available.
        else:
            new_list.append(list_of_windows[panel]+list_of_windows[panel+1])
    return new_list

# Define a function to get the state of the top floor based on the state of the bottom floor.
def window_get(panel_combination):
    upper_floor = []
    my_dict = {
    "GW":"G",
    "WG":"W",
    "GG":"W",
    "WW":"G"}
    # For every panel combination in the 2 letter sequence, we find it's meaning in the dictionary.
    for combo in panel_combination:
        # And add it to the upper floor's layout.
        upper_floor.append(my_dict[combo])
    return upper_floor

if __name__ == "__main__":
    # Re-executing the loop for the amount of floors.
    for loop_count in range(M):
        sequence = sorting(N, new_floor)
        new_floor = window_get(sequence)

        # Final output.
        print(f"Level {loop_count+1}" + str(new_floor))
