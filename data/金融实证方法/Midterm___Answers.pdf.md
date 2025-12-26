# Solutions to Midterm Exam

MGT 295F - Winter 2021

Empirical Methods in Finance

©2021 Alexander Barinov

# 1 Multiple Choice Questions (10 questions, 3 points each)

1. A stock generates an annual return of  $16\%$ , a beta of 1.6 and a standard deviation of  $40\%$ . The market index return is  $12\%$  and has a standard deviation of  $12\%$ , and the risk free rate is  $4\%$ . The stock's return is positively correlated with future values of GDP growth.

a The stock beats the CAPM prediction, but not necessarily the ICAPM prediction  
b The stock underperforms the CAPM prediction, but not necessarily the ICAPM prediction  
c The stock beats both the CAPM prediction and the ICAPM prediction  
The stock underperforms both the CAPM prediction and the ICAPM prediction

We can compute the alpha of the stock as

$$
\alpha = (\overline {{R e t}} - \overline {{R F}}) - \beta \cdot (\overline {{M K T}} - \overline {{R F}}) = (1 6 \% - 4 \% ) - 1.6 \cdot (1 2 \% - 4 \% ) = - 0.8 \%
$$

The alpha is negative, hence the stock trails the CAPM. The positive correlation with future values of GDP growth that the stock loses just before the GDP growth drops and the economy as whole dips, which makes it riskier than what the CAPM says. Hence, the stock also trails the ICAPM - ICAPM finds the stock is even riskier than what the CAPM says and would

peg its expected return even higher than the CAPM, and the stock already underperforms even the CAPM prediction.

2. If a certain anomaly is risk, then the correlation between the realized returns to the arbitrage portfolio that is trying to exploit it and earn a positive CAPM alpha and the current level of aggregate investment should be

a Negative  
b Positive  
c Positive in expansions and negative in recessions  
d Impossible to tell

Current level of any variable has two components: expected and unexpected, which pull returns in different directions, so (d) is the answer. In particular, if aggregate investment is expectedly high, then we are in a good period with low expected (and realized, if no news arrive) returns. If aggregate volatility is unexpectedly high, then it is good news and realized returns will be high. Since "high level of aggregate investment" can mean both situation, we are not sure whether it will correspond in the data to high or low returns.

3. Accrual anomaly, first discovered by Sloan (TAR, 1996), finds that low (high) accruals firms have positive (negative) alphas. What of the following suggests that liquidity risk can be an explanation of the accrual anomaly?

a High accruals firms become illiquid when the average Roll measure in the market jumps up  
b Low accruals firms have higher bid-ask spread when average Amihud measure in the market goes up  
c High accruals firms have higher price impact when market loses  
Low accruals firms covary positively with the factor that buys illiquid firms and shorts liquid firms

We are looking for either high liquidity risk of low accruals firms (which have positive alphas) or low liquidity risk of high accruals firms (which have negative alphas). (b) fits the bill: it says that low accruals firms become illiquid when the market becomes illiquid.

(a) says the same about high accruals firms (coupling high liquidity risk with negative alphas, which only exacerbates the anomaly). (c) also says that high accruals firms have high liquidity risk: a bad thing (low liquidity) happens to them in a bad period of time (when market dips). (d) is not about liquidity risk, but rather liquidity, because the factor from (d) has no apparent link with the market liquidity or the state of the economy.

4. Consider the economy with two stocks, A and B, with the Roll measures of  $2.1\%$  and  $1.5\%$ , respectively, and two investors, X and Y, with the investment horizons of 3 and 6 years, respectively. If the net-of-cost expected returns to A and B are  $12\%$  and  $15\%$  per year, respectively, then in the equilibrium, in which one investor holds one stock

a Expected returns to A and B are  $11.5\%$  and  $14.24\%$  
Expected returns to A and B are  $14.1\%$  and  $16.5\%$  
Expected returns to A and B are  $12.69\%$  and  $15.5\%$  
Expected returns to A and B are  $12.7\%$  and  $15.49\%$

$X$ , the investor with the shorter horizon, holds  $B$ , the stock with the smaller bid-ask spread, and receives no abnormal return. For that to happen,  $B$  has to make just enough to compensate him for his holding costs,  $1.5\% / 3 = 0.5\%$  per year. Thus,  $B$  should make  $15.5\%$ .

$Y$ , the investor with the longer horizon, holds  $A$ , the stock with the larger bid-ask spread. He prices that using the holding costs of  $X$ ,  $2.1\% / 3 = 0.7\%$  and takes 1 bp off to make sure that  $X$  does not want to hold  $B$ . Hence,  $A$  has to make  $12\% + 0.7\% - 1$  bp = 12.69%.

