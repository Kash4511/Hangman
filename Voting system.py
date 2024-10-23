def voter_ID(used_id):
    result = []
    
    while True:
        id = input("Enter your Voter ID: ")
        if id in used_id:
            print("The ID entered has already been used.")
            return None
        user = input("Enter your Name: ")
        if "ID" in id and len(id) < 7:
            result.append("----------------------- \nUser Name: {}\nUser Voter ID: {}\n -----------------------".format(user, id))
            used_id.append(id)
            
            break
        else:
            print("Invalid Voter ID or Name")
            break
    
    return result
def candidate():
    used_id = []
    while True:
        voter_data = voter_ID(used_id)
        if voter_data:
            for data in voter_data:
                print(data)
            vote = {'Alex': 0, 'Bob': 0, 'Tom': 0, 'Harry': 0}
            print("The Candidates are:\n .Alex\n .Bob\n .Tom\n .Harry")
            pick_candi = input("Enter the candidate you want to vote for: ") 
            if pick_candi in vote:
                vote[pick_candi] += 1
                print("Vote casted for {}".format(vote))
    
            else:
                print("The entered candidate does not exist.")
    
        else:
            print("No valid voter ID entered. Exiting the voting process.")
            break
    
candidate()

