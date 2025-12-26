# Momentum

Professor Alexander Barinov

School of Business Administration University of California Riverside

MGT 295F Empirical Methods

# Outline

1 Definitions: Momentum and the Like  
Rational Stories  
3 Behavioral Stories  
Is Momentum Real?  
Some Useful Cut-Offs

# Definition of Momentum

- Jegadeesh and Titman (JF 1993) find that recent winners consistently outperform recent losers by more than  $1\%$  per month  
- Basic momentum strategy: each month, sort on cumulative returns in the past six months  
- Then buy winners (top  $10\%$  on past returns) and short losers (bottom  $10\%$  on past returns), then hold for another six months (6-0-6 strategy)  
- The return to the arbitrage portfolio in each month is the average return of six portfolios:

- 1st one - formed last month and held for its first month  
- 2nd one - formed in the month before last and held for its second month  
Etc.

# Definition of Momentum

$$
L _ {t} - R F _ {t} = - \begin{array}{c} 0. 9 1 \\ (0. 2 1) \end{array} + \begin{array}{c} 1. 4 5 \\ (0. 0 6 5) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

$$
W _ {t} - R F _ {t} = \begin{array}{l} 0. 5 8 \\ (0. 1 4 5) \end{array} + \begin{array}{l} 1. 1 7 \\ (0. 0 5) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- Momentum ( $W_{t} - L_{t}$ ) can be as high as  $1.6\%$  per month (more commonly mentioned number is  $1\%$  per month)  
- Momentum comes primarily from the short side - you really have to short losers to get most of the momentum return  
- It can be tough: not many investors are brave enough to lend them to you

# Alpha as Trading Strategy Return

$$
W _ {t} - R F _ {t} = \begin{array}{l} 0. 5 8 \\ (0. 1 4 5) \end{array} + \begin{array}{l} 1. 1 7 \\ (0. 0 5) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- The regression above suggests a trading strategy with  $0.58\%$  monthly return, no investment, and no (systematic) risk  
- First, borrow  $1 at the risk-free rate (or, which is the same thing, short sell Treasuries for$ 1)  
- Second, use the proceeds ( $1) to buy the recent winners ($ Wt portfolio)  
- To hedge the risk of buying winners, short MKT for  $1.17 (the value of the beta) and invest the$ 1.17 in Treasuries  
- Alpha (0.58% per month) is the return from performing those two operations  
- Notice that this strategy requires no money down and its market beta is exactly zero

# Properties of Momentum Portfolios

Extreme winners gain  $50 - 100\%$  in the 6-12 months before the portfolio formation  
Extreme losers lose  $30 - 50\%$  in the same period  
- Which implies that both winners and losers are very volatile  
- Winners and losers are typically small firms (winners are obviously somewhat bigger)  
- Both winners and losers have high betas  
- The beta of losers is higher, since they are distressed and their equity is like an option on the assets

# Short-Term Reversal

- When stock goes up and up, everyone is buying  
- The trades happen at the ask price and there is also temporary price pressure  
- Eventually, the market for the stock will calm down and the price will bounce back (Jegadeesh, JF 1990)  
- If you sort on last month return, the next month bounce back for the firms with the most extreme returns will be large (could be up to  $0.5 - 1\%$ )  
- If you sort on last year return, the bounce back in the first month after you sort will be smaller, at about  $0.25\%$ .

# Trading on Short-Term Reversal?

- The short-term reversal is concentrated among small firms, since those are more likely to have extremely high and extremely low returns  
- You cannot trade on short-term reversal and make a profit: for small firms, round-trip trading costs can easily top  $1 \%$  
- Also keep in mind that you have to both buy and short to capture the  $1 - 2\%$  short term reversal

# Short-Term Reversal and Momentum

- Extreme losers and extreme winners that make up the momentum strategy, usually double or half their price in the six months we look at to form portfolios  
- For such firms, the short-term reversal will be an issue  
- Therefore, skip a month when betting on momentum: form portfolios, wait a month, then buy and sell what you plan to hold (6-1-6 momentum strategy)

