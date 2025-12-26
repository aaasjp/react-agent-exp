# Alpha

Professor Alexander Barinov

School of Business Administration University of California Riverside

MGT 295F Empirical Methods

# Outline

![](images/6f9d6d348d9029ecb1a0b7eff3aab2f5a955c200e297a4fb298584e80a19eaba.jpg)

Some Theory

![](images/036c7ed4bd03a94804d2e07210aa361ecf9fa3f1495bbf39b710869b4224bc4e.jpg)

Empirical Examples

# What the CAPM Says

$$
E (R _ {t}) = R F _ {t} + \beta \cdot \left(E (M K T _ {t}) - R F _ {t}\right)
$$

- According to the CAPM, the expected return you should be getting, on average, from an asset (say, a stock) consists of three parts  
- The first part is the risk-free return,  $RF_{t}$  - this is the premium for waiting and tying up your money; you will get it even on the assets that have no risk  
- The second part is the market risk premium  $E(MKT_{t}) - RF_{t}$  - this is the premium per unit of risk you bear  
- The third part is the asset's risk exposure, or the beta - it says how many units of risk you bear when you invest in the asset

# The CAPM and the Alpha

- Rearrange  $E(R_{t}) = RF_{t} + \beta \cdot (E(MKT_{t}) - RF_{t})$  
- You will get  $E(R_{t}) - RF_{t} = \beta \cdot (E(MKT_{t}) - RF_{t})$  
- When you run the regression with real data, you estimate  $R_{t} - RF_{t} = \alpha + \beta \cdot (MKT_{t} - RF_{t})$  
- According to the CAPM, the intercept of the regression - the alpha - has to be zero  
- Notice that both sides of the regression use excess returns, not raw returns: you do that in order to have zero as a natural benchmark for the alpha

# Alpha of Zero-Investment Portfolios

- If you estimate the magnitude of the value effect, you estimate  $HML_{t} = \alpha + \beta \cdot (MKT_{t} - RF_{t})$  
- Notice no  $RF_{t}$  on the LHS - this is because HML is a zero-investment portfolio  
- Economic intuition: when you create a zero-investment portfolio, you put no money down  
- Hence, you should not make  $RF_{t}$  (the premium for tying up your money) if you happen to have no risk (zero beta), you should make 0 instead

# Alpha of Zero-Investment Portfolios

- Another way to look at that is to look at the long side and the short side separately  
- According to the CAPM,

$E(H_{t}) = RF_{t} + \beta_{H}\cdot (E(MKT_{t}) - RF_{t})$  
$E(L_{t}) = RF_{t} + \beta_{L}\cdot (E(MKT_{t}) - RF_{t})$

- Subtracting the top from the bottom, we see that  $RF_{t}$  cancels out and we get

$$
E \left(H M L _ {t}\right) = \left(\beta_ {H} - \beta_ {L}\right) \cdot \left(E \left(M K T _ {t}\right) - R F _ {t}\right)
$$

- We also notice that  $\alpha_{HML} = \alpha_{H} - \alpha_{L}$  and

$$
\beta_ {H M L} = \beta_ {H} - \beta_ {L}
$$

# Alpha: Common Mistakes

- First rule: deduct the risk-free rate (RF) from all assets you have to invest in, do not deduct it from the zero-investment portfolios

- If the LHS variable is an asset (what you want to buy or what you want to short), you have to deduct the risk-free rate  
- If the LHS variable is a zero-investment portfolio (i.e., the return to the "long-plus-short" position, e.g., HML), you should not deduct the risk-free rate  
- You have to deduct the risk-free rate from the market return (MKT) on the RHS  
- If you use other factors, like SMB, HML, MOM, which are zero-investment portfolios, do not deduct the risk-free rate

# Alpha: Common Mistakes

