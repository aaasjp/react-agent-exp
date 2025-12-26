# Anomalies: Introduction

Professor Alexander Barinov

School of Business Administration University of California Riverside

MGT 295F Empirical Methods

# Outline

Definition and Ways to Fix  
Rational Stories  
3 Behavioral Stories  
4 Are Anomalies Real?

# Anomaly: Definition

- Anomaly - a regularity in returns that cannot be explained by the benchmark asset-pricing model (most usually CAPM)

$$
H M L _ {t} = \begin{array}{c} 0. 5 9 \\ (0. 1 4) \end{array} - \begin{array}{c} 0. 2 7 \\ (0. 0 4) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- The significantly positive alpha of the HML strategy means that the value effect is an anomaly  
- All tests of CAPM are joint tests of CAPM and EMH  
- The value effect may violate EMH, but not CAPM: yes, alpha is abnormal return, and we can predict abnormal return using market-to-book values everyone knows (behavioral story)  
- The value effect may violate CAPM, but not EMH: the alpha is not the true abnormal return, we need to find additional source of risk (rational explanation)

# Three Sources of the Amazon Alpha

- Probably, the alpha is the compensation for some extra risk that is missing from our models

- Then we can count on the alpha to be there in the future, but we should be cautious trying to make money on it

- Probably, the alpha is the evidence of mispricing, e.g., a positive alpha means that observed returns are "too high", because the price was "too low" to start with

- We should probably expect the alpha to be there in the future, especially if it is the alpha of some broad class of stocks, and we should trade on it and make our (almost) free money

- Probably, the alpha is just luck - for example, Amazon had a clearly unusual fate compared to an average dot-com company that performed an IPO in 1997

- Then the alpha will not be there in the future, and we can forget about it

# Anomaly: Ways to Fix

- We can try to (loosely) tie the anomaly to a plausible source of risk - if we follow the prescribed strategy, something bad will tend to happen to us during bad times  
- We can try to show it is likely to be mispricing - it is stronger for the firms, for which we expect mispricing to be stronger  
- We can try to show that it is a statistical fluke (does not hold outside of the sample it was discovered in) or that the gains are smaller than trading costs

# Ad-Hoc CCAPM and ICAPM

- Develop an ad-hoc version of ICAPM or conditional CAPM that would fix the anomaly  
CCAPM: the beta of the anomalous strategy goes up when market risk is high  
- ICAPM: the anomalous strategy trails the CAPM in bad times  
- Modern tests of CCAPM/ICAPM consider one anomaly at a time, even though the correct CCAPM/ICAPM should price everything  
- Main benefit of this approach - find a particular source of risk behind each anomaly

# Beware of Ad-Hoc Models

- Testing at  $5\%$  level means we will reject the null  $5\%$  of the time even if the null is true  
- If we regress the market (or HML, or anything else) on random draws from normal distribution, we should get the slope of zero  
- But if we make the draws and run the regression 100 times, roughly 5 times we will get significance  
- If we try enough macro variables, something will work as CCAPM/ICAPM by pure chance  
- This false model will break down out-of-sample (in the next few years)  
- Be cautious: e.g., always test if the variables you use predict market risk

# Linking Anomaly to Macro Variables

- If we are not able to come up with the version of CCAPM/ICAPM that will explain the anomaly, i.e. that will produce zero alpha for the anomalous strategy, we can try to show that at least the risk is there  
CCAPM: the beta of the anomalous strategy goes up when market risk is high  
- Instead, we can try to show that expected returns of the strategy go up in bad times

# Linking Anomaly to Macro Variables

- ICAPM: the anomalous strategy trails the CAPM in bad times  
- If we cannot form a decent factor-mimicking portfolio, we can try to show that the current return to the strategy drops with bad news  
- Third way (neither CCAPM nor ICAPM): we can try to show that the returns to the strategy predict bad times, i.e., they are negative right before recession hits

# Value Effect and Default Risk

- Consider a hypothetical example: assume that the value effect can be explained by default risk  
HML is the return to the value minus growth strategy  
High default premium signals recession  
- We have the following three possible way to loosely tie the value effect to default risk

# Value Effect and Default Risk

