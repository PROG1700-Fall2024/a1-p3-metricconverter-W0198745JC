#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#print Imperial To Metric Conversion
    print("Imperial To Metric Conversion")
    print("")
# tons input 
    tons= int(input ("Enter the number of tons:"))
#stone input
    stone= int(input ("Enter the number of Stone:"))
#pounds input
    pounds= int(input ("Enter the number of pounds:"))
#ounces input
    ounces= int(input ("Enter the number of ounces:"))
#calculate total ounces
    totalOunces=((35840*tons)+(224*stone)+(16*pounds)+ounces)
#calculate total kilos
    totalKilos= totalOunces/35.274
#calculate metric tons
    metricTons= int(totalKilos/1000)
#figure out how to seperate Tons / kilos/ and grams ( AHHHHHHHHH)
# equation for kilos ( first try praying it works)
   # kilos=(totalKilos-metricTons)/1000 it Failed :(
    
#equation for kilos seperation ATTEMPT 2 SUCCESFUL just need to make it an INT!
    metricTonsFloat=(totalKilos/1000)
    kilos=(metricTonsFloat-metricTons)*1000
#equation for grams seperation
    grams=(metricTonsFloat-kilos)*1000

    print(str(metricTonsFloat))
    print(str(kilos))
    print(str(grams))

    # YOUR CODE ENDS HERE

main()