def merge(List1, List2, Length_List1, Length_List2):
	Merged_List = [None] * (Length_List1 + Length_List2)
	i = 0
	j = 0 
	k = 0
	while i < Length_List1 and j < Length_List2:
		if List1[i] < List2[j]:
			Merged_List[k] = List1[i]
			k = k + 1
			i = i + 1
		else:
			Merged_List[k] = List2[j]
			k = k + 1
			j = j + 1
	
	while i < Length_List1:
		Merged_List[k] = List1[i];
		k = k + 1
		i = i + 1
  
	while j < Length_List2:
		Merged_List[k] = List2[j];
		k = k + 1
		j = j + 1
	print("Merged List: ")
	for i in range(Length_List1 + Length_List2):
		print(str(Merged_List[i]), end = " ")

List1 = [1, 3, 5, 7]
Length_List1 = len(List1)
print("List1 is : ", List1)
List2 = [2, 4, 6, 8]
Length_List2 = len(List2)
print("List2 is : ", List2)
merge(List1, List2, Length_List1, Length_List2);