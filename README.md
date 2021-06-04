# Bee Movie Spammer
Python script that will type every bee movie sentence and press enter. 9 Seconds to Highlight a textbox before the spamming begins, has an 0.4s delay to prevent issues. Made to be annoying. **! REQUIRES `beemovie.txt` TO FUNCTION !**

Works best with [Discord](https://discord.gg/)

Find the entire script [Here](https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script)

# Libraries Used

Used `pyautogui` for typing automation. Can be installed with `pip install pyautogui`

Also used `time`, used for delays/wait functions. Can be installed with `pip install time`


# How it Works


Here's the entire script, its not as complicated as it seems.


<img width="378" alt="Entire Code" src="https://user-images.githubusercontent.com/75379747/120868859-fb637c00-c562-11eb-958a-1342e57a9c7d.png">

It simply waits 0.4s (to prevent issues), then types the sentence, presses enter, prints what it typed to output, and repeat.

***

Imports `time` and `pyautogui` libaries using the `import` function.

<img width="192" alt="Screen Shot 2021-06-04 at 6 35 52 PM" src="https://user-images.githubusercontent.com/75379747/120869177-d6bbd400-c563-11eb-8678-7f04b15b20ed.png">


Waits 9 seconds (only once) to give time to select a text field.

<img width="160" alt="Screen Shot 2021-06-04 at 6 38 15 PM" src="https://user-images.githubusercontent.com/75379747/120869265-08349f80-c564-11eb-921a-1415c478b1b4.png">

Assigns the `beemovie.txt` file to a variable called `beemovie`

<img width="357" alt="Screen Shot 2021-06-04 at 6 39 24 PM" src="https://user-images.githubusercontent.com/75379747/120869393-63ff2880-c564-11eb-8389-81133b202b41.png">
<img width="174" alt="Screen Shot 2021-06-04 at 6 43 16 PM" src="https://user-images.githubusercontent.com/75379747/120869565-bb9d9400-c564-11eb-8d18-699ca7ed9461.png">

For every word in `beemovie` (aka `beemovie.txt`), wait 0.4s, type that sentence and press enter.

<img width="310" alt="Screen Shot 2021-06-04 at 6 44 56 PM" src="https://user-images.githubusercontent.com/75379747/120869752-22bb4880-c565-11eb-83db-0e80a5ff4c5d.png">

`Print` what has been typed.

<img width="183" alt="Screen Shot 2021-06-04 at 6 53 05 PM" src="https://user-images.githubusercontent.com/75379747/120870130-197eab80-c566-11eb-8ee1-a2972655ffcf.png">



