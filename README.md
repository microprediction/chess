# chess

This gitaction-powered mini-project demonstrates the use of the general purpose time series prediction [api](http://api.microprediction.org/) to source predictions of bullet and blitz chess ratings for top players (and some not so top players - pull requests with your chess.com user handle are welcome). This creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky). That stream is monitored by lots of time series algorithms who fight for supremacy. The result is distributional predictions that get slowly better over time and incorporate more exogenous data. For instance the algorithms have access to all public data including all games played.   

There's more at www.microprediction.com/blog and more about the Halloween Gambit in the chess blog www.chess.com/blog/microprediciton 


