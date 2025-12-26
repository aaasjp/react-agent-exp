# EMH and Trading Costs

Professor Alexander Barinov

School of Business Administration University of California Riverside

MGT 295F Empirical Methods

# Outline

EMH Is About Abnormal Returns  
2 EMH and Trading Costs  
3 EMH and Information Production  
Trading Costs: Bid-Ask Spread  
Measuring the Bid-Ask Spread  
Trading Costs: Price Impact  
Measuring the Price Impact  
8 Numerical Example

# Definition

- EMH: Stock prices reflect all available information (on average, the price is right)  
- Intuition: If I know that the price of a stock is  $10, but the stock is really worth$ 12, I will continue buying until the price becomes $12. At this point, the price will reflect my information  
- Assumption: Everyone who has relevant information trades, and the information gets into the price  
- Implication: you cannot profit from what someone else already knows  
- That is, do not try to outsmart the market!

# EMH and Expected Return

- The most primitive form of EMH is called Random Walk Theory: "The best expectation of the price next period is the price this period"  
- May be true in the short-run, but in the long run - where is our risk premium?  
- Better statement: "The best expectation of the price tomorrow is the price today times (1 + expected return)" (expected return may come, e.g., from the CAPM)  
- Realized Return = Expected Return + Abnormal Return (aka News)  
- EMH is a theory about abnormal return: it should be unpredictable, not the whole return

# Testing EMH

- All tests of EMH are joint tests of EMH and the asset-pricing model  
Example: Apple has beta of 1.5, you predict that in a year Apple stock will go up by  $12\%$  
- Is it enough to compensate you for the risk you bear when you hold Apple?  
Is  $15\%$  gain enough? Are you sure CAPM is the right model?  
- Expected return can be predictable, and unless we know exactly how to measure expected return, we cannot claim with full certainty that abnormal return is predictable

# EMH "with Traction"

$$
M K T _ {t} = \begin{array}{c} 0. 0 3 6 \\ (0. 0 0 9) \end{array} + \begin{array}{c} 0. 0 8 5 \\ (0. 0 0 9) \end{array} M K T _ {t - 1} + \epsilon_ {t}
$$

- The slope is significant: we can indeed predict tomorrow market return from today's return  
- If today market goes up by  $1 \%$ , tomorrow it will go up by another 8.5 bp (0.085%)  
-  $0.085\%$  is not enough to even beat the bid-ask spread - the predictability of the market return is consistent with EMH

# EMH "with Traction"

- The main thing is that the market should be efficient within the boundaries set by trading costs  
- Even abnormal returns can be predictable, but if this predictability is so small that no profits can be made net of trading costs, the market is still efficient despite the predictability

# Information Production

- Suppose we have analyzed the financial statements for Google and figured it should be selling for $700  
- Suppose we have found the money and driven the price to $700  
It makes the market efficient and leaves us with good profit on the first buys at $580  
We are being paid for making the market efficient

# Information Production

- Suppose we come to the market which is already efficient  
- Would we bother to analyze financial statements and produce information?  
- No, and this is nice: we can just buy assuming that the price is fair  
- But somebody has to produce information and get it into stock prices!  
- Grossman and Stiglitz (AER 1980) - market cannot be efficient in the sense that nobody makes profit from trading there  
- Some people have to make sure the market is efficient and make their living from it in return

# EMH and Competition

- EMH is similar to the result that economic profit is zero under perfect competition  
Zero economic profit does not mean that the firm makes no money - it makes just enough to compensate owners for their effort and to stop exit/entry  
- "Technical analysis does not work" means there are 1000 guys doing technical analysis, earning just enough to make them stay in and everyone else stay out  
- If you are as good as Morgan Stanley traders, you should be able to earn their salary by trading  
- But: think about all information and trading opportunities they have access to and you do not

# How Bid-Ask Spread is Created

- The easy way to understand the bid-ask spread is to imagine that there is one market-maker who keeps an inventory of the stock and is obligated to make sure every buyer finds a seller and sometimes to step in  
- The market-maker has two sources of losses: the inventory risk and informed traders, and one source of profit: the bid-ask spread

# How Bid-Ask Spread is Created

