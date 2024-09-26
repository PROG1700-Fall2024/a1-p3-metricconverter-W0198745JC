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
    
#equation for kilos seperation ATTEMPT 3 SUCCESFUL just need to make it an INT!
    metricTonsFloat=(totalKilos/1000)
    kilos=int(metricTonsFloat-metricTons)*1000
    kilosFloat=(metricTonsFloat-metricTons)*1000
    kilosFinal=int(kilosFloat-kilos)

    #equation for grams seperation
    #grams=(metricTonsFloat-kilos)*1000 FAILURE 
    gramsFloat=((kilosFloat-kilos)-kilosFinal)*1000  #YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS it just needed an extra bracket for function order
    print(str(metricTons))
    print(str(kilosFinal))
    print(str(gramsFloat))

    # YOUR CODE ENDS HERE

main()