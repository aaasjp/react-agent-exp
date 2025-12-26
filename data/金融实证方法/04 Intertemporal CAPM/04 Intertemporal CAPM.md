# Intertemporal CAPM

Professor Alexander Barinov

School of Business Administration  
University of California Riverside

MGT 295F Empirical Methods

# Outline

Consumption CAPM  
2 Intertemporal CAPM  
3 ICAPM and Inflation Risk  
VIX as a Candidate ICAPM Factor  
Volatility Risk and the Value Effect  
6 Factor-Mimicking Portfolio  
Autoregression  
8 Recap

# Consumption is the Ultimate Goal

CAPM says that risk means losses when the market goes down

- What is the most fundamental reason we care about the losses?  
Why do we care more when the market goes down?

- Consumption CAPM answers these two questions

- We care because losses mean lower consumption  
- We care more because during market downturns our consumption is usually low and the marginal utility of consumption is therefore high

# Replace Market with Consumption

- Since in the end we care about consumption, replace the market portfolio in CAPM by aggregate consumption  
CAPM: risk is losses when the market goes down  
- Consumption CAPM: risk is losses when aggregate consumption goes down  
- Consumption CAPM explains why expected market return is high in recessions, while CAPM cannot do it  
- John Cochrane: Consumption CAPM has to be true, because any rational argument about risk is in the end an argument about consumption

# We Need Consumption Proxies

- Consumption is notoriously hard to measure (think about durables, houses, etc.)  
- Instead, we have to use proxies that are correlated with consumption  
- For example, market volatility is high in recessions, when consumption is low  
Hence, market volatility can be one of empirical proxies for consumption (also called state variables)

# What is a Good Proxy?

- Having a good story about why the variable you have in mind is correlated with consumption is good, but not enough  
- But how do we check whether the variable is correlated with consumption if we cannot measure consumption well?  
- What we do have is expected return, which should be proportional to the marginal utility of consumption  
- Hence, only those variables that predict market return should be considered for an ICAPM factor

# ICAPM vs CAPM

- Simple CAPM assumes that all periods are the same and investors do not try to shift consumption from good periods to bad ones  
- ICAPM acknowledges the consumption smoothing desire and argues that the assets that let investors transfer wealth from good to bad periods (by earning relatively low return in good periods and relatively high return in bad periods) should have higher prices and lower expected returns  
- Such assets do not have to gain in bad times, they may only lose not as much

# ICAPM vs Conditional CAPM

- Conditional CAPM acknowledges that periods are different, but still does not consider the desire of investors to smoothen their consumption  
- ICAPM agrees that higher risk during tough times is bad, but points out it is bad because of greater losses in tough times  
- In this sense, ICAPM is broader than Conditional CAPM  
- Though making the market beta time-varying may help in ICAPM as well

# How Our Idea of Risk Has Changed

CAPM: risk is losses when the market declines  
- Conditional CAPM: in addition to that, risk is higher risk exposure when risks increase  
- Consumption CAPM: risk is losses when consumption declines  
- ICAPM: risk is losses in response to bad news

# Example: Inflation Risk

$$
S G _ {t} - R F _ {t} = \begin{array}{c} 0. 4 3 \\ (0. 3 7) \end{array} + \begin{array}{c} 0. 8 9 \\ (0. 5 7) \end{array} \cdot \left(T B _ {t} - T B _ {t - 1}\right)
$$

- Small firms gain when expected inflation increases - is it good?  
- But this also implies that they lose when expected inflation decreases (recession is coming, bad news), which is a risk in ICAPM sense  
However, the coefficient on the expected inflation news is insignificant

# Example: Inflation Risk

$$
S G _ {t} - R F _ {t} = - \begin{array}{c} 0. 2 3 \\ (0. 2 8) \end{array} + \begin{array}{c} 1. 4 2 \\ (0. 0 7) \end{array} \cdot (M K T _ {t} - R F _ {t}) + \begin{array}{c} 0. 8 9 \\ (0. 3 5) \end{array} \cdot (T B _ {t} - T B _ {t - 1})
$$

- Almost all firms, including the market, react positively to the news of higher expected inflation (higher inflation means stockholders rip off bondholders)  
- This is part of the reason why they are risky  
- But if the loading on inflation news is the same for everyone, controlling for the market factor should control for this risk as well

# Example: Inflation Risk