- The inventory risk means the risk of the stocks in the inventory losing value and/or the market-maker being unable to unload them in time  
- The market-maker is also concerned about having to trade with an informed trader, who always makes the right trade (and the market-maker then has to make the wrong trade)  
- The market-maker compensates for the possible losses by setting a higher bid-ask spread

# Determinants of Bid-Ask Spread

- Bid-ask spread increases with

- Uncertainty - market-maker fears that the counterparty is informed  
- Volatility - market-maker holds inventory to fill the orders that are not filled without him, volatility makes inventory position risky  
- Tick size - cannot be less than the minimum tick

- Bid-ask spread decreases with

- Liquidity - if the stock is "easy to find", the necessary inventory level is smaller  
Stock price - partly tick effect, partly liquidity and uncertainty effect

- Tells you where to seek mispricing, but be careful - others may have lower trading costs than you do

# Measuring the Bid-Ask Spread

- The bid-ask spread is normally reported in real time on Google Finance and the like, but there are a few caveats about this  
- First, the historical data are not available: you know what the spread is right now, but you have no way of knowing what it was on average in the past month  
- Second, the bid-ask spread changes a lot throughout the day: it can be 20 cents at the open and 1 cent at 1 pm  
- The unfortunate thing is that you will want to trade at the open, not at 1 pm if you learned something new overnight  
- Third, what you see is the quoted spread: trades do not necessarily happen at these prices

# Roll (JF 1984) Measure

- One simple measure of effective spread is the Roll measure

$$
\mathrm {R o l l} = 2 0 0 \cdot \sqrt {- \mathrm {C o v} \left(\mathrm {R} _ {\mathrm {t}} , \mathrm {R} _ {\mathrm {t} - 1}\right)}
$$

- If you use percentage returns, you need to multiply by 2, not 200  
- The Roll measure is scale-free: it gives you percentage spread, i.e., the spread in cents per one dollar of the stock price  
- Which is good, because that makes you able to compare the spread of two different stocks with different prices

# Understanding the Roll Measure

- Intuition: assume the price is flat  
- If the market closes at the ask, next day the return will be either zero (it closes at the ask again) or negative (it closes on the bid)  
- If the market closes at the bid, next day the return will be either zero (it closes at the bid again) or positive (it closes on the ask)  
- This is how spread brings about the negative covariance of return with its lag, and the magnitude of the bounce-back/covariance measures the magnitude of the spread

# Calculating the Roll Measure

- How to do it in Excel: copy the return series next to itself and shift it by one cell down (this creates  $R_{t - 1}$ )  
- Then compute the covariance (COVAR function) between the two series and perform the necessary calculations  
- One obvious problem with the Roll measure is that the return covariance may be positive, and then the square root is undefined

# Fixing the Roll Measure

- There are several ways to fix the positive covariance  
- We can assume that if the covariance is positive the spread is very small, like 1 cent  
- We can cut the sample in smaller pieces, redo the Roll measure for each piece and take the average, assuming that when the Roll measure is undefined, it is zero or missing  
- Or we can simply multiply the positive covariance by -1, because, presumably, the price predictability as simple as that is caused by illiquidity

# Price Impact

- The demand for stock at the market price is finite  
- The maximum amount you can sell at the market price is called market depth  
- If you have to sell more, you are likely to get a lower price  
- If you are a big player or an insider, your sale can lead others to believe that you have negative information about the stock, and the price will drop  
- Example: in June 1998, Warren Buffet did not report his holdings of Wells Fargo, seeking confidentiality - the stock price of Wells Fargo lost several percent in a single day

# Price Impact

- Example of an order book: buy orders for 3000 shares at the market price, buy orders for 1000 shares 5 cents below, buy orders for 2000 shares at 10 cents below  
- In this example, 3000 shares is the market depth (at the market price)  
- If you sell 5000 shares using the market order, you sell the last 1000 shares at 10 cents below, this is a $100 loss for you (plus $50 loss from selling one more 1000 at 5 cents below)

# Price Impact: Trying to Hide

- One reason why we see an order book like that is because people are afraid of trading with a big informed trader and put some orders below the market price just in case  
- Suppose you decide to feed your trade to the market as a sequence of 100 shares orders  
- People will figure you out - deals will happen only at the bid prices, so clearly someone is selling  
- If they see the order book, they will also see that (after 3000 shares at the market price are gone) there is always someone selling 100 shares and nobody is buying (order imbalance)

# Determinants of Price Impact