- We can run  $HML_{t} = \gamma_{0} + \gamma_{1} \cdot DEF_{t - 1}$

-  $\gamma_{1} > 0$  would mean that the risk of HML increases when DEF is high, i.e. in recessions

We can run

$$
H M L _ {t} = \gamma_ {0} + \gamma_ {1} \cdot (M K T _ {t} - R F _ {t}) + \gamma_ {2} \cdot \Delta D E F _ {t}
$$

-  $\gamma_{2} < 0$  would mean that HML trails the CAPM when DEF is high, i.e. in recessions

- We can run  $DEF_{t+1} = \gamma_0 + \gamma_1 \cdot HML_t$

-  $\gamma_{1} < 0$  would mean that HML posts losses right before DEF goes up, i.e. right before recessions

# Fama-French Model

- If the CAPM fails to explain the anomaly, we can check if the Fama-French (FF) model does  
- What we read from the results depends on what we think about the FF factors  
- If SMB and HML are risk factors (FF model is ICAPM), then zero alpha means the anomaly has a risk-based explanation, and SMB and HML beta measure the risk of the anomalous strategy  
- If SMB and HML are APT factors (FF model is APT), then zero alpha means the anomaly does not violate EMH  
- If SMB and HML are themselves anomalies, then zero alpha means that the anomaly is not an independent anomaly, it is the size effect and the value effect repackaged

# Example: "Utilities Anomaly"

- Consider returns to the equal-weighted portfolio of utility companies, denoted  $\text{Util}$

$$
U t i l _ {t} - R F _ {t} = \begin{array}{c} 0. 3 2 \\ (0. 1 3) \end{array} + \begin{array}{c} 0. 5 2 \\ (0. 0 4) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

- Utilities beat the CAPM by 32 bp per month, statistically significant  
- Does it mean that we can earn abnormal return by just checking whether the firm is a utility company?

# Example: "Utilities Anomaly"

$$
\begin{array}{l} U t i l _ {t} - R F _ {t} = - \begin{array}{c} 0. 0 1 \\ (0. 1 0) \end{array} + \begin{array}{c} 0. 6 7 \\ (0. 0 3) \end{array} \cdot (M K T _ {t} - R F _ {t}) + \\ + \begin{array}{l} 0. 0 1 \\ (0. 0 4) \end{array} \cdot S M B _ {t} + \begin{array}{l} 0. 5 6 \\ (0. 0 6) \end{array} \cdot H M L _ {t} \\ \end{array}
$$

- Suppose SMB and HML are risk factors (FF model is a version of the ICAPM)  
- Then we conclude that utilities earn just enough return to compensate us for risk  
- CAPM alpha was significantly positive, because the "size risk" and "value risk" were missing from the model  
- Utilities are riskier that what the CAPM says because they are exposed to the "value risk" (HML beta is positive and significant)

# Example: "Utilities Anomaly"

$$
\begin{array}{l} U t i l _ {t} - R F _ {t} = - \begin{array}{l} 0. 0 1 \\ (0. 1 0) \end{array} + \begin{array}{l} 0. 6 7 \\ (0. 0 3) \end{array} \cdot (M K T _ {t} - R F _ {t}) + \\ + \begin{array}{l} 0. 0 1 \\ (0. 0 4) \end{array} \cdot S M B _ {t} + \begin{array}{l} 0. 5 6 \\ (0. 0 6) \end{array} \cdot H M L _ {t} \\ \end{array}
$$

- Suppose SMB and HML are APT factors (FF model is a version of the APT)  
- Then we conclude that the "utilities anomaly" does not violate EMH and does not create an arbitrage opportunity  
- Suppose SMB and HML are anomalies themselves  
- Then we conclude that the "utilities anomaly" is the value effect in disguise and nothing more

# Starting Point

- It is sufficient to have one arbitrageur in order to have all prices right  
- The arbitrageur will bet against mispricing until it disappears  
- Several crucial assumptions:

- Limitless supply of capital and ability to short (equivalent to "any positive NPV project can be financed")  
- Arbitrageur has the incentive to maximize the alpha even if she trades with investor's money  
- Low trading costs (EMH: prices are right plus-minus trading costs)

