# chess

This gitaction-powered mini-project demonstrates the use of the general purpose time series prediction [api](http://api.microprediction.org/) to source predictions of bullet and blitz chess ratings for top players...

| Player            | Home                                                              | Ratings                                                                                                   |
|-------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Hikaru Nakamura   | [Hikaru](https://www.chess.com/member/hikaru)                     | [blitz](https://www.microprediction.org/stream_dashboard.html?stream=chess_blitz_level_Hikaru)            |
| Daniel Naroditsky | [DanielNaroditsky](https://www.chess.com/member/danielnaroditsky) | [blitz](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky) |
| Alireza Firouzja  | [Firouzja2003](https://www.chess.com/member/firouzja2003)         | [blitz](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_Firouzja2003)     |

... and some not-so-top players. We're more than happy to include your rating too. Make a pull requests with your chess.com user handle to [set.py](https://github.com/microprediction/chess/blob/main/set.py) or just leave an issue with your chess.come username. 

The script, run every hour, creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky). That stream is monitored by lots of time series algorithms who fight for supremacy. The result is distributional predictions that get slowly better over time and incorporate more exogenous data. For instance the algorithms have access to all public data including all games played.   

There's more at www.microprediction.com/blog about chess and data science. 

Oh yeah, and if you want to increase your bullet rating by 100, use right click to cancel pre-moves. And play the Halloween Gambit! See our little [chess blog](www.chess.com/blog/microprediction).  