$$
S G _ {t} - R F _ {t} = - \begin{array}{l} 0. 2 3 \\ (0. 2 8) \end{array} + \begin{array}{l} 1. 4 2 \\ (0. 0 7) \end{array} \cdot \left(M K T _ {t} - R F _ {t - 1}\right) + \begin{array}{l} 0. 8 9 \\ (0. 3 5) \end{array} \cdot \left(T B _ {t} - T B _ {t - 1}\right)
$$

- Regression above is more like ICAPM: it asks "do small growth firms bear larger-than-average losses when expected inflation suddenly decreases?"  
- Regression suggests that they do, hence they have a positive exposure to inflation risk  
- Notice that by inflation risk we do not mean losses from inflation - we would not mind them if they are accompanied by gains in deflationary periods  
- ICAPM idea of inflation risk is losses when deflation looms on the horizon

# How to Fix the Alphas

- The main problem with the regression above is that we can use it to see what factor is priced, but we cannot judge its importance (by how much it reduces the alphas)  
- In the time-series regression with a non-traded factor the alpha is not abnormal return and does not have to equal zero  
- We have to make the factor Tradable

- Create a factor-mimicking portfolio by projecting the innovation to the non-traded factor into the return space  
- Create an arbitrage portfolio (like HML - value-minus-growth) and try to relate its returns to innovations to some state variables

# VIX Index

VIX is measures market volatility as implied by the options on S&P 500 index  
- We know that options are more valuable if the volatility of the underlying asset is high  
Hence, market volatility is one of the determinants of the price of the options on S&P 500  
- If we know the prices of the options, we can recover the volatility implied by the prices - implied volatility  
- Implied volatility is what investors expect volatility to be using all information they have  
- VIX - implied volatility of S&P 500 - is the best way to read the market's mind on what the market volatility will be

# Why do We Care about VIX?

- Market volatility is high during downturns - increasing VIX is bad news  
- If VIX increases, we understand that harder times are ahead and we have to save more for the rainy day  
- Which makes us cut current consumption - it would be nice to have an insurance against VIX increases  
- The asset providing such insurance (relatively good returns when VIX increases) will have low expected return

# Why do We Care about VIX?

- Volatility is very persistent - once it jumps up, it will continue to stay high for quite a while  
- Cautious investors will increase their savings facing higher volatility, in order to protect themselves against possible setbacks  
This is called precautionary savings  
- Increased precautionary savings mean decrease in the current consumption, so again we want an insurance against VIX increases  
- The assets that fare relatively well when VIX increases will have low risk and low expected return

# VIX and Recessions

$$
V I X _ {t} = \begin{array}{c} 2 0. 1 \\ (0. 9 6) \end{array} + \begin{array}{c} 6. 1 2 \\ (0. 8 9) \end{array} \cdot R e c _ {t}
$$

- The stories above sound reasonable, but do they go through in the data?  
- VIX is indeed significantly higher in recessions, hence it can be a good proxy for consumption and a valid ICAPM factor  
- The magnitude might be an issue: on average, VIX is only 6.12 points higher in recessions, compared to the 20.1 average in expansions  
- However, we all remember how VIX changed from low teens in the beginning of 2007 to seventies and even eighties in October 2008

# VIX and Market Risk Premium

$$
M K T _ {t} - R F _ {t} = - \begin{array}{c} 0. 5 6 \\ (0. 6 8) \end{array} + \begin{array}{c} 0. 0 5 8 \\ (0. 0 3 2) \end{array} \cdot V I X _ {t - 2}
$$

- If higher VIX means lower consumption, it should also mean higher marginal utility of consumption and therefore higher expected return  
- In order to be a viable ICAPM factor, VIX has to predict market return with a positive sign  
- In the regression above VIX is lagged by two months, because it is forward-looking:  $MKT_{t}$  is market return from (t-1) to t, but  $VIX_{t-1}$  is also volatility between (t-1) and t  
- The coefficient is positive and marginally significant (t-statistic 1.84) - VIX can be an ICAPM factor

# Change in VIX and Market Return

$$
M K T _ {t} - R F _ {t} = \begin{array}{c} 0. 6 3 \\ (0. 2 2) \end{array} - \begin{array}{c} 0. 6 1 \\ (0. 0 7) \end{array} \cdot (V I X _ {t} - V I X _ {t - 1})
$$

