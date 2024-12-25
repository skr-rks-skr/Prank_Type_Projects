import instaloader

# Initialize Instaloader
loader = instaloader.Instaloader()

# Instagram credentials
USERNAME = 'deepak__skr___'
PASSWORD = 'qazmko'

def login_instagram(username, password):
    """Login to Instagram."""
    try:
        loader.login(username, password)
        print(f"Logged in as {username}.")
    except Exception as e:
        print(f"Error during login: {e}")

def scrape_profile_info(profile_name):
    """Scrape basic profile information."""
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        
        print(f"Profile: {profile_name}")
        print(f"Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")

    except Exception as e:
        print(f"Error while fetching profile info: {e}")

def scrape_followers(profile_name):
    """Scrape a list of followers."""
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        print(f"Followers of {profile_name}:")
        for follower in profile.get_followers():
            print(follower.username)
    except Exception as e:
        print(f"Error while fetching followers: {e}")

def scrape_followees(profile_name):
    """Scrape a list of followees (people the user is following)."""
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        print(f"Followees of {profile_name}:")
        for followee in profile.get_followees():
            print(followee.username)
    except Exception as e:
        print(f"Error while fetching followees: {e}")

def scrape_posts(profile_name):
    """Scrape posts of a user."""
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        print(f"Posts by {profile_name}:")
        for post in profile.get_posts():
            print(f"Caption: {post.caption}")
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}")
            print(f"URL: {post.url}")
            print("-" * 40)
    except Exception as e:
        print(f"Error while fetching posts: {e}")

def main():
    target_username = "sparkle__soul_02"  # Replace with the target Instagram username
    
    login_instagram(USERNAME, PASSWORD)
    scrape_profile_info(target_username)
    scrape_followers(target_username)
    scrape_followees(target_username)
    scrape_posts(target_username)

if __name__ == "__main__":
    main()

