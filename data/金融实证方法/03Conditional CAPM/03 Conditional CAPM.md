# Conditional CAPM

Professor Alexander Barinov

School of Business Administration University of California Riverside

MGT 295F Empirical Methods

# Outline

Conditional CAPM: Theory  
Empirical Setup  
Empirical Results  
4 Changing Beta and Hedging

# Changing Risk Argument

CAPM: risk premium for a stock is its beta times the market risk premium  
- Your investment can become more risky because

- The market as a whole becomes more risky (expected market return increases)  
- The risk exposure (aka market beta) of your investment increases

- Higher risk during risky (bad) times is undesirable, hence investors would appreciate stocks with procyclical betas (low in recessions, high in booms)  
- Such stocks will have high prices and low expected returns

# Market Timing Argument (ICAPM)

- Increase in risk means higher expected returns and decline in price  
- Stocks with larger increases in risk during recessions suffer larger losses, and losses during bad times are undesirable  
- Stocks with procyclical betas witness smaller increase in risk and smaller losses during recessions, which makes investors want them  
- These stocks are natural market timers: they load less on the market factor when the market goes down and load more on it when the market goes up  
- Stocks with procyclical betas will have high prices and low expected returns

# Static CAPM vs Conditional CAPM

CAPM is a one-period model, but the world is multi-period  
- When we estimate CAPM, we assume that all periods are about the same and the CAPM holds on average  
- Conditional CAPM assumes that CAPM holds period-by-period (but may not hold on average)  
- Conditional CAPM lets betas and risk premiums vary across time  
- Empirically, we use time-varying betas, because the market risk premium will vary anyway

# Stock A: Countercyclical Beta

<table><tr><td></td><td>Market risk premium</td><td>Stock beta</td><td>Stock risk premium</td></tr><tr><td>Recession (p=1/4)</td><td>12%</td><td>2</td><td>24%</td></tr><tr><td>Expansion (p=3/4)</td><td>4%</td><td>2/3</td><td>8/3%</td></tr><tr><td>Average</td><td>6%</td><td>1</td><td>8%</td></tr><tr><td>Static CAPM</td><td>6%</td><td>1</td><td>6%</td></tr></table>

- Stock A has countercyclical beta:  $\beta_{A} = 2$  in recessions,  $\beta_{A} = 2 / 3$  in expansions  
Under Conditional CAPM, its risk premium is

$$
\frac{3}{4}\cdot \left(\frac{2}{3}\cdot 4\%\right) + \frac{1}{4}\cdot \left(2\cdot 12\%\right) = 8\%
$$

Static CAPM would just multiply the average market risk premium by the average beta, estimating the risk premium of stock A at  $6\%$

# Stock B: Procyclical Beta

<table><tr><td></td><td>Market risk premium</td><td>Stock beta</td><td>Stock risk premium</td></tr><tr><td>Recession (p=1/4)</td><td>12%</td><td>1/2</td><td>6%</td></tr><tr><td>Expansion (p=3/4)</td><td>4%</td><td>7/6</td><td>14/3%</td></tr><tr><td>Average</td><td>6%</td><td>1</td><td>5%</td></tr><tr><td>Static CAPM</td><td>6%</td><td>1</td><td>6%</td></tr></table>

- Stock B has procyclical beta:  $\beta_{A} = 1 / 2$  in recessions,  $\beta_{A} = 7 / 6$  in expansions  
Under Conditional CAPM, its risk premium is

$$
\frac{3}{4}\cdot \left(\frac{7}{6}\cdot 4\%\right) + \frac{1}{4}\cdot \left(\frac{1}{2}\cdot 12\%\right) = 5\%
$$

Static CAPM would just multiply the average market risk premium by the average beta, estimating the risk premium of stock B at  $6\%$

# How Static CAPM Failed

Static CAPM averages, then multiplies  
- Conditional CAPM multiplies, then averages  
- We needed to calculate the expected excess return to the stock,  $E(R_{S}^{e})$

$$
E \left[ R _ {S} ^ {e} \right] = E \left[ \beta_ {S} \cdot R _ {M K T} ^ {e} \right] = E \left(\beta_ {S}\right) \cdot E \left(R _ {M K T} ^ {e}\right) + C o v \left(\beta_ {S}, R _ {M K T} ^ {e}\right)
$$

