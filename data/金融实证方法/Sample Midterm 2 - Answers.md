# Sample Midterm Exam #2

MGT 295F - Winter 2016

Empirical Methods in Finance

©2016 Alexander Barinov

# 1 Multiple Choice Questions (10 questions, 3 points each)

1. Post earnings announcement drift is an anomaly documenting that stocks with positive (negative) earnings surprises have positive (negative) CAPM alphas in the quarter following the earnings announcement. Assume that the post earnings announcement drift is risk. Then

a Realized returns of the stocks with positive earnings surprises should be lower in recessions than realized returns of the stocks with negative earnings surprises, and the same should be true about their expected returns  
b Realized returns of the stocks with positive earnings surprises should be higher in recessions than realized returns of the stocks with negative earnings surprises, and the reverse should be true about their expected returns  
Realized returns of the stocks with positive earnings surprises should be lower in recessions than realized returns of the stocks with negative earnings surprises, and the reverse should be true about their expected returns  
Realized returns of the stocks with positive earnings surprises should be higher in recessions than realized returns of the stocks with negative earnings surprises, and the same should be true about their expected returns

Post earnings announcement drift (PEAD) means that stocks with positive earnings surprises earn abnormally high returns, and stocks with negative earnings surprises earn abnormally low returns. If it is risk, positive earnings

surprise stocks have to be riskier. Then they would either take larger losses in recessions than negative earnings surprise stocks (lower realized returns) or become riskier than negative earnings surprise stocks during recessions (higher expected returns).

2. Mispricing or apparent mispricing should be stronger for

a Volatile firms, large firms, firms with low Roll measure  
b Firms with high Amihud measure, firms with high bid-ask spread, firms with high short interest  
c Low volatility firms, firms with low Amihud measure, firms with high probability to be on special  
d Small firms, firms with high residual institutional ownership, illiquid firms

We are looking for the firms with high limits to arbitrage ("mispricing") or high trading costs ("apparent mispricing"). In (a), both large firms and firms with low Roll measure (high bid-ask spread) do not fit this description. In (c), low volatility firms have low limits to arbitrage and firms with low Amihud measure (low price impact) have low trading costs. In (d), firms with high IO have low limits to arbitrage.

3. Momentum is an anomaly documenting that in the stock market past winners beat past losers not only historically, but also going forward. Assuming that momentum is caused by risk, you would expect the realized returns to the winners-minus-lossers portfolio to be

a Positively correlated with future unemployment and positively correlated with future default premium  
b Negatively correlated with future unemployment and positively correlated with future default premium  
c Positively correlated with future unemployment and negatively correlated with future default premium

# d Negatively correlated with future unemployment and negatively correlated with future default premium

This is the question about momentum predicting business conditions, like in Chordia and Shivakumar (2006). If momentum is risk, the winners-minuslosers portfolio (which captures momentum) should post negative returns before the economy heads down, i.e. before future unemployment and future default premium increase. That is, we are looking for the two negative correlations, which is (d).

4. You are creating a multifactor model with the factor that mimics the changes in unemployment. You can call this model the ICAPM

a Only if unemployment is related to the marginal utility of consumption  
b Only if the unemployment factor earns a significant risk premium  
c Only if unemployment predicts the market risk premium  
d Only if all of the above is true.

(a) is the most fundamental property of an ICAPM factor. Since consumption data have very poor quality, it is impossible to test (a) directly, and (c) is the best way to do it, since we know that the market risk premium is proportional to the marginal utility of consumption (high when it is high, low when it is low). (b) is also necessary for the factor to be an ICAPM factor, because if the risk premium is insignificant, investors probably do not care about the risk source. Hence, the correct answer is (d).

5. Consider a mutual fund with a zero CAPM alpha and negative correlation of returns with returns to high accruals firms. If high accruals firms have negative alphas, then

a The fund is not an attractive investment irrespective of whether the accrual anomaly is risk or mispricing  
The fund is an attractive investment if the accrual anomaly is risk, but not if it is mispricing

The fund is an attractive investment irrespective of whether the accrual anomaly is risk or mispricing  
The fund is an attractive investment if the accrual anomaly is mispricing, but not if it is risk

High accruals firms have negative CAPM alphas. If the fund is negatively correlated with high accruals firms, it should earn a positive CAPM alpha just because of this correlation. If it does not, the managers are doing something wrong, and the fund not an attractive investment no matter how we view the negative alpha of high accruals firms - as risk (high accruals firms have low risk) or as mispricing (high accruals firms are overpriced).

6. A portfolio generates an annual return of  $13\%$ , a beta of 1.25 and a standard deviation of  $19\%$ . The market index return is  $12\%$  and has a standard deviation of  $16\%$ , and the risk free rate is  $4\%$ . The portfolio return is negatively correlated with future values of default premium.

