# tetrica_test

# Quick start

1. Install ```pipenv``` (you can do that via ```pip```)
2. ```git clone https://github.com/AdamKhagar/tetrica_test.git```
3. Install requierements:
    ``` 
    pipenv install -d --pre 
    pipenv shell 
    
## Task 3
  Used flask
  Run ```views.py``` and send post request to ```/appearance``` with JSON body:
   ```
    {
      "lesson": [1594663200, 1594666800],
      "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
      "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
    }
   ```