5. Consider the economy with two stocks, A and B, with the Amihud measures of  $0.5\%$  and  $0.2\%$ , respectively, and two investors, X and Y, with the usual trade size of $5

million and $3 million, respectively. If the net-of-cost expected returns to A and B are 11% per year and 12% per year, respectively, then in the equilibrium, in which one investor holds one stock

a X holds A and receives the abnormal return of  $0.59\%$  
b X holds A and receives the abnormal return of  $0.99\%$  
c Y holds A and receives the abnormal return of  $0.59\%$  
d Y holds A and receives the abnormal return of  $0.99\%$

$X$ , the investor with the larger trade size, holds  $B$ , the stock with the smaller price impact, and receives no abnormal return. Thus, (a) and (b) are wrong.  $Y$ , the investor with the smaller trade size, holds  $A$ , the stock with the larger price impact and prices it using the  $X$ 's holding costs,  $5 \cdot 0.5\% = 2.5\%$ . He takes off 1 bp to make sure that  $Y$  does not want to hold  $A$ .  $X$ 's holding costs for  $A$  are  $3 \cdot 0.5\% = 1.5\%$ . Hence, his abnormal return is the premium he receives,  $2.49\%$ , less his holding costs,  $1.5\%$ , that is, his abnormal return is  $0.99\%$ .

6. Assuming that negative alphas are caused by risk, you would expect the returns to a negative alpha portfolio to be

a Positively correlated with future dividend yield and positively correlated with future average wages  
b Positively correlated with future dividend yield and negatively correlated with future average wages  
c Negatively correlated with future dividend yield and positively correlated with future average wages  
d Negatively correlated with future dividend yield and negatively correlated with future average wages

Risk is losing right before the economy goes down (and both dividend yield and average wages drop). A negative alpha portfolio should have low risk and thus do the opposite - go up when dividend yield and average wages drop.

7. You are creating a new ICAPM factor, which is mimicking changes in average house prices in US. To be a valid factor, this factor has to

a Earn positive average return and be negatively correlated with lagged Treasury bill rate  
b Earn positive average return and be positively correlated with lagged Treasury bill rate  
c Earn negative average return and be negatively correlated with lagged Treasury bill rate  
d Earn negative average return and be positively correlated with lagged Treasury bill rate

The factor, by construction, earns bad returns in bad times, when house prices go down. That sounds like risk, hence, the factor return should be positive. One way to be risky is to have high risk when Treasury bill rate is low, since the Treasury bill rate is known to be lower in bad times. Thus, the correct answer is (a).

8. Mispricing or apparent mispricing should be stronger for

a Volatile firms, small firms, firms with low Roll measure  
b Firms with low Amihud measure, firms with high bid-ask spread, firms with high short interest  
c Volatile firms, firms with high Amihud measure, firms with low shorting fees  
d Small firms, firms with low institutional ownership, illiquid firms

We are looking for the firms with high limits to arbitrage ("mispricing") or high trading costs ("apparent mispricing"). In (a), firms with low Roll measure (low bid-ask spread) do not fit this description. In (b), firms with low Amihud measure (low price impact) have low trading costs. In (c), firms with low shorting fees have low trading costs (they are easy to short).

9. Accrual anomaly, first discovered by Sloan (TAR, 1996), finds that low (high) accruals firms have positive (negative) alphas. Assume that the accrual anomaly can be explained by the conditional CAPM. Then

a During recessions, the CAPM beta of high accruals firms has to be smaller than the CAPM beta of low accruals firms, to explain why high accruals firms have lower risk on average  
b During recessions, the CAPM beta of high accruals firms has to be larger than the CAPM beta of low accruals firms, to explain why high accruals firms have lower risk on average  
c During recessions, the CAPM beta of high accruals firms has to be smaller than the CAPM beta of low accruals firms, to explain why high accruals firms have higher risk on average  
During recessions, the CAPM beta of high accruals firms has to be larger than the CAPM beta of low accruals firms, to explain why high accruals firms have higher risk on average

The accrual anomaly says that high accruals firms have low alpha (i.e., low risk). Hence, (c) and (d) are wrong. (b) says that high accruals firms

are riskier than low accrual firms (their beta is higher in recessions), which cannot explain why high accruals firms have low returns. (a) says that high accruals firms are less risky (their beta is lower in recessions), which is what we need.

10. Diether, Malloy, and Scherbina (JF 2002) discovered the analyst disagreement effect: the higher is analyst disagreement about the firm's earnings, the lower is its CAPM alpha. Assuming that the analyst disagreement effect is mispricing, you would expect that