a The portfolio beats the CAPM prediction, but not necessarily the ICAPM prediction  
b The portfolio underperforms the CAPM prediction, but not necessarily the ICAPM prediction  
The portfolio beats both the CAPM prediction and the ICAPM prediction  
The portfolio underperforms both the CAPM prediction and the ICAPM prediction

We can compute the alpha of the portfolio as

$$
\alpha = (\overline {{R e t}} - \overline {{R F}}) - \beta \cdot (\overline {{M K T}} - \overline {{R F}}) = (13 \% - 4 \% ) - 1.25 \cdot (12 \% - 4 \% ) = - 1 \%
$$

The alpha is negative, hence the portfolio underperforms the CAPM prediction. The negative correlation with changes in future values of default premium means that the portfolio loses just before bad times, when default

premium increases, which makes it even riskier than what the CAPM says. Hence, the portfolio underperforms both the CAPM and the ICAPM, because the ICAPM says that it is even riskier and has to make even more.

Alternatively, you can do the Sharpe ratios and conclude that if the fund has a smaller Sharpe ratio than the market portfolio, that it is no good, because a passive investment in the market would be better than investing in the fund.

$$
S _ {p t f} = \frac {13 \% - 4 \%}{19 \%} = 0.47 <   S _ {M K T} = \frac {12 \% - 4 \%}{16 \%} = 0.5
$$

