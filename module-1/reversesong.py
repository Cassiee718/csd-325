#Cassiany Noel 1/9/25 Module 1.3

def bottle_song(bottles):
#Loop for number of bottles	
	while bottles > 0:
		if bottles >1:
			print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer." 
			" Take one down and pass it around,")
			
		else:
			print(f"1 bottle of beer on the wall, 1 bottle of beer"
			" Take one down and pass it around, no more bottles of beer on"
			" the wall.")
		bottles -=1	
			
	print("No more bottles of beer on the wall, no more bottles of beer."
	" It's time to buy more bottles of beer,") 
	print("99 bottles of beer on the wall")
	
def main():
#get the number of bottles from user	
	bottles = int(input("How many bottles of beer are on the wall? "))
	bottle_song(bottles)

if __name__== "__main__":
			main()
