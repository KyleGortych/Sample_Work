"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Kyle Gortych
Date:   02/16/2022
"""
import currency

src = input("3-letter code for original currency: ")
src = str(src)

dst = input("3-letter code for the new currency: ")
dst = str(dst)

amt = input("Amount of the original currency: ")
amt = float(amt)

json = currency.service_response(src,dst,amt)
# print(json)

src_result = currency.before_space(currency.get_src(json))
sub_str = src

dst_result = currency.exchange(src,dst,amt)
dst_rounded = round(dst_result, 3)
sub_str2 = str(dst_rounded)

sub_str3 = dst

print("You can exchange " + src_result + " " + sub_str + " for " + sub_str2 + " " + sub_str3 + ".")