# Long-Term Reversal

- If we cumulate returns for the months t-60 to t-13, we will see reversal (DeBondt and Thaler, JF 1985, JF 1987)  
- Past losers eventually gain back part of the losses - sounds like investors got too scared  
- Part winners continue winning for a year, but then slide back - it looks like investors got too excited  
- By the end of year five, all momentum from year one is erased

# Long-Term Reversal and Momentum

Why do we see momentum: because investors underreact or because investors overreact?  
- If investors underreact, recent winners are still underpriced at the portfolio formation date  
- Momentum is then created when the underpricing is erased in the next year  
- If that was the case, we would not have the reversal  
- Then we should buy recent winners and we should not worry about when we close the positions

# Long-Term Reversal and Momentum

- If investors overreact after big gains, recent winners are probably priced right at the portfolio formation date  
- Momentum is then created because they push recent winners higher than the true price  
- When investors realize their mistake, we see the long-term reversal  
- The long-term reversal suggest that we have to close our momentum positions after a year  
- We have to understand also that if we trade on momentum, we are running with the crowd, and the crowd is running astray - we have to know when to stop

# Long-Term Reversal in the Fama-French Model

- Past losers are small and have high book-to-market, so they have to have high return in Fama-French world  
- So, is reversal just size and value effects repackaged?  
Fama and French (JF 1996) show it is  
- They take the long-term reversal portfolio (buy losers, short winners based on the return in the months t-60 to t-13) and regress it returns on the three factors (MKT, SMB, HML)  
- The alpha of the long-term reversal portfolio comes out to be insignificant

# Long-Term Reversal in the Fama-French Model

- How we view the Fama-French model impacts what we think about the implications of long-term reversal for momentum  
- Suppose SMB and HML is risk - then low returns to past winners just reflect their low risk  
- Which means that if we buy recent winners, we will get momentum returns and in a year we will be left with low-risk firms earning fair returns  
- If SMB and HML is risk, momentum is underreaction, and we do not need to sell recent winners after we hold them for a year

# Long-Term Reversal in the Fama-French Model

- Suppose SMB and HML are anomalies: they reflect, in particular, the overpricing of large and growth firms  
- Then long-term reversal means that recent winners become overpriced large growth firms after you hold them for a year  
- Long-term reversal is not an independent anomaly, it is the size and value effects in disguise  
- But you still do not want to hold recent winners longer than a year and have to get rid of them then  
- If SMB and HML are anomalies, momentum is overreaction, and timing your exit is crucial

# Post-Earnings Announcement Drift

- Post-earnings announcement drift (PEAD) - look at the earnings surprise at the announcement, buy two days after the announcement, hold for the next few months  
- Bernard and Thomas (JAR 1989) discovered that stocks with the worst surprise go down by  $2\%$  in the three months after earnings announcement and stocks with the best surprises go up by  $2\%$  in the same period  
- Stocks with worst surprises have negative returns - almost hopeless for a risk-based story

# Measuring Earnings Surprise

- Simplest thing that would work: take year-on-year earnings growth (in percentage), that is, compare Q1 2011 with Q1 2010  
- A bit more intricate: compute the absolute value of the year-on-year earnings growth and divide it by the standard deviation of earnings in the past few years (looks like a t-stat)  
- Alternative 1: compare the current earnings with consensus analyst forecast instead of the earnings a year ago  
- Alternative 2: look at the returns at the announcement (2-3% return usually means you should dig in)

# Trading on PEAD

- The PEAD returns sound really sweet -  $4 \%$ per three months adds up to  $16 \%$ per year!  
However, you have to do 8 (!) round-trip trades per year to get that, so one-way trading costs of  $1\%$  will erase all the profits  
- You buy good surprise firms, short bad surprise firms  
- In two months you sell what you bought and cover the short positions  
- Then you open new positions, etc.  
- Compare it with momentum, when you have to do a similar thing once a year, or with the value effect, where you can do it once every 3-5 years

# Trading on PEAD

