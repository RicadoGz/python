companyName="bbbfesf"
companyCode="000032324342"
currentPrice=19.998
priceRaise=1.2
afterDay=7
finallyPrice=currentPrice*priceRaise**7
# in next line code the arguement:.xf means how many you want for show the point
print(f"company name is {companyName},company code is{companyCode},current price is {currentPrice:.2f}")
print("after %d day the price raise to %.2f"% (afterDay,finallyPrice))