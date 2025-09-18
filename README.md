# 🍿 Popcorn

Popcorn is a Django web application for sharing and discussing movies! 🎬✨ Users can create posts about movies, comment and reply to comments, and manage their profiles. The app features a modern, responsive UI and supports user authentication. Grab your popcorn and join the fun! 😸🍿

## Features & Functionality 🚀

### User Authentication 🔐
- **Sign Up**: New users can register for an account using a simple form. 📝
- **Login/Logout**: Secure login and logout functionality using Django's built-in authentication system. 🔑
- **Profile Management**: Each user has a profile page displaying their posts. 👤

### Movie Posts 🎥
- **Create Post**: Authenticated users can add new movie posts with a title, description, and image URL. 🖼️
- **View Posts**: All users can browse movie posts on the main movie page, with each post displayed as a card. 🃏
- **Edit/Delete Post**: Users can edit or delete their own posts from the post detail page or their profile. ✏️🗑️

### Comments & Replies 💬
- **Add Comment**: Users can comment on any movie post. 💭
- **Threaded Replies**: Users can reply to comments, creating nested threads for discussions. 🔗
- **Edit/Delete Comment**: Users can edit or delete their own comments and replies. 📝🗑️

### User Profiles 🧑‍💻
- **Profile Page**: Displays the user's information and a list of their posts. 📋
- **View Other Profiles**: Browse other users' profiles and see their posts. 👀

### Search Functionality 🔎
- **Search Bar**: Search for posts by title or description on the movie page. 🕵️‍♂️
- **Instant Filtering**: Results update based on the search query. ⚡

### Responsive UI 📱💻
- **Custom CSS**: The app uses custom styles for a modern look and adapts to desktop and mobile screens. 🎨
- **Navigation**: Easy navigation via the header menu, with links to all main pages. 🧭

### Admin Panel 🛠️
- **Django Admin**: Manage users, posts, and comments via Django's admin interface (accessible to superusers). 👑

## Project Structure 🗂️

```
Popcorn/
├── main_app/
│   ├── models.py        # Post and Comment models
│   ├── views.py         # Core views (CRUD, profile, movie, comments)
│   ├── urls.py          # App URL routes
│   ├── templates/       # HTML templates (base, home, signup, movie, profile, post, comment)
│   └── static/          # CSS and images
├── popcorn/
│   ├── settings.py      # Django settings
│   └── urls.py          # Project URL routes
├── db.sqlite3           # Default SQLite database (can be changed in settings)
├── manage.py            # Django management script
├── Pipfile              # Python dependencies
└── README.md            # Project documentation
```

## Models

- **Post**: Title, description, image URL, user (author)
- **Comment**: Post, user, content, created_at, parent (for replies)

## Views & Templates

- **Home**: Login page
- **Signup**: User registration
- **About**: Project info
- **Movie**: List/search posts
- **Profile**: User's posts
- **Post Detail**: View post and comments
- **Post/Comment Forms**: Add/edit/delete posts and comments

## Getting Started

1. **Clone the repository**
	```zsh
	git clone https://github.com/A7med-p/Popcorn.git
	cd Popcorn
	```

2. **Install dependencies**
	```zsh
	pipenv install
	```

3. **Apply migrations**
	```zsh
	pipenv run python manage.py migrate
	```

4. **Create a superuser (optional)**
	```zsh
	pipenv run python manage.py createsuperuser
	```

5. **Run the development server**
	```zsh
	pipenv run python manage.py runserver
	```

6. **Access the app**
	- Visit `http://localhost:8000/` in your browser.

## Usage

- Sign up for an account or log in.
- Create and view movie posts.
- Comment and reply to comments (threaded).
- Edit or delete your posts and comments.
- View your profile and other users' profiles.
- Search for posts using the search bar on the movie page.
- Manage content via the Django admin panel (for superusers).

## Customization

- Update static files in `main_app/static/` for custom styles.
- Modify templates in `main_app/templates/` for UI changes.
- Change database settings in `popcorn/settings.py` as needed (default is PostgreSQL, can be changed to SQLite for local dev).

## Database

- Default: PostgreSQL (`popcorn` database)
- For local development, you can switch to SQLite by updating `DATABASES` in `popcorn/settings.py`:
  ```python
  'ENGINE': 'django.db.backends.sqlite3',
  'NAME': BASE_DIR / 'db.sqlite3',
  ```

## License

This project is for educational purposes.

---

Made with 🍿 by A7med-p
