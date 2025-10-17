#! /usr/bin/env python3

"""
Dugga script 
Author: Amanda
This script perfomrs several tasks including:
1. Analyzing a list of numbers to compute sums, cubes, and find repeats.
2. Reading gene expression data from a CSV file and plotting the distribution of log2-transformed expression values.
3. I included error handling for file reading and command-line argument parsing.
4. The script is modular with functions for better organization.
5. Comments are provided throughout for clarity.
6. Argparse is used for command-line argument parsing. -> This allows other users to specify input/output files easily.
    - Note: To run this script, use the command line to specify the input CSV file and optionally the output image file.
    - Example: python dugga_script.py -i brca_head500_genes.csv
    - Example with output file: python dugga_script.py -i brca_head500_genes.csv -o my_output.png

And yes, I like emojis! 😊
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import argparse 

# Set up argument parser

def get_args():
    # Setting up and return command-line arguments.
    parser = argparse.ArgumentParser(description="Dugga: Analyze gene expression data from a CSV file.")
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Path to the input CSV file (e.g., brca_head500_genes.csv)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="fpkm_distribution.png",
        help="Name of the output image file (default: fpkm_distribution.png)"
    )
    return parser.parse_args()


# Part 1 of the dugga script.

print("\n Part 1:")

# Input data:

numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]

# Task 1: Identify numbers with absolute value ≥ 10 and compute their sum.

sum_large = 0
for n in numbers: 
    # Check if the absolute value of n is ≥ 10
    if abs(n) >= 10:
        sum_large += n # add n to the sum if condition is met

print(f"1. Sum of numbers with |value| ≥ 10: {sum_large}") # print the result


# Task 2: Build a list of the cubes (n^3) of all negative numbers, then print the list.

cubes_neg = [] # list to store cubes of negative numbers
for n in numbers: # iterate through each number
    if n < 0: # check if the number is negative
        cubes_neg.append(n ** 3) # compute cube and add to the list

print(f"2. Cubes of negative numbers: {cubes_neg}") # print the list of cubes


# Task 3: # Scan left-to-right and print the first repeated absolute value, if any.

seen = set()     # to track absolute values we’ve already seen
repeat_found = None   # store first repeat when found

for n in numbers:
    abs_n = abs(n) # get absolute value
    if abs_n in seen: # check if we’ve seen it before
        repeat_found = abs_n # store the first repeat when found
        break          # stop scanning after the first repeat
    else:
        seen.add(abs_n) # add to seen set

if repeat_found is not None: # if we found a repeat
    print(f"3. First repeated absolute value: {repeat_found}")
else:
    print("3. No repeats.")



# Part 2 of the dugga script.
print("\n Part 2:")

# Task 2.1: Read the CSV file 'brca_head500_genes.csv' into a dataframe.

args = get_args() # get command-line arguments


try:
    df = pd.read_csv(args.input, sep=",")
    print("\n✅ File successfully loaded!") # confirm successful load, show first few rows (hihi I like emoljis)
    print(df.head())  # shows first few rows (by using head())
except FileNotFoundError:
    print(f"❌ Error: File '{args.input}' not found. Please check the file name or path.")


# Task 2.2:
# Task 2.2.1: Create function

def plot_fpkm_distribution(dataframe, output_file="fpkm_distribution.png"):
    """
    Plotting a histogram of the fpkm_log2 values and saving it as 'fpkm_distribution.png'.
    Adds title, axis labels, and shows the distribution of log2-transformed expression values.
    """

    # Creating the histogram
    plt.figure(figsize=(8, 5)) # setting figure size just for aesthetics
    plt.hist(dataframe["fpkm_log2"], bins=20, color="skyblue", edgecolor="black")

    # Adding title and labels to axes (Task 2.2.3 added to task 2.2.1)
    plt.title("Distribution of gene expression")
    plt.xlabel("Expression")
    plt.ylabel("Number of genes")

    # Saving the figure
    plt.tight_layout() # adjusting the layout
    plt.savefig(output_file) # save the plot as a PNG file

    # Show plot now and then comment out before handing in
    # plt.show()


    print(f"✅ Histogram saved as '{output_file}'") # confirming that the plot was saved successfully

# Task 2.2.2: Calling the function to actually run the code
plot_fpkm_distribution(df, args.output)

# End of dugga_script.py

print("\n End of my dugga_script.py\n")

