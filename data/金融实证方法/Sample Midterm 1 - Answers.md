# Sample Midterm Exam #1

MGT 295F - Winter 2016

Empirical Methods in Finance

©2016 Alexander Barinov

# 1 Multiple Choice Questions (10 questions, 3 points each)

1. If the value effect is explained by risk, then the value minus growth portfolio should

a Have positive market beta  
b React positively to a sudden increase in dividend yield  
c Have high expected return in the periods of high GDP growth  
d Have lower returns than the CAPM predicts in the periods of increasing market volatility

If value effect is an anomaly, it means that the market beta cannot explain why the returns to value firms and growth firms are different. Hence, the market beta of the value minus growth portfolio can be anything, it does not matter. If the value minus growth portfolio gains in response to a sudden increase in dividend yield (usually a signal of bad times), it is a hedge against recessions, and it is even more puzzling why it has a positive CAPM alpha. If the expected return (and, hence, the risk) of the value minus growth portfolio is high when GDP growth is high (good times) and low otherwise, it is a hedge again. But trailing the CAPM when market volatility increases (usually during market downturns) clearly point towards the value minus growth portfolio being risky, which may explain its positive average CAPM alpha.

2. Mispricing or apparent mispricing should be stronger for

a Volatile firms, small firms, firms with low price impact  
b Small firms, firms with high Roll measure, firms with low institutional ownership  
c Low volatility firms, firms with low bid-ask spread, firms with high Amihud measure  
High uncertainty firms, firms with high institutional ownership, illiquid firms

We are looking for the firms with high limits to arbitrage ("mispricing") or high trading costs ("apparent mispricing"). In (a), firms with low price impact have low trading costs. In (c), low volatility firms have low limits to arbitrage and firms with low bid-ask spread have low trading costs. In (d), firms with high IO have low limits to arbitrage.

3. Assuming that the value effect is caused by risk, you would expect the realized returns to the HML factor to be

a Positively correlated with future labor income and positively correlated with future Treasuries yield  
b Negatively correlated with future labor income and positively correlated with future Treasuries yield  
c Positively correlated with future labor income and negatively correlated with future Treasuries yield  
d Negatively correlated with future labor income and negatively correlated with future Treasuries yield

Risk is losing money just before things turn south - i.e., labor income drops and Treasury yields (and expected inflation) decrease.

4. You are creating a multifactor model with the momentum factor. The momentum factor is the portfolio long in winner firms and short in loser firms. You can interpret this model as the ICAPM

a Only if momentum is mispricing  
b Only if momentum is risk  
The ICAPM does not allow the use of the momentum factor  
d You can use the momentum factor in the ICAPM irrespective of whether you think momentum is risk or mispricing

ICAPM is a risk-based model, in contrast to APT, which just assumes that the factors "are there", and other multifactor models, which may ask the question if the LHS variable is simply related to existing anomalies. All ICAPM factors have to be risk.

5. A portfolio generates an annual return of  $17\%$ , a beta of 1.2 and a standard deviation of  $19\%$ . The market index return is  $12\%$  and has a standard deviation of  $16\%$ . The risk free rate is  $4\%$  per annum. The portfolio return is positively correlated with changes in GDP growth.

a The portfolio beats the CAPM prediction, but not necessarily the ICAPM prediction  
b The portfolio underperforms the CAPM prediction, but not necessarily the ICAPM prediction  
c The portfolio beats both the CAPM prediction and the ICAPM prediction  
The portfolio underperforms both the CAPM prediction and the ICAPM prediction

We can compute the alpha of the portfolio as

$$
\alpha = (\overline {{R e t}} - \overline {{R F}}) - \beta \cdot (\overline {{M K T}} - \overline {{R F}}) = (17 \% - 4 \% ) - 1.2 \cdot (12 \% - 4 \% ) = 3.4 \%
$$

The alpha is positive, hence the portfolio beats the CAPM. The positive correlation with changes in GDP growth means that the portfolio loses in bad

times, when GDP growth dips, which makes it riskier than what the CAPM says. Hence, the portfolio beats the CAPM, but not necessarily ICAPM - if its losses when GDP growth dips are really big, even  $3.4\%$  extra per year may be inadequate compensation.

You can also reach the conclusion that the portfolio beats the CAPM by showing that its Sharpe ratio is greater than the Sharpe ratio of the market (in the CAPM, the market is the mean-variance efficient portfolio with the maximum possible Sharpe ratio):

