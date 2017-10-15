## Gyaku

Gyaku is a small project which uses [Kyoukai](https://github.com/SunDwarf/Kyoukai) (a flask-like asynchronous web framework) and [aiohttp](https://github.com/aio-libs/aiohttp) to scrape Google's reverse image search and return a JSON response.

### Attribution
This project was inspired by [MRISA](https://github.com/vivithemage/mrisa), which uses Pycurl and Flask to achieve the same task. The code to scrape the Google results was derived directly from this project.

### Setup
Simply clone the repository and run `python main.py`.  


**Note:**  
Per aiohttp, this project requires Python3.4.2+ to function. Feel free to use 3.6, though---it's vastly superior.
### Usage
Make a POST request to `localhost:8000/search` with an image URL.  
e.g.  
`$ curl -X POST localhost:8000/search -d 'https://supermariorun.com/img/stage/mario03.png'`  
This will return:  
```JSON
{
  "links":[
    "https://supermariorun.com/",
    "https://supermariorun.com/en/",
    "https://www.nintendo.com/games/detail/super-mario-run-mobile",
    "https://www.inverse.com/article/25514-super-mario-run-nintendo-mobile-titles",
    "http://www.gameinformer.com/games/super_mario_run/b/ios/archive/2016/12/15/super-mario-run-iphone-game-informer-review.aspx",
    "https://www.inverse.com/topic/super-mario-run",
    "https://mic.com/articles/161992/super-mario-run-release-date-and-time-when-will-the-nintendo-game-launch"
  ],
  "descriptions":[
    "A new kind of Mario game that you can play with one hand. SUPER MARIO RUN Scheduled for 12.15.2016 release.",
    "A new kind of Mario game that you can play with one hand. SUPER MARIO RUN Scheduled for 12.15.2016 release.",
    "360 \u00d7 490 - Dec 15, 2016 - Learn more details about SUPER MARIO RUN for iOS/Android and take a look at gameplay screenshots and videos.",
    "3072 \u00d7 3072 - Dec 20, 2016 - Here's the thing about Super Mario Run: It's fine. It's not some kind of life-changing revelation now that Nintendo has fully, officially come to\u00a0...",
    "1000 \u00d7 1000 - Dec 15, 2016 - Run is a great Mario platformer, but it left me wanting more, to a fault.",
    "3072 \u00d7 3072 - Super Mario Run breaking news, reviews, videos, photos, arguments, and predictions: Everything you need to know about Super Mario Run.",
    "1600 \u00d7 900 - Dec 13, 2016 - What time will 'Super Mario Run' launch on the App Store?"
  ],
  "titles":[
    "SUPER MARIO RUN | Nintendo",
    "Super Mario Run",
    "SUPER MARIO RUN for iOS/Android - Nintendo Game Details",
    "'Super Mario Run' Is Only the Beginning | Inverse",
    "Hitting The Stumbling Block - Super Mario Run - iOS - www ...",
    "Super Mario Run | Inverse",
    "'Super Mario Run' Release Date and Time: When will the Nintendo ..."
  ],
  "similar_images":[
    "https://cdn.arstechnica.net/wp-content/uploads/2016/12/super-mario-run.jpg"
  ],
  "best_guess":"super mario run mario"
}
```
### Bugs & Questions

If you have any questions or problems, feel free to message me via discord naught0#4417 or submit an issue.