- Determinants of price impact are the same as the determinants of bid-ask spread, since price impact is also created by information asymmetry  
- If stock is volatile and investors are uncertain about it, the possible losses from trading to an informed guy are larger and the price impact is bigger  
- If the stock is heavily traded, it is easier for informed people to hide in the flow, and the probability to meet one is lower, hence price impact is lower

# Trends in Price Impact

One way trading desks at IB are making money is they try to minimize the price impact of their trades  
- High-frequency trading: figure out the precise time to buy/sell during the day  
- Consequence: trading became more frequent (in 10 times since 1993) and median trade size became smaller (in 3 times since 1993)  
- The minimum trade size that makes the price move has declined from 10,500 shares to 2,800 during the past two decades

# Trends in Price Impact

One way trading desks at IB are making money is they try to minimize the price impact of their trades  
- High-frequency trading: figure out the precise time to buy/sell during the day  
- Consequence: trading became more frequent (in 10 times since 1993) and median trade size became smaller (in 3 times since 1993)  
- The minimum trade size that makes the price move has declined from 10,500 shares to 2,800 during the past two decades

# Amihud (JFM 2002) Measure

- A simple measure of price impact is the Amihud (JFM 2002) ratio  
- The Amihud ratio is the average ratio of the absolute value of returns to the dollar trading volume  
- How to do it in Excel: download the data on volume and returns  
- Keep in mind that volume is quoted in number of shares traded, unless indicated otherwise, so you will have to multiply it by the respective stock prices first  
- Then, divide the dollar volume you get by 1,000,000 to make sure that you get return movements per $1 million traded, and only then divide the returns by the volume

# Amihud (JFM 2002) Measure

- The Amihud measure estimates the price movement caused by pushing, say, $1 million through the market in a day  
This is the exact definition of price impact  
- The Amihud measure is mechanically low for high-volume stocks, but that does not necessarily mean that it does not measure the price impact of high-volume stocks correctly  
- If the volume is high, a lot of it is coming from uninformed traders, and the prices do not react as much to pushing a big order through the market  
- One can say that the Roll measure can also pick up price impact, because the prices moved by the volume are likely to bounce back the next day, and the Roll measure picks up exactly the bounce-back (but attributes it to the bid-ask spread)

# Roll and Amihud Measures for Adobe

Adobe (ticket: ADBE) is a large software company with market cap around $14 billion  
- It is also actively traded: the average daily volume in 2011 was $186 million, which means that each year about  $330\%$  of the market cap changes hands  
For a median company, about  $180\%$  of the market cap changes hands each year  
- Question: what would it cost, in dollars and in percents, to buy $140 million (1% of the market cap) of Adobe in one day?

# Losses Implied by Bid-Ask Spread

- Roll measure of Adobe is 1.51 - it means that the average effective bid-ask spread for Adobe is  $1.51\%$  of the stock price  
Amihud measure is only 0.009 - it means that buying $1 million of Adobe will move the prices by only 0.9 bp  
- Assume that the true price is exactly at the midpoint and the price impact of a buy starts at the ask  
- Then when you buy, you lose half of the spread - the distance between the ask, at which you buy, and the true price. which is the midpoint

# Losses Implied by Price Impact

- In addition to that, if you trade X million, you move the deal price by X times the Amihud measure above the ask  
- When you trade the first lot, you trade exactly at the ask  
- When you trade the last lot, you trade at  $X$  times the Amihud measure above the ask  
- On average, you trade X/2 times the Amihud measure above the ask

# Total Trading Cost for Adobe

In million dollars, you lose

$$
1 4 0 \cdot \frac {0 . 0 1 5 1}{2} + 1 4 0 \cdot \frac {0 . 0 0 0 0 9 \cdot 1 4 0}{2} = \\ \\ 1. 0 5 6 + \\ \\ 0. 8 6 4 = \\ \\ 1. 9 2
$$

In percent, you lose

$$
\frac {1.51}{2} + \frac {0.00009 \cdot 140}{2} = 0.755 \% + 0.617 \% = 1.372 \%
$$

- The more you trade, the more you lose on the price impact  
- Practical implication: if you think that Adobe is mispriced by less than  $2 \cdot 1.372\% = 2.75\%$  (two-way trading cost) or roughly 80 cents per share, do not bother trading