- Stocks with the largest earnings surprises tend to be small and volatile (this is how their earnings surprises are so large)  
-  $1 \%$ one- way trading cost is quite plausible for them  
- Since PEAD is not followed by reversal, you do not have to close the positions after two months, but you still need to close them eventually, so it does not matter much when you close them  
- Probably PEAD does not violate EMH after all, since it looks like, net of trading costs, you cannot make money on that  
- Can we have a similar trading strategy that does not involve trading that often?

# Earnings Momentum

- Earnings momentum - look at the earnings surprise in the past calendar quarter, buy at the end of the quarter, hold for the next few quarters  
- Chan, Jegadeesh, Lakonishok (1996) called it earnings momentum and showed it lasts for a year and then dies, without any reversal  
- This strategy earns  $6\%$  per year and, like PEAD, appears to reflect underreaction of investors to earnings surprises

# Earnings Momentum and Price Momentum

- Earnings momentum looks like price momentum: good performance is good performance, and high earnings growth tends to coincide with high returns  
- If earnings surprises and past returns mean the same thing, we can look at the winners with the best and worst earnings surprises, and their future returns will be the same (because for all recent winners earnings surprises are good)  
- Then we would conclude that there is only one momentum, and price momentum and earnings momentum are two manifestations of the same thing

# Earnings Momentum and Price Momentum

Turns out not to be the case: sorting firms with comparable recent returns on earnings surprise still provides the spread in future returns of about  $3\%$  per year  
- This is less than the  $6\%$  per year earnings momentum initially was at, hence price momentum and earnings momentum do overlap, but not completely  
- It also suggest a refinement of the price momentum strategy: buy the recent winners and short recent losers only if they have recent earnings surprises to back up the stock performance  
- That way, you will increase the returns from the price momentum strategy from  $12\%$  per year to  $15\%$  per year

# What We Need to Explain

- Short-term reversal is not tradable and therefore does not violate EMH  
- Long-term reversal is the size effect and the value effect repackaged  
- Hence, short-term reversal and long-term reversal do not need any explanation, risk-based or behavioral  
- PEAD is probably non-tradable as well, and it is similar to earnings momentum, which is tradable  
Hence, we need to address the earnings momentum, and PEAD will take care of itself  
- Price momentum and earnings momentum need an explanation badly, but for risk-based stories it is tough  
Why winners would be much riskier than losers?

# Momentum in 2009

- If you were turning around  $100 in the momentum strategy, in 2009 you would have lost$ 83  
- Very scary result, because 2009 was a very bad year in terms of consumption and economic growth  
- Happened because losers picked up by so much

$$
1 9 6 4 - 2 0 0 8: W _ {t} - L _ {t} = \begin{array}{l} 0. 8 8 \\ (0. 1 6) \end{array} - \begin{array}{l} 0. 0 7 6 \\ (0. 0 7 6) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

$$
1 9 6 4 - 2 0 0 9: W _ {t} - L _ {t} = \begin{array}{l} 0. 7 7 \\ (0. 1 8) \end{array} - \begin{array}{l} 0. 1 3 3 \\ (0. 0 8 8) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

$$
2 0 0 0 - 2 0 0 9: W _ {t} - L _ {t} = \begin{array}{c} 0. 0 3 \\ (0. 5 5) \end{array} - \begin{array}{c} 0. 6 2 \\ (0. 2 0) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- Such things happened before: Chordia and Shivakumar (JF 2002) find that  $W_{t} - L_{t}$  makes 53 bp per month in expansions and -72 bp per month in recessions

# Momentum in Bull and Bear Markets

- Cooper, Gutierrez, and Hameed (JF 2004) show that momentum exists only after cumulative market return in the past three years is positive (bull market)  
- After bear markets (negative cumulative market returns in the past three years) momentum is negative, but statistically insignificant  
- This definition of bull/bear markets is unconventional: e.g., it would classify the rally of 2009 as bear market, since S&P was lower in 2009 than in 2006  
- However, the story worked well in 2009: momentum was negative, just as Cooper et al. would predict