- Marginal significance above may seem unconvincing, but we can tease out the effect of VIX on expected returns by looking at the news about VIX  
VIX is almost random walk, so its change is news  
- If VIX unexpectedly turns higher, and higher VIX means higher expected return, then a positive change in VIX should mean negative contemporaneous return  
- The regression shows that it is really the case: t-statistic for the slope is close to -9  
- Or we can just reliably say "unexpected increase in VIX is bad news" - anyway VIX seems a good ICAPM factor

# Main Story

- Growth options are options: they are risky, but you can choose whether you execute them or not  
- Therefore, all else equal, higher volatility should benefit growth firms  
- "All else equal" means "controlling for market beta"  
- Growth firms have higher market betas than value firms and surely lose value in recessions  
- But they perform far better than what the CAPM predicts when volatility goes up, thus providing a valuable insurance

# VIX as Volatility Risk Factor

$$
H M L _ {t} = \begin{array}{l} 0. 6 3 \\ (0. 2 2) \end{array} - \begin{array}{l} 0. 3 9 \\ (0. 0 6) \end{array} \cdot \left(M K T _ {t} - R F _ {t}\right) - \begin{array}{l} 0. 0 6 5 \\ (0. 0 3 6) \end{array} \cdot \Delta V I X _ {t}
$$

- HML buys value and short sells growth, which means that you forego the insurance against VIX increases  
- Hence, HML loading on VIX change should be negative  
- The extra losses when volatility increases explain why investors want higher return from HML than what the CAPM says they should demand  
- The loading of HML on the VIX change is negative, but marginally significant (t-statistic -1.8)  
- Notice than we use change, not level, because it is the change that impacts returns

# VIX as Volatility Risk Factor

$$
H M L _ {t} = \begin{array}{l} 0. 0 3 0 \\ (0. 0 0 7) \end{array} - \begin{array}{l} 0. 3 6 6 \\ (0. 0 2 1) \end{array} \cdot \left(M K T _ {t} - R F _ {t}\right) - \begin{array}{l} 0. 0 3 2 \\ (0. 0 0 8) \end{array} \cdot \Delta V I X _ {t}
$$

- VIX is closer to random walk at daily frequency, hence the daily change in VIX is a better proxy for news about expected market volatility than the monthly change  
- The loading of HML on VIX change stays negative and becomes much more significant

# Magnitude Issues

- HML significantly underperforms the CAPM prediction when VIX unexpectedly rises  
However, the coefficients are very small: the regression with monthly data suggests that the extra loss of HML is 6.5 bp per each point of increase in VIX  
- Even the recent huge change in VIX from 10 to 70 would mean at most an extra  $4\%$  of loss for HML  
- The insurance against such small and improbable loss cannot cost  $7 \%$  per year  
- Notice that in regressions frequency does not matter: the loading on the change in VIX in daily returns should have been the same as in monthly returns, but it is much lower

# Error-in-Variables

- Error-in-variables problem means that if the explanatory variable is measured with noise, its coefficient will be biased downwards  
- Probably VIX contains some measurement error or something people deem irrelevant for pricing stocks  
- Higher loading on VIX change in monthly data strongly suggests that noise may be an issue  
- Noise always creates more trouble in changes than in levels

# When Alpha Has to Be Zero

- Another very important question is just what portion of the value effect can be explained by the exposure to VIX changes  
- If one of the variable on the right-hand side is not return (like change in VIX) is not return, the intercept (alpha) does not have to be zero  
- One reason is that alpha is measured in percentage, and VIX change is in some "points" (cannot add apples and oranges)  
- Another problem is that the average change in VIX can be anything (whereas, e.g., the average excess return to the market is the market risk premium)

# Alpha as Trading Strategy Return

$$
H M L _ {t} = \begin{array}{c} 0. 5 8 \\ (0. 1 2) \end{array} - \begin{array}{c} 0. 2 7 \\ (0. 0 3) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- The regression above suggests a trading strategy with  $7\%$  annual return, no investment, and no risk  
- First, short sell growth firms and use the proceeds to buy value firms  
- Now, for each  $100 turned over in HML buy the market portfolio for$ 27 and short sell Treasury bills for the same amount  
- Alpha is the return from performing those two operations  
- Notice that this strategy requires no money down and its market beta is exactly zero

# Factor-Mimicking Portfolio

- What we need is a combination of stocks that would correlate well with VIX changes  
- This combination is called factor-mimicking portfolio  
- We will use the return to the factor-mimicking portfolio as the second ICAPM factor along with the market factor  
- In this case we can call the intercept alpha again, and test if it is zero  
- Also, noise in VIX will not get into the factor-mimicking portfolio returns - why should noise impact returns?