a Low disagreement firms will have positive returns around earnings announcements, and even more so if they have low Amihud measure  
b Low disagreement firms will have negative returns around earnings announcements, but less so if they have low Amihud measure  
c Low disagreement firms will have positive returns around earnings announcements, but less so if they have low Amihud measure  
d Low disagreement firms will have negative returns around earnings announcements, and even more so if they have low Amihud measure

The analyst disagreement effect means that low disagreement firms beat high disagreement firms on the risk-adjusted basis, i.e., low disagreement firms have positive alpha and are underpriced. Hence, their value should increase at earnings announcements, when investors learn that low disagreement firms better than they thought. The underpricing and the magnitude of the gain at earnings announcements will be higher for the firms that are more costly to trade, e.g., the firms with high Amihud measure (high price impact).

# 2 Short Questions (3 questions, 10 points each)

1. Michaelly, Thaler, and Womack (JF 1995) show that dividend initiations are followed by positive abnormal long-run stock performance and dividend omissions are followed by negative abnormal long-run stock performance. If we form the portfolio long in dividend initiators and short in dividend emitters, what will be our expectation of the correlation of its realized returns with the lagged and future values of the industrial production growth? Explain your answer.

The arbitrage portfolio long in dividend initiators and short in dividend emitters has positive abnormal returns. If we are to find a risk-based explanation, we should show why holding this portfolio means high risk.

When we look at the portfolio return correlation with lagged values of industrial production growth, we look at the behavior of expected returns (aka risk) over the business cycle. If the arbitrage portfolio has positive abnormal returns, its risk should be higher in recessions, when industrial production growth is low. Hence, in the regression of the arbitrage portfolio returns on lagged values of industrial production growth the coefficient should be negative.

Another source of risk would be losses just before the recessions - i.e., a risky portfolio will react very negatively to bad news about industrial production growth, which will appear in the industrial production growth numbers in the future. Hence, in the regression of the arbitrage portfolio returns on the future values of industrial production growth the coefficient should be positive.

2. You have noticed that the zero-investment portfolio buying firms that do not invest a lot and shorting firms that do invest a lot has positive and significant CAPM alpha. The next regression you ran was the two-factor model with the market factor and the HML factor, and in this model the investment-based arbitrage portfolio turned out to have an insignificantly negative alpha. What do you conclude if you believe that the value effect is risk? How does the conclusion change if you believe that the value effect is mispricing?

If the value effect is risk, than HML (which is essentially the value minus growth portfolio) is a risk factor. The fact that adding it to the market model eliminates the alpha of the investment strategy means in this case that the CAPM alpha of the investment strategy is not abnormal return, but rather a fair compensation for the "value risk".

If you believe that the value effect is mispricing, you would conclude from the insignificant alpha of the two-factor model that the "investment anomaly" is just another reincarnation of the value effect.

3. The Roll measure of Delta Airlines (DAL) is  $1.2\%$ , the Amihud measure of Delta Airlines is  $0.009\%$ . What is the dollar cost of buying $50M worth of Delta shares in one day? Assume that the true price is at the midpoint and the price impact starts at the ask.

You lose half of the bid-ask spread when you buy every share of DAL. The Roll measure measures the bid-ask spread. Hence, you lose 0.006·$50M = $300K on the bid-ask spread.

Then the price impact happens. On the first lot, you lose nothing. By the time you trade the last lot, the price has gone up by  $0.009\% \cdot 50 = 0.45\%$  (0.009% is the Amihud measure). On average, you lose half of this number, or, in dollars,  $0.0045 \cdot \\(50M = \$ 112.5K\).

The total loss of the one-way trade is  $300\mathrm{K} +$ 112.5K = $412.5K.

# 3 Longer Question (20 points)

Consider an economy with three stocks A, B and C with the Amihud measures of  $0.4\%$ ,  $0.2\%$ , and  $0.1\%$ , respectively, and three investors X, Y, and Z with the average trade size of $4 million, $3 million, and $2 million, respectively. The investors also have different investment horizons of 5 years, 3 years, and 1 year, respectively. What is the equilibrium, in which each investor holds only one stock? Assume that the expected before-cost returns to A, B, and C are  $11\%$ ,  $10\%$  and  $12\%$ , respectively. (20 points)

The table below tabulates the holding costs for each investor and each

stock. The holding costs are the price impact the investor will create trading as much as he usually does (the trade size times the Amihud measure) spread out over the investment horizon (divided by the respective number of years).

