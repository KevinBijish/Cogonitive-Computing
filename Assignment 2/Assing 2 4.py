A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

#1
unique_scores = A | B
print(unique_scores)

#2
common_scores = A & B
print(common_scores)

#3
exclusive_scores = A ^ B
print(exclusive_scores)

#4
A_sub_B= A.issubset(B)
B_sup_A= B.issuperset(A)
print(A_sub_B)
print(B_sup_A)  

#5
user_score=int(input('Enter the score to remove it:'))
if user_score in A:
    A.remove(user_score)
    print(f"Removed {user_score} from set A.")
else:
    print(f"{user_score} is not present in set A.")
print(A)