$$
S _ {p t f} = \frac {17 \% - 4 \%}{19 \%} = 0.684 > S _ {M K T} = \frac {12 \% - 4 \%}{16 \%} = 0.5
$$

6. Consider the economy with two stocks, A and B, with the Roll measures of  $2\%$  and  $1\%$ , respectively, and two investors, X and Y, with the investment horizons of 2 and 4 years, respectively. If the net-of-cost expected return to A and B is  $10\%$  per year, then in the equilibrium, in which one investor holds one stock

a Expected returns to A and B are  $11.99\%$  and  $11\%$  
Expected returns to A and B are  $11\%$  and  $10.49\%$  
Expected returns to A and B are  $10.5\%$  and  $10.25\%$  
Expected returns to A and B are  $10.99\%$  and  $10.5\%$

In the equilibrium,  $X$ , the investor with the shorter investment horizon, holds  $B$ , the stock with the lower spread and receives no abnormal return. His holding costs are  $1\% / 2 = 0.5\%$  per year, which makes the return to  $B$ $10.5\%$ .  $Y$ , the investor with the longer investment horizon, holds the stock with the higher spread and prices it using the holding cost of  $X$ ,  $2\% / 2 = 1\%$ .  $Y$  takes off 1 bp from the  $1\%$  premium to make sure that  $X$  does not want to hold  $A$ , hence the expected return to  $A$  is  $10.99\%$ .

7. Consider the economy with two stocks, A and B, with the Amihud measures of 0.25% and 0.1%, respectively, and two investors, X and Y, with the usual trade size of $7 million and $3 million, respectively. If the net-of-cost expected return to A and B is 12% per year, then in the equilibrium, in which one investor holds one stock

a X holds B and receives the abnormal return of  $0.014\%$  
b X holds B and receives the abnormal return of  $0.7\%$  
c Y holds A and receives the abnormal return of  $0.99\%$  
d Y holds A and receives the abnormal return of  $1.74\%$

In the equilibrium,  $X$ , the investor with the higher trade size, holds  $B$ , the stock with the lower price impact and receives no abnormal return. Hence, (a) and (b) are wrong.  $Y$ , the investor with the smaller trade size, holds the stock with the higher price impact and prices it using the holding cost of  $X$ ,  $7 \cdot 0.25\% = 1.75\%$ .  $Y$  takes off 1 bp from the  $1.75\%$  premium to make sure that  $X$  does not want to hold  $A$ , but  $1.74\%$  is not his abnormal return yet. He needs to take out his holding costs,  $3 \cdot 0.25\% = 0.75\%$ , and the rest,  $1.74\% - 0.75\% = 0.99\%$  will be his abnormal return.

8. Accrual anomaly, first discovered by Sloan (TAR, 1996), finds that low (high) accruals firms have positive (negative) alphas. What of the following suggests that liquidity risk can be an explanation of the accrual anomaly?

a High accruals firms lose value when market illiquidity goes up  
b High accruals firms become less liquid when market gains  
c Low accruals firms become more liquid when market illiquidity goes up  
Low accruals firms covary positively with the factor that buys illiquid firms and shorts liquid firms

First, we exclude  $(d)$ , because the factor measures liquidity, not liquidity risk. The positive covariance to the factor suggests that low accruals firms comove with illiquid firms, but it does not suggest that they, for example, win

or lose in response to changes in market liquidity. Second, we recall that the accrual anomaly says that high (low) accruals have negative (positive) alphas, so we are looking for low (high) risk of high (low) accruals firms. (a) says high accruals firms have high liquidity risk (they suffer losses in bad periods of time). (c) says that low accruals firms are low-risk firms, because good things (high liquidity) happen to them in bad times (when the market is illiquid). (b) is the answer, because it implies that high accruals firms become more liquid (good thing) when market drops (bad times), so they are low-risk firms and that explains their negative alphas.

9. If a certain anomaly is risk, then the correlation between the expected returns to the arbitrage portfolio that is trying to exploit it and earn a positive CAPM alpha and the lagged value of implied volatility of the S&P 500 options (aka the VIX index) should be

a Negative  
b Positive  
c Positive in expansions and negative in recessions  
d Impossible to tell

If an anomaly is risk, exploiting it should mean higher risk, in particular in recessions, when VIX is high. More risk in recessions means higher expected return in recessions, which VIX should be able to predict with a positive sign.

10. Stocks that lost a significant chunk of value in the recent six to twelve months (recent losers) are known to underperform for another year. Assuming that this effect is mispricing, you would expect that