# Factor-Mimicking Regression

$$
\begin{array}{l} \Delta V I X _ {t} = \begin{array}{c} 0. 0 5 9 \\ (0. 0 3 2) \end{array} - \begin{array}{c} 0. 7 7 \\ (0. 1 2) \end{array} \cdot (L G _ {t} - R F _ {t}) - \begin{array}{c} 0. 7 4 \\ (0. 2 8) \end{array} \cdot (L N _ {t} - R F _ {t}) - \begin{array}{c} 0. 1 7 \\ (0. 2 0) \end{array} \cdot (L V _ {t} - R F _ {t}) + \\ + \begin{array}{c} 0. 1 3 \\ (0. 1 3) \end{array} \cdot \left(S G _ {t} - R F _ {t}\right) + \begin{array}{c} 0. 4 6 \\ (0. 3 4) \end{array} \cdot \left(S N _ {t} - R F _ {t}\right) - \begin{array}{c} 0. 5 2 \\ (0. 3 7) \end{array} \cdot \left(S V _ {t} - R F _ {t}\right) \\ \end{array}
$$

- We use the two-by-three sorts on size and market-to-book as base assets

- L stands for large (above NYSE market cap median), S stands for small (below the median)  
- V is value (bottom  $30\%$  on M/B), G is growth (top  $30\%$  on M/B), N is neutral (middle  $40\%$ )

- FVIX is the fitted part of this regression less the constant  
- FVIX is a zero-investment portfolio that buys Treasuries and short sells everything else but small growth firms

# Factor-Mimicking Recipe

$$
\begin{array}{l} \Delta V I X _ {t} = \begin{array}{c} 0. 0 5 9 \\ (0. 0 3 2) \end{array} - \begin{array}{c} 0. 7 7 \\ (0. 1 2) \end{array} \cdot \left(L G _ {t} - R F _ {t}\right) - \begin{array}{c} 0. 7 4 \\ (0. 2 8) \end{array} \cdot \left(L N _ {t} - R F _ {t}\right) - \begin{array}{c} 0. 1 7 \\ (0. 2 0) \end{array} \cdot \left(L V _ {t} - R F _ {t}\right) + \\ + \begin{array}{c} 0. 1 3 \\ (0. 1 3) \end{array} \cdot (S G _ {t} - R F _ {t}) + \begin{array}{c} 0. 4 6 \\ (0. 3 4) \end{array} \cdot (S N _ {t} - R F _ {t}) - \begin{array}{c} 0. 5 2 \\ (0. 3 7) \end{array} \cdot (S V _ {t} - R F _ {t}) \\ \end{array}
$$

- The regression above tells us exactly how to form FVIX: the slopes are the weights

- We need to short LG (large growth firms) for  $77, short LN for$ 74, short LV for $17  
- The proceeds are invested in Treasuries (actually left with the lender who pays us the Treasury bill rate minus shorting fee)  
- We also buy SG (small growth firms) for $13, financing the purchase by borrowing at the Treasury bill rate plus the lending fee  
- Similarly, we also buy SN for  $46 and short SV for$ 52

# Some More Recipes

- Always use excess returns to the base assets so that the resulting factor is a zero-investment portfolio, just like the market factor  
- Base assets should be different and representative of the economy - then what is uncorrelated with their returns is likely to be unimportant for asset pricing  
- The important part is to estimate the intercept precisely, because it will be responsible for the factor risk premium

# FVIX Portfolio

- FVIX mimics daily changes in VIX, but we cumulate it to monthly frequency  
- The correlation between FVIX and the change in VIX is 0.53  
- Negative FVIX beta is volatility risk (losing money when volatility increases)  
- FVIX factor loses  $1\%$  per month, t-statistic -4.35 - FVIX hedges against volatility risk and has negative market beta  
CAPM alpha of FVIX is -56 bp per month, t-statistic -3.0

# FVIX Explains the Value Effect

$$
H M L _ {t} = \begin{array}{c} 0. 2 1 \\ (0. 1 3) \end{array} - \begin{array}{c} 1. 7 3 \\ (0. 1 1) \end{array} \cdot (M K T _ {t} - R F _ {t}) - \begin{array}{c} 1. 0 0 \\ (0. 0 7) \end{array} \cdot F V I X _ {t}
$$

