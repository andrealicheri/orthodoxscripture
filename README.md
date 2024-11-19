# OrthodoxScripture

The largest collection of Easter Orthodox scripture in one website.

## Features

- All of the EO Holy Biblical Canon with original language side by side with literal translation
- Church Fathers commentaries on individual verses
- All of the 7 Holy Ecumenical Councils plus the other local Councils
- A web version of "Anti-Nicean Church Fathers" and "Nicean and Post-Nicean Church Fathers" for a deeper insight on the Early Church

## TBA

- [ ] Automatically change `escape-string-regexp` from .js to .cjs
- [ ] Canons of the Church Fathers (looking for an API to do that)
- [ ] Other Works (Didache, 85 Canons of the Apostles, Apostolic Constitution, etc.)
- [ ] About Page
- [ ] Referencing System
- [ ] TOR

## "Pages are slow"

Fetching is all done on the server side to allow JS-free browsing in safe enviornements like TOR. Taking in consideration that when you fetch a verse with the `/verse` route, the server has to make three requests to bolls.life for Bible verses and filter commentaries from Catena. This takes about 3 seconds, and all of the other routes are way faster. 

## Credits and APIs

- [bolls.life](https://bolls.life) for Bible translations
- [catenabible.com](https://catenabible.com) for Church Fathers commentaries 
- [ccel.org](https://ccel.org) for ANF and NPNF