Static CAPM missed the covariance between the beta and the market risk premium  
In order for the covariance to be non-zero, both the beta and the market risk premium have to change!  
- Preferably they both should depend on the same variables)

# How Static CAPM Failed

- For Stock A (countercyclical beta), the covariance was positive  
Static CAPM underestimated stock A's expected return (said  $6 \%$  when it was in fact  $8 \%$  
Stock A will have positive  $\alpha = 2\%$  in static CAPM and  $\alpha = 0$  in conditional CAPM  
- For Stock B (procyclical beta), the covariance was negative  
Static CAPM overestimated stock B's expected return (said  $6 \%$  when it was in fact  $5 \%$  
Stock B will have negative  $\alpha = -1\%$  in static CAPM and  $\alpha = 0$  in conditional CAPM

# Playing with Covariance

- By definition

$$
C o v (R _ {i}, R _ {j}) = E [ (R _ {i} - E (R _ {i})) \cdot (R _ {j} - E (R _ {j}) ] =
$$

- Open the brackets inside of the expectation:

$$
= E \left[ R _ {i} \cdot R _ {j} - R _ {i} \cdot E (R _ {j}) - R _ {j} \cdot E (R _ {i}) + E (R _ {i}) \cdot E (R _ {j}) \right] =
$$

- Average sum is the sum of the averages:

$$
= E \left[ R _ {i} \cdot R _ {j} \right] - E \left[ R _ {i} \cdot E (R _ {j}) \right] - E \left[ R _ {j} \cdot E (R _ {i}) \right] + E (R _ {i}) \cdot E (R _ {j}) =
$$

# Playing with Covariance

-  $E(R_{i})$  is just a number, hence

$$
\begin{array}{l} E \left[ R _ {j} \cdot E \left(R _ {i}\right) \right] = E \left(R _ {i}\right) \cdot E \left(R _ {j}\right) \\ = E \left[ R _ {i} \cdot R _ {j} \right] - E (R _ {i}) \cdot E (R _ {j}) - E (R _ {i}) \cdot E (R _ {j}) + E (R _ {i}) \cdot E (R _ {j}) \Rightarrow \\ \end{array}
$$

- Covariance is average product minus the product of the averages:

$$
\Rightarrow C o v (R _ {i}, R _ {j}) = E [ R _ {i} \cdot R _ {j} ] - E (R _ {i}) \cdot E (R _ {j}) \Rightarrow
$$

- Average product differs from the product of the averages by the covariance:

$$
\Rightarrow E \left[ R _ {i} \cdot R _ {j} \right] = E \left(R _ {i}\right) \cdot E \left(R _ {j}\right) + C o v \left(R _ {i}, R _ {j}\right)
$$

# What We Learned about Risk

- For static CAPM, risk is the covariance with the market  
CAPM: Risk is losses when the market goes down  
- Conditional CAPM introduces another dimension of risk: covariance of the beta with the expected market risk premium  
- Conditional CAPM: Risk is also higher beta (and greater losses) during risky times

# Magnitude Issue

- In the numerical example above, we assumed that the expected market risk premium changes from  $4\%$  per year in expansion to  $12\%$  per year in recession  
-  $8\%$  per year change in the market risk premium is close to the largest change we can predict from predictive regressions  
- We also assumed that the beta can double or even triple from its high to its low - can be true for a few stocks, but such stocks are rare  
- Even with these extreme assumptions, the deviations from the static CAPM were at most  $2\%$  each way  
Economically, conditional CAPM produces small effects  
This is called Lewellen-Nagel (JFE 2006) critique

# Market-to-Book

Definition: market capitalization divided by book value of equity  
Firms with high market-to-book are growth firms  
Firms with low market-to-book are value firms  
- Behavioral finance: high market-to-book means the firm is overvalued, so value firms should beat growth firms  
- Asset pricing initial belief: growth options are riskier because they are options, so growth firms should beat value firms

# Value Effect

$$
H M L _ {t} = \begin{array}{c} 0. 5 8 \\ (0. 1 2) \end{array} - \begin{array}{c} 0. 2 7 \\ (0. 0 3) \end{array} \cdot (M K T _ {t} - R F _ {t})
$$

HML buys value and short sells growth  
- Regression above shows that growth firms indeed have higher beta than value firms  
However, value firms beat growth firms by 58 bp per month (7% per year) on risk-adjusted basis  
- "Value beats growth" is the value effect

# Why Value is Riskier than Growth?

- Value firms are mature and capital-intensive, growth firms are young and only plan to invest  
- Zhang (JF 2005) argues that value is riskier in recessions, because value firms are locked in with useless capital  
- Growth is riskier in expansions, when growth firms lack capital  
- Main prediction: value is riskier in recessions and therefore riskier overall, but static CAPM does not see it

# Petkova and Zhang (JFE 2005) Estimate Conditional CAPM

- We estimated  $HML_{t} = \alpha + \beta \cdot (MKT_{t} - RF_{t})$  and found the value effect - static CAPM is not valid  
- Probably, the problem is the correlation between the market beta of HML and the market risk premium  
- Then  $HML_{t} = \alpha + \beta_{t} \cdot (MKT_{t} - RF_{t})$  should work, i.e. produce  $\alpha = 0$  
It was first estimated in Petkova and Zhang (JFE 2005)

# Empirical Strategy

- Assume that the beta of HML is a linear function of the variables that predict market return:

- Default spread (DEF)  
Dividend yield (DIV)  
- Treasury bill rate (TB)  
- Term premium (TERM)

$$
\beta_ {t} = \gamma_ {0} + \gamma_ {1} \cdot D E F _ {t - 1} + \gamma_ {2} \cdot D I V _ {t - 1} + \gamma_ {3} \cdot T B _ {t - 1} + \gamma_ {4} \cdot T E R M _ {t - 1}
$$

- If this is the case, then the beta of HML and the market risk premium are surely correlated

# Empirical Strategy

- We estimate  $HML_{t} = \alpha + \beta_{t} \cdot (MKT_{t} - RF_{t})$  with  $\beta_{t}$  as specified above

$$
H M L _ {t} = \alpha + \left(\gamma_ {0} + \gamma_ {1} \cdot D E F _ {t - 1} + \gamma_ {2} \cdot D I V _ {t - 1} \right.
$$

$$
+ \gamma_ {3} \cdot T B _ {t - 1} + \gamma_ {4} \cdot T E R M _ {t - 1}) \cdot \left(M K T _ {t} - R F _ {t}\right)
$$

- Or, rearranging, we just regress HML on the market return and its products with the macro variables:

$$
H M L _ {t} = \alpha + \gamma_ {0} \left(M K T _ {t} - R F _ {t}\right) + \gamma_ {1} D E F _ {t - 1} \cdot \left(M K T _ {t} - R F _ {t}\right) +
$$

$$
\begin{array}{l} + \gamma_ {2} D I V _ {t - 1} \cdot \left(M K T _ {t} - R F _ {t}\right) + \gamma_ {3} T B _ {t - 1} \cdot \left(M K T _ {t} - R F _ {t}\right) + \\ + \gamma_ {4} T E R M _ {t - 1} \cdot \left(M K T _ {t} - R F _ {t}\right) \\ \end{array}
$$

# Petkova and Zhang: Main Result

$$
\begin{array}{l} H M L _ {t} =\begin{array}{c}0. 4 5\\(0. 1 1 5)\end{array}+ \left( \right.-\begin{array}{c}0. 3 6\\(0. 0 9)\end{array}-\begin{array}{c}0. 1 1\\(0. 0 8)\end{array}D E F _ {t - 1} +\begin{array}{c}0. 2 1\\(0. 0 3)\end{array}D I V _ {t - 1} - \\ - \begin{array}{c} 0. 0 7 \\ (0. 0 2) \end{array} T B _ {t - 1} - \begin{array}{c} 0. 0 1 \\ (0. 0 3) \end{array} T E R M _ {t - 1}) \cdot (M K T _ {t} - R F _ {t}) \\ \end{array}
$$

- As expected (Lewellen-Nagel critique), we go in the right direction, but the distance covered is too small  
- The alpha declines by 14 bp, but still remains large and significant

# Do the Signs Make Sense?

$$
\begin{array}{l} \beta_ {t} = - \begin{array}{c} 0. 3 6 \\ (0. 0 9) \end{array} - \begin{array}{c} 0. 1 1 \\ (0. 0 8) \end{array} D E F _ {t - 1} + \begin{array}{c} 0. 2 1 \\ (0. 0 3) \end{array} D I V _ {t - 1} - \\ - \begin{array}{c} 0. 0 7 \\ (0. 0 2) \end{array} T B _ {t - 1} - \begin{array}{c} 0. 0 1 \\ (0. 0 3) \end{array} T E R M _ {t - 1}) \\ \end{array}
$$

