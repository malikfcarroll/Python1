import pandas as pd
election_data = pd.read_csv('election_data.csv')
election_data.head()
print('Total number of votes: ' + str(len(election_data)))
candidates = election_data['Candidate']
khan = []
correy = []
li = []
otooley = []

for i in range(0, len(candidates)):
    if candidates[i] == 'Khan':
        vote = 'Khan'
        khan.append(vote)
    elif candidates[i] == 'Correy':
        vote = 'Correy'
        correy.append(vote)
    elif candidates[i] == 'Li':
        vote = 'Li'
        li.append(vote)
    else:
        vote = "O'Tooley"
        otooley.append(vote)
        
khanvotes = len(khan)
correyvotes = len(correy)
livotes = len(li)
otooleyvotes = len(otooley)
print('Khan: ' + str(khanvotes) + ' votes, ' + str(100*(khanvotes / len(election_data))) + ' % of the popular vote')
print('Correy: ' + str(correyvotes) + ' votes, ' + str(100*(correyvotes / len(election_data))) + ' % of the popular vote')
print('Li: ' + str(livotes) + ' votes, ' + str(100*(livotes / len(election_data))) + ' % of the popular vote')
print("O'Tooley: " + str(otooleyvotes) + ' votes, ' + str(100*(otooleyvotes / len(election_data))) + ' % of the popular vote')
print('The winner is: Khan')