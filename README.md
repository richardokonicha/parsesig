# Parsesig


## A Telegram program that forwards Forex Signals from one Telegram group or channel to another

Listens for message events on CHATINPUT channel that matches the Regex pattern 
`^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]` 
and passes it with `pasig()` Engine

```comment
                                |     #EURUSD
BUY EURUSD (@ 1.0877)           |     BUY📈1.0877
Take profit 1 at 1.0897         |     ✅TP 1.0897
Take profit 2 at 1.0927         |     ✅TP 1.0927
Take profit 3 at 1.0977         |     ✅TP 1.0977
Stop loss at 1.07978            |     🛑SL 1.07978
```

Sigparser takes the following environment variables or configure .env file in the project directory
Main pair

  ```python
  CHATINPUT=-12345678901234
  CHATOUTPUT=-1234567890123
  ```

Test pair

  ```python
  TESTINPUT=-12345678901234
  TESTOUTPUT=-1234567890123
  ```

All matching messages from the channel set in the CHATINPUT environment variable 
is forwarded to the channel set in the CHATOUTPUT environment variable same goes for the test variables


## Heroku setup

---

* Create new Heroku app on your [Heroku account](https://heroku.com).
* Link app to using the gihub option and select the repository
* From terminal set git heroku remote url
  
  ```bash
  git remote set-url --add heroku https://git.heroku.com/{your_app_name}.git
  heroku login
  ```

* After build and deploy succeed, check for the number of running dynos

  ```bash
  heroku ps
  ```

  *this application is define from the Procfile as a worker process, on first build number of dynos=0*
* Set environment variables on heroku, goto settings and reveal config vars and set key:value
  *Start up one dyno with a single process*

  ```bash
  heroku ps:scale worker=1
  ```
