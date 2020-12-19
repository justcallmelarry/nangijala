# Nangijala

Nangijala is a webservice handling what is commonly known as a "Dead Man's Switch" (morbid, I know, but seems useful!).\
A dead man's switch is basically a button (or switch) needed to be refreshed every once in a while, or something will happen.

In the movies it's usually the bad guy releasing some sort of world devastating event if he (or she, but going with the statistics here) dies, but for my own part its mostly sendin SMS's, emails, and files to people I know, ensuring that someone takes care of my cats in case I vanish off of the face of the earth (or rather, the internet). At least until I can figure out what my own world devastating event will be.

## ROADMAP (in loose order)
* Database adapter, maybe with models
* Update database with timestamp on renewal
* Add actions to happen when X time has passed
  * Alert that an action will soon be taken
  * SMS notification
  * Email notification
* Possibility to update switch with new actions
* Montly/quarterly test of service
* Unit tests
* Github actions or similar for tests
* In service-test, ask people to confirm the used keypair
* Possibility to add new switches
* Possibility to delete switches
