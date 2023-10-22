# randomly picks a value based on the value's weights

# weights can be any integer

# weights do not have to sum to 1, but must not sum to zero

# value picked can be text, numeric, or any other type

import pandas as pd

#input format dataframe
input = pd.DataFrame(columns=['value', 'weight', 'partition'])


def select_single_winner(input):
    '''select a single winner for the entire input dataset'''

    return input['value'].sample(n=1, weights=input['weight'], random_state=1)


def select_winners_by_partition(input):
    '''select multiple winners based on a dataset partition'''

    winners = []

    #p represents each partition
    for p in input['partition'].drop_duplicates():

        #filter the input df to show only the data in the partition
        partitioned_df = input[input['partition'] == p]

        winner_for_this_partition = partitioned_df['value'].sample(n=1, weights=partitioned_df['points'], random_state=1)

        #append results to the winners list for concatenation at a later point
        winners.append(pd.DataFrame({'partition':p, 'winner':winner_for_this_partition}))

    #combine all dfs in the winners list
    winners_df = pd.concat(winners, ignore_index=True)


    return winners_df