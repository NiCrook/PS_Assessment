def max_capicity(weights: list, days: int) -> int:
    max_capicity = sum(weights) // days
    counter = 0
    daily_weight = 0
    cur_days = 1

    # iterate through each weight
    while counter != len(weights):
        # check if current weight exceeds capacity
        if weights[counter] > max_capicity:
            # if current weight exceeds capcity, increment max_capacity by one
            # reset placeholder variables to 0
            # run through the while loop again
            max_capicity += 1
            counter = 0
            daily_weight = 0
            cur_days = 1
        else:
            # if current weight does not exceed capacity, check if current weight + next weight would exceed capacity
            if daily_weight + weights[counter] > max_capicity:
                # if current weight + next weight exceeds, check if there are still any days left
                if cur_days < days:
                    # if days left, reset daily_weight and increment to next day
                    daily_weight = 0
                    cur_days += 1
                else:
                    # if no days left, increment max_capacity by one
                    # reset placeholder variables to 0
                    # run through the while loop again
                    max_capicity += 1
                    counter = 0
                    daily_weight = 0
                    cur_days = 1
            else:
                # add next weight to daily_weight, increment counter by 1
                daily_weight += weights[counter]
                counter += 1

    return max_capicity


print(max_capicity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