# Momentum in Bull and Bear Markets

- After bear markets, marginal utility of consumption is high (or at least your retirement account is beaten down)  
- The negative momentum returns after bear markets hint that momentum can be risk (think about 2009 again)  
- However, reversal is stronger after the bear market  
- Momentum and reversal seem to be two disjoint phenomena - thus, momentum is not overreaction

# Predicting Momentum

- Main idea (Chordia and Shivakumar, JF 2002): if we can predict momentum returns from something related to business conditions, it means that momentum is most probably caused by changes in risk  
- Label the predicted returns from regressions of the winners-minus-lossers portfolio on macro variables as "risk", see what is left

- What is the story behind "momentum is risk"?  
- Why we cannot come up with an asset-pricing model based on the predictive variables?

- Chordia and Shivakumar find that, on average, nothing is left - so, all momentum is risk-based?

# Predicting Momentum

$$
\begin{array}{l} W _ {t} - L _ {t} = - \begin{array}{c} 5. 6 0 \\ (2. 4 2) \end{array} - \begin{array}{c} 6. 3 5 \\ (3. 0 8) \end{array} D E F _ {t - 1} - \\ - \begin{array}{c} 0. 4 2 \\ (0. 9 9) \end{array} D I V _ {t - 1} + \begin{array}{c} 2. 1 0 \\ (0. 6 1) \end{array} T B _ {t - 1} + \begin{array}{c} 2. 9 4 \\ (0. 7 5) \end{array} T E R M _ {t - 1} \\ \end{array}
$$

- High term spread means recession and high expected momentum (high risk of the momentum strategy) - OK, sounds like risk  
- High inflation (TB yield) means expansion and high expected momentum - does not sound like risk  
- But probably the positive sign is because momentum was stronger in the 70ies, during stagflation - then the positive sign is capturing risk

# Predicting Momentum

$$
\begin{array}{l} W _ {t} - L _ {t} = - \begin{array}{c} 5. 6 0 \\ (2. 4 2) \end{array} - \begin{array}{c} 6. 3 5 \\ (3. 0 8) \end{array} D E F _ {t - 1} - \\ - \begin{array}{c} 0. 4 2 \\ (0. 9 9) \end{array} D I V _ {t - 1} + \begin{array}{c} 2. 1 0 \\ (0. 6 1) \end{array} T B _ {t - 1} + \begin{array}{c} 2. 9 4 \\ (0. 7 5) \end{array} T E R M _ {t - 1} \\ \end{array}
$$

- Low default spread means expansion and high expected momentum (low risk of the momentum strategy)  
- This is because  $W_{t} - L_{t}$  shorts losers, which have high default risk - but  $W_{t} - L_{t}$  does not sound like a risky strategy  
- Same is true for dividend yield: the sign of the slope does not suggest that  $W_{t} - L_{t}$  is a risky strategy (the slope is insignificant though)

# Data Definitions

DEF is the difference in the yields between Baa and Aaa bonds  
- DIV can be calculated in two ways:

- The rigorous way: take the difference between the cum-dividend and the ex-dividend return to an index and sum it up for the previous 12 months (but ex-dividend returns are hard to find)  
- The simple way: check out some ETFs that mimic S&P 500 and look at their current dividend yield; check out Robert Shiller's website for historical data and comparison

- TB - the yield of 1-month (sometimes 3-month) Treasury bills  
- TERM - the difference in the yields between 10-year and 1-year Treasuries

# Explaining Earnings Momentum

- If we forget about the initial  $4 \%$ in two months and negative returns for the worst performers, earnings momentum may be a better target for a risk- based explanation - earnings are "fundamentals"  
- However, keep in mind that in the eyes of the market, recessions are recessions because of high risk (and expected returns), not because of low cash flows  
- Chordia and Shivakumar (JFE 2006) show that earnings momentum predicts future business conditions  
- They form an "earnings momentum factor" (long positive surprise firms, short negative surprise firms) and use it to explain price momentum

# Earnings Momentum Factor