<table><tr><td></td><td>A</td><td>B</td><td>C</td></tr><tr><td>X</td><td>4·0.4% / 5 = 0.32%</td><td>4·0.2% / 5 = 0.16%</td><td>4·0.1% / 5 = 0.08%</td></tr><tr><td>Y</td><td>3·0.4% / 3 = 0.4%</td><td>3·0.2% / 3 = 0.2%</td><td>3·0.1% / 3 = 0.1%</td></tr><tr><td>Z</td><td>2·0.4% / 1 = 0.8%</td><td>2·0.2% / 1 = 0.4%</td><td>2·0.1% / 1 = 0.2%</td></tr></table>

$Z$  turns out to be the one with the highest trading costs, because even though he trades little, he trades fast. He will hold  $C$ , the low-cost stock, and  $C$ 's return will be  $12\% + 0.2\% = 12.2\%$ .

$Y$  will hold  $B$ . He would make  $0.2\% - 0.1\%$  holding  $C$ , so he will ask for  $0.11\%$  abnormal return from  $B$ , making its return  $10\% + 0.11\% + 0.2\% = 10.31\%$ , where  $0.2\%$  is  $Y$ 's holding cost for  $B$ .

$X$  will hold  $A$ . He will make sure that  $Y$  does not hold it, because if  $Y$  does,  $Y$  will make only  $0.1\%$ . Hence, the premium to  $A$  is  $0.4\%$  ( $Y$ 's holding cost for  $A$ ) plus  $0.1\%$ . That is,  $A$  will make  $11.5\%$ .

$X$  will make  $0.5\% - 0.32\% = 0.18\%$  holding  $A$  and  $0.31\% - 0.16\% = 0.17\%$  holding  $B$ ,  $X$  does not want to hold  $B$ .

# 4 Long Question (4 parts, 5 points each)

This question refers to the predictive regression, estimated for the Turn strategy that buys stocks with low turnover and shorts stocks with high turnover. The regression uses the data from January 1986 to December 2010. The numbers in brackets are standard errors.

$$
T u r n _ {t} = - \begin{array}{c} 1. 7 3 \\ (1. 9 3) \end{array} - \begin{array}{c} 1. 4 1 \\ (0. 7 0) \end{array} \cdot D I V _ {t - 1} + \begin{array}{c} 0. 7 7 \\ (0. 3 8) \end{array} \cdot T B _ {t - 1}
$$

Looking at the coefficients on  $DIV_{t-1}$  and  $TB_{t-1}$ , does the Turn strategy look riskier than what the static CAPM implies? Explain.

In the efficient market, the predictive regression above predicts risk, because under EMH one cannot predict  $\text{News}_t$  with  $\text{DIV}_{t-1}$  and  $\text{TB}_{t-1}$ . Hence, we read from the regression above that the risk of Turn is low when DIV is high and TB is low, i.e. in recessions. Low risk is desirable, hence Turn is less risky than what the CAPM says.

Partial credit: Up to 3 points for each slope, 5 points maximum. 2 points only for "Turn makes positive returns, so it has to be riskier than what the CAPM says" or for ICAPM-type of reasoning "DIV is high in recessions, and Turn seems to make low returns when DIV is high, so Turn is risky"

Can you interpret the intercept as the alpha aka abnormal return? Why or why not?

No, because in order to hedge out the exposure to DIV, you would have to buy "dividend yield from the last period", which is impossible.

Partial credit: Depending on how close the answer is.

In July 2011, TB was at 0 and DIV was at about 2. What was the expected return to the Turn strategy in August 2011?

The expected return was  $-1.73 - 1.41 \cdot 2 + 0.77 \cdot 0 = -4.55\%$ .

Partial credit: Depending on how close it is.

How would your interpretation of the answer to the previous question would differ in the efficient and inefficient market? (Hint: Think about whether the answer gives you a buy/sell signal and/or gives you any gauge of the risk of Turn in August 2011).

The return of Turn is risk plus news,  $\text{Turn}_t = \text{Risk}_t + \text{News}_t$ .

In the efficient market, we can only use  $DIV_{t-1}$  and  $TB_{t-1}$  to predict  $Risk_t$ . We will conclude from the previous answer that the risk premium of Turn in August 2011 was  $-4.55\%$  per month, that is, Turn was an extremely good hedge.

In the inefficient market, we can use  $DIV_{t-1}$  and  $TB_{t-1}$  to predict  $News_t$ . Hence, the expected return of  $-4.55\%$  would be a very strong sell signal (i.e., in

August 2011 we need to flip the Turn strategy and start buying high turnover firms and short low turnover firms).

Partial credit: Up to 3 points for the second and third paragraphs, 5 points maximum.