a Recent losers will have positive returns around earnings announcements, and even more so if they were highly volatile before they started losing value  
b Recent losers will have negative returns around earnings announcements, and even more so if they were highly volatile before they started losing

c Recent losers will have positive returns around earnings announcements, but less so if they were highly volatile before they started losing value  
d Recent losers will have negative returns around earnings announcements, but less so if they were highly volatile before they started losing value

Losers continue to lose - hence, they are still overpriced even given the initial loss. The overpricing is stronger for the stocks with high limits to arbitrage and will be corrected at earnings announcements.

# 2 Short Questions (5 questions, 10 points each)

1. Investment-to-capital ratio is known to be higher during expansions (firms invest a lot if demand is high). What is the expected sign of the correlation between expected market return and the lagged value of the aggregate investment-to-capital ratio to be? Explain.

High investment-to-capital ratio means expansion, when risks are low and expected returns are also low. Therefore, high investment-to-capital ration should predict low expected market returns. That is, the correlation has to be negative.

2. You are trying to explain the negative alphas of initial public offerings (IPOs) using Conditional CAPM. What will be your hypothesis about the relation between the CAPM beta of IPOs and lagged values of GDP growth and unemployment rate? Explain.

IPOs have negative CAPM alphas. Therefore, they have to be less risky than what the CAPM thinks. In the conditional CAPM, the only form of low risk is the decrease in the CAPM beta during recessions. GDP growth is low during recessions, hence it has to be positively correlated with the CAPM beta of IPOs to explain the new issues puzzle. The unemployment rate is high in recessions, hence it has to be negatively correlated with the CAPM beta of IPOs.

3. Taking the Carhart model as a benchmark, the performance of Fund M in 2005 was abnormally poor. The manager defends his performance by saying that he was hedging you against the increases in market volatility and default risk. What should have happened to market volatility and default risk during 2005 to make it a valid defense?

If the manager hedges you against market volatility and default risk, the fund should beat the CAPM when those variables increase (because they are high in bad times). Hence, if the fund was trailing the CAPM

in 2005, market volatility and default risk must have declined in 2005. Otherwise mentioning the hedging effort is not a valid defence of the poor performance.

4. You come across a study that claims to have explained the value effect by liquidity risk. The main evidence in the study is that the alpha of the value-minus-growth strategy is reduced if one controls for the "Roll factor" that buys firms with high Roll measure and shorts firms with low Roll measure. What is wrong with the liquidity risk interpretation? What is the correct interpretation of the evidence? What should the study change to make the method consistent with the interpretation?

The evidence says that the value-minus-growth portfolio likely covaries positively with illiquid firms (high Roll measure, the one the factor buys) and covaries negatively with liquid firms (low Roll measure, the one the factor shorts). Hence, the correct interpretation is to say that we explain the value effect by liquidity, pointing out that value firms behave as if they were illiquid and growth firms behave as if they are liquid.

This is not a liquidity risk story, because even if value firms are illiquid and growth firms are liquid, we cannot conclude, say, that value firms will lose value or become illiquid when the market liquidity deteriorates, which would have been the indication of liquidity risk.

An easy way to switch to the analysis of liquidity risk would be to compute the average Roll measure, take the innovation/change of it, and check whether value firms load negatively on that (i.e., if they lose money when the market illiquidity grows) and whether growth firms load positively on that.

5. Consider an economy with two stocks A and B with the Roll measures of  $2.5\%$  and  $1.2\%$ , respectively, and three investors X, Y, and Z with the investment horizons of 2, 4, and 5 years, respectively. What are the two possible equilibria in this economy? Assume that the expected before-cost returns to A and B are 10 and  $13\%$ , respectively.

The two equilibria are: "X and Y hold B, Z holds A" and "X holds B, Y and Z hold A".

In the first equilibrium,  $B$  makes just enough to make sure  $X$  wants to hold it. The cost of holding  $B$  for  $X$  is  $\frac{1.2\%}{2} = 0.6\%$ , hence  $B$  should be making  $13.6\%$ .  $Y$  also holds  $B$ -his costs of doing so are  $\frac{1.2\%}{4} = 0.3\%$ , so he gets abnormal return of  $0.3\%$  from holding  $B$ .

