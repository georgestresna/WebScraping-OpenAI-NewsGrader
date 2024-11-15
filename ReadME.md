# Financial Data Web Scraper and Scorer with the OpenAI API

### This project is was made for educational purposes only. 

It scrapes the latest and hottest news of (ForexFactory)[www.forexfactory.com/news], gives the news a predefined weight. 

The weight measures how much the news influence the market, and it is a discretionary metric, set by the user.

It is currently running on 60% weight for the hottest news and 40% for the latest news. The hottest news will also likely appear in the latest news also.

After scraping the content off each news article, the text is fed into the OpenAI API, and it returns a value calculated on how important the news article is, on a scale from -20 to 20. 
- -20 is the worst predicted outcome
- 0 is neutral
- 20 is the best predicted outcome

This happens for every mentioned currency.

After that these values are stored in a `currencies.json` file, where all of the results reside.

---
### The concept is that using web scraping and AI, we could exctract the current market sentiment and use it in out financial analisys of the forex/futures market.

---
### Cost
1. ForexFactory is completely free, so no subscription fees there
2. The OpenAI API is a pay-per-token-used type of thing. I use the `gpt-04-mini` model, which is cheap and effective enought. I haven't yet spent $0.10 on the API  
---
Things to inplement in the future:

- a more user friendly experience. Make the weight adjustable outside the code (although for consistent results, a consistent weight is recomended)
- a `schedule` implementation to run th program every 4 hours on a weekday, to get a consistent evolution on how the prices fluctuate