- Since the alpha improves when we use conditional CAPM instead of static CAPM, the market beta of HML has to be countercyclical, as we want it to be  
- The beta of HML is high when:

- Default spread is low - wrong, but insignificant  
- Dividend yield is high - right and significant  
- Treasury bill rate (aka expected inflation) is low - right and significant  
- Term premium is low - wrong, but insignificant

# Are Magnitudes of the Coefficients above Realistic?

- If dividend yield increases by  $1\%$  per year, the market beta of HML increases by 0.2  
- Dividend yield changes by about  $2\%$  peak to trough - the market beta of HML changes by 0.4 peak to trough. Realistic  
If expected inflation increases by  $1\%$  per year, the market beta of HML decreases by 0.07  
- Expected inflation changes by about  $4\%$  peak to trough - the market beta of HML should change by 0.28 peak to trough. Realistic

# Market Betas of HML in Expansions and Recessions

- I use the estimated equation for  $\beta_{t}$  to estimate the time-varying market beta of HML  
- I split the sample into recessions and expansions based on the expected market return from the same regression (above median - recession, below median - expansion)  
Market beta of HML is -0.41 in expansion, -0.135 in recession  
- Even with quite large variation in risk premium of  $1\%$  per month between expansions and recessions, the 0.275 difference in beta will explain less than half of the HML alpha  
- Also, growth firms are still always riskier than value firms

