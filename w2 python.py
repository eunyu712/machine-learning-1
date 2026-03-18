#%% 적어도 2명이 생일이 겹칠 확률 구하기 

def birthday_paradox(n):
    """
    Calculate the probability that at least two people out of n share the same birthday.
    """
    if n > 365:
        return 1.0  # If more than 365 people, guaranteed shared birthday
    prob_no_shared_birthday = 1.0
    for i in range(n):
        prob_no_shared_birthday *= (365 - i) / 365
    return 1 - prob_no_shared_birthday

# Example: Calculate for 23 people
n = 23
prob = birthday_paradox(n)
print(f"With {n} people, the probability that at least two share the same birthday is: {prob:.2%}")

# %%