- High earnings momentum predicts low growth of industrial production, consumption, and labor income - does not sound like risk  
- High earnings momentum predicts high inflation - contradicts the first one, but does look like risk  
- So, if we do the earnings momentum strategy ("buy the firms with the best earnings surprises, short the firms with the worst earnings surprises"), we will lose money just before inflation goes down, but we will win just before industrial production and labor income dip  
- In total, does not sound like the earnings momentum factor is a risk factor: I would be more concerned about labor income than deflation

# Earnings Momentum Factor

- Chordia and Shivakumar take the  $W_{t} - L_{t}$  strategy returns and regress them on the three Fama-French factors (MKT, SMB, HML) and their own earnings momentum factor  
- The alpha of the  $W_{t} - L_{t}$  strategy is gone  
- They also do it the other way: take their earnings momentum factor and regress it returns on the three Fama-French factors (MKT, SMB, HML) and  $W_{t} - L_{t}$  (aka the price momentum factor)  
- The alpha of the earnings momentum factor is still there

# What is Price Momentum in the End?

- If we buy Chordia and Shivakumar story that earnings momentum is risk, we should conclude that price momentum is explained by the same sort of risk  
- Namely, if you do "buy winners, short losers", you will lose money just before deflation hits, but you will gain money just before your paycheck takes a hit, and that should scare you  
- Otherwise, we conclude that earnings momentum is the main anomaly, and price momentum is its scaled-up version

# Momentum is Stronger for Small and Young Firms

- Momentum is stronger for small and young firms (Zhang, JF 2006)  
- These stocks are neglected and hard to trade - mispricing should be stronger there  
- Now swap "if" for "only if" - since momentum is stronger for small stocks, momentum is mispricing, and the alpha of the "buy winners, short losers" strategy is free lunch  
- "Stronger momentum for smaller firms" works only for the firms with market cap above $250-500 mln  
- There is no momentum for even smaller stocks

# Momentum is Stronger for Small and Young Firms

- Momentum for younger and smaller firms is upwards of  $2\%$  per month with the standard errors of around 40 bp  
- Momentum for older and larger stocks is about 40 bp per month (insignificant)  
- But we can still pull the trading cost story: probably you will not make money from momentum if you have to trade small and young stocks to get most of the gains from momentum

# Momentum is Stronger for Small and Young Firms

- Stronger momentum for smaller stocks can also mean that you probably cannot profit from momentum net of trading costs and therefore momentum does not violate EMH  
- Also, if momentum is risk-based and exists because of higher sensitivity of winners to business cycle, small and young winners are likely to be the most sensitive  
Hence, stronger momentum for smaller stocks is also consistent with the hypothesis that momentum is risk

# Momentum is Stronger for Volatile and High Turnover Firms

- Momentum is stronger for stocks with high firm-specific volatility (Zhang, JF 2006 - 250 bp per month vs. 80 bp per month)  
- Momentum is stronger for stocks with high turnover (Lee and Swaminathan, JF 2000 - 150 bp per month vs. 50 bp per month)

- Turnover is trading volume over market cap and measures either uncertainty or liquidity

- Stocks with high levels of uncertainty are dangerous to bet on, hence anomalies should be stronger for these firms  
- If momentum is stronger for high volatility/uncertainty stocks, then momentum must be mispricing

# Momentum is Stronger for Volatile and High Turnover Firms

- Trading costs story and rational story can say it all happens because firm-specific volatility is high for small firms  
- However, high turnover firms are large and liquid (but still have high uncertainty)  
- The trading costs story and the risk-based stories cannot easily explain why momentum is stronger for high turnover firms  
- Same caveat as before: the link between momentum and turnover/volatility works only for firms with market cap above $50-100 mln

# Momentum is Stronger for Growth Firms

