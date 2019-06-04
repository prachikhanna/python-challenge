import os
import csv

vote_file_path = os.path.join("Resources","election_data.csv")
output_file_path = os.path.join("Resources","output_data.txt")

count_row=0
name_list=[]
vote_count=[]
candidate_list={"Candidate":name_list,"VoteCount":vote_count}

with open(vote_file_path) as vote_file:
    csv_reader=csv.reader(vote_file,delimiter=",")
    csv_header=next(csv_reader)
    i=0
    for row in csv_reader:
        count_row=count_row+1
        candidate_name=row[2]
        if candidate_name in name_list:
            candidate_list["Candidate"]=name_list
            i=name_list.index(candidate_name)
            vote_count[i]=vote_count[i]+1
            candidate_list["VoteCount"]=vote_count
        else:
            name_list.append(candidate_name)
            candidate_list["Candidate"]=name_list
            i=name_list.index(candidate_name)
            vote_count.append(1)


with open(output_file_path,"w") as output_data:
    print("Election Results")
    output_data.write("Election Results\n")
    output_data.write("-------------------------\n")
    print("-------------------------")   
    output_data.write("Total Votes: " + str(count_row) + "\n")    
    print("Total Votes: " + str(count_row))    
    output_data.write("-------------------------\n")
    print("-------------------------")    

    i=0
    for name in name_list:
        VotePercent=(candidate_list["VoteCount"][i]/count_row)*100
        x = str("%.3f" % round(VotePercent,3))
        output_data.write(name + ": " + x + "% " + "(" + str(candidate_list["VoteCount"][i]) + ")\n")
        print(name + ": " + x + "% " + "(" + str(candidate_list["VoteCount"][i]) + ")")    
        i=i+1
 

    index=candidate_list["VoteCount"].index(max(candidate_list["VoteCount"]))
    output_data.write("-------------------------\n")
    print("-------------------------")    
    output_data.write("Winner: "  + name_list[index] + "\n" )
    print("Winner: "  + name_list[index] )    
    output_data.write("-------------------------\n")
    print("-------------------------")