# Agency Problems of Arbitrage

- Shleifer and Vishny (JF 1997) point out that arbitrage is performed by a small number of money managers, who play with someone else's money  
- You want your money manager to maximize the alpha, even if it means taking a lot of idiosyncratic risk  
- You will be able to diversify away the idiosyncratic risk, but the money manager has her pay tied to the portfolio performance and has to bear the idiosyncratic risk  
- Professional arbitrageurs tend to underexploit anomalies for the fear of the idiosyncratic risk  
- Anomalies are stronger for stocks with high volatility, uncertainty, etc.

# Agency Problems of Arbitrage

- Suppose the manager correctly identifies the mispricing, but in the next period noise traders only make the mispricing worse  
- The manager will lose money and may face withdrawals up to the point where he will have to close the position against the mispricing, even though the position is more profitable than before  
- Withdrawals of the funds will make arbitrageurs to decrease their bets against the anomalies exactly when the mispricing is the most severe  
- Higher volatility makes withdrawals more likely and makes money managers less willing to bet on anomalies

# Agency Problems of Arbitrage

- Investors use performance as indication of manager's skill and effort  
- If volatility of the portfolio is small, even small losses will be enough as a reliable evidence that the manager is either stupid or lazy  
- If volatility is high, you may have to wait until you lose your last shirt before you get a reliable signal  
- Therefore, investors just do not finance very volatile strategies  
- Anomalies may survive for volatile stocks just because there no funds available to arbitrage the anomalies away

# Limits to Arbitrage Proxies

- Any variable that is plausibly related to stock price volatility and the degree of uncertainty can be used as a proxy for limits to arbitrage  
The long and non-exhaustive list includes:

- Return volatility (high-low spread, standard deviation)  
- Analyst disagreement (same measures for analyst forecasts)  
- Institutional ownership (firms not owned by institutions are "unknown" and "not safe")  
Number of analysts covering the firm (same logic)  
- Size (small firms are volatile, "ignored", "unknown", etc.)

- Short-sale constraints are often (somewhat erroneously) included in the list of proxies for limits to arbitrage

# Limits to Arbitrage and EMH

- Limits to arbitrage are not like fixed trading costs: they tell you how you can create value

- Hedge funds: investors cannot pull money out for the first two or three years  
- Risk management: how you can hedge your bets without foregoing much of the alpha

- Limits to arbitrage are necessary, but not sufficient condition for the existence of anomalies

- If investors were rational, prices would fluctuate within the bounds determined by limits to arbitrage, but prices would be unbiased  
- We need some systematic behavioral bias to create the anomaly, and then limits to arbitrage to protect its existence

# Anomalies in Cross-Section

- Behavioral stories make predictions on the types of firms for which anomalies are stronger  
- Confirming these predictions is useful: we will know what to concentrate on if we decide to profit from an anomaly  
- Behavioral finance also uses this evidence as suggestive that anomalies are mispricing  
- The real statement: "If an anomaly is mispricing, it will be stronger for small (or volatile, or low IO, etc.) firms"

# Anomalies in Cross-Section

- A little cheating: pretend "if" is "only if" and flip it over: "If an anomaly is stronger for small (or volatile, or etc.) firms, then the anomaly is mispricing"  
- This is similar to "if it walks like a duck and it talks like a duck, it is a duck"  
- If we buy that, the stronger anomaly where it should be stronger suggests that the anomaly is mispricing everywhere  
- Then the alpha of the respective trading strategy is free lunch and we should dig in

# Anomalies and

# Earnings Announcements

- If an anomaly is mispricing, it will be partially corrected when the information is revealed  
One example is earnings announcements:

- If something (e.g., value stocks) is underpriced, it will do very well at the announcements  
- If something (e.g., growths stocks) is overpriced, it will do very poorly then

Each firm announces its quarterly earnings four times a year  
- We look at the day of the announcement, the day before (information leakage), and the day after (announcements after the bell)  
- All three are called "earnings announcement days"

# Anomalies and Earnings Announcements

