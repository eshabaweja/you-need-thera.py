# I'ma skim through the rest of it
## Terrible from day 50-ish onwards
- the creator abandoned the course
- I'm not learning much, just googling errors
- at least 3-4 days were just a recycle of the web-dev course
- good for learning python fundamentals but the rest of it is super outdated/deprecated
- jut go to youtube and [roadmap.sh](roadmap.sh)
- > It's just that spending a week+ on something I don't really have an interest in or a talent for seems a bit of a waste, when I could instead learn other stuff.

## Day 66-67
- more about Postman than RESTful API
- watch Postman video on freecodecamp

## Day 68

- learn SQL before all this copy-paste SQLite and SQLAlchemy
- take `user id` and `password` input using form
- save it to `users.db`
- show a success message to user
- `send_from_directory()` to send file to user
- use Flask_Login to ensure only registered users can access `/secret`

### Encryption and Hashing

- Level 1: `plaintext` password saved to database
- Level 2: Encryption: using a `key` to encode it
    - The imitation games
    - enigma machine
    - videos by [numberphile](https://www.youtube.com/watch?v=G2_Q9FoD-oQ&ab_channel=Numberphile)
- Level 3: Hashing: use a `hash function` (math) and save the output to server database
    - [https://cryptii.com/](https://cryptii.com/)
    - `same input always gives same output` in a hash function
    - vulnerability: commonly used passwords can be used to reverse-engineer the hash
    - **Dictionary Attack**: systematically entering every word in a dictionary as a password

![image-20230102205001090](README-assets/image-20230102205001090.png)

- **Salting**: `password + salt -> hash function -> hash`
  - salt is a random set of characters
  - hashing algorithms: look up some industry standard ones
  - salt **rounds**
