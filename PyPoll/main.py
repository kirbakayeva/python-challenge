import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

#Values
totalVotes = 0
candidates = []
voteCount = []
winnerVoteCount = 0

#Data
with open(csvpath, 'r', newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Header
    csv_header = next(csvreader)

    #Looping
    for row in csvreader:
        #Total votes
        totalVotes += 1

        #List
        if(row[2] not in candidates):
            candidates.append(row[2])
            voteCount.append(0)
        
        #Index
        candidateIndex = candidates.index(row[2])
        #Vote Count
        voteCount[candidateIndex] += 1

    #Printing Output
    print(f"\nElection Results")
    print(f"Total votes: {totalVotes}")
        
    for x in range(len(candidates)):
        votePercent = round((voteCount[x]/totalVotes)*100,3)
        print(f"{candidates[x]}: {votePercent}% ({voteCount[x]})")
        if (winnerVoteCount<voteCount[x]):
            winnerVoteCount = voteCount[x]
            winner = candidates[x]
    
        print(f"Winner: {winner}")
    

Election = open('output.txt','w')

#Writing output
Election.write("Election Results")
Election.write("\nTotal votes:" + str(totalVotes))

    
for x in range(len(candidates)):
    votePercent = round((voteCount[x]/totalVotes)*100,3)
    Election.write("\n" + str(candidates[x]) +" : " + str(votePercent)
                + "% ("+ str(voteCount[x]) + ")")
Election.write("\nWinner: " + str(winner))

Election.close()

