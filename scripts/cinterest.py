def compute_comp_int(inv: float, rate: float, years=1) -> float:
    """Given an initial investment, rate, and optional year,
    returns the new ammount after interest has been computed."""
    if years == 1:
        return inv + (inv * rate)
    else:
        year_computed = inv + (inv * rate) # 1 year of compound interest computed
        return compute_comp_int(year_computed, rate, years - 1)

# if __name__ == "__main__":
#     print("Testing the cinterest.py module")
#     init_invest = 100
#     int_rate = .10
#     years = 3
#     print("Initial investment: $", init_invest, sep = '')
#     print("Interest Rate:", int_rate)
#     print("Years:", years)
#     print("After ", years, " years of investment, you should have a balance of $", compute_comp_int(init_invest, int_rate, years), sep = '')