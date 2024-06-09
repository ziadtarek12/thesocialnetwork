# The Social Network

This is a social networking web application built with Django.

## Project Structure

### Main Application: `network`

The `network` directory contains the core components of the application:

- **`models.py`**: Defines the database models for the application.
  - [`User`](network/models.py): Represents the users of the network.
  - [`Post`](network/models.py): Represents individual posts made by users.
  - [`Likes`](network/models.py): Tracks the likes on posts.
  - [`Follow`](network/models.py): Manages the follower-following relationships between users.

- **`views.py`**: Handles the application's routing and views.
  - [`index`](network/views.py): Displays the main page with posts.
  - [`following`](network/views.py): Shows posts from followed users.
  - [`login_view`](network/views.py): Manages user login.
  - [`logout_view`](network/views.py): Handles user logout.
  - [`register`](network/views.py): Manages user registration.
  - [`create_post`](network/views.py): Allows users to create new posts.
  - [`profile`](network/views.py): Displays user profiles.
  - [`follow`](network/views.py): Manages following and unfollowing users.
  - [`edit`](network/views.py): Allows users to edit their posts.
  - [`like`](network/views.py): Handles liking and unliking of posts.

- **`urls.py`**: Defines the URL routes for the application.
  - `index`: Main page route.
  - `login`: Login page route.
  - `logout`: Logout route.
  - `register`: Registration page route.
  - `create_post`: Route for creating new posts.
  - `profile`: User profile route.
  - `follow`: Route for following/unfollowing users.
  - `following`: Route for viewing followed users' posts.
  - `edit`: Route for editing posts.
  - `like`: Route for liking/unliking posts.

- **`static/`**: Contains static files like CSS and JavaScript.

### Project Settings: `thesocialnetwork`

The `thesocialnetwork` directory contains the main project settings and configurations.

## Setup

Follow these steps to set up and run the application:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/thesocialnetwork.git
    cd thesocialnetwork
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the database migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser (optional but recommended for admin access):

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Register**: Create a new user account.
- **Login**: Access your user account.
- **Create Post**: Share new content.
- **Follow Users**: Follow other users to see their posts.
- **Like Posts**: Like or unlike posts.
- **Edit Posts**: Modify your existing posts.
- **Profile**: View and manage your profile and posts.
- **Following**: See posts from users you follow.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

