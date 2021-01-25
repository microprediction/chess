# chess

This gitaction-powered mini-project demonstrates the use of the general purpose time series prediction [api](http://api.microprediction.org/) to source predictions of bullet and blitz chess ratings for top players...

| Player            | Home                                                              | Blitz                                                                                                   |
|-------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Hikaru Nakamura   | [Hikaru](https://www.chess.com/member/hikaru)                     | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_blitz_level_Hikaru),  [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_blitz_daily_Hikaru)            |
| Daniel Naroditsky | [DanielNaroditsky](https://www.chess.com/member/danielnaroditsky) | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky), [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_daily_DanielNaroditsky) |
| Alireza Firouzja  | [Firouzja2003](https://www.chess.com/member/firouzja2003)         | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_Firouzja2003), [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_daily_Firouzja2003)     |

... and some not-so-top players. We're more than happy to include your rating too. Make a pull requests with your chess.com user handle for [set.py](https://github.com/microprediction/chess/blob/main/set.py) or just leave an issue with your chess.come username. 

The script [set.py](https://github.com/microprediction/chess/blob/main/set.py) runs every hour, and creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky). That stream is monitored by lots of time series algorithms who fight for supremacy. The result is distributional predictions that get slowly better over time and incorporate more exogenous data. For instance the algorithms have access to all public data including all games played.   

There's more at www.microprediction.com/blog about chess and data science. 

Oh yeah, and if you want to increase your bullet rating by 100, use right click to cancel pre-moves. And play the Halloween Gambit! See our little [chess blog](www.chess.com/blog/microprediction).  