# Why Changing Beta Matters

Market beta of HML is -0.41 in expansion, -0.135 in recession, -0.27 on average  
- Suppose you invest  $100 in HML and buy the market for$ 27 to hedge out the market movements and earn the (relatively) constant alpha  
- Then the expansion happens, the beta of HML becomes -0.41  
- The beta of your position "invest  $100 in HML and buy the market for$ 27" becomes -0.14  
- In the expansion, the market goes up, and you lose, since you have a negative beta (you under-bought the market)

# Why Changing Beta Matters

- Then the recession happens, the beta of HML becomes -0.135  
- The beta of your position "invest  $100 in HML and buy the market for$ 27" becomes 0.135  
- In the recession, the market goes down, and you lose, since you have a positive beta (you over-bought the market)  
- The countercyclicality of the beta means that if you hedge your position based on average beta, you lose no matter where the market goes  
- This is what is wrong with countercyclical beta

# Hedging Changing Beta

$$
\begin{array}{l} \beta_ {t} = - 0. 3 6 - 0. 1 1 \cdot D E F _ {t - 1} + 0. 2 1 \cdot D I V _ {t - 1} - \\ - 0. 0 7 \cdot T B _ {t - 1} - 0. 0 1 \cdot T E R M _ {t - 1}) \\ \end{array}
$$

- The equation below (borrowed from the estimation of the Conditional CAPM) can be used to predict beta in each period of time  
- Example: in October 2001, DEF=0.86%, DIV=1.23%, TB=2.38%, TERM=1.91%  
- Substituting into the beta equation above, one can calculate that the expected beta of HML in November 2001 is -0.384

# Dynamic Hedging

Hence, in October 2001 the trader that turns around  $100 in HML should have bought the market for$ 38.4 to hedge out the market exposure  
- One can redo the calculation using November 2001 values of DEF, DIV, TB, TERM and figure out that the beta was expected to be at -0.36 in December 2001  
- Thus, going into December 2001, the trader will have to adjust his position in the market in the end of November 2001  
- He wants to make sure he holds  $36 of the market for each$ 100 in HML, not $38.4, as in the end of October 2001

# Recap

- Conditional CAPM introduces a new dimension of risk (in addition to static market beta)  
- Risk is higher beta (and greater losses) during risky times  
- However, we have to assume unrealistically large changes in market risk premium and betas to produce economically meaningful effects  
- Conditional CAPM can point correctly to where the risk is coming from, but cannot measure its magnitude