- Earnings announcement days take only 12 days out of 250 trading days in a year (5%)  
- If an anomaly is risk, the earning announcement days are no different than other days, and  $5\%$  out of the anomaly should be realized then  
- LaPorta, Lakonishok, Shleifer, Vishny (JF 1997) sort firms on market-to-book and record only announcement days returns of value and growth stocks  
- They find that about a third of the value effect (4% out of 12% in their sample) is realized around earnings announcements, with growth stocks losing 0.5% and value stocks gaining 3.5%

# Earnings Announcements and Risk

- The concentration of anomalies around earnings announcements is prima facie evidence that at least the part of the anomaly that is realized then is mispricing  
- Probably earnings announcement days are riskier than average  
- They are more volatile for sure, but this volatility is most likely firm-specific and the betas likely do not change at earnings announcements  
- Yet, no risk we know of is large enough to warrant the  $4 \%$ return over 12 days (it will be close to  $90 \%$ annualized!)  
- Also, it is hard to explain by a risk story why growth stocks lose at earnings announcements - does their beta changes from large and positive to large and negative and then back again within the three-day interval?

# Earnings Announcements and Trading Strategies

- If a third of value effect is realized around earnings announcements, this third is your free lunch  
- If you do "buy value, short growth" strategy, a third will be free lunch, two-thirds may be compensation for some risk  
- You cannot have only free lunch though: you can try "buying value, shorting growth" right before the announcements and closing the positions right after the announcements  
- But the trading costs of doing so four times a year will be way larger than all the profits

# Data Mining

- Testing at  $5\%$  level means we will reject the null  $5\%$  of the time even if the null is true  
Academics and practitioners search for anomalies a lot  
- If you sort stocks on thousand variables, in about 50 cases you will have the return spread you cannot explain with the CAPM  
- Out-of-sample test is the answer: take a different period or a different country  
- If you discovered the anomaly because you were lucky, you will not get lucky the second time (because the probability to get lucky is  $5\%$ )

# Trading Costs

- EMH: markets are efficient within the bounds set by trading costs  
- Probably anomalous strategies are so costly to perform that the abnormal return will not be enough to cover trading costs  
- Then anomalies do not violate EMH - they are not real, you cannot make money on them  
- But anomalies have to come from somewhere - there have to be some behavioral biases that create them

# Trading Costs and Anomalies

- If you observe an alpha, take out the bid-ask spread first and see if the alpha is still two standard deviations away from zero  
- Then estimate the price impact: a simple measure would be the Amihud (JFM 2002) ratio  
- Also, if the anomaly is stronger for illiquid firms, it should start you thinking about how likely you are to actually make a profit

# Limits to Arbitrage versus Trading Costs

- Trading costs say: "You cannot profit from trading"  
- Limits to arbitrage say: "You can, but you do not want to"  
- You need cash to trade against market inefficiency, but here are three stories about volatility:

- You go on the margin, but the higher is the volatility, the scarier it is: imagine the price swerves in the wrong way and you get the margin call  
- You open a fund and get the money, but you will not bet the fund on one mispriced stock, because your whole paycheck depends on it (investors would be fine, they can diversify)  
- If your fund is volatile, you will not get the money, because investors cannot control you by watching your performance

# Liquidity Risk

- Consider two stocks: on average, one costs  $0.1\%$  to trade, the other costs  $1\%$  to trade  
- Assume that in bad times liquidity dries up and the trading costs above double  
- You are more likely to liquidate your portfolio in bad times  
- On average, your extra loss from liquidating a position in the second stock is  $0.9\%$  
- In recessions, this extra loss increases to  $1.8\%$ .  
If you go with the second stock, you will lose by  $0.9\%$  more in recessions  
- ICAPM: second stock should have higher return  
This is called liquidity risk

# Common Mistake

- Suppose both value and growth stocks are illiquid  
- Then value minus growth portfolio is also illiquid, no wonder it earns positive alpha  
- Answer #1: both value and growth stocks have sizeable market betas, but the market beta of HML is small and negative: same thing about liquidity betas  
- Answer #2: If growth stocks are illiquid, why they have negative alphas?  
- Liquidity risk explains only the value part of the value minus growth strategy and makes the growth part even more puzzling