# brokerage calculator
# A = buyPrice * quantity
# B = sellPrice * quantity
# turnover = A + B

# each % tax convert into decimal
# Exampl= 0.03/100 = 0.003
# percentage or  fixed exchange rates :-
#  Brokerage 0.0003 = 0.03%  -------------------------------Intraday Brokerage Rate per side applyed
#  0.0000345 = 0.00345%  Exchange Transaction Charge--------buy + sell charges apllyed
#  0.18 = 18%  Goods and Services Tax ----------------------brokerage + EXCHANGE transaction apply
#  0.00025 = 0.025%  Securities Transaction Tax ------------only for sell side apply
#  0.000001 = 0.0001%  SEBI Charges ------------------------buy + Sell  apply
#  0.00003 = 0.003%  Stamp Duty-----------------------------only BUy apply

def intradayCount(buyPrice, sellPrice, quintity):
    turnover = (buyPrice + sellPrice) * quintity
    # brokerage = min((buyPrice * quintity) * 0.0003, 20)---------------------------------------
    # min(a, b) return the samall amount ,0.0003 return ----------------------------------------
    brokerage = min(20, buyPrice * quintity * 0.0003) + min(20, sellPrice * quintity * 0.0003)
    exchangeTransactionCharge = turnover * 0.0000345
    GoodsServicesTax = 0.18 * (brokerage + exchangeTransactionCharge)
    SecuritiesTransactionTax = sellPrice * quintity * 0.00025
    sebiCharges = turnover * 0.000001
    stampDuty = (buyPrice * quintity) * 0.00003
    totalCharges = exchangeTransactionCharge + sebiCharges + stampDuty +SecuritiesTransactionTax + GoodsServicesTax + brokerage
    ProfitBeforeCharges = (sellPrice - buyPrice) * quintity  # Calculate profit before charges gross profit
    PnL = ProfitBeforeCharges - totalCharges
    
    return {
        "Turnover              ": turnover,
        "Brokerage             ": brokerage,
        "ExchangeTransactionCharge": exchangeTransactionCharge,
        "GoodsServicesTax -GST ": GoodsServicesTax,
        "SecuritiesTransactionTax -STT": SecuritiesTransactionTax,
        "SebiCharges           ": sebiCharges,
        "stampDuty             ": stampDuty,
        "totalCharges          ": totalCharges,
        "ProfitBeforeCharges   ": ProfitBeforeCharges,
        "Total Profit and loss ": PnL
    }


if __name__ == "__main__":
    print("\n calculating brokerage at intra-day possition")

    buyPrice = float(input("Enter Buy Price: "))
    sellPrice = float(input("Enter Sell Price: "))
    quantity = float(input("Enter Quantity: "))

    result = intradayCount(buyPrice, sellPrice, quantity)
    # result = intraday(100, 105, 10)
    # print("\nCalculation Result:")
    for key, value in result.items():
    #  print(f"{key}: {value:}")
    #  print(f"{key}: {value.3f}")
       print(f"{key}: {value:.2f}")
