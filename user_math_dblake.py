"""
Author: Desiree Blake Date: 5/17/2023
Purpose: Complete P2 by utilizing math functions 
Domain: Books-I want to see data for the books i've read this week including:
least read/most read genres, average page number, and 
calculate the area of my new potential bookshelf!

Includes code copied from defensive.math.py

"""
import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#The purpose of this code is to take a list of books and calculate the following: 
#1. min genre read
#2. max genre read
#3. average page number
#4. Area of bookshelf

#Calculate minimum and maximum genres read this week from a total of 10 books
genre_read_counts = {
    "Romance": 4,
    "Fiction": 2,
    "Thriller": 1,
    "Nonfiction": 2
}

min_genre = min(genre_read_counts, key=genre_read_counts.get)
max_genre = max(genre_read_counts, key=genre_read_counts.get)

#Print Results
print("Least read genre:", min_genre)
print("Most read genre:", max_genre)

#Calculate average page number read
page_count = [33,172,263,436,90,523,244,345,190,222]

average = sum(page_count) / len(page_count)
#Print results
print("Average page count:", average)

#(Now I think I deserve a new bookshelf after all that haha)
#Calculate the area of the bookshelf with a try with exception

def calculate_bookshelf_area():
    try:
        area = 2 * math.pi * 20
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
result = calculate_bookshelf_area()
print(result)

#Permutations and combinations
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

