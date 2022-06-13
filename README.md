1. Clone repository
2. Create virtual environment
3. Install all packages in requirements.txt
4. In .env file change configurations(db, max_posts_per_user, number_of_users etc.)
5. Connect to database and make migrations
6. Open bot.py in bot package
7. Set project_path
8. Run project
9. Run script(bot.py) file



API:
    /auth/register/ - User registration, fields(username, password1, password2) </br>
    /auth/login/ - User login, fields(username, password) </br>
    /api/post/create/ - Post create, fields(title, description) </br>
    /api/post/get-all/ - Get all posts, fields(title, description, author, likes) </br>
    /api/post/post_id/like/ - Like post, fields() </br>
    /api/post/post_id/unlike/ - Unlike post, fields() </br>
    /api/analytics?date_from=YYYY-mm-dd&date_to=YYYY-mm-dd - Analytics how many posts liked in date range,
                            fields() </br>

Also, we have a middleware that will track, last_request time of user, and record to database to the field last_request. </br>