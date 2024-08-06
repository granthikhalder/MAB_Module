import numpy as np

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def unflatten(flat_list, structure):
    flat_iter = iter(flat_list)
    def helper(struct):
        result = []
        for elem in struct:
            if isinstance(elem, list):
                result.append(helper(elem))
            else:
                result.append(next(flat_iter))
        return result
    return helper(structure)

# Multi-Armed Bandit (UCB) Agent
def mab_function(parameter_values, bounds, m_iterations, e_factor):

    print("MAB Algorithm Started")

    para = flatten(parameter_values)
    len_para = len(para)

    max_iterations = m_iterations
    k = len_para
    exploration_factor = e_factor
    initial_values = [bounds[i][0] for i in range(len_para)]
    values = initial_values
    counts = np.zeros(k)
    reward_array = []

    def select_arm():
        total_counts = np.sum(counts)
        ucb_values = values + exploration_factor * np.sqrt(np.log(total_counts + 1) / (counts + 1e-6))
        return np.argmax(ucb_values)

    def update(arm, reward):
        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]

    for iter in range(max_iterations):

        # Select arm (parameter) to adjust using UCB
        arm = select_arm()
        para[arm] = max(bounds[arm][0], min(bounds[arm][1], para[arm] + np.random.uniform(-0.1, 0.1)))
        
        temp = unflatten(para, parameter_values)
        reward = objective_function(temp)

        update(arm, reward)

        reward_array.append(reward)

        if iter % 100 == 0 or iter == (max_iterations-1):
            print(f"Iteration {iter}: Best value = {max(reward_array)}")
    return reward_array