- Momentum is significantly stronger for growth firms (Asness, FAJ 1997 - 97 bp per month vs 13 bp per month)  
- Investors seem to be overexcited about hi-tech winners and too pessimistic about hi-tech losers  
- On average, growth firms are large - stronger momentum for growth firms does not square well with EMH, since large stocks are cheap to trade  
- Growth also means low non-CAPM risk - stronger momentum for growth firms does not square well with risk-based stories, since sorting low-risk firms on anything, even related to risk, is unlikely to produce a large spread in risk

# Momentum and Earnings Announcements

-  $25\%$  of price momentum is realized around earnings announcements (5% of trading days)  
-  $50\%$  of earnings momentum and post-earnings announcement drift is realized around earnings announcements (5% of trading days)  
- Thus, at least  $25\%$  of price momentum and at least  $50\%$  of earnings momentum and PEAD is mispricing (and, therefore, free lunch)  
- However, you cannot take only this mispricing part, it would be too costly - you have to take the momentum strategy "as is", with all possible risks that may be creating the other part of it

# Trading Cost Story: Pro et Contra

- Pro: momentum strategy implies turnover of  $100\%$  and more - high trading costs  
- Pro: momentum is stronger for small, young, volatile stocks  
- Contra: momentum is stronger for high turnover  
- Contra: the results on the cross-section of momentum are true only for stocks above 20th NYSE market cap percentile  
- Contra: momentum is absent for microcaps (firms in the bottom NYSE market cap quintile)

# Illusory Momentum

- Lesmond, Shill, Zhou (JFE 2001) find that momentum returns are very close to zero or even negative if we subtract the trading costs  
- The trading costs are  $40\%$  bid-ask spread (wide for extreme winners and extreme losers),  $40\%$  interest and commission,  $20\%$  "other" (price impact?)  
- Trading costs naturally increase with size and explain why momentum is stronger for small stocks (for which bid-ask spread turns out to be  $3\%$  and above)  
- Relation between momentum and turnover is driven by high turnover losers, which are very hard to short

# Momentum Out-of-Sample

- Rouwenhorst (JF 1999): momentum is positive in other 12 countries, significant in 11 of them, stronger for small stocks in most of them  
- Jegadeesh and Titman (JF 2001): momentum is still there in 1990s, but was absent before World War II  
- We saw that momentum disappeared in 2000s, but this is because of 2009

# Recap: Momentum

- Momentum is large and stubborn, sometimes losers have negative return and quite often they trail the risk-free rate  
- Rational stories exist, but they are shaky: not all links with the business cycle have the right sign, all evidence is often based on one variable, etc.  
- Momentum is stronger for many classes of stocks, for which behavioral biases are stronger  
- Earnings momentum is strongly concentrated at earnings announcements, price momentum less so  
- Momentum strategies involve high trading costs, probably net profits are much lower or even zero

# Some Facts about Cumulative Returns

- The cut-off for forming momentum portfolios depend a lot on both the market return and market volatility in the past 6-12 months  
- If the market was going up, the cut-offs will drift to the right and vice versa  
- If the market was volatile, the cut-offs for the losers and the winners will be further apart  
- If what follows, I show the cut-offs for four regimes:

- Low-volatility rally, 2003 - market return  $33\%$ , VIX around 20  
- Flat market, 2005 - market return  $7\%$ , VIX around 12  
Big sell-off, 2008 - market return  $-41\%$ , VIX around 50  
High-volatility rally, 2009 - market return  $32\%$ , VIX around 30

# 6-month Cut-Offs

<table><tr><td></td><td>10th</td><td>25th</td><td>75th</td><td>90th</td></tr><tr><td>2003</td><td>-21.2%</td><td>-2.36%</td><td>40.5%</td><td>85.9%</td></tr><tr><td>2005</td><td>-25.6%</td><td>-9.53%</td><td>20.4%</td><td>41.4%</td></tr><tr><td>2008</td><td>-59.7%</td><td>-39.0%</td><td>0.40%</td><td>19.0%</td></tr><tr><td>2009</td><td>-55.7%</td><td>-28.1%</td><td>37.5%</td><td>87.8%</td></tr></table>

- Column labels signify the percentile cutoffs (i.e., in 2008  $25\%$  of NYSE firms had 6-month cumulative returns of  $-39\%$  and below)

