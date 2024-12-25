import instaloader

def download_instagram_video(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Extract the shortcode from the URL
    shortcode = url.split("/")[-2]

    try:
        # Download the post using the shortcode
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=post.owner_username)
        print("Download completed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    insta_url = input("Enter Instagram post URL: ")
    download_instagram_video(insta_url)









# from pytube import YouTube

# def download_youtube_video(url):
#     try:
#         # Create a YouTube object
#         yt = YouTube(url)
        
#         # Get the highest resolution stream available
#         stream = yt.streams.get_highest_resolution()
        
#         print(f"Downloading: {yt.title}")
        
#         # Download the video
#         stream.download()
#         print(f"Download completed: {yt.title}")
    
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     youtube_url = input("Enter YouTube video URL: ")
#     download_youtube_video(youtube_url)
