#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(string,substring):
   positions= []
   if substring in string:
      place= 0
      for index in string:
         positions.append(int(string.find(substring, place))+1)
         place+= 1
   templist= []
   for place in positions:
      if place not in templist and place != 0 :
         templist.append(place)
      positions= templist
   return positions

def validate_sequence(string):
   if len(string)>8 and len(string)<=16:
      for index in string:
         if index in '1234567890':
            return False
      else:
         return True        
   else: 
      return False

def validate_subsequence(string):
   if len(string)==4:
      for index in string:
         if index in '1234567890':
            return False
      else:
         return True        
   else: 
      return False