If  $Z$  wants to hold  $A$  alone, then he has to make sure  $Y$  does not want to do that. The cost of holding  $A$  to  $Y$  are  $\frac{2.5\%}{4} = 0.625\%$  and he cannot get  $0.3\%$  on top of that, because otherwise he will try to hold  $A - A$  has to make  $10.92\%$ .

The last thing to do for full credit is to check that in this equilibrium  $Z$  does not want to hold  $B$ . The cost of holding  $A$  to  $Z$  are  $\frac{2.5\%}{5} = 0.5\%$  and the abnormal returns are then  $(10.92\%-10\%) - 0.5\% = 0.42\%$ . The cost of holding  $B$  to  $Z$  are  $\frac{1.2\%}{5} = 0.24\%$  and the abnormal returns are  $(13.6\%-13\%) - 0.24\% = 0.36\%$ . Hence,  $Z$  does not want to hold  $B$ , which is what we want.

In the second equilibrium,  $B$  makes 13.6% again, and  $Y$  would be making 0.3% abnormal return from holding  $B$ , but  $Z$  lets him have  $A$ , and  $Y$  and  $Z$  just have to make sure that  $X$  does not switch to  $A$  too. The costs of holding  $A$  for  $X$  are  $\frac{2.5\%}{2} = 1.25\%$ , hence if the return to  $A$  is 11.24%,  $X$  stays out.

$Z$  is making  $11.24\% - 10\% - 0.5\% = 0.74\%$  abnormal return holding  $A$  and would make  $13.6\% - 13\% - 0.24\% = 0.36\%$  holding  $B$ ,  $Z$  does not want to switch.  $Y$  is making  $11.24\% - 10\% - 0.625\% = 0.615\%$  abnormal return holding  $A$  and would make  $13.6\% - 13\% - 0.3\% = 0.3\%$  holding  $B$ ,  $Y$  does not want to switch.

# 3 Long Question (4 parts, 5 points each)

This question refers to the ICAPM, estimated for Vanguard International Value (VTRIX) fund using the data from January 1999 to December 2009. The numbers in brackets are standard errors.

$$
R e t _ {t} - R F _ {t} = \begin{array}{c} 0. 3 5 \\ (0. 2 4) \end{array} + \begin{array}{c} 0. 8 8 \\ (0. 0 5) \end{array} \left(M K T _ {t} - R F _ {t}\right) + \begin{array}{c} 1. 2 1 \\ (6. 5 5) \end{array} \Delta T B _ {t} - \begin{array}{c} 5. 8 6 \\ (2. 8 8) \end{array} \Delta D I V _ {t}
$$

Looking at the coefficient on the change in the dividend yield, does the fund look riskier than what its market beta implies? Explain.

Dividend yield is high in recessions, so an increase in dividend yield is bad news. The negative slope on DIV suggests that, controlling for the market risk, the fund responds to the bad news by posting negative return, which means that the fund is riskier than what its market beta implies. (Note also that the coefficient is statistically significant).

If dividend yield increases by  $1\%$  and the expected inflation decreases by  $3\%$ , by how much will the fund beat/trail the CAPM?

If dividend yield increases by  $1\%$ , the fund will post  $-5.86\%$  loss on top of the loss coming from the market decline that normally accompanies increases in dividend yield. If expected inflation decreases by  $3\%$ , the Treasury bill rate also decreases by  $3\%$ . The fund will respond by posting  $1.21 \cdot 3\% = 3.63\%$  loss on top of the loss coming from the market decline that normally accompanies decreases in the Treasury bill rate. Hence, if dividend yield increases by  $1\%$  and the expected inflation decreases by  $3\%$ , the fund will underperform the CAPM by  $5.86\% + 3.63\% = 9.49\%$ . (Note: 5.86 and 1.21 in the solution are slopes from the regression above).

Your colleague suggests that the Vanguard fund is a good investment, because the ICAPM above estimates that its alpha is positive. Give two objections.

One obvious objection is that the alpha is not significant  $(0.35 / 0.24 = 1.46;2)$ . The second more subtle objection is that the dividend yield on the market

portfolio is not a return to a tradable asset, hence, the alpha does not have to equal zero and can be anything even if the fund yields no abnormal return.

Another colleague suggest that you throw in the change in GDP as the fourth factor. What sign of the slope on GDP growth would suggest that the fund is even riskier than what you would think looking at the regression above?

Low values of GDP growth mean recessions. Risk means losing money in recessions, i.e., having low return when GDP growth is low. Hence, if the fund is even riskier than what you would conclude from the regression above, the slope on GDP growth should be positive.