# 12-month Cut-Offs

<table><tr><td></td><td>10th</td><td>25th</td><td>75th</td><td>90th</td></tr><tr><td>2005</td><td>-39.1%</td><td>-14.6%</td><td>30.5%</td><td>63.3%</td></tr><tr><td>2008</td><td>-71.5%</td><td>-51.9%</td><td>-3.12%</td><td>20.0%</td></tr><tr><td>2010</td><td>-28.0%</td><td>-2.86%</td><td>60.0%</td><td>123.2%</td></tr></table>

- Column labels signify the percentile cutoffs (i.e., in 2008  $25\%$  of NYSE firms had 12-month cumulative returns of  $-51.9\%$  and below)

# 1-month Cut-Offs

<table><tr><td></td><td>10th</td><td>25th</td><td>75th</td><td>90th</td><td>MKT(-1)</td><td>VIX(-1)</td></tr><tr><td>Nov 2008</td><td>-46.4%</td><td>-33.8%</td><td>-8.74%</td><td>0.45%</td><td>-18.6%</td><td>≈ 60</td></tr><tr><td>May 2009</td><td>-6.68%</td><td>2.30%</td><td>32.0%</td><td>57.1%</td><td>11.1%</td><td>≈ 32</td></tr><tr><td>Oct 2009</td><td>-8.09%</td><td>-1.51%</td><td>12.3%</td><td>23.9%</td><td>4.52%</td><td>≈ 25</td></tr><tr><td>Jul 2010</td><td>-21.3%</td><td>-13.5%</td><td>-0.91%</td><td>3.69%</td><td>-5.22%</td><td>≈ 32</td></tr><tr><td>Dec 2010</td><td>-11.0%</td><td>-3.76%</td><td>7.34%</td><td>16.0%</td><td>0.57%</td><td>≈ 22</td></tr></table>

- You need the cut-offs above to form the momentum strategy and not to suffer from short-term reversal  
- For example, suppose the market was flat last month and you picked a few winners and losers  
- Then you are better off not shorting losers with last month return of  $-11\%$  and below

# Some Facts about Earnings Growth

- The easiest way to construct the earnings momentum portfolios is to sort firms on year-on-year earnings growth  
It turns out that the cut-offs are pretty stable at:

10th percentile: -160% to -180%  
25th percentile: -75% to -100%  
- 75th percentile: +30% to +40%  
- 90th percentile: +140% to +165%

- Notice that, unlike returns, the earnings growth is not bounded from below by  $-100\%$ , because earnings, in contrast to price, can easily become negative

# Some Facts about Turnover

- Turnover is measured in percentage of market cap that changes hands in a month  
- If you need daily turnover, divide the monthly number by 20 or 22  
- If you have daily data, do take the average, because turnover changes greatly day-to-day  
- Normally, turnover is high when the new information hits the market: e.g., on the earnings announcement day it goes through the roof

# Some Trends in Turnover

- Turnover, on average, is increasing steadily, due to high-frequency trading and the like  
- Theoretically, in bad times turnover may be high (if it picks up disagreement/uncertainty) or low (if it picks up liquidity)  
- Empirically, in US it is higher in bad times, but in other markets it can potentially be different

# Turnover Cut-Offs

<table><tr><td></td><td>10th</td><td>25th</td><td>75th</td><td>90th</td></tr><tr><td>2006</td><td>0.05</td><td>0.08</td><td>0.22</td><td>0.35</td></tr><tr><td>2008</td><td>0.09</td><td>0.14</td><td>0.36</td><td>0.56</td></tr><tr><td>2010</td><td>0.06</td><td>0.11</td><td>0.28</td><td>0.45</td></tr></table>

- Rows show the cut-offs (as fractions of market cap) for three years: 2006 (market peak), 2008 (financial panic), 2010 (more or less normal state)  
- Column labels signify the percentile cutoffs (i.e., in 2008  $25\%$  of NYSE firms had monthly turnover of  $36\%$  of market cap and above)