However, it would be wrong to say that the fund trails the CAPM because its Sharpe ratio is smaller, because the CAPM prediction is that the market has the highest Sharpe (and other assets, unless smartly measured, have same or smaller Sharpe ratios.

7. Consider the economy with two stocks, A and B, with the Roll measures of  $1.5\%$  and  $0.5\%$ , respectively, and two investors, X and Y, with the investment horizons of 2 and 5 years, respectively. If the net-of-cost expected return to A and B is  $11\%$  per year, then in the equilibrium, in which one investor holds one stock

a X holds A and receives the abnormal return of  $0\%$  
b X holds B and receives the abnormal return of  $0.25\%$  
c Y holds A and receives the abnormal return of  $0.74\%$  
d Y holds A and receives the abnormal return of  $0.44\%$

In the equilibrium,  $X$ , the investor with the shorter investment horizon, holds  $B$ , the stock with the lower spread and receives no abnormal return. His holding costs are  $0.5\% / 2 = 0.25\%$  per year, which makes the return to  $B$ $11.25\%$ . (a) is wrong, because  $X$  holds  $B$ , not  $A$ , (b) is wrong, because  $X$  receives no abnormal return.

$Y$ , the investor with the longer investment horizon, holds  $A$ , the stock with the higher spread and prices it using the holding cost of  $X$ ,  $1.5\% / 2 = 0.75\%$ .

$Y$  takes off 1 bp from the  $0.75\%$  premium to make sure that  $X$  does not want to hold  $A$ , hence the expected return to  $A$  is  $11.74\%$ .  $0.74\%$ . However,  $0.74\%$  is not the abnormal return  $Y$  gets from  $A$ , because he does have his holding costs,  $1.5\% / 5 = 0.3\%$ . The abnormal return  $Y$  gets from  $A$  is the difference between the two,  $0.74\% - 0.3\% = 0.44\%$ .

8. Consider the economy with two stocks, A and B, with the Amihud measures of 0.35% and 0.2%, respectively, and two investors, X and Y, with the usual trade size of $5 million and $2 million, respectively. If the net-of-cost expected return to A and B is 13% per year, then in the equilibrium, in which one investor holds one stock

Expected returns to A and B are  $13.06\%$  and  $13.04\%$  
Expected returns to A and B are  $13.17\%$  and  $13.1\%$  
Expected returns to A and B are  $13.69\%$  and  $13.4\%$  
Expected returns to A and B are  $14.74\%$  and  $14\%$

In the equilibrium,  $X$ , the investor with the higher trade size, holds  $B$ , the stock with the lower price impact and receives no abnormal return. The holding costs of  $A$  for  $X$  are  $5 \cdot 0.2\% = 1\%$ . Hence,  $B$  should be making  $14\%$ .

$Y$ , the investor with the smaller trade size, holds  $A$ , the stock with the higher price impact and prices it using the holding cost of  $X$ ,  $5 \cdot 0.35\% = 1.75\%$ .  $Y$  takes off 1 bp from the  $1.75\%$  premium to make sure that  $X$  does not want to hold  $A$ . Hence,  $A$  makes  $14.74\%$ .

9. In order for a positive alpha to be explained by risk, the realized returns to positive alpha firms should be

a Positively related to changes in GDP growth and positively related to changes in VIX  
b Positively related to changes in GDP growth and negatively related to changes in VIX

c Negatively related to changes in GDP growth and positively related to changes in VIX  
d Negatively related to changes in GDP growth and negatively related to changes in VIX

To explain a positive alpha by risk, we need to show that positive alpha firms have high risk, i.e., that they lose in response to bad news, which would be a drop in GDP growth and an increase in VIX. Hence, we are looking for a positive relation between the returns to positive alpha firms with GDP growth (returns are bad when GDP growth drops) and a negative relation between the returns to positive alpha firms with changes in VIX (returns are bad when VIX increases).

10. Distress risk puzzle refers to the puzzling tendency of healthy firms to have higher expected returns than distressed firms. What of the following suggests that liquidity risk can be an explanation of the distress risk puzzle?

a Healthy firms gain when market illiquidity goes up  
b Healthy firms become more illiquid when market illiquidity goes up  
Distressed firms become more liquid when market gains  
Distressed firms covary negatively with the factor that buys illiquid firms and shorts liquid firms

The distress risk puzzle says that healthy firms have positive CAPM alphas (we are looking for the exposure of these firms to liquidity risk to explain the alphas) and distressed firms have negative CAPM alphas (we are looking for the ability of these firms to hedge against liquidity risk to explain the alphas).

(a) says that healthy firms gain in bad times, does not sound like risk, hence (a) is wrong. (b) says bad things happen to healthy firms in bad times - it is risk, (b) is the answer. (c) says good things happen to distressed firms

in good times, which implies that bad things will be happening to them in bad times. This is risk, and we need distressed firms (with negative alphas) to be a hedge, so (c) is wrong. (d) is not about liquidity risk at all, it is about liquidity.

# 2 Short Questions (5 questions, 10 points each)

1. Labor income to consumption ratio is known to be lower during recessions (people tap on their savings when they lose their jobs or receive an unusually slim paycheck). What is the expected sign of the correlation between expected market return and the lagged value of the aggregate labor income to consumption ratio to be? Explain.

In recessions, risks are high and expected market return should be high as well. If we know that labor income to consumption ratio is low in recession, we expect a negative correlation between it and expected market return.

2. A mutual fund with a positive CAPM alpha has a positive HML beta and a negative correlation of its abnormal returns with the unexpected changes in the inflation rate. How do both pieces of evidence impact your view of the manager's stock-picking ability?

A positive HML beta means that the fund will have a positive alpha even if the manager has no stock-picking ability, because the manager is just tilting towards value firms that are known to beat the CAPM. Hence, the positive HML beta makes me more sceptical that the positive CAPM alpha means that the manager is a good stock-picker.

A negative correlation of returns with changes in inflation implies gains when inflation dips, which happens in bad times. That is, the negative correlation means that the fund has low risk and therefore should have low returns. That makes the positive alpha more surprising and more suggestive that the manager has some stock-picking ability.

3. The ratio of durables consumption to non-durables consumption (DND ratio) is known to be lower during recessions (consumers delay big-ticket purchases in recessions). The relative short interest (RSI) effect refers to the fact that high RSI firms have negative alphas. What should be the sign of the correlation between the returns

to high RSI firms and the lagged value of the DND ratio in order to help explain the RSI effect?

The RSI effect says that high RSI firms have negative alphas. Hence, if we want to explain the RSI effect, we need to show that these firms are low-risk firms. One way to do it is to show that the risk of high RSI firms is low in bad times. That is, the expected return to these firms has to be low when the DND ratio is low. Which means that we are looking for the positive correlation between the returns to high RSI firms and the lagged value of the DND ratio.

4. Consider an economy with three stocks A, B and C with the Amihud measures of 0.5%, 0.3%, and 0.2%, respectively, and three investors X, Y, and Z with the average trade size of $5 million, $2 million, and $1 million, respectively. What is the equilibrium, in which each investor holds only one stock? Assume that the expected before-cost returns to A, B, and C are 10%, 11%, and 13%, respectively. (20 points)

$X$ , the investor with the highest trading size, holds  $C$ , the stock with the lowest price impact and receives no abnormal return. For  $X$ , the costs of holding  $C$  are  $5 \cdot 0.2\% = 1\%$ . Hence, expected return to  $C$  is  $14\%$ .

$Y$  would earn the abnormal return of  $1\% - 2 \cdot 0.2\% = 0.6\%$  holding  $C$ , so he has to earn  $0.61\%$  holding  $B$ . His costs of holding  $B$  are  $2 \cdot 0.3\% = 0.6\%$ , hence,  $B$  has to earn  $11\% + 0.6\% + 0.61\% = 12.21\%$ .

$Z$  has to make sure that  $Y$  does not hold  $A$  by letting him earn only  $0.6\%$  doing that. The holding costs of  $A$  for  $Y$  are  $2 \cdot 0.5\% = 1\%$ , hence,  $A$  can earn  $10\% + 0.6\% + 1\% = 11.6\%$ .

For  $Z$ , the holding costs of  $A$  are  $1 \cdot 0.5\% = 0.5\%$  and the holding costs of  $B$  are  $1 \cdot 0.3\% = 0.3\%$ . Hence,  $Z$  earns  $1.6\% - 0.5\% = 1.1\%$  holding  $A$  and  $1.21\% - 0.3\% = 0.91\%$  holding  $B$ , and does not want to hold  $B$ , which is what we need. This last paragraph is needed for the full credit.

5. You were estimating the Conditional CAPM for the Disp strategy that buys stocks with low analyst disagreement and shorts stocks with high analyst disagreement and got the following estimation output

$$
D i s p _ {t} = \begin{array}{l} 0. 3 2 \\ (0. 2 2) \end{array} - \begin{array}{l} 0. 8 8 \\ (0. 2 5) \end{array} (M K T _ {t} - R F _ {t}) + \begin{array}{l} 0. 4 6 \\ (0. 0 9) \end{array} (M K T _ {t} - R F _ {t}) \cdot D I V _ {t - 1} - \begin{array}{l} 0. 3 8 \\ (0. 1 0) \end{array} (M K T _ {t} - R F _ {t}) \cdot D E F _ {t - 1}
$$

Looking at the signs of the coefficients on  $(MKT_{t} - RF_{t})\cdot DEF_{t - 1}$  and  $(MKT_{t} - RF_{t})\cdot DIV_{t - 1}$ , does the strategy look riskier than what the static CAPM implies? Explain.

The coefficient on  $(MKT_{t} - RF_{t})\cdot DIV_{t - 1}$  means that the risk of Disp increases in bad times, when DIV is high, which makes Disp riskier than what the static CAPM says. The coefficient on  $(MKT_{t} - RF_{t})\cdot DEF_{t - 1}$  means that the risk of Disp decreases in bad times, when DEF is high, which makes Disp less risky than what the static CAPM says.

# 3 Long Question (4 parts, 5 points each)

This question refers to the Conditional CAPM, estimated for the strategy that buys stocks with low idiosyncratic volatility and shorts stocks with high idiosyncratic volatility (IVol). The regression uses the data from January 1986 to December 2006. The numbers in brackets are standard errors.

$$
I V o l _ {t} = \begin{array}{c} 0. 9 9 \\ (0. 3 1) \end{array} - \begin{array}{c} 0. 8 1 4 \\ (0. 1 2 5) \end{array} \left(M K T _ {t} - R F _ {t}\right) + \begin{array}{c} 0. 0 2 2 \\ (0. 0 0 9) \end{array} \Delta V I X _ {t - 1} \cdot \left(M K T _ {t} - R F _ {t}\right)
$$

Does the strategy look riskier than what the static CAPM would imply? Explain.

The Conditional CAPM above suggests that the beta of the IVol strategy is high when VIX increases. Since VIX is high in recessions, when consumption is low, this evidence means that the risk of the IVol strategy is high in bad times, and the IVol strategy is therefore riskier than what the static CAPM says.

According to the Conditional CAPM, does the strategy earn statistically significant abnormal return? Do you expect this abnormal return to be higher or lower in the static CAPM? Explain.

Yes, the alpha (aka average abnormal return) is statistically significant:  $0.99 / 0.31 = 3.18 > 2$ . Since in the previous question we found out that the fund is riskier than what the static CAPM says, the alpha in the static CAPM will be even more positive. The compensation for the extra risk discovered by the Conditional CAPM will be viewed by the static CAPM as some extra return the strategy earns for no good reason, and this part of expected return from the Conditional CAPM will become part of the static CAPM alpha.

In October 2008, VIX increased from 39.39 to 59.89. According to the regression above, what should be the value of the market beta of the IVol strategy in November 2008?

$$
\beta_ {1 1 / 0 8} = - 0. 8 1 4 + 0. 0 2 2 \cdot \Delta V I X _ {1 0 / 0 8} = - 0. 8 1 4 + 0. 0 2 2 \cdot (5 9. 8 9 - 3 9. 3 9) = - 0. 3 6 3
$$

Your colleague suggests that the alpha of the IVol strategy may be due to the fact that the beta of the IVol strategy is also correlated with past changes in the default premium. If your colleagues are right, what should be the sign of the correlation?

If we want to explain the alpha from the Conditional CAPM above, we have to show that the beta of the IVol strategy increases in recessions even more than what the Conditional CAPM above implies. Default premium is high in recessions, and changes in default premium during recessionary periods should be mostly positive. These positive changes should coincide with higher values of the beta of the IVol strategy. Thus, in order to explain the positive alpha, the correlation between the beta of the IVol strategy and the changes in default premium should be positive.