- The alpha becomes insignificant after we control for volatility risk  
- FVIX beta is large and significantly negative - HML has negative CAPM alpha when VIX increases, which is risky  
- Thus, volatility risk explains the value effect  
- Controlling for volatility risk, growth firms have way higher market betas than value firms - makes sense, growth options are options

# Definition

- We have already talked about persistence and autocorrelation when we talked about predictive regressions and overlapping horizons  
- Autoregression is the regression of a variable on its own lag:

$$
X _ {t} = \boldsymbol {c} + \rho \cdot X _ {t - 1} + \epsilon_ {t}
$$

-  $\rho$  is autocorrelation (if  $X_{t}$  is stable aka stationary and never "explodes")  
- The closer  $\rho$  is to 1, the more persistent (closer to random walk) is the process  
-  $\epsilon_{t}$  is the news one gets about  $X_{t}$  in time  $t$  
- Persistence mean that the news stay in  $X_{t}$  longer

# Change and News: Random Walk

- Consider random walk,  $X_{t} = X_{t - 1} + \epsilon_{t}$  ( $\rho = 1$ )  
- This is an extremely persistent process: shocks stay in  $X_{t}$  forever  
- If  $X_{t}$  goes up by 1, our expectation of both  $X_{t+1}$  and  $X_{t+100}$  go up by 1  
- For random walk, change  $\Delta X_{t} = X_{t} - X_{t - 1} = \epsilon_{t}$  equals to news

# Change and News: Mean-Reversion

- Consider an arbitrary autoregression,

$$
X _ {t} = \rho \cdot X _ {t - 1} + \epsilon_ {t} (0 <   \rho <   1)
$$

- Change,  $\Delta X_{t}$ , is not equal to news then:

$$
X _ {t} - X _ {t - 1} = \epsilon_ {t} - (1 - \rho) \cdot X _ {t - 1}
$$

The first part of the change is the news, the unexpected part  
- The second part is mean-reversion, we expect that  $X_{t}$  will change, because if there is no news, it will just converge to its long-term mean (in this case 0)

# Using Autoregression

- Estimating autoregression and looking at the residuals is the way to back out news about the variable in each moment of time

$$
X _ {t} - X _ {t - 1} = \epsilon_ {t} - (1 - \rho) \cdot X _ {t - 1}
$$

- If the process is persistent ( $\rho$  is close to 1), change and the autoregression residuals will be almost the same  
- You can see in the formula above that the mean reversion piece is small if  $\rho$  is close to 1  
- If news stay in the process forever ( $\rho = 1$ , random walk), there is no mean reversion and change and news are the same

# VIX Example

$$
V I X _ {t} = \begin{array}{c} 0. 8 4 3 \\ (0. 0 8 6) \end{array} + \begin{array}{c} 0. 9 5 9 \\ (0. 0 0 4) \end{array} \cdot V I X _ {t - 1}
$$

- VIX is very persistent at daily frequency - if VIX jumps up, it will stay high for a long time  
- You can think about  $\rho = 0.959$  as the decay rate: in  $t + 1$ ,  $95.9\%$  of the news from  $t$  will still be in VIX  
- The correlation between the residuals from the autoregression and the change in VIX is 0.99  
- They are almost the same, even though their values are far from identical  
- You can redo FVIX using the residuals instead of the change in VIX and observe that the new FVIX will be almost the same as the old one

# Recap: Notion of Risk

CAPM: risk is losses when the market declines  
- Conditional CAPM: in addition to that, risk is higher risk exposure when risks increase  
- Consumption CAPM: risk is losses when consumption declines  
- ICAPM: risk is losses in response to bad news

# Recap: ICAPM Factors

- The state variable has to be correlated with consumption (as proxied for by recessions or market downturns)  
- The state variable has to be correlated with the marginal utility of consumption  
- That is, the state variable has to predict market returns  
- ICAPM uses news about the state variables (can be changes if the variable is persistent), not the variables themselves  
- Add the news measure to the market model: if high values of the state variable are good (bad) and the coefficient of the news variable is positive (negative), then the asset on the left-hand side is riskier than what the CAPM says

# Recap: Factor-Mimicking Portfolio

- Factor-mimicking portfolios help to decide if the loading on (the news about) the state variable is enough to explain the alpha we think about  
- Also, returns to the factor-mimicking portfolio are probably less noisy than the news variable  
- Returns to the factor-mimicking portfolio have to correlate significantly with the news variable we mimic  
- The risk premium of the factor-mimicking portfolio should be sizeable and significant