def most_profit(difficulty: list, profit: list, worker: list) -> int:
    # checking test cases
    if len(difficulty) < 1 or \
            len(difficulty) > 10000 or \
            len(difficulty) != len(profit) or \
            len(worker) < 1 or \
            len(worker) > 10000:
        return 0

    # create placeholder variables
    job_counter = 0
    work_counter = 0
    cur_profit = 0

    # begin logic
    while work_counter != len(worker):
        # iterate through worker list
        if worker[work_counter] == difficulty[job_counter]:
            # worker skill is same level as difficulty
            # add profit, move to next worker, reset job_counter
            cur_profit += profit[job_counter]
            work_counter += 1
            job_counter = 0
        elif worker[work_counter] > difficulty[job_counter]:
            # worker skill level is greater than difficulty
            if worker[work_counter] < difficulty[job_counter + 1]:
                # if next difficulty level is greater than worker skill
                # add profit, move to next worker, reset job_counter
                cur_profit += profit[job_counter]
                work_counter += 1
                job_counter = 0
            else:
                # next difficulty level is not greater than worker skill
                # move to next job
                job_counter += 1
        else:
            # worker can't complete any jobs
            # no profit to add, move to next worker, reset job_counter
            work_counter += 1
            job_counter = 0

    return cur_profit


print(most_profit([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
