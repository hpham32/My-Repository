def isfloat(num):
    try:
        float(num)
        return True
	      print(“This is a float!”)
    except ValueError:
        return False
		    print(“Not a float”)
      

print(isfloat('1.123'))
