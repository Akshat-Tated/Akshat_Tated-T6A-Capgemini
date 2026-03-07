# Password Strength Validator
class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ##Write your code here
        for pwd in passwords:
            if len(pwd) < 8:
                continue

            has_upper = False
            has_digit = False
            has_special = False

            for ch in pwd:
                if ch.isupper():
                    has_upper = True
                elif ch.isdigit():
                    has_digit = True
                elif ch in "@#$":
                    has_special = True

            if has_upper and has_digit and has_special:
                strong.append(pwd)
        return strong
    

# Product Stock Shortage Report
class Solution:
    def low_stock_products(self, inventory):
        result = []
        #Write your code here
        for i in inventory:
            if inventory[i] < 10:
                result.append(i)
        return result
    

# Consecutive Duplicate Word Detector
class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        #Write your code here
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                duplicates.append(words[i])
       
        return duplicates
    

# Unique Product Purchase Analyzer
class Solution:
    def unique_products(self, products):
        result = []
        #Write your code here
        for p in products:
            if products.count(p) == 1:
                result.append(p)

        return result