- Always make sure that the units match (i.e., the LHS and RHS variables are either all in percentages, or all in decimals)  
- If the beta is 0.01 or 100 and statistically significant, then the units do not match  
- Hint: if Excel reports numbers as "1.05%\%, it still thinks they are decimals - you have to multiply the numbers by 100 to turn them into percentages from decimals  
- If the beta is small (below 0.1) and insignificant, you mismatched the dates (stock return from today sits next to MKT return from yesterday, or vice versa)

# CAPM for Amazon

$$
A M Z N _ {t} - R F _ {t} = \begin{array}{l} 3. 4 1 \\ (1. 7 8) \end{array} + \begin{array}{l} 2. 5 7 \\ (0. 4 0) \end{array} \cdot \left(M K T _ {t} - R F _ {t}\right)
$$

- The regression above uses data from 1998-2007 and shows that Amazon has a positive and significant (at the  $10\%$  level) alpha of  $3.41\%$  per month  
We could have got  $3.41\%$  with no (systematic) risk and no money down by playing with the Amazon stock  
Here is how: first, borrow $1 at the risk-free rate and invest it in Amazon  
- Now, short the market for $2.57 (the value of Amazon's beta!) and invest the proceeds in Treasuries

# CAPM for Amazon

$$
A M Z N _ {t} - R F _ {t} = \begin{array}{l} 3. 4 1 \\ (1. 7 8) \end{array} + \begin{array}{l} 2. 5 7 \\ (0. 4 0) \end{array} \cdot \left(M K T _ {t} - R F _ {t}\right)
$$

- On average,  $AMZN_{t} - RF_{t}$  changes by 2.57 when  $MKT_{t} - RF_{t}$  changes by 1  
- Our position "long  $AMZN_{t} - RF_{t}$ , short  $MKT_{t} - RF_{t}$ " should not depend on the market movements at all  
- Every time the market goes up by  $1 \%$ , we should win 2.57 cents on the long side and lose 2.57 cents on the short side, and vice versa  
- But the equation above says "long  $AMZN_{t} - RF_{t}$ , short  $MKT_{t} - RF_{t}$ " makes 3.41% per month - riskless arbitrage!

# Alpha in the Fama-French Model

$$
A M Z N _ {t} - R F _ {t} = \begin{array}{l} 4. 5 0 \\ (1. 9 4) \end{array} + \begin{array}{l} 2. 0 6 \\ (0. 4 5) \end{array} (M K T _ {t} - R F _ {t}) - \begin{array}{l} 0. 9 9 \\ (0. 5 8) \end{array} S M B _ {t} - \begin{array}{l} 1. 6 7 \\ (0. 5 9) \end{array} H M L _ {t}
$$

The alpha of Amazon is  $4.5\%$  per month in the Fama-French model  
- How do we make that much with no risk and no money down?  
- We will start with investing  $1 into Amazon (by borrowing$ 1 at the risk-free rate)  
- We will short the stuff on the right-hand side, and the betas are the sums for which we short

# How to Make It Work in Excel

- On PC, Data tab in the upper menu, Data Analysis on the far right  
- You need Regression in the first dialog box  
In the regression dialog box, Ret-RF is Y, MKT-RF is X  
- When you do the Fama-French model, select all three columns (MKT-RF, SMB, HML) at once as X  
- The multiple X columns have to be next to each other  
- Check "Labels" if you selected the column headers  
- Make sure the number of observations is equal in all columns

# Reading Excel Output

- "Intercept" row is the alpha  
- MKT-RF (and further rows) report the betas  
A coefficient is significant if (three equivalent ways of testing)

t-stat is greater than 2  
p-value is less than 0.05  
- 0 does not fall between "Lower  $95\%$  " and "Upper  $95\%$ "

# Constructing Riskless Arbitrage

$$
A M Z N _ {t} - R F _ {t} = \begin{array}{l} 4. 5 0 \\ (1. 9 4) \end{array} + \begin{array}{l} 2. 0 6 \\ (0. 4 5) \end{array} (M K T _ {t} - R F _ {t}) - \begin{array}{l} 0. 9 9 \\ (0. 5 8) \end{array} S M B _ {t} - \begin{array}{l} 1. 6 7 \\ (0. 5 9) \end{array} H M L _ {t}
$$

- Borrow $1 at the risk-free rate (short Treasuries) and buy Amazon for $1  
- Short MKT for \(2.06 and invest it in Treasuries (cancels out the market factor from the long position in Amazon)  
- "Short" SMB for -\ $0.99, i.e. "buy" SMB for \$ 0.99, that is, short big firms for \$0.99 and invest the proceeds (\$0.99) in small firms (cancelled out the SMB factor from the long position in Amazon)  
- Short growth firms for  $1.67 and buy value firms for$ 1.67 (cancels out the SMB factor from the long position in Amazon)

# Constructing Riskless Arbitrage

$$
A M Z N _ {t} - R F _ {t} = \begin{array}{l} 4. 5 0 \\ (1. 9 4) \end{array} + \begin{array}{l} 2. 0 6 \\ (0. 4 5) \end{array} \left(M K T _ {t} - R F _ {t}\right) - \begin{array}{l} 0. 9 9 \\ (0. 5 8) \end{array} S M B _ {t} - \begin{array}{l} 1. 6 7 \\ (0. 5 9) \end{array} H M L _ {t}
$$

- What if MKT increases by  $1\%$ ? - Amazon makes \ $2.06, the "short side" loses \$ 2.06, the total position sees no change in value  
- What if SMB makes  $1\%$ ? - Amazon loses \ $0.99, the "short side" gains \$ 0.99, the total position sees no change in value  
- What if HML makes  $1\%$ ? - Amazon loses $1.67, the "short side" gains $1.67, the total position sees no change in value  
- But the total position gains  $4.5\%$  per month - riskless arbitrage!

# Two Standard Errors

- "Standard Error" that sits right next to the coefficients measures their precision and is used for constructing the t-statistics and confidence intervals  
- If the alpha is  $4.50\%$  with standard error  $1.94\%$ , the true alpha can be 2 standard errors away from  $4.5\%$  - anywhere between  $4.5\% - 2 \cdot 1.94\% = 0.62\%$  and  $4.5\% + 2 \cdot 1.94\% = 8.38\%$  
- The interval above means: "If we observe Amazon in the next decade (and assuming nothing changes about Amazon), the average return will be somewhere between  $0.62\%$  and  $8.38\%$  per month"  
- The  $95\%$  confidence interval in Excel uses a more precise z-score of 1.96 instead of 2

# Two Standard Errors

- "Standard Error" from the very top table is the standard deviation of residuals aka idiosyncratic volatility  
- This standard error measures the precision of the forecast for each individual month  
- For example, the no-risk, no-money-down strategy we just constructed would yield constant return of  $4.5\%$  if the Fama-French model was exactly true and the three Fama-French factors were the only source of variation  
The standard error from the top table tells us though that in each particular month the return to this strategy can be between  $4.5\% - 2 \cdot 18.89\% = -33.28\%$  and  $4.5\% + 2 \cdot 18.89\% = 42.28\%$  
- Hence, the strategy is not actually no-risk, it just has no systematic risk - if we find 100 stocks like Amazon and create a diversified portfolio, the return to the portfolio will (hopefully) be almost constant

# Three Sources of the Alpha

- Probably, the alpha is the compensation for some extra risk that is missing from our models

- Then we can count on the alpha to be there in the future, but we should be cautious trying to make money on it

- Probably, the alpha is the evidence of mispricing, e.g., a positive alpha means that observed returns are "too high", because the price was "too low" to start with

- We should probably expect the alpha to be there in the future, especially if it is the alpha of some broad class of stocks, and we should trade on it and make our (almost) free money

- Probably, the alpha is just luck - for example, Amazon had a clearly unusual fate compared to an average dot-com company that performed an IPO in 1997

- Then the alpha will not be there in